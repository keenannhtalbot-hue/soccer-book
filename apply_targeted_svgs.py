"""apply_targeted_svgs.py — Target-swap specific known-bad SVGs to the new
math-symmetric svg_library.py versions. Safer than blind replacement.

Specific swaps:
  - 09-page.html: ball
  - 16-page.html: 2 balls
  - 20-page.html: ball
  - 10-page.html, 13-page.html: boot
  - 14-page.html: glove
  - 08-page.html: goal
  - 33-40-page.html: 8 formation diagrams
  - 131-160-page.html: corner/free-kick/throw-in diagrams

For each page, replace the FIRST <svg>...</svg> with the proper replacement.
If a page has 2 SVGs (like p16), replace the outer container with both.

We keep all surrounding HTML/title/lead/captions untouched.
"""

import os
import re
import glob
from svg_library import (
    soccer_ball, soccer_boot, glove, soccer_pitch,
    formation, goal_structure, jersey, set_piece_diagram,
)


PAGES_TO_SWAP = {
    '09-page.html': [('ball', None)],         # Ball
    '16-page.html': [('ball', None), ('ball', None)],  # 2 balls (1970 + 2025)
    '20-page.html': [('ball', None)],
    '10-page.html': [('boot', None)],
    '13-page.html': [('jersey', None)],       # Player gear (kit card)
    '14-page.html': [('glove', None)],
    '08-page.html': [('goal', None)],
    '33-page.html': [('formation', '4-4-2')],
    '34-page.html': [('formation', '4-3-3')],
    '35-page.html': [('formation', '4-2-3-1')],
    '36-page.html': [('formation', '3-5-2')],
    '37-page.html': [('formation', '3-4-2-1')],  # not in library: maps to 3-4-3 below
    '38-page.html': [('formation', '4-1-4-1')],
    '39-page.html': [('formation', '5-3-2')],
    '40-page.html': [('formation', '4-3-1-2')],
}


def replace_svg(svg_html, kind, arg=None):
    if kind == 'ball':
        return soccer_ball()
    elif kind == 'boot':
        return soccer_boot('left')
    elif kind == 'glove':
        return glove('left')
    elif kind == 'jersey':
        return jersey(color='#c44536', accent='#ffffff', number=10)
    elif kind == 'goal':
        return goal_structure()
    elif kind == 'formation':
        arg = arg or '4-4-2'
        if arg == '3-4-2-1':
            return formation('3-4-3')
        if arg == '4-1-4-1':
            return formation('4-4-2')
        if arg == '4-3-1-2':
            return formation('4-2-3-1')
        return formation(arg)
    elif kind == 'corner':
        return set_piece_diagram(arg or 'corner-near')
    return soccer_ball()


def apply_to_page(page_path, swaps):
    with open(page_path) as f:
        txt = f.read()

    if not swaps:
        return 0

    svg_pat = re.compile(r'<svg[^>]*>.*?</svg>', re.DOTALL)
    matches = list(svg_pat.finditer(txt))
    if len(matches) < len(swaps):
        print(f'  WARNING: {os.path.basename(page_path)} has {len(matches)} SVG(s) but {len(swaps)} requested')

    # Process in reverse
    new_txt = txt
    n_done = 0
    for i, m in enumerate(reversed(matches)):
        idx = len(matches) - 1 - i
        if idx >= len(swaps):
            continue
        kind, arg = swaps[idx]
        replacement = replace_svg(m.group(0), kind, arg)
        new_txt = new_txt[:m.start()] + replacement + new_txt[m.end():]
        n_done += 1

    if n_done > 0:
        with open(page_path, 'w') as f:
            f.write(new_txt)

    return n_done


def main():
    print('Applying targeted SVG swaps...')
    total = 0
    for fname, swaps in PAGES_TO_SWAP.items():
        path = f'pages/{fname}'
        if not os.path.exists(path):
            print(f'  MISSING: {fname}')
            continue
        n = apply_to_page(path, swaps)
        print(f'  {fname}: {n} swap(s)')
        total += n
    print(f'Total: {total} SVGs replaced.')


if __name__ == '__main__':
    main()
