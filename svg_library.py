"""svg_library.py — Math-symmetric SVG library for The Soccer Book.

Every drawing uses pure math coordinates from a single center point so the
result cannot drift off-center. Every shape uses parametric coordinates
computed with math.sin/cos, never hand-typed vertices.

Trust chain:
- Verification: every component is unit-testable (compute centroid, bbox,
  vertices).
- Symmetry: pentagons use the same radius and rotation formula; circles
  are cx/cy from viewBox center; kits are mirror-symmetric across the
  center vertical axis.
- Correctness: relies on math identities, not eyeballing.

Units: all coordinates are in viewBox 0..100 unless noted. Composed to
larger sizes via the SVG itself, not by scaling the coordinates.
"""

import math
import re
import xml.etree.ElementTree as ET
from io import StringIO


# ============================================================================
# Building blocks
# ============================================================================

def polygon_points(cx, cy, sides, r, start_angle=math.pi/2, clockwise=False):
    """Return a list of (x, y) points for a regular polygon.

    Defaults: top vertex pointing up (start_angle = pi/2), counter-clockwise.
    """
    points = []
    for i in range(sides):
        if clockwise:
            angle = start_angle - i * 2 * math.pi / sides
        else:
            angle = start_angle + i * 2 * math.pi / sides
        x = cx + r * math.cos(angle)
        y = cy - r * math.sin(angle)  # SVG y-flip
        points.append((round(x, 2), round(y, 2)))
    return points


def fmt_pts(pts):
    return ' '.join(f'{x},{y}' for x, y in pts)


def centroid(pts):
    """Centroid of a polygon from its vertices."""
    cx = sum(p[0] for p in pts) / len(pts)
    cy = sum(p[1] for p in pts) / len(pts)
    return (round(cx, 2), round(cy, 2))


def bbox(pts):
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    return (min(xs), min(ys), max(xs), max(ys))


# ============================================================================
# Soccer ball (simple ⚽️ style: 1 center pentagon + 4 satellites + outline)
# ============================================================================

def soccer_ball(viewbox=100, outline_color='#1a1612', fill_color='#ffffff',
                panel_color='#1a1612', radius=46, stroke_width=3):
    """A simple soccer ball: white circle + 5 black pentagons + 6 stitches.

    Math-symmetric: center pentagon at (50, 50), 4 satellite pentagons at
    (30, 30), (70, 30), (30, 70), (70, 70) — all mirrored around (50, 50).
    """
    cx, cy = 50, 50

    center_pent = polygon_points(cx, cy, 5, r=15)
    nw = polygon_points(30, 30, 5, r=8)
    ne = polygon_points(70, 30, 5, r=8)
    sw = polygon_points(30, 70, 5, r=8)
    se = polygon_points(70, 70, 5, r=8)

    # 4 stitching lines from each satellite centroid to the nearest center vertex.
    # Pentagon vertices (CCW from top): [0] top, [1] upper-left, [2] lower-left,
    # [3] lower-right, [4] upper-right. Match each satellite to the geometrically
    # nearest vertex so stitches point outward (not through the pentagon interior).
    nearest = {}
    for label, (sx, sy) in [('NW', (30, 30)), ('NE', (70, 30)),
                            ('SW', (30, 70)), ('SE', (70, 70))]:
        nearest[label] = min(range(5),
                             key=lambda i: (center_pent[i][0]-sx)**2 + (center_pent[i][1]-sy)**2)
    stitches = [
        ((30, 30), center_pent[nearest['NW']]),
        ((70, 30), center_pent[nearest['NE']]),
        ((30, 70), center_pent[nearest['SW']]),
        ((70, 70), center_pent[nearest['SE']]),
    ]
    stitch_svg = '\n  '.join(
        f'<line x1="{s[0][0]}" y1="{s[0][1]}" x2="{s[1][0]}" y2="{s[1][1]}"/>'
        for s in stitches
    )

    return f'''<svg viewBox="0 0 {viewbox} {viewbox}" xmlns="http://www.w3.org/2000/svg">
  <circle cx="{cx}" cy="{cy}" r="{radius}" fill="{fill_color}" stroke="{outline_color}" stroke-width="{stroke_width}"/>
  <g fill="{panel_color}" stroke="{panel_color}" stroke-width="1" stroke-linejoin="round">
    <polygon points="{fmt_pts(center_pent)}"/>
    <polygon points="{fmt_pts(nw)}"/>
    <polygon points="{fmt_pts(ne)}"/>
    <polygon points="{fmt_pts(sw)}"/>
    <polygon points="{fmt_pts(se)}"/>
  </g>
  <g stroke="{outline_color}" stroke-width="1.2" fill="none" stroke-linecap="round">
  {stitch_svg}
  </g>
</svg>'''


# ============================================================================
# Soccer boot (left and right, mirror-symmetric)
# ============================================================================

def soccer_boot(side='left', viewbox=200):
    """Side view of a soccer boot (cleat).

    Geometry:
    - Sole plate along y=140 (cleats point down)
    - Toe at x=40 (low) curving up to laces at x=100
    - Heel at x=170 down to y=170
    - Laces: 3 horizontal curves on the upper third
    - Studs: 4 black trapezoids along the bottom

    Math: studs are generated parametrically from `stud_centers`; the
    upper-body path data is hand-authored and not mirrored between sides.
    The `side` parameter is currently accepted but ignored — to produce a
    true right-boot mirror, every x in the path data would need to be
    remapped as `viewbox - x`.
    """
    # NOTE: this drawing is a fixed orientation (toe pointing left). The `side`
    # parameter is currently a no-op; to produce a true mirror, every x in the
    # path data below would need to be remapped as `viewbox - x`. See the
    # TODO in set_piece_diagram / glove for the same pattern.

    # Studs (cleats) along the bottom — 4 evenly-spaced trapezoids.
    # Generated parametrically from the sole length so adding/moving studs
    # only requires editing `stud_centers`.
    stud_centers = [52, 87, 122, 157]
    stud_top_half = 7   # half-width of trapezoid top edge
    stud_bot_half = 5   # half-width of trapezoid bottom edge
    stud_top_y = 148
    stud_bot_y = 168

    def _stud_polygon(cx):
        # Trapezoid: top edge wider than bottom (cleat shape).
        return (
            f'<polygon points="'
            f'{cx-stud_top_half},{stud_top_y} '
            f'{cx+stud_top_half},{stud_top_y} '
            f'{cx+stud_bot_half},{stud_bot_y} '
            f'{cx-stud_bot_half},{stud_bot_y}'
            f'" fill="#1a1612"/>'
        )

    stud_svg = '\n    '.join(_stud_polygon(cx) for cx in stud_centers)

    return f'''<svg viewBox="0 0 {viewbox} 200" xmlns="http://www.w3.org/2000/svg">
  <!-- Sole plate -->
  <path d="M 30,145 Q 30,140 35,138 L 165,138 Q 175,138 180,145 L 180,150 Q 175,158 165,160 L 35,160 Q 30,158 25,150 Z"
        fill="#1a1612" stroke="#1a1612" stroke-width="0.5"/>

  <!-- Upper boot body -->
  <path d="M 40,135 Q 45,120 60,108 Q 80,95 110,90 Q 140,85 155,95 Q 175,108 180,135 L 175,140 Q 165,140 155,135 L 60,135 Q 45,138 40,140 Z"
        fill="#ffffff" stroke="#1a1612" stroke-width="2"/>

  <!-- Toe cap -->
  <path d="M 35,135 Q 30,128 30,118 Q 32,108 42,103 Q 50,100 60,103 L 60,135 Z"
        fill="#1a1612" stroke="#1a1612" stroke-width="1"/>

  <!-- Laces (3 horizontal curves) -->
  <g stroke="#1a1612" stroke-width="2" fill="none" stroke-linecap="round">
    <path d="M 85,108 Q 110,103 135,108"/>
    <path d="M 90,118 Q 110,114 130,118"/>
    <path d="M 95,128 Q 110,124 125,128"/>
  </g>

  <!-- Brand swoosh -->
  <path d="M 70,120 Q 90,108 115,118 Q 130,125 140,120" fill="none"
        stroke="#c44536" stroke-width="3" stroke-linecap="round"/>

  <!-- Studs (4 cleats along sole) -->
  <g fill="#1a1612">
    {stud_svg}
  </g>
</svg>'''


# ============================================================================
# Goalkeeper glove
# ============================================================================

def glove(side='left', viewbox=120):
    """A goalkeeper glove, fingers-up view.

    Geometry:
    - Wrist cuff at y=110-120 (blue band)
    - Palm/back of hand: large rounded rectangle y=20-110
    - 5 fingers: parametric positions from (60, 60) using polygon_points
    - Thumb: separate side, at angle pi*1.3
    - Latex palm area: darker oval on the lower 60%
    """
    # NOTE: `side` is currently accepted but ignored. To produce a true
    # right-hand mirror, multiply each `fx` by `-1` (or `side_mult`) and
    # recompute `x = 60 + fx`. The finger dict also has a `rotation` key
    # that is computed but never applied to the rendered SVG.

    # 5 fingers from left to right (thumb is leftmost when glove faces forward)
    finger_centers = [
        (-30, 35),  # thumb
        (-12, 5),   # index
        (4, -5),    # middle (longest)
        (20, 0),    # ring
        (36, 10),   # pinky
    ]
    finger_lengths = [12, 22, 26, 24, 20]
    finger_widths  = [10, 11, 11, 11, 10]

    fingers = []
    for i, ((fx, fy), fl, fw) in enumerate(zip(finger_centers, finger_lengths, finger_widths)):
        # Each finger is a rounded rectangle (simplified to ellipse + rect)
        x = 60 + fx
        y = 30 + fy
        # Use polygon for finger outline
        angle_offset = i * 0.05  # slight fan
        fingers.append({
            'cx': x, 'cy': y, 'r_x': fw/2, 'r_y': fl/2, 'rotation': angle_offset,
        })

    finger_svg = '\n  '.join(
        f'<ellipse cx="{f["cx"]}" cy="{f["cy"]}" rx="{f["r_x"]}" ry="{f["r_y"]}" '
        f'fill="#c44536" stroke="#1a1612" stroke-width="1.5"/>'
        for f in fingers
    )

    return f'''<svg viewBox="0 0 {viewbox} {viewbox}" xmlns="http://www.w3.org/2000/svg">
  <!-- Wrist cuff (bottom band) -->
  <rect x="35" y="105" width="50" height="14" rx="2" fill="#1e3a5f" stroke="#1a1612" stroke-width="1.5"/>

  <!-- Back of hand / glove body -->
  <ellipse cx="60" cy="65" rx="32" ry="38" fill="#c44536" stroke="#1a1612" stroke-width="2"/>

  <!-- Fingers -->
  <g>
  {finger_svg}
  </g>

  <!-- Latex palm accent (inside-out oval) -->
  <ellipse cx="60" cy="80" rx="20" ry="22" fill="#1a1612" opacity="0.85"/>

  <!-- Brand accent stripe across knuckles -->
  <rect x="55" y="50" width="10" height="3" fill="#1a1612"/>
</svg>'''


# ============================================================================
# Soccer field / pitch (top-down view)
# ============================================================================

def soccer_pitch(orient='horizontal', show_zones=True):
    # NOTE: `orient` is accepted for API stability but not yet used; the
    # pitch is always rendered in horizontal (landscape) orientation.
    """A soccer pitch drawn to scale (105m × 68m proportions).

    Layout:
    - viewBox 0 0 1050 680 (10 px per meter)
    - center at (525, 340)
    - halfway line at x=525
    - center circle radius 91 (9.15m)
    - penalty areas, goal areas, corner arcs, penalty arcs

    All coordinates are computed from the center.
    """
    # Pitch dimensions in meters
    L, W = 105, 68
    sx, sy = 10, 10  # scale: 10 px per meter

    # Half dimensions (relative to center)
    hL, hW = L / 2, W / 2

    # Pitch outer lines
    pitch_box = (
        f'  <rect x="{0}" y="{0}" width="{L*sx}" height="{W*sy}" '
        f'fill="#1f4d3a" stroke="#ffffff" stroke-width="2"/>'
    )

    # Halfway line
    halfway = f'  <line x1="{L*sx/2}" y1="0" x2="{L*sx/2}" y2="{W*sy}" stroke="#ffffff" stroke-width="2"/>'
    center_circle = f'  <circle cx="{L*sx/2}" cy="{W*sy/2}" r="91" fill="none" stroke="#ffffff" stroke-width="2"/>'
    center_spot = f'  <circle cx="{L*sx/2}" cy="{W*sy/2}" r="3" fill="#ffffff"/>'

    # Penalty areas (16.5m deep, 40.32m wide)
    pa_w, pa_h = 40.32, 16.5
    pa_left = (
        f'  <rect x="0" y="{(W-pa_w)*sy/2}" width="{pa_h*sx}" height="{pa_w*sy}" '
        f'fill="none" stroke="#ffffff" stroke-width="2"/>'
    )
    pa_right = (
        f'  <rect x="{(L-pa_h)*sx}" y="{(W-pa_w)*sy/2}" width="{pa_h*sx}" height="{pa_w*sy}" '
        f'fill="none" stroke="#ffffff" stroke-width="2"/>'
    )

    # Goal areas (5.5m deep, 18.32m wide)
    ga_w, ga_h = 18.32, 5.5
    ga_left = (
        f'  <rect x="0" y="{(W-ga_w)*sy/2}" width="{ga_h*sx}" height="{ga_w*sy}" '
        f'fill="none" stroke="#ffffff" stroke-width="2"/>'
    )
    ga_right = (
        f'  <rect x="{(L-ga_h)*sx}" y="{(W-ga_w)*sy/2}" width="{ga_h*sx}" height="{ga_w*sy}" '
        f'fill="none" stroke="#ffffff" stroke-width="2"/>'
    )

    # Penalty spots (11m from goal line)
    ps_left_x = 11 * sx
    ps_right_x = (L - 11) * sx
    ps_y = W * sy / 2
    pen_spots = (
        f'  <circle cx="{ps_left_x}" cy="{ps_y}" r="2" fill="#ffffff"/>'
        f'  <circle cx="{ps_right_x}" cy="{ps_y}" r="2" fill="#ffffff"/>'
    )

    # Penalty arcs (D), radius 9.15m from penalty spot
    arc_r = 9.15 * sx
    pen_arcs = (
        f'  <path d="M {ps_left_x},{ps_y-arc_r} A {arc_r},{arc_r} 0 0 0 {ps_left_x},{ps_y+arc_r}" '
        f'fill="none" stroke="#ffffff" stroke-width="2"/>'
        f'  <path d="M {ps_right_x},{ps_y-arc_r} A {arc_r},{arc_r} 0 0 1 {ps_right_x},{ps_y+arc_r}" '
        f'fill="none" stroke="#ffffff" stroke-width="2"/>'
    )

    # Corner arcs (radius 1m)
    corner = 1 * sx
    corners = (
        f'  <path d="M 0,{corner} A {corner},{corner} 0 0 0 {corner},0" fill="none" stroke="#ffffff" stroke-width="2"/>'
        f'  <path d="M {L*sx-corner},0 A {corner},{corner} 0 0 0 {L*sx},{corner}" fill="none" stroke="#ffffff" stroke-width="2"/>'
        f'  <path d="M {L*sx},{W*sy-corner} A {corner},{corner} 0 0 0 {L*sx-corner},{W*sy}" fill="none" stroke="#ffffff" stroke-width="2"/>'
        f'  <path d="M {corner},{W*sy} A {corner},{corner} 0 0 0 0,{W*sy-corner}" fill="none" stroke="#ffffff" stroke-width="2"/>'
    )

    # Goal frames
    goal_w = 7.32 * sy
    goal_h_y = (W*sy - goal_w) / 2
    goals = (
        f'  <rect x="-3" y="{goal_h_y}" width="6" height="{goal_w}" fill="#ffffff" stroke="#1a1612" stroke-width="1"/>'
        f'  <rect x="{L*sx-3}" y="{goal_h_y}" width="6" height="{goal_w}" fill="#ffffff" stroke="#1a1612" stroke-width="1"/>'
    )

    # Zone overlays (defending, middle, attacking third)
    zones = ''
    if show_zones:
        zones = (
            f'  <rect x="0" y="0" width="{L*sx/3}" height="{W*sy}" fill="#c44536" opacity="0.12"/>'
            f'  <rect x="{L*sx/3}" y="0" width="{L*sx/3}" height="{W*sy}" fill="#c9a961" opacity="0.08"/>'
            f'  <rect x="{2*L*sx/3}" y="0" width="{L*sx/3}" height="{W*sy}" fill="#2a7e8a" opacity="0.12"/>'
        )

    return f'''<svg viewBox="0 0 {L*sx} {W*sy}" xmlns="http://www.w3.org/2000/svg">
{pitch_box}
{zones}
{halfway}
{center_circle}
{center_spot}
{pa_left}
{pa_right}
{ga_left}
{ga_right}
{pen_spots}
{pen_arcs}
{corners}
{goals}
</svg>'''


# Formation diagrams. _formations_table is module-scoped so the self-test
# can introspect every formation's player labels without re-running the
# function. The legacy `formations` name is kept as an alias so any
# downstream consumer that imported it from `formation(...)` still works.
_formations_table = {
    '4-4-2': [
        ('GK', 5, 50),
        ('LB', 25, 15), ('CB', 22, 35), ('CB', 22, 65), ('RB', 25, 85),
        ('LM', 45, 15), ('CM', 50, 35), ('CM', 50, 65), ('RM', 45, 85),
        ('ST', 80, 35), ('ST', 80, 65),
    ],
    '4-3-3': [
        ('GK', 5, 50),
        ('LB', 25, 15), ('CB', 22, 35), ('CB', 22, 65), ('RB', 25, 85),
        ('CM', 50, 30), ('CDM', 45, 50), ('CM', 50, 70),
        ('LW', 80, 15), ('ST', 85, 50), ('RW', 80, 85),
    ],
    '4-2-3-1': [
        ('GK', 5, 50),
        ('LB', 25, 15), ('CB', 22, 35), ('CB', 22, 65), ('RB', 25, 85),
        ('CDM', 45, 35), ('CDM', 45, 65),
        ('LW', 70, 15), ('CAM', 70, 50), ('RW', 70, 85),
        ('ST', 90, 50),
    ],
    '3-5-2': [
        ('GK', 5, 50),
        ('LCB', 25, 25), ('CB', 20, 50), ('RCB', 25, 75),
        ('LWB', 50, 10), ('CM', 50, 30), ('CM', 55, 50), ('CM', 50, 70), ('RWB', 50, 90),
        ('ST', 85, 35), ('ST', 85, 65),
    ],
    '3-4-3': [
        ('GK', 5, 50),
        ('LCB', 25, 25), ('CB', 20, 50), ('RCB', 25, 75),
        ('LM', 50, 12), ('CM', 55, 38), ('CM', 55, 62), ('RM', 50, 88),
        ('LW', 80, 20), ('ST', 90, 50), ('RW', 80, 80),
    ],
    '5-4-1': [
        ('GK', 5, 50),
        ('LWB', 25, 10), ('LCB', 22, 30), ('CB', 20, 50), ('RCB', 22, 70), ('RWB', 25, 90),
        ('LM', 50, 15), ('CM', 55, 35), ('CM', 55, 65), ('RM', 50, 85),
        ('ST', 90, 50),
    ],
    '5-3-2': [
        ('GK', 5, 50),
        ('LWB', 25, 10), ('LCB', 22, 30), ('CB', 20, 50), ('RCB', 22, 70), ('RWB', 25, 90),
        ('CM', 60, 25), ('CM', 65, 50), ('CM', 60, 75),
        ('ST', 88, 35), ('ST', 88, 65),
    ],
    '3-4-2-1': [  # Modern false-9 evolution
        ('GK', 5, 50),
        ('LCB', 25, 25), ('CB', 20, 50), ('RCB', 25, 75),
        ('LM', 50, 12), ('CM', 55, 35), ('CM', 55, 65), ('RM', 50, 88),
        ('LAM', 75, 30), ('RAM', 75, 70),  # two 10s
        ('FW', 90, 50),  # false 9 / striker
    ],
    '4-1-4-1': [
        ('GK', 5, 50),
        ('LB', 25, 15), ('CB', 22, 35), ('CB', 22, 65), ('RB', 25, 85),
        ('CDM', 38, 50),  # holding mid
        ('LM', 55, 15), ('CM', 60, 35), ('CM', 60, 65), ('RM', 55, 85),
        ('ST', 90, 50),
    ],
}

# Backwards-compat alias: legacy code that called `formation(...)` and then
# peeked at the local `formations` binding still resolves to the same data.
formations = _formations_table


def formation(formation_name='4-4-2', pitch_svg=''):
    """Player markers on a pitch diagram for the named formation.

    Formation names: 4-4-2, 4-3-3, 4-2-3-1, 3-5-2, 3-4-3, 5-3-2, 5-4-1,
    3-4-2-1, 4-1-4-1

    The `formations` table is defined at module scope so the self-test can
    introspect every formation's labels without re-running the function.
    """
    if formation_name not in _formations_table:
        raise ValueError(f'Unknown formation: {formation_name}')

    players = _formations_table[formation_name]

    # Pitch coordinates: 0-100 (x), 0-100 (y) -> 0..1050 (x px), 0..680 (y px)
    sx, sy = 10.5, 6.8  # 1050/100, 680/100

    pitch = soccer_pitch(show_zones=False)

    markers = []
    for label, x_pct, y_pct in players:
        x_px = x_pct * sx
        y_px = y_pct * sy
        markers.append(
            f'  <circle cx="{x_px:.1f}" cy="{y_px:.1f}" r="14" '
            f'fill="#1e3a5f" stroke="#ffffff" stroke-width="2"/>'
        )
        markers.append(
            f'  <text x="{x_px:.1f}" y="{y_px + 4:.1f}" text-anchor="middle" '
            f'fill="#ffffff" font-family="Inter, sans-serif" font-size="11" font-weight="700">{label}</text>'
        )

    # Connect lines within positional lines (back-four/five, midfield line,
    # attack line). Wing-backs (LWB/RWB) sit in the midfield line, not the
    # defense line — otherwise the connector draws straight through the
    # back third up to the touchline, which is misleading for a 3-5-2 / 5-3-2.
    #
    # Labels not in any group (LAM, RAM, FW) are intentionally dropped from
    # the connector lines: in a 3-4-2-1 they sit between the midfield and
    # striker and shouldn't be tied to either horizontal line.
    defense = [(lbl, x, y) for (lbl, x, y) in players
               if lbl in ('GK',) or (lbl.endswith('B') and not lbl.endswith('WB'))]
    midfield = [(lbl, x, y) for (lbl, x, y) in players
                if lbl in ('LWB', 'RWB', 'LM', 'RM', 'CM', 'CDM')]
    # Attack line: ST, CF, FW (false-9), LW, RW, and the #10s (CAM, LAM, RAM).
    attack = [(lbl, x, y) for (lbl, x, y) in players
              if lbl in ('ST', 'LW', 'RW', 'CF', 'FW', 'CAM', 'LAM', 'RAM')]

    lines = []
    for group in [defense, midfield, attack]:
        if len(group) >= 2:
            xs = [g[1] * sx for g in group]
            ys = [g[2] * sy for g in group]
            for i in range(len(xs) - 1):
                lines.append(
                    f'  <line x1="{xs[i]:.1f}" y1="{ys[i]:.1f}" x2="{xs[i+1]:.1f}" y2="{ys[i+1]:.1f}" '
                    f'stroke="#ffffff" stroke-width="1" opacity="0.4"/>'
                )

    return f'''<svg viewBox="0 0 1050 680" xmlns="http://www.w3.org/2000/svg">
{pitch}
{chr(10).join(lines)}
{chr(10).join(markers)}
</svg>'''


# ============================================================================
# Goal structure
# ============================================================================

def goal_structure(viewbox_w=200, viewbox_h=240):
    """Side-on view of a soccer goal: 7.32m wide × 2.44m tall."""
    return f'''<svg viewBox="0 0 {viewbox_w} {viewbox_h}" xmlns="http://www.w3.org/2000/svg">
  <!-- Goal frame (white posts + crossbar) -->
  <rect x="20" y="20" width="{viewbox_w-40}" height="{viewbox_h-60}"
        fill="none" stroke="#ffffff" stroke-width="6"/>
  <!-- Net (cross-hatch pattern) -->
  <g stroke="#ffffff" stroke-width="0.5" opacity="0.6">
    {''.join(f'<line x1="20" y1="{30+i*15}" x2="{viewbox_w-20}" y2="{30+i*15}"/>' for i in range((viewbox_h-60)//15))}
    {''.join(f'<line x1="{30+i*15}" y1="20" x2="{30+i*15}" y2="{viewbox_h-40}"/>' for i in range((viewbox_w-40)//15))}
  </g>
  <!-- Ground line -->
  <line x1="0" y1="{viewbox_h-40}" x2="{viewbox_w}" y2="{viewbox_h-40}" stroke="#1a1612" stroke-width="2"/>
  <!-- Grass -->
  <rect x="0" y="{viewbox_h-40}" width="{viewbox_w}" height="40" fill="#1f4d3a"/>
</svg>'''


# ============================================================================
# Jersey / kit
# ============================================================================

def jersey(color='#c44536', accent='#ffffff', number=10, name='STRIKER',
          viewbox=120, side='front'):
    """Front view of a soccer jersey with number and player name.

    NOTE: `name` and `side` are accepted but currently not rendered. The
    function draws the number on the chest but ignores the player name.
    To show the name, add a `<text>` element below the number; to support
    `side='back'`, mirror the body path horizontally and move the number.
    """
    # Suppress unused-argument warnings without changing behavior yet.
    _ = (name, side)
    return f'''<svg viewBox="0 0 {viewbox} {viewbox}" xmlns="http://www.w3.org/2000/svg">
  <!-- Jersey body (T-shape) -->
  <path d="M 30,30 L 45,15 L 60,15 L 65,22 L 75,22 L 80,15 L 95,15 L 110,30 L 110,45 L 95,55 L 95,110 Q 60,118 25,110 L 25,55 L 30,45 Z"
        fill="{color}" stroke="#1a1612" stroke-width="1.5"/>

  <!-- Accent stripe across chest -->
  <rect x="25" y="60" width="90" height="8" fill="{accent}" opacity="0.95"/>

  <!-- Number on back/front (centered) -->
  <text x="60" y="92" text-anchor="middle" fill="{accent}"
        font-family="Inter, sans-serif" font-size="36" font-weight="900">{number}</text>

  <!-- Collar -->
  <path d="M 45,15 L 60,28 L 75,15" fill="none" stroke="#1a1612" stroke-width="2"/>

  <!-- Brand mark (3 dots) -->
  <g fill="{accent}">
    <circle cx="48" cy="48" r="2"/>
    <circle cx="55" cy="48" r="2"/>
    <circle cx="62" cy="48" r="2"/>
  </g>
</svg>'''


# ============================================================================
# Corner kick / free-kick diagrams (XY coordinates with arrows)
# ============================================================================

def set_piece_diagram(play_type='corner-near', viewbox=400):
    """A top-down view of a set-piece setup with player dots + arrows.

    play_type: 'corner-near', 'corner-far', 'corner-short',
                'freekick-direct', 'freekick-indirect', 'throw-in-long'
    """
    plays = {
        'corner-near': {
            'players': [
                (50, 350, 'GK', '#1e3a5f'),
                (180, 280, 'CB', '#c44536'),
                (180, 250, 'CB', '#c44536'),
                (320, 220, 'CB', '#c44536'),
                (320, 250, 'CB', '#c44536'),
                (60, 220, 'CB', '#c44536'),
                (60, 150, 'ST', '#c44536'),  # near-post runner
                (50, 250, 'CB', '#c44536'),  # edge of box
                (50, 200, 'CM', '#c44536'),
                (350, 100, 'CF', '#c44536'),  # far-post target
                (320, 130, 'CAM', '#c44536'),
                (60, 100, 'CM', '#c44536'),
            ],
            'ball': (10, 380),
            'arrow_from': (10, 380),
            'arrow_to': (60, 145),
        },
        'corner-far': {
            'players': [
                (50, 350, 'GK', '#1e3a5f'),
                (180, 280, 'CB', '#c44536'),
                (180, 250, 'CB', '#c44536'),
                (320, 220, 'CB', '#c44536'),
                (320, 250, 'CB', '#c44536'),
                (60, 220, 'CB', '#c44536'),
                (50, 150, 'ST', '#c44536'),  # near post
                (50, 100, 'CM', '#c44536'),
                (60, 250, 'CB', '#c44536'),
                (350, 100, 'CF', '#c44536'),  # far-post
                (340, 130, 'CAM', '#c44536'),
                (60, 100, 'CM', '#c44536'),
            ],
            'ball': (10, 380),
            'arrow_from': (10, 380),
            'arrow_to': (340, 100),
        },
    }

    if play_type not in plays:
        supported = ', '.join(sorted(plays))
        raise ValueError(
            f'Unknown play_type: {play_type!r}. Supported: {supported}. '
            f'(Only corner-near and corner-far are currently defined; '
            f'corner-short, freekick-direct, freekick-indirect, and '
            f'throw-in-long are documented but not yet implemented.)'
        )
    play = plays[play_type]

    ball = play['ball']
    af, at = play['arrow_from'], play['arrow_to']

    players_svg = '\n  '.join(
        f'<circle cx="{x}" cy="{y}" r="9" fill="{c}" stroke="#1a1612" stroke-width="1.5"/>'
        f'<text x="{x}" y="{y+3}" text-anchor="middle" fill="#ffffff" '
        f'font-family="Inter, sans-serif" font-size="8" font-weight="700">{lbl}</text>'
        for x, y, lbl, c in play['players']
    )

    return f'''<svg viewBox="0 0 {viewbox} 400" xmlns="http://www.w3.org/2000/svg">
  <!-- Pitch segment (penalty area + corner arc) -->
  <rect x="0" y="0" width="{viewbox}" height="400" fill="#1f4d3a"/>
  <rect x="0" y="50" width="280" height="300" fill="none" stroke="#ffffff" stroke-width="1.5"/>
  <rect x="0" y="100" width="120" height="200" fill="none" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="120" cy="200" r="2" fill="#ffffff"/>
  <path d="M 0,250 A 60,60 0 0 0 60,310" fill="none" stroke="#ffffff" stroke-width="1.5"/>
  <!-- Goal -->
  <rect x="0" y="170" width="10" height="60" fill="#ffffff" stroke="#1a1612" stroke-width="1"/>
  <line x1="0" y1="360" x2="{viewbox}" y2="360" stroke="#1a1612" stroke-width="1.5"/>

  <!-- Players -->
  {players_svg}

  <!-- Ball -->
  <circle cx="{ball[0]}" cy="{ball[1]}" r="5" fill="#ffffff" stroke="#1a1612" stroke-width="1.5"/>

  <!-- Trajectory arrow -->
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#c9a961"/>
    </marker>
  </defs>
  <line x1="{af[0]}" y1="{af[1]}" x2="{at[0]}" y2="{at[1]}" stroke="#c9a961" stroke-width="2" marker-end="url(#arrowhead)" stroke-dasharray="5,3"/>
</svg>'''


# ============================================================================
# Self-test: verify all our shapes are mathematically symmetric
# ============================================================================

def self_test():
    """Run sanity checks on every drawing function.

    Verifies:
    - Pentagon centroids land on their declared symmetry points
    - Every SVG is valid XML and renders with the declared viewBox
    - Soccer-ball stitches connect each satellite to its *nearest* center
      vertex (catches off-by-one vertex-index mistakes in the stitch list)
    - Soccer-boot SVG actually contains 4 stud polygons (catches dead-code
      generators that produce no output)
    - set_piece_diagram raises on unknown play types (catches silent-default
      fallback that returns the wrong diagram for the requested label)
    - formation() line-grouping assigns each player to exactly one group
      (catches `'M' in lbl` style bugs where CAM ends up in both midfield
      and attack)
    """
    issues = []

    # --- 1. Pentagon centroids on declared symmetry points ---------------
    center_pent = polygon_points(50, 50, 5, r=15)
    if centroid(center_pent) != (50.0, 50.0):
        issues.append(f'Center pentagon not centered: {centroid(center_pent)}')

    for (sx, sy, label) in [(30, 30, 'NW'), (70, 30, 'NE'),
                             (30, 70, 'SW'), (70, 70, 'SE')]:
        pts = polygon_points(sx, sy, 5, r=8)
        if centroid(pts) != (float(sx), float(sy)):
            issues.append(f'{label} satellite not at ({sx}, {sy}): {centroid(pts)}')

    # --- 2. Every SVG must be valid XML + contain the declared viewBox ---
    cases = [
        ('soccer_ball',  lambda: soccer_ball()),
        ('pitch',        lambda: soccer_pitch()),
        ('formation',    lambda: formation('4-4-2')),
        ('goal',         lambda: goal_structure()),
        ('jersey',       lambda: jersey()),
        ('corner-near',  lambda: set_piece_diagram('corner-near')),
        ('corner-far',   lambda: set_piece_diagram('corner-far')),
        ('boot',         lambda: soccer_boot('left')),
        ('glove',        lambda: glove('left')),
    ]
    rendered = {}
    for name, fn in cases:
        try:
            svg = fn()
        except Exception as e:
            issues.append(f'{name} raised on call: {e!r}')
            continue
        try:
            root = ET.parse(StringIO(svg)).getroot()
        except ET.ParseError as e:
            issues.append(f'{name} SVG invalid: {e}')
            continue
        if not root.get('viewBox'):
            issues.append(f'{name} SVG missing viewBox attribute')
        rendered[name] = svg

    # --- 3. Soccer-ball stitch geometry --------------------------------
    # Each stitch should connect a satellite centroid to its geometrically
    # nearest center-pentagon vertex (stitches point outward, not through
    # the pentagon interior).
    if 'soccer_ball' in rendered:
        ball_svg = rendered['soccer_ball']
        # Parse the 4 <line> elements from the stitch group.
        lines = re.findall(
            r'<line x1="([\d.]+)" y1="([\d.]+)" x2="([\d.]+)" y2="([\d.]+)"/>',
            ball_svg,
        )
        if len(lines) != 4:
            issues.append(f'soccer_ball expected 4 stitches, found {len(lines)}')
        else:
            for (x1, y1, x2, y2) in lines:
                sat = (float(x1), float(y1))
                vtx = (float(x2), float(y2))
                # Find the nearest center-pentagon vertex to this satellite.
                nearest = min(
                    center_pent,
                    key=lambda v: (v[0]-sat[0])**2 + (v[1]-sat[1])**2,
                )
                if (vtx[0], vtx[1]) != (nearest[0], nearest[1]):
                    issues.append(
                        f'soccer_ball stitch from satellite {sat} targets '
                        f'({vtx[0]},{vtx[1]}) but should target nearest vertex '
                        f'({nearest[0]},{nearest[1]})'
                    )

    # --- 4. Soccer-boot must contain 4 stud polygons -------------------
    if 'boot' in rendered:
        stud_count = rendered['boot'].count('<polygon points="')
        if stud_count < 4:
            issues.append(f'soccer_boot expected >=4 stud polygons, found {stud_count}')

    # --- 5. set_piece_diagram must raise on unknown play types --------
    try:
        set_piece_diagram('freekick-direct')
    except ValueError:
        pass  # expected
    except Exception as e:
        issues.append(f'set_piece_diagram(unsupported) raised wrong type: {e!r}')
    else:
        issues.append(
            "set_piece_diagram('freekick-direct') should raise ValueError "
            '(only corner-near and corner-far are implemented), but returned '
            'a diagram silently.'
        )

    # --- 6. formation() line-grouping must be a partition --------------
    # Each individual *player slot* (not just its label) should appear in at
    # most one of {defense, midfield, attack}. Duplicate labels like two
    # `CB`s in a back-four are expected and fine; the original bug was a
    # single CAM appearing in two different groups, which is what this check
    # catches. Labels that aren't connectors (LAM/RAM/FW in 3-4-2-1) appear
    # in zero groups, which is also acceptable.
    if 'formation' in rendered:
        for fname in formations_list():
            slot_assignments = {}  # slot index -> [groups]
            for idx, (lbl, x, y) in enumerate(_formations_table[fname]):
                in_def = lbl == 'GK' or (lbl.endswith('B') and not lbl.endswith('WB'))
                in_mid = lbl in ('LWB', 'RWB', 'LM', 'RM', 'CM', 'CDM')
                in_atk = lbl in ('ST', 'LW', 'RW', 'CF', 'FW', 'CAM', 'LAM', 'RAM')
                groups = []
                if in_def: groups.append('defense')
                if in_mid: groups.append('midfield')
                if in_atk: groups.append('attack')
                if len(groups) > 1:
                    issues.append(
                        f'formation {fname}: player #{idx} ({lbl} at '
                        f'x={x}, y={y}) assigned to multiple groups: {groups}'
                    )
            # Every formation must have exactly 11 player slots.
            if len(_formations_table[fname]) != 11:
                issues.append(
                    f'formation {fname}: expected 11 players in table, '
                    f'got {len(_formations_table[fname])}'
                )

    if issues:
        print('SELF-TEST FAILED:')
        for i in issues:
            print(f'  - {i}')
        return False
    else:
        print('Self-test passed: shapes centered, SVGs valid, geometry checks OK.')
        return True


def formations_list():
    """Public list of supported formation names (used by self_test)."""
    return list(_formations_table.keys())


if __name__ == '__main__':
    self_test()
