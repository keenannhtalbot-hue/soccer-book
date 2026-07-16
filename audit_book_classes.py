#!/usr/bin/env python3
"""
Audit every page in a flat static-HTML book for:

1. Page-level CSS class coverage
   - For every HTML class used in any `pages/*.html`, confirm there is a
     matching CSS rule in the linked stylesheet. Missing selectors render
     as unstyled content (the bug that shipped the soccer book back cover
     unstyled on 2026-07-15 — see umbrella pitfall "CSS class-coverage is
     the cheapest catch for unstyled ships").
   - For every CSS rule in the linked stylesheet, confirm at least one page
     uses the selector. Dangling rules are not bugs but indicate generator
     churn worth noting.

2. Page-number metadata
   - Confirm every `pages/*.html` (excluding cover/back-cover/halftitle/contents)
     has a page-num element with content matching its filename's numeric
     prefix. Catches "we added page 175 but the page-num says 174".

3. Cover-vs-actual-count drift
   - Greps 01-cover.html for `cover-strap` and `cover-sub` text. Reports
     the largest page number present in the file system. When they disagree,
     you've found the classic "we grew the book to 200 but the cover still
     says 100" bug.

4. ISBN parity front-to-back
   - Greps 01-cover.html and the back-cover file for any `ISBN` token.
     When they differ, you've found the classic "front cover says
     978-0-00000-000-0 placeholder, back cover has the real one" bug.

5. Viewer bounds parity (if viewer.html present)
   - Reads the `<input min=... max=...>` attributes from viewer.html AND
     the matching `goToPage()` `if (n >= X && n <= Y)` guard. Reports a
     mismatch if they don't agree on the same [min, max].

This is intentionally a single fast script — the go/no-go check before
shipping ANY batch extension. Output is human-readable text. Exit code is
non-zero only when a check fails (so it's CI-friendly if you want to wire
it in).
"""
import argparse
import glob
import html.parser
import os
import re
import sys


class ClassCoverageCheck(html.parser.HTMLParser):
    """Collect every distinct class name used in any HTML page."""

    def __init__(self):
        super().__init__()
        self.classes_used = set()

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        cls = d.get("class", "")
        for c in cls.split():
            self.classes_used.add(c)


def _gather_used_classes(pages_dir):
    used = set()
    pages = sorted(glob.glob(os.path.join(pages_dir, "*.html")))
    for f in pages:
        p = ClassCoverageCheck()
        p.feed(open(f).read())
        for c in p.classes_used:
            used.add(c)
    return used, pages


def _gather_defined_selectors(css_path):
    """Naive selector extraction: a `.name` not followed by a colon that's a
    pseudo-class, OR `,`/space/`{` etc. Returns the set of simple class
    selectors defined anywhere in the CSS."""
    text = open(css_path).read()
    sels = set()
    # match `.foo{` `.foo,` `.foo ` `.foo:`
    for m in re.finditer(r"\.([A-Za-z][A-Za-z0-9_-]*)\s*[{,:]", text):
        sels.add(m.group(1))
    return sels


def _check_class_coverage(pages_dir, css_path, out):
    if not os.path.exists(css_path):
        out.append(f"  (skipping CSS check: {css_path} not found)")
        return
    used, pages = _gather_used_classes(pages_dir)
    defined = _gather_defined_selectors(css_path)
    used_only = used - defined
    defined_only = defined - used
    if used_only:
        out.append(
            f"  ❌ {len(used_only)} CLASSES USED IN HTML BUT NOT IN CSS:"
        )
        for c in sorted(used_only):
            used_in = []
            for f in pages:
                if c in open(f).read():
                    used_in.append(os.path.basename(f))
                    if len(used_in) >= 3:
                        break
            out.append(f"      .{c}  (e.g. {', '.join(used_in)})")
    else:
        out.append(
            f"  ✓ class coverage OK ({len(used)} used, {len(defined)} defined)"
        )
    out.append(
        f"  ({len(defined_only)} defined classes not used by any page — informational only)"
    )


def _check_page_num_consistency(pages_dir, out, excluded_prefixes=("00-", "01-", "02-", "03-")):
    """Every body page's <page-num> content should match its filename number.

    excluded_prefixes covers front matter: back cover (00), cover (01),
    halftitle (02), contents (03)."""
    pages = sorted(glob.glob(os.path.join(pages_dir, "*-page.html")))
    if not pages:
        out.append("  (no body pages found)")
        return
    mismatches = []
    for f in pages:
        name = os.path.basename(f)
        # Skip excluded prefixes
        if any(name.startswith(p) for p in excluded_prefixes):
            continue
        m = re.match(r"(\d+)-page\.html", name)
        if not m:
            continue
        expected_num = int(m.group(1))
        body = open(f).read()
        m2 = re.search(
            r'<div\s+class="page-num">\s*(\d+)\s*</div>', body
        )
        if not m2:
            mismatches.append(f"      {name}: no <page-num> found")
            continue
        if int(m2.group(1)) != expected_num:
            mismatches.append(
                f"      {name}: filename says {expected_num} but <page-num> says {m2.group(1)}"
            )
    if mismatches:
        out.append(f"  ❌ PAGE-NUM MISMATCHES ({len(mismatches)}):")
        out.extend(mismatches)
    else:
        out.append("  ✓ page-num consistency OK")


def _check_cover_actual_count(pages_dir, cover_path, out):
    if not os.path.exists(cover_path):
        out.append(f"  (no cover at {cover_path})")
        return
    pages = [
        f
        for f in glob.glob(os.path.join(pages_dir, "*-page.html"))
        if not os.path.basename(f).startswith(
            ("00-", "01-", "02-", "03-", "04-")
        )
    ]
    actual_max = max(
        (int(re.match(r"(\d+)-", os.path.basename(f)).group(1)) for f in pages),
        default=0,
    )
    body = open(cover_path).read()
    strap = re.search(r'class="cover-strap">([^<]+)<', body)
    sub = re.search(r'class="cover-sub">([^<]+)<', body)
    out.append(f"  Actual max page number in pages/: {actual_max}")
    if strap:
        out.append(f"  cover-strap text:      {strap.group(1)!r}")
    if sub:
        out.append(f"  cover-sub text:        {sub.group(1)!r}")
    if strap:
        s = strap.group(1)
        # Look for any "N pages" or first all-digit run
        m = re.search(r"(\d+)\s*pages?", s, re.IGNORECASE)
        if m:
            claimed = int(m.group(1))
            if claimed < actual_max:
                out.append(
                    f"  ⚠️  cover strap claims {claimed} pages, but actual max is {actual_max}"
                )


def _check_isbn_parity(pages_dir, cover_path, out):
    if not os.path.exists(cover_path):
        out.append(f"  (no cover at {cover_path})")
        return
    cover_isbn = re.search(r"ISBN\s+([0-9-]+)", open(cover_path).read())
    back = sorted(glob.glob(os.path.join(pages_dir, "00-*.html")))
    if not back:
        out.append("  (no back cover found)")
        return
    back_isbn = re.search(r"ISBN\s+([0-9-]+)", open(back[0]).read())
    out.append(f"  front-cover ISBN: {cover_isbn.group(1) if cover_isbn else 'NONE'}")
    out.append(f"  back-cover ISBN:  {back_isbn.group(1) if back_isbn else 'NONE'}")
    if cover_isbn and back_isbn and cover_isbn.group(1) != back_isbn.group(1):
        out.append("  ❌ ISBN MISMATCH between front and back cover")


def _check_viewer_bounds(pages_dir, out):
    viewer = sorted(glob.glob(os.path.join(pages_dir, "viewer.html")))
    if not viewer:
        out.append("  (no viewer.html)")
        return
    body = open(viewer[0]).read()
    in_min = re.search(r'<input[^>]*\bmin="([0-9]+)"', body)
    in_max = re.search(r'<input[^>]*\bmax="([0-9]+)"', body)
    guard = re.search(r"if\s*\(\s*n\s*>=\s*(\d+)\s*&&\s*n\s*<=\s*(\d+)\s*\)", body)
    if in_min and in_max and guard:
        out.append(
            f"  viewer input min={in_min.group(1)} max={in_max.group(1)} | "
            f"goToPage guard: n in [{guard.group(1)}, {guard.group(2)}]"
        )
        if (in_min.group(1), in_max.group(1)) != (
            guard.group(1),
            guard.group(2),
        ):
            out.append("  ❌ viewer bounds mismatch")
    else:
        out.append("  (could not parse viewer bounds)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--pages",
        default="pages",
        help="Path to the pages/ directory (default: pages relative to cwd)",
    )
    ap.add_argument(
        "--css",
        default="pages/book.css",
        help="Path to the shared stylesheet (default: pages/book.css)",
    )
    args = ap.parse_args()

    pages_dir = args.pages
    css_path = args.css

    # Resolve `pages` dir relative to cwd if it's a bare name
    if not os.path.isabs(pages_dir):
        pages_dir = os.path.join(os.getcwd(), pages_dir)
    if not os.path.isabs(css_path):
        css_path = os.path.join(os.getcwd(), css_path)

    print(f"Auditing {pages_dir} against {css_path}\n")
    failed = False

    print("=== 1. CSS class coverage (USED-in-HTML vs DEFINED-in-CSS) ===")
    out = []
    _check_class_coverage(pages_dir, css_path, out)
    print("\n".join(out))
    if any("❌" in line for line in out):
        failed = True

    print("\n=== 2. Page-number consistency (filename vs <page-num>) ===")
    out = []
    _check_page_num_consistency(pages_dir, out)
    print("\n".join(out))
    if any("❌" in line for line in out):
        failed = True

    print("\n=== 3. Cover-strap / cover-sub vs actual page count ===")
    out = []
    _check_cover_actual_count(pages_dir, os.path.join(pages_dir, "01-cover.html"), out)
    print("\n".join(out))

    print("\n=== 4. ISBN parity (front cover vs back cover) ===")
    out = []
    _check_isbn_parity(pages_dir, os.path.join(pages_dir, "01-cover.html"), out)
    print("\n".join(out))
    if any("❌" in line for line in out):
        failed = True

    print("\n=== 5. Viewer bounds parity (input attr vs goToPage guard) ===")
    out = []
    _check_viewer_bounds(pages_dir, out)
    print("\n".join(out))
    if any("❌" in line for line in out):
        failed = True

    print()
    if failed:
        print("❌ AUDIT FAILED — fix the items marked ❌ before shipping.")
        sys.exit(1)
    else:
        print("✓ All blocking checks passed.")


if __name__ == "__main__":
    main()
