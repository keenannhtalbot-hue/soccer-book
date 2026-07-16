"""apply_svgs.py — Replace all hand-drawn SVGs in pages/ with the new svg_library.py versions.

Goals:
1. Every ball SVG → svg_library.soccer_ball() (math-symmetric)
2. Every boots page → svg_library.soccer_boot() (anatomically correct)
3. Every glove page → svg_library.glove()
4. Every pitch page → svg_library.soccer_pitch()
5. Every formation page → svg_library.formation(<correct-name>)
6. Every goal page → svg_library.goal_structure()

Strategy: walk pages/*.html, find <svg>...</svg> blocks, classify by
surrounding context (text mentions "ball", "boot", "glove", etc.), replace.

Preserve: all HTML outside <svg>...</svg> intact. Title, lead, body, page-num
all untouched.
"""

import os
import re
import glob
from svg_library import (
    soccer_ball, soccer_boot, glove, soccer_pitch,
    formation, goal_structure, jersey, set_piece_diagram,
)


def classify_svg_context(page_text, svg_start_offset):
    """What does this SVG illustrate? Look at the text BEFORE the SVG for keywords."""
    # Look 500 chars before the SVG
    context = page_text[max(0, svg_start_offset - 500):svg_start_offset].lower()
    # Check for keywords
    if any(w in context for w in ['boot', 'cleat', 'stud', 'shoe']):
        return 'boot'
    if any(w in context for w in ['glove', 'keeper glove']):
        return 'glove'
    if 'formation' in context or any(w in context for w in ['4-4-2', '4-3-3', '3-5-2', '5-3-2', '4-2-3-1', '5-4-1']):
        return 'formation'
    if 'pitch' in context or 'field' in context or 'field of play' in context:
        return 'pitch'
    if 'goal' in context:
        return 'goal'
    if 'corner' in context:
        return 'corner'
    # Default: ball
    return 'ball'


def detect_formation_name(page_text):
    """Extract the formation name (e.g., '4-4-2') from the page text."""
    m = re.search(r'\b(\d-\d-\d(?:-\d)?)\b', page_text)
    return m.group(1) if m else '4-4-2'


def replace_svg_with(svg_html, kind, formation_name='4-4-2'):
    """Build the replacement SVG based on the classification."""
    if kind == 'ball':
        return soccer_ball()
    elif kind == 'boot':
        return soccer_boot('left')
    elif kind == 'glove':
        return glove('left')
    elif kind == 'pitch':
        return soccer_pitch('horizontal')
    elif kind == 'formation':
        return formation(formation_name)
    elif kind == 'goal':
        return goal_structure()
    elif kind == 'corner':
        return set_piece_diagram('corner-near')
    return soccer_ball()


def fix_page(page_path, dry_run=False):
    """Replace all SVGs in a single page file."""
    with open(page_path) as f:
        txt = f.read()

    # Find all SVG blocks
    svg_pat = re.compile(r'<svg[^>]*>.*?</svg>', re.DOTALL)
    matches = list(svg_pat.finditer(txt))

    if not matches:
        return False  # No SVGs in this page

    # Process in reverse so offsets stay valid
    new_txt = txt
    n_replacements = 0
    for m in reversed(matches):
        svg = m.group(0)
        kind = classify_svg_context(new_txt, m.start())
        form_name = detect_formation_name(new_txt)
        replacement = replace_svg_with(svg, kind, form_name)
        new_txt = new_txt[:m.start()] + replacement + new_txt[m.end():]
        n_replacements += 1

    if n_replacements == 0:
        return False

    if not dry_run:
        with open(page_path, 'w') as f:
            f.write(new_txt)

    return n_replacements


def main():
    pages = sorted(glob.glob('pages/*-page.html'))
    pages += sorted(glob.glob('pages/0*-cover.html'))
    pages += sorted(glob.glob('pages/0*-contents.html'))
    pages += sorted(glob.glob('pages/0*-halftitle.html'))

    summary = {}
    for p in pages:
        n = fix_page(p)
        if n:
            summary[os.path.basename(p)] = n

    print(f'Processed {len(summary)} pages with SVG replacements.')
    print(f'Total: {sum(summary.values())} SVGs replaced.')
    return summary


if __name__ == '__main__':
    main()
