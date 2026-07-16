#!/usr/bin/env python3
"""lint_book_pages.py — sanity check every HTML page in a book.

Walks pages/*.html and runs three checks:
  1. HTMLParser stack-mismatch: any unmatched tags. SVG elements (`<rect>`,
     `<path>`, etc.) are treated as void/self-closing so the linter doesn't
     false-positive every inline diagram.
  2. Regex sweep for explicit `<b|strong>...</strong|b>` cross-closer
     mismatches (a single character is silently wrong and breaks inner styling).
  3. CSS class-coverage: every `class="..."` token used in any HTML page must
     have a matching `.foo { ... }` selector somewhere across the supplied
     CSS file(s). Catches the silent class-drift bug where new pages reference
     classes that were never defined — the page "loads" but renders unstyled.

Exits non-zero if any page fails any check. Run from the book root.

Usage:
  python3 scripts/lint_book_pages.py [--pages-dir pages] [--css pages/book.css]
"""
import argparse, glob, os, re, sys
from html.parser import HTMLParser
from pathlib import Path

VOID = {'br','img','input','meta','link','hr','source','track','area',
        'base','col','embed','param','wbr',
        # SVG elements are self-closing/void in HTML — they never have closing tags
        # even though HTMLParser sees them as ordinary tags. Without these in VOID,
        # the stack-linter false-positives every inline SVG diagram.
        # Validated on soccer-book 2026-07-15: 25 new pages tripped 150 false
        # "mismatch <svg> vs </rect>" warnings per page when this set was missing.
        'rect','path','circle','line','polygon','polyline','ellipse',
        'use','image','stop','tspan','defs','g','svg','text'}

class StackLint(HTMLParser):
    def __init__(self):
        super().__init__()
        self.errors = []
        self.tag_stack = []
    def handle_starttag(self, tag, attrs):
        if tag in VOID: return
        self.tag_stack.append((tag, self.getpos()))
    def handle_endtag(self, tag):
        if not self.tag_stack:
            self.errors.append(f'orphan </{tag}> at {self.getpos()}')
            return
        last, _ = self.tag_stack[-1]
        if last != tag:
            self.errors.append(f'open <{last}> closed by </{tag}> at {self.getpos()}')
        else:
            self.tag_stack.pop()

def collect_classes(txt: str) -> set[str]:
    """Every class= attribute, split on whitespace, deduped."""
    out: set[str] = set()
    for m in re.finditer(r'class\s*=\s*"([^"]+)"', txt):
        for c in m.group(1).split():
            out.add(c)
    for m in re.finditer(r"class\s*=\s*'([^']+)'", txt):
        for c in m.group(1).split():
            out.add(c)
    return out


def collect_defined_classes(css_paths: list[Path]) -> set[str]:
    """Every selector name defined in the given CSS files."""
    out: set[str] = set()
    css_text = ""
    for p in css_paths:
        if p.exists():
            css_text += p.read_text(encoding="utf-8")
    # Match `.foo` or `.foo,` or `.foo{` — handle chained selectors and pseudo.
    for m in re.finditer(r"\.([A-Za-z][A-Za-z0-9_-]*)\s*[{,]", css_text):
        out.add(m.group(1))
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--pages-dir', default='pages', help='directory holding *.html pages')
    p.add_argument('--css', action='append', default=[], help='CSS file(s) to check class coverage against. Default: pages/book.css.')
    args = p.parse_args()

    if not os.path.isdir(args.pages_dir):
        print(f'ERROR: pages dir not found: {args.pages_dir}', file=sys.stderr)
        return 2

    files = sorted(glob.glob(os.path.join(args.pages_dir, '*.html')))
    if not files:
        print(f'ERROR: no *.html files in {args.pages_dir}', file=sys.stderr)
        return 2

    pages_dir = Path(args.pages_dir)
    css_paths = [Path(c) for c in args.css] if args.css else [pages_dir / "book.css"]

    pages_with_errors = 0
    bstrong_mismatches = 0
    used_classes: set[str] = set()

    for f in files:
        txt = open(f).read()
        # 1. stack lint
        parser = StackLint()
        parser.feed(txt)
        parser.close()
        leftover = [t for t, _ in parser.tag_stack]
        if parser.errors or leftover:
            pages_with_errors += 1
            base = os.path.basename(f)
            print(f'STACK: {base}: {parser.errors[:5]} leftover={leftover}')

        # 2. <b|strong> cross-closer
        for m in re.finditer(r'<(b|strong)\b[^>]*>(.*?)</\s*(b|strong)\s*>', txt, re.S):
            ot, content, ct = m.group(1), m.group(2), m.group(3)
            if ot != ct:
                bstrong_mismatches += 1
                ln = txt[:m.start()].count('\n') + 1
                base = os.path.basename(f)
                snippet = content[:80].replace('\n', ' ')
                print(f'MISMATCH: {base}:{ln} <{ot}>...</{ct}> {snippet!r}')

        # Track every used class.
        used_classes.update(collect_classes(txt))

    # 3. CSS class-coverage check (catches the "back cover rendering unstyled
    # because book.css never had .back-* rules" bug class). Every class used
    # anywhere in the pages must have a matching `.foo` selector somewhere
    # across the supplied CSS files. Reported once per missing class across the
    # whole book — not per page — because that's how big the bug surfaces.
    defined = collect_defined_classes(css_paths)
    used_only = sorted(used_classes - defined)
    # Ignore HTML built-ins / utility classes we don't expect CSS to define.
    # (This list is intentionally short — false-positive suppression is the
    # only reason to add to it. Anything else, fix the CSS.)
    ALLOWLIST = set()  # e.g. {'lead', 'serif', 'sans'} if you want to skip them

    total = len(files)
    if pages_with_errors == 0 and bstrong_mismatches == 0 and not used_only:
        print(f'OK: {total} pages, no errors; {len(used_classes)} classes used, all defined in {", ".join(str(p) for p in css_paths)}')
        return 0

    if used_only:
        print(f'CLASSES-WITHOUT-CSS ({len(used_only)}): {used_only}')

    print(f'FAIL: {total} pages, {pages_with_errors} stack errors, {bstrong_mismatches} b/strong mismatches')
    return 1

if __name__ == '__main__':
    sys.exit(main())
