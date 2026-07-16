"""apply_trionda.py — Apply the new Trionda SVG to all pages with ball diagrams.

Cover (page 01): NO BALL (user removed it earlier)
Pages with the ball:
  - 09-page.html: 1 ball (variant=full, with gold accent)
  - 16-page.html: 2 balls (variant=full)
  - 20-page.html: 1 ball (variant=full)

These are the only 3 pages with the soccer ball SVG per the user's earlier audit.
The cover has no ball anymore.
"""

import os
import re
import sys

# Import the trionda_v5 module from /home/kbot
sys.path.insert(0, '/home/kbot')
from trionda_v5 import trionda_ball


def replace_balls_in_page(page_path, n_balls):
    """Replace ALL `<svg>...</svg>` blocks in the page with Trionda variants.

    n_balls: how many of the SVGs to replace (first n_balls SVGs).
    """
    with open(page_path) as f:
        txt = f.read()

    svg_pat = re.compile(r'<svg[^>]*>.*?</svg>', re.DOTALL)
    matches = list(svg_pat.finditer(txt))

    if not matches:
        return False

    new_txt = txt
    # Replace in reverse to preserve offsets
    for i, m in enumerate(reversed(matches)):
        idx = len(matches) - 1 - i
        if idx >= n_balls:
            continue
        # Use full variant (with gold accent)
        replacement = trionda_ball(variant='full')
        new_txt = new_txt[:m.start()] + replacement + new_txt[m.end():]

    if new_txt != txt:
        with open(page_path, 'w') as f:
            f.write(new_txt)
        return True
    return False


def main():
    # Pages with balls and number of SVGs to replace (only the BALL SVGs)
    # p09 has 1 SVG (the ball). p16 has 2 SVGs (both balls). p20 has 1 SVG (the ball).
    # If a page has other SVGs first (like a header diagram), only replace the ball ones.

    pages_to_update = {
        '09-page.html': 1,
        '16-page.html': 2,
        '20-page.html': 1,
    }

    base = '/home/kbot/soccer-book/pages'
    for fname, n in pages_to_update.items():
        path = os.path.join(base, fname)
        if not os.path.exists(path):
            print(f'MISSING: {fname}')
            continue
        ok = replace_balls_in_page(path, n)
        print(f'  {fname}: replaced {n} SVG(s): {ok}')


if __name__ == '__main__':
    main()
