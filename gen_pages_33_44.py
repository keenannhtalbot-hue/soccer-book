#!/usr/bin/env python3
"""
Pages 33-44 of The Soccer Book — Formations & Positions.
Each page renders ONE formation OR ONE position archetype
on an inline SVG pitch, with player dots coloured by role:
  GK       ->  gold           (#c9a961)
  Defenders -> navy           (#1e3a5f)
  Midfielders -> green        (#1f4d3a)
  Forwards   -> terracotta    (#c44536)

All 12 pages share the same pitch geometry (1000 x 690 SVG units,
aspect 1.45 : 1 matching the .pitch CSS class). Field markings are
drawn the same way on every page, then each page overlays its own
player layout and (for archetype pages) dotted-leader annotations.

References book.css for: page chrome, .pitch / .player-dot colour
tokens (--gold --navy --green --terracotta), .form-pill, .sidebar,
.factbox, .callout, .pill, .cap, etc.
"""
import os

PAGES_DIR = '/home/kbot/soccer-book/pages'
os.makedirs(PAGES_DIR, exist_ok=True)

# ---------- Pitch geometry constants (SVG units, 1000 x 690) ----------
W, H = 1000, 690
# Conversion helpers
def X(pct): return pct * W / 100          # 0..1000
def Y(pct): return pct * H / 100          # 0..690

# Colour tokens (mirrored from book.css for SVG use)
COL_GK       = '#c9a961'   # gold
COL_DEF      = '#1e3a5f'   # navy
COL_MID      = '#1f4d3a'   # green
COL_FWD      = '#c44536'   # terracotta
COL_PITCH_A  = '#4caf50'
COL_PITCH_B  = '#3d8b41'
COL_LINE     = 'rgba(255,255,255,0.75)'
COL_FAINT    = 'rgba(255,255,255,0.35)'
COL_INK      = '#1a1612'

# ---------- Pitch SVG fragment (drawn identically on every page) ----------
PITCH_DEFS = """
<defs>
  <linearGradient id="pitchG" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#5cba60"/>
    <stop offset="50%" stop-color="#4caf50"/>
    <stop offset="100%" stop-color="#3d8b41"/>
  </linearGradient>
  <pattern id="mow" x="0" y="0" width="40" height="40" patternUnits="userSpaceOnUse">
    <rect width="40" height="40" fill="none"/>
    <path d="M0 40 L40 0" stroke="rgba(255,255,255,0.04)" stroke-width="0.5"/>
  </pattern>
</defs>
"""

def pitch_marks():
    """White pitch markings: outline, halfway line, centre circle,
    penalty + goal areas on both ends, penalty spots, goal frames."""
    return f"""
<!-- Outer pitch outline -->
<rect x="3" y="3" width="{W-6}" height="{H-6}" fill="url(#pitchG)"/>
<rect x="3" y="3" width="{W-6}" height="{H-6}" fill="url(#mow)"/>
<rect x="3" y="3" width="{W-6}" height="{H-6}" fill="none" stroke="{COL_LINE}" stroke-width="3"/>

<!-- Halfway line + centre circle + centre spot -->
<line x1="{X(50)}" y1="3" x2="{X(50)}" y2="{H-3}" stroke="{COL_LINE}" stroke-width="2.5"/>
<circle cx="{X(50)}" cy="{Y(50)}" r="87" fill="none" stroke="{COL_LINE}" stroke-width="2.5"/>
<circle cx="{X(50)}" cy="{Y(50)}" r="3" fill="{COL_LINE}"/>

<!-- LEFT penalty area (16.5m x 40.32m = 15.7% x 59.3%) -->
<rect x="3" y="{Y(20.4)}" width="{X(15.7)}" height="{Y(59.3)}"
      fill="none" stroke="{COL_LINE}" stroke-width="2"/>
<!-- LEFT goal area (5.5m x 18.32m = 5.2% x 27%) -->
<rect x="3" y="{Y(36.5)}" width="{X(5.2)}" height="{Y(27)}"
      fill="none" stroke="{COL_LINE}" stroke-width="2"/>
<!-- LEFT penalty spot (11m from goal line) -->
<circle cx="{X(10.5)}" cy="{Y(50)}" r="4" fill="{COL_LINE}"/>
<!-- LEFT goal (7.32m wide = 10.8%) -->
<rect x="0" y="{Y(44.6)}" width="9" height="{Y(10.8)}" fill="{COL_LINE}" stroke="{COL_INK}" stroke-width="1"/>

<!-- RIGHT penalty area -->
<rect x="{X(84.3)}" y="{Y(20.4)}" width="{X(15.7)}" height="{Y(59.3)}"
      fill="none" stroke="{COL_LINE}" stroke-width="2"/>
<!-- RIGHT goal area -->
<rect x="{X(94.8)}" y="{Y(36.5)}" width="{X(5.2)}" height="{Y(27)}"
      fill="none" stroke="{COL_LINE}" stroke-width="2"/>
<!-- RIGHT penalty spot -->
<circle cx="{X(89.5)}" cy="{Y(50)}" r="4" fill="{COL_LINE}"/>
<!-- RIGHT goal -->
<rect x="{W-9}" y="{Y(44.6)}" width="9" height="{Y(10.8)}" fill="{COL_LINE}" stroke="{COL_INK}" stroke-width="1"/>

<!-- Corner arcs (small 1/4 circles at the corners) -->
<path d="M 3 {Y(3.5)} A {X(2)} {Y(2.5)} 0 0 0 {X(2.5)} 3" fill="none" stroke="{COL_LINE}" stroke-width="2"/>
<path d="M {W-3} {Y(3.5)} A {X(2)} {Y(2.5)} 0 0 1 {W-X(2.5)} 3" fill="none" stroke="{COL_LINE}" stroke-width="2"/>
<path d="M 3 {H-Y(3.5)} A {X(2)} {Y(2.5)} 0 0 0 {X(2.5)} {H-3}" fill="none" stroke="{COL_LINE}" stroke-width="2"/>
<path d="M {W-3} {H-Y(3.5)} A {X(2)} {Y(2.5)} 0 0 1 {W-X(2.5)} {H-3}" fill="none" stroke="{COL_LINE}" stroke-width="2"/>
"""

def player_dot(x_pct, y_pct, role, num, name=None, r=22):
    """One player dot on the pitch. role in {gk,def,mid,fwd}."""
    color = {'gk': COL_GK, 'def': COL_DEF, 'mid': COL_MID, 'fwd': COL_FWD}[role]
    cx, cy = X(x_pct), Y(y_pct)
    text_color = COL_INK if role == 'gk' else '#faf6ec'
    parts = [
        f'<circle cx="{cx}" cy="{cy}" r="{r+3}" fill="rgba(0,0,0,0.35)"/>',  # shadow
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}" stroke="#faf6ec" stroke-width="2"/>',
        f'<text x="{cx}" y="{cy+1}" font-family="\'Cormorant Garamond\', Georgia, serif" '
        f'font-size="20" font-weight="700" text-anchor="middle" dominant-baseline="middle" '
        f'fill="{text_color}">{num}</text>'
    ]
    if name:
        # Sub-label below the dot
        parts.append(
            f'<text x="{cx}" y="{cy+r+12}" font-family="\'Inter\',sans-serif" '
            f'font-size="11" font-weight="600" text-anchor="middle" '
            f'fill="#faf6ec" style="text-shadow: 0 0 3px black;">{name}</text>'
        )
    return '\n'.join(parts)


def leader(x_pct, y_pct, tx, ty, text, anchor='start', color=None):
    """Dotted leader line from a point on the pitch to an external label.
    tx, ty are viewBox coords. text is shown beside (tx, ty).
    """
    color = color or COL_INK
    cx, cy = X(x_pct), Y(y_pct)
    return (
        f'<line x1="{cx}" y1="{cy}" x2="{tx}" y2="{ty}" '
        f'stroke="{COL_INK}" stroke-width="0.7" stroke-dasharray="3,3" opacity="0.85"/>'
        f'<circle cx="{tx}" cy="{ty}" r="2.5" fill="{COL_INK}"/>'
        f'<rect x="{tx + (4 if anchor=="start" else -4 - 168)}" y="{ty-12}" width="168" height="22" '
        f'rx="3" fill="#faf6ec" stroke="{color}" stroke-width="1.4" opacity="0.97"/>'
        f'<text x="{tx + (8 if anchor=="start" else -4)}" y="{ty+3}" font-family="\'Inter\',sans-serif" '
        f'font-size="10.5" font-weight="600" text-anchor="{anchor}" fill="{color}">{text}</text>'
    )


def arch_chip(x_pct, y_pct, title, body, color):
    """Inline labeled chip on the pitch: a coloured chip with title + body."""
    cx, cy = X(x_pct), Y(y_pct)
    return (
        f'<g transform="translate({cx},{cy})">'
        f'<rect x="-90" y="-22" width="180" height="44" rx="3" '
        f'fill="#faf6ec" stroke="{color}" stroke-width="1.4"/>'
        f'<rect x="-90" y="-22" width="6" height="44" fill="{color}"/>'
        f'<text x="-78" y="-7" font-family="\'Inter\',sans-serif" '
        f'font-size="9.5" font-weight="700" fill="{color}" letter-spacing="0.05em">{title.upper()}</text>'
        f'<text x="-78" y="9" font-family="\'Inter\',sans-serif" '
        f'font-size="9" fill="#1a1612">{body}</text>'
        f'</g>'
    )


def formation_svg_body(players, kicker=None, extra_svg=''):
    """Render the pitch + players. players is a list of dicts:
        {'x': int, 'y': int, 'role': str, 'num': int, 'name': str (opt)}
    extra_svg is appended after players (used for leader annotations).
    """
    body = pitch_marks()
    # players drawn FIRST so leaders / chips sit ON TOP
    body += ''.join(
        player_dot(
            x_pct=p['x'], y_pct=p['y'],
            role=p['role'], num=p['num'], name=p.get('name')
        ) for p in players
    )
    body += extra_svg
    return body


def wrap_diagram(kicker, formation_code, svg_body, caption):
    """Wrap an SVG body in the diagram block used by the page."""
    code_pill = ''
    if formation_code:
        code_pill = (
            f'<div style="text-align:center; margin-bottom: 0.12in;">'
            f'<span class="form-pill">{formation_code}</span></div>'
        )
    kicker_html = (
        f'<div class="kicker" style="text-align:center;margin-bottom:0.08in;">{kicker}</div>'
        if kicker else ''
    )
    return (
        f'<div class="diagram" style="padding:0.18in;">'
        f'{kicker_html}'
        f'{code_pill}'
        f'<svg viewBox="0 0 {W} {H}" style="width:100%; height:auto; display:block; '
        f'border:0.03in solid var(--rule); border-radius:0.04in;">'
        f'{PITCH_DEFS}{svg_body}</svg>'
        f'<p class="cap">{caption}</p>'
        f'</div>'
    )


# ---------- Page writer ----------
def page(num, title, header_subtitle='Section III', body_html='', layout=''):
    cls = f'page {layout}' if layout else 'page'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Page {num} — {title}</title>
<link rel="stylesheet" href="book.css">
</head>
<body class="{cls}">
<div class="page-inner">

<div class="page-header">
  <div class="page-num">{num}</div>
  <div><div class="section-num">{header_subtitle}</div><h1 class="section-title">{title}</h1></div>
</div>

{body_html}

</div>
</body>
</html>
"""


# ============================================================
# PAGES 33-44
# ============================================================

# ---------- Page 33: 4-4-2 classic ----------
def page33():
    players = [
        {'x':4,  'y':50, 'role':'gk',  'num':1,  'name':'GK'},
        {'x':18, 'y':12, 'role':'def', 'num':3,  'name':'LB'},
        {'x':22, 'y':32, 'role':'def', 'num':5,  'name':'LCB'},
        {'x':22, 'y':68, 'role':'def', 'num':6,  'name':'RCB'},
        {'x':18, 'y':88, 'role':'def', 'num':2,  'name':'RB'},
        {'x':40, 'y':12, 'role':'mid', 'num':11, 'name':'LM'},
        {'x':40, 'y':38, 'role':'mid', 'num':8,  'name':'LCM'},
        {'x':40, 'y':62, 'role':'mid', 'num':4,  'name':'RCM'},
        {'x':40, 'y':88, 'role':'mid', 'num':7,  'name':'RM'},
        {'x':50, 'y':36, 'role':'fwd', 'num':10, 'name':'LST'},
        {'x':50, 'y':64, 'role':'fwd', 'num':9,  'name':'RST'},
    ]
    diagram = wrap_diagram(
        kicker='The 4-4-2',
        formation_code='4 – 4 – 2',
        svg_body=formation_svg_body(players),
        caption='Two banks of four and two strikers. The shape that defined English football for forty years, from the 1966 World Cup winners to the Premier League’s first decade.'
    )
    body = f"""
<div class="two-col">
  <div>
    <p class="lead">Two flat banks of four, two strikers up top. The defining shape of the British game — and, with variations, of most European football — for the latter half of the twentieth century.</p>
    <p>The <strong>4-4-2</strong> balances the pitch in three zones: four defenders form a flat back line; four midfielders split into pairs (wide and central); two strikers lead the press and the counter-attack. Width comes from the full-backs and the wide midfielders.</p>
    <p>Its weakness is structural: against a deep-lying <em>regista</em> and a mobile front four (the 4-2-3-1), the two strikers can be outnumbered in central midfield, and the flat-back-four concedes space between the lines.</p>
    <div class="sidebar green" style="margin-top:0.25in;">
      <h3>Hall of fame</h3>
      <p style="font-size:8.5pt;"><b>Brazil 1970</b>, <b>AC Milan 1988–90</b>, <b>Manchester United 1998–99</b>, <b>Leicester City 2015–16</b> — four of the great 4-4-2 sides, separated by three decades and three continents.</p>
    </div>
    <div class="callout" style="margin-top:0.2in;">
      <h3 style="font-size:10pt; margin-bottom:0.06in;">Why it endures</h3>
      <p style="font-size:8.5pt; margin:0;">Every coach knows where their next pass is going. Players learn the shape from age seven. Recruitment is simple — find a full-back, two centre-backs, four midfielders, two strikers.</p>
    </div>
  </div>
  <div>{diagram}</div>
</div>
"""
    return page(33, 'The 4-4-2 classic', body_html=body, layout='formation formation-442')


# ---------- Page 34: 4-3-3 ----------
def page34():
    players = [
        {'x':4,  'y':50, 'role':'gk',  'num':1,  'name':'GK'},
        {'x':18, 'y':8,  'role':'def', 'num':3,  'name':'LB'},
        {'x':20, 'y':30, 'role':'def', 'num':4,  'name':'LCB'},
        {'x':20, 'y':70, 'role':'def', 'num':5,  'name':'RCB'},
        {'x':18, 'y':92, 'role':'def', 'num':2,  'name':'RB'},
        {'x':35, 'y':50, 'role':'mid', 'num':6,  'name':'CDM'},
        {'x':42, 'y':28, 'role':'mid', 'num':8,  'name':'LCM'},
        {'x':42, 'y':72, 'role':'mid', 'num':10, 'name':'RCM'},
        {'x':65, 'y':15, 'role':'fwd', 'num':11, 'name':'LW'},
        {'x':68, 'y':50, 'role':'fwd', 'num':9,  'name':'CF'},
        {'x':65, 'y':85, 'role':'fwd', 'num':7,  'name':'RW'},
    ]
    diagram = wrap_diagram(
        kicker='The 4-3-3',
        formation_code='4 – 3 – 3',
        svg_body=formation_svg_body(players),
        caption='A back four, a midfield three, and a front line of a striker flanked by two wingers. The shape that became the global standard under Guardiola, Klopp, and the Spanish national team.'
    )
    body = f"""
<div class="two-col">
  <div>
    <p class="lead">A back four, a midfield three, and a front three built around a centre-forward with two wingers. The 4-3-3 is the modern standard — it became dominant after Spain won Euro 2008 and the 2010 World Cup with it.</p>
    <p>Its strength is <strong>numerical superiority in midfield</strong>: three against two (versus a 4-4-2), plus a <em>free eighth</em> that drops into the half-space to create passing triangles. The trade-off is a single striker — that requires a complete number 9.</p>
    <p>Variants include the <b>4-3-3 false 9</b> (no striker — the centre-forward drops deep), the <b>4-1-4-1</b> (defensive six shielding the back four), and the inverted <b>4-3-3</b> where the wide forwards tuck inside.</p>
    <div class="sidebar terracotta" style="margin-top:0.25in;">
      <h3>Hall of fame</h3>
      <p style="font-size:8.5pt;"><b>Ajax 1995</b> (Louis van Gaal), <b>Barcelona 2008–12</b> (Guardiola), <b>Spain 2008–12</b>, <b>Liverpool 2017–19</b> (Klopp). Each played the shape with extreme attacking intent.</p>
    </div>
    <div class="callout" style="margin-top:0.2in;">
      <h3 style="font-size:10pt; margin-bottom:0.06in;">The inverted full-back</h3>
      <p style="font-size:8.5pt; margin:0;">The defining tactical trick of the modern 4-3-3: when the winger tucks inside, the full-back steps into the wide midfield slot, creating a back-three-with-midfield-three structure that traps the opposition.</p>
    </div>
  </div>
  <div>{diagram}</div>
</div>
"""
    return page(34, 'The 4-3-3 modern standard', body_html=body, layout='formation formation-433')


# ---------- Page 35: 4-2-3-1 ----------
def page35():
    players = [
        {'x':4,  'y':50, 'role':'gk',  'num':1, 'name':'GK'},
        {'x':18, 'y':8,  'role':'def', 'num':3, 'name':'LB'},
        {'x':20, 'y':30, 'role':'def', 'num':5, 'name':'LCB'},
        {'x':20, 'y':70, 'role':'def', 'num':4, 'name':'RCB'},
        {'x':18, 'y':92, 'role':'def', 'num':2, 'name':'RB'},
        {'x':32, 'y':38, 'role':'mid', 'num':6, 'name':'CDM-L'},
        {'x':32, 'y':62, 'role':'mid', 'num':8, 'name':'CDM-R'},
        {'x':48, 'y':12, 'role':'mid', 'num':11,'name':'LAM'},
        {'x':50, 'y':50, 'role':'mid', 'num':10,'name':'CAM'},
        {'x':48, 'y':88, 'role':'mid', 'num':7, 'name':'RAM'},
        {'x':65, 'y':50, 'role':'fwd', 'num':9, 'name':'ST'},
    ]
    diagram = wrap_diagram(
        kicker='The 4-2-3-1',
        formation_code='4 – 2 – 3 – 1',
        svg_body=formation_svg_body(players),
        caption='A double pivot in front of the back four, three attacking midfielders, and a lone striker. The shape of choice for Löw’s Germany, Deschamps’ France, and most modern Champions League sides.'
    )
    body = f"""
<div class="two-col">
  <div>
    <p class="lead">A <strong>double pivot</strong> of two defensive midfielders sits in front of the back four; behind the striker, three attacking midfielders split wide-and-central. The 4-2-3-1 is the modern tactical lingua franca.</p>
    <p>Why? It works <strong>against anything</strong>. The double-pivot outnumbers a single opposing striker and provides cover against a 4-3-3; the front three overloads the back four of a 4-4-2. Against another 4-2-3-1, it becomes a tactical chess match.</p>
    <p>The shape asks two things of the wide attackers (LAM and RAM): come back to defend, and go past the full-backs to attack. Classic examples: <b>Ribéry</b>, <b>Robben</b>, <b>Bale</b>, <b>Mbappé</b>.</p>
    <div class="sidebar navy" style="margin-top:0.25in;">
      <h3>Where it runs</h3>
      <p style="font-size:8.5pt;"><b>Germany 2014</b> (Löw), <b>France 2018</b> (Deschamps), <b>Real Madrid 2014–18</b>, <b>Liverpool 2018–20</b>. The template has won five of the last six major international tournaments.</p>
    </div>
    <div class="callout" style="margin-top:0.2in;">
      <h3 style="font-size:10pt; margin-bottom:0.06in;">Flexibility</h3>
      <p style="font-size:8.5pt; margin:0;">In attack, the formation is effectively a 4-3-3 (CAMS push wide, ST holds the line). In defence, it is a 4-5-1 (CAM drops to the pivot). One shape, two looks — the half-time tactical switch is built in.</p>
    </div>
  </div>
  <div>{diagram}</div>
</div>
"""
    return page(35, 'The 4-2-3-1 — flexibility king', body_html=body, layout='formation formation-4231')


# ---------- Page 36: 3-5-2 ----------
def page36():
    players = [
        {'x':4,  'y':50, 'role':'gk',  'num':1, 'name':'GK'},
        {'x':18, 'y':22, 'role':'def', 'num':6, 'name':'LCB'},
        {'x':18, 'y':50, 'role':'def', 'num':5, 'name':'CB'},
        {'x':18, 'y':78, 'role':'def', 'num':4, 'name':'RCB'},
        {'x':30, 'y':8,  'role':'mid', 'num':11,'name':'LWB'},
        {'x':30, 'y':92, 'role':'mid', 'num':2, 'name':'RWB'},
        {'x':40, 'y':28, 'role':'mid', 'num':8, 'name':'LCM'},
        {'x':40, 'y':50, 'role':'mid', 'num':10,'name':'CM'},
        {'x':40, 'y':72, 'role':'mid', 'num':7, 'name':'RCM'},
        {'x':62, 'y':38, 'role':'fwd', 'num':9, 'name':'LST'},
        {'x':62, 'y':62, 'role':'fwd', 'num':99,'name':'RST'},
    ]
    diagram = wrap_diagram(
        kicker='The 3-5-2',
        formation_code='3 – 5 – 2',
        svg_body=formation_svg_body(players),
        caption='Three centre-backs, wing-back corridors the length of the pitch, a midfield three, and two strikers. The shape of Antonio Conte, the Italian national team, and the 1990s Serie A.'
    )
    body = f"""
<div class="two-col">
  <div>
    <p class="lead">Three centre-backs for width in defence, two <strong>wing-backs</strong> who cover the entire touchline, a midfield three, and two strikers. The 3-5-2 is the formation of the Italian school — and, lately, of Antonio Conte.</p>
    <p>The trade is stark: the wing-backs give you <strong>two extra players in midfield</strong>, but leave huge channels behind them. If the wing-backs are caught high, the outside centre-backs are exposed one-on-one against opposing wingers.</p>
    <p>Three at the back demands three centre-backs who can play — one ball-playing sweeper, two aggressive markers. The shape has come back in cycles: <b>Bergomi-Baresi-Costacurta</b> for Milan, <b>Bonucci-Chiellini-Barzagli</b> for Juventus and Italy.</p>
    <div class="sidebar green" style="margin-top:0.25in;">
      <h3>Hall of fame</h3>
      <p style="font-size:8.5pt;"><b>Juventus 2015–17</b>, <b>Italy 1990</b> (Sacco), <b>Chelsea 2016–17</b> (Conte), <b>Inter 2020–21</b> (Conte). One shape, multiple success stories.</p>
    </div>
    <div class="callout" style="margin-top:0.2in;">
      <h3 style="font-size:10pt; margin-bottom:0.06in;">The wing-back engine</h3>
      <p style="font-size:8.5pt; margin:0;">In a 3-5-2, the wing-back covers more ground than any other player on the pitch — typically 11–12 km per match, the highest of any outfield role. <b>Jardel, Hakimi, Perisic</b> — all are essentially wingers wearing defensive jerseys.</p>
    </div>
  </div>
  <div>{diagram}</div>
</div>
"""
    return page(36, 'The 3-5-2 — wing-back era', body_html=body, layout='formation formation-352')


# ---------- Page 37: 3-4-2-1 false 9 ----------
def page37():
    players = [
        {'x':4,  'y':50, 'role':'gk',  'num':1, 'name':'GK'},
        {'x':18, 'y':22, 'role':'def', 'num':5, 'name':'LCB'},
        {'x':18, 'y':50, 'role':'def', 'num':6, 'name':'CB'},
        {'x':18, 'y':78, 'role':'def', 'num':4, 'name':'RCB'},
        {'x':28, 'y':8,  'role':'mid', 'num':3, 'name':'LWB'},
        {'x':28, 'y':92, 'role':'mid', 'num':2, 'name':'RWB'},
        {'x':40, 'y':35, 'role':'mid', 'num':8, 'name':'LCM'},
        {'x':40, 'y':65, 'role':'mid', 'num':10,'name':'RCM'},
        {'x':52, 'y':28, 'role':'mid', 'num':11,'name':'LAM'},
        {'x':52, 'y':72, 'role':'mid', 'num':7, 'name':'RAM'},
        {'x':65, 'y':50, 'role':'fwd', 'num':9, 'name':'F9'},
    ]
    diagram = wrap_diagram(
        kicker='The 3-4-2-1 false 9',
        formation_code='3 – 4 – 2 – 1',
        svg_body=formation_svg_body(players),
        caption='Three centre-backs, wing-backs, two #10s behind a striker who drops to receive between the lines. The shape that defined Spain 2012, Barcelona under Messi, and Guardiola’s Manchester City.'
    )
    body = f"""
<div class="two-col">
  <div>
    <p class="lead">A back three, a midfield four (wing-backs plus two central midfielders), two <strong>#10s</strong> tucked behind a <em>false nine</em> — a striker who drops deep to receive and let wing-backs or #10s run in behind.</p>
    <p>The false nine is the key. With no traditional number 9 to mark, opposing centre-backs must decide: follow the false nine into midfield (and leave the back line exposed), or hold the line (and let the false nine receive unopposed). <b>Messi</b>, <b>Fàbregas</b> for Spain at Euro 2012, and <b>Haaland</b> at times for City have all played the role.</p>
    <p>The shape is a <em>front</em>-five in possession (the two #10s and three centre-backs funnel into passing lanes) and a <em>back</em>-five out of possession (the wing-backs drop to the back four).</p>
    <div class="sidebar terracotta" style="margin-top:0.25in;">
      <h3>Hall of fame</h3>
      <p style="font-size:8.5pt;"><b>Spain 2012</b>, <b>Barcelona 2009–15</b>, <b>Manchester City 2022–24</b>. Each squeezed through the centre by giving the false nine freedom to roam.</p>
    </div>
    <div class="callout" style="margin-top:0.2in;">
      <h3 style="font-size:10pt; margin-bottom:0.06in;">The problem of the #10</h3>
      <p style="font-size:8.5pt; margin:0;">Two #10s behind one striker means three players in a 20-metre zone between the lines. Brilliant to play in, hard to defend transitions from — the 3-4-2-1 is vulnerable to a single deep ball over the top into the space vacated by the false nine.</p>
    </div>
  </div>
  <div>{diagram}</div>
</div>
"""
    return page(37, 'The 3-4-2-1 false-9 evolution', body_html=body, layout='formation formation-3421')


# ---------- Page 38: 4-1-4-1 defensive block ----------
def page38():
    players = [
        {'x':4,  'y':50, 'role':'gk',  'num':1, 'name':'GK'},
        {'x':15, 'y':8,  'role':'def', 'num':3, 'name':'LB'},
        {'x':17, 'y':30, 'role':'def', 'num':5, 'name':'LCB'},
        {'x':17, 'y':70, 'role':'def', 'num':4, 'name':'RCB'},
        {'x':15, 'y':92, 'role':'def', 'num':2, 'name':'RB'},
        {'x':26, 'y':50, 'role':'mid', 'num':6, 'name':'CDM'},
        {'x':38, 'y':12, 'role':'mid', 'num':11,'name':'LM'},
        {'x':38, 'y':38, 'role':'mid', 'num':8, 'name':'LCM'},
        {'x':38, 'y':62, 'role':'mid', 'num':10,'name':'RCM'},
        {'x':38, 'y':88, 'role':'mid', 'num':7, 'name':'RM'},
        {'x':50, 'y':50, 'role':'fwd', 'num':9, 'name':'ST'},
    ]
    diagram = wrap_diagram(
        kicker='The 4-1-4-1',
        formation_code='4 – 1 – 4 – 1',
        svg_body=formation_svg_body(players),
        caption='A back four, a single defensive midfielder (the anchor), a bank of four midfielders, and one striker. The shape of choice for teams playing on the counter — Atlético Madrid under Simeone in particular.'
    )
    body = f"""
<div class="two-col">
  <div>
    <p class="lead">A back four, a <strong>single defensive midfielder</strong> as a shield, a flat line of four ahead of them, and a lone striker. The 4-1-4-1 is the formation for <em>the team without the ball</em> — the deep block that makes space look small.</p>
    <p>The aim is to compress play into a <strong>30-metre band</strong> in front of the box. The four-bank-mid-four press any pass into that band, the striker closes the centre-backs’ passing lane, and the anchor screens the back four.</p>
    <p>The trade-off: it concedes possession. <b>Atlético Madrid under Simeone</b> averaged <strong>43% possession</strong> in La Liga with it — but won two league titles, two Europa Leagues, and reached two Champions League finals.</p>
    <div class="sidebar navy" style="margin-top:0.25in;">
      <h3>Hall of fame</h3>
      <p style="font-size:8.5pt;"><b>Atlético Madrid 2013–16</b> (Simeone), <b>Leicester City 2015–16</b> (Ranieri), <b>Chelsea 2004–06</b> (Mourinho’s first Chelsea). The underdog’s shape.</p>
    </div>
    <div class="callout" style="margin-top:0.2in;">
      <h3 style="font-size:10pt; margin-bottom:0.06in;">The anchor’s job</h3>
      <p style="font-size:8.5pt; margin:0;">The single pivot (the 6) is the most isolated role on the pitch — no partner to share the work. <b>Busquets</b>, <b>Kanté</b>, <b>Casemiro</b>: each is a one-man midfield, screening four defenders and launching the counter from the half-turn.</p>
    </div>
  </div>
  <div>{diagram}</div>
</div>
"""
    return page(38, 'The 4-1-4-1 — defensive block', body_html=body, layout='formation formation-4141')


# ---------- Page 39: 5-3-2 parked bus ----------
def page39():
    players = [
        {'x':4,  'y':50, 'role':'gk',  'num':1, 'name':'GK'},
        {'x':12, 'y':18, 'role':'def', 'num':6, 'name':'LCB'},
        {'x':12, 'y':50, 'role':'def', 'num':5, 'name':'CB'},
        {'x':12, 'y':82, 'role':'def', 'num':4, 'name':'RCB'},
        {'x':16, 'y':5,  'role':'def', 'num':3, 'name':'LWB'},
        {'x':16, 'y':95, 'role':'def', 'num':2, 'name':'RWB'},
        {'x':28, 'y':25, 'role':'mid', 'num':8, 'name':'LCM'},
        {'x':28, 'y':50, 'role':'mid', 'num':6, 'name':'CM'},
        {'x':28, 'y':75, 'role':'mid', 'num':10,'name':'RCM'},
        {'x':50, 'y':38, 'role':'fwd', 'num':9, 'name':'LST'},
        {'x':50, 'y':62, 'role':'fwd', 'num':7, 'name':'RST'},
    ]
    diagram = wrap_diagram(
        kicker='The 5-3-2',
        formation_code='5 – 3 – 2',
        svg_body=formation_svg_body(players),
        caption='Three centre-backs plus two wing-backs in a defensive five, a midfield three, and two strikers up top. The formation of the underdog defending a one-goal lead in the 89th minute — the "parked bus".'
    )
    body = f"""
<div class="two-col">
  <div>
    <p class="lead">Five defenders, three midfielders, two strikers. The 5-3-2 is football’s <strong>emergency shape</strong> — played for a half, a quarter, or a full match by a team protecting a lead against a superior opponent. The “parked bus”.</p>
    <p>José Mourinho named it: <em>“if you have 11 men behind the ball, what is the point of having the ball?”</em> The 5-3-2 minimises <em>central</em> space — the wing-backs tuck in to make a five, the three centre-backs mark the striker, the three midfielders screen the box.</p>
    <p>When the equaliser comes, it usually comes from a set piece — because open play is impossible. The 5-3-2 concedes corners and crosses. <b>Inter 2010</b> (Mourinho) won the Champions League playing it in the knockout rounds.</p>
    <div class="sidebar terracotta" style="margin-top:0.25in;">
      <h3>Hall of fame</h3>
      <p style="font-size:8.5pt;"><b>Inter 2010</b> (Mourinho’s treble), <b>Greece 2004</b> (Rehhagel’s Euro win), <b>Switzerland 2010</b> (held Spain 1–0 in the World Cup opener). Defensive art.</p>
    </div>
    <div class="callout" style="margin-top:0.2in;">
      <h3 style="font-size:10pt; margin-bottom:0.06in;">When to play it</h3>
      <p style="font-size:8.5pt; margin:0;">Only as a reaction: a half-time tactical switch, a red-card response, or a European tie against a much stronger opponent. As a default shape, the 5-3-2 concedes too many shots over 90 minutes.</p>
    </div>
  </div>
  <div>{diagram}</div>
</div>
"""
    return page(39, 'The 5-3-2 — parked bus', body_html=body, layout='formation formation-532')


# ---------- Page 40: 4-3-1-2 Christmas tree ----------
def page40():
    players = [
        {'x':4,  'y':50, 'role':'gk',  'num':1, 'name':'GK'},
        {'x':18, 'y':8,  'role':'def', 'num':3, 'name':'LB'},
        {'x':20, 'y':30, 'role':'def', 'num':5, 'name':'LCB'},
        {'x':20, 'y':70, 'role':'def', 'num':4, 'name':'RCB'},
        {'x':18, 'y':92, 'role':'def', 'num':2, 'name':'RB'},
        {'x':32, 'y':30, 'role':'mid', 'num':6, 'name':'LCM'},
        {'x':32, 'y':70, 'role':'mid', 'num':8, 'name':'RCM'},
        {'x':32, 'y':50, 'role':'mid', 'num':10,'name':'CM'},
        {'x':46, 'y':50, 'role':'mid', 'num':9, 'name':'CAM'},
        {'x':60, 'y':38, 'role':'fwd', 'num':11,'name':'LST'},
        {'x':60, 'y':62, 'role':'fwd', 'num':7, 'name':'RST'},
    ]
    diagram = wrap_diagram(
        kicker='The 4-3-1-2',
        formation_code='4 – 3 – 1 – 2',
        svg_body=formation_svg_body(players),
        caption='A midfield three, a #10 tucked behind two strikers, no wingers. The formation that narrows the pitch and overloads the centre. Italian tradition — and a Mourinho favourite.'
    )
    body = f"""
<div class="two-col">
  <div>
    <p class="lead">Sometimes called the <em>albero di Natale</em> — the Christmas tree — because the shape narrows upward from the four-defender base to a single number 10, with two strikers at the top. Drawn schematically, the dots look like a fir tree.</p>
    <p>The 4-3-1-2 is a <strong>central-overload</strong> shape: no wingers, no natural width. The full-backs must bomb on, the #10 must drop deep, the two strikers must press as a pair. In exchange: numerical dominance in central midfield and a constant passing triangle around the box.</p>
    <p>The trade-off is <strong>width</strong>. Against a 4-4-2 sitting deep, the Christmas tree can find no crossing angle. The shape demands a creative #10 (a <em>trequartista</em>) and two strikers who interchange — the older the football culture, the more naturally this comes.</p>
    <div class="sidebar green" style="margin-top:0.25in;">
      <h3>Hall of fame</h3>
      <p style="font-size:8.5pt;"><b>AC Milan 1988–90</b> (Sacchi), <b>Juventus 1995–96</b> (Lippi), <b>Real Madrid 2013–14</b> (Ancelotti, ’La Décima’), <b>Chelsea 2013–14</b> (Mourinho). Italian-bred.</p>
    </div>
    <div class="callout" style="margin-top:0.2in;">
      <h3 style="font-size:10pt; margin-bottom:0.06in;">The trequartista</h3>
      <p style="font-size:8.5pt; margin:0;">The single #10 — “three-quarter” in Italian, between the midfield and the strikers — is the formation’s reason for being. <b>Cassano</b>, <b>Baggio</b>, <b>Del Piero</b>, <b>Özil</b>: the role is a playmaker, not a finisher.</p>
    </div>
  </div>
  <div>{diagram}</div>
</div>
"""
    return page(40, 'The 4-3-1-2 — Christmas tree', body_html=body, layout='formation formation-4312')


# ---------- Page 41: GK roles (archetype page) ----------
def page41():
    # Four GK archetypes on the pitch — each at a different depth (the higher
    # the dot, the more progressive the role). Dotted leaders from each dot
    # to a labelled chip on the right side of the pitch.
    players = [
        {'x':8,  'y':50, 'role':'gk', 'num':1, 'name':'SS'},   # stays on line
        {'x':16, 'y':35, 'role':'gk', 'num':2, 'name':'SK'},   # behind high line
        {'x':22, 'y':22, 'role':'gk', 'num':3, 'name':'AG'},   # aggressive / sweeper-up
        {'x':16, 'y':65, 'role':'gk', 'num':4, 'name':'CO'},   # build-out / play
    ]
    # Chips on the right (each describes one archetype)
    extras = [
        arch_chip(72, 14, 'Traditional shot-stopper',
                  'Stays on the line; reaction specialist.',
                  COL_GK),
        arch_chip(72, 38, 'Sweeper-keeper',
                  'Plays behind a high line; covers through-balls.',
                  COL_GK),
        arch_chip(72, 62, 'Aggressive / sweeper-up',
                  'Charges 1v1s; smothers strikers early.',
                  COL_GK),
        arch_chip(72, 88, 'Distributed / build-out',
                  'Starts attacks; plays short under pressure.',
                  COL_GK),
    ]
    # Dotted leader lines from the four DOTS to the four CHIPS
    mapping = [
        ((8,  50), (72, 14)),   # SS  ->  shot-stopper
        ((16, 35), (72, 38)),   # SK  ->  sweeper-keeper
        ((22, 22), (72, 62)),   # AG  ->  aggressive
        ((16, 65), (72, 88)),   # CO  ->  build-out
    ]
    leader_lines = []
    for (sx, sy), (ex, ey) in mapping:
        cx, cy = X(sx), Y(sy)
        ex2, ey2 = X(ex-9), Y(ey)
        leader_lines.append(
            f'<line x1="{cx}" y1="{cy}" x2="{ex2}" y2="{ey2}" '
            f'stroke="{COL_INK}" stroke-width="0.7" stroke-dasharray="3,3" opacity="0.85"/>'
            f'<circle cx="{ex2}" cy="{ey2}" r="2.5" fill="{COL_INK}"/>'
        )
    extras += leader_lines
    extra = ''.join(extras)
    diagram = wrap_diagram(
        kicker='The four goalkeeper roles',
        formation_code='GK 1–4',
        svg_body=formation_svg_body(players, extra_svg=extra),
        caption='Modern goalkeepers are not interchangeable. Four archetypes, defined by how high they play and what they do with their feet.'
    )
    body = f"""
<div class="two-col">
  <div>
    <p class="lead">A goalkeeper is a position; the goalkeeper’s role is a choice. Modern football distinguishes at least four GK archetypes — defined by where they start, how far they come off their line, and what they do with the ball at their feet.</p>
    <p>The trend across the last decade is clear: the modern keeper starts <strong>higher</strong> and <strong>passes shorter</strong>. Of the 16 keepers at the 2022 World Cup, every one was expected to play short under pressure. The traditional line-hugger is essentially extinct.</p>
    <h3 style="font-family:var(--serif);color:var(--green);font-size:12pt;margin:0.2in 0 0.06in;">On the diagram</h3>
    <p style="font-size:9pt;">Four positions inside or just outside the penalty area, each labelled by dotted leader to a chip on the right. The deeper the dot sits, the more reactive the GK; the higher, the more progressive.</p>
  </div>
  <div>{diagram}</div>
</div>

<div style="margin-top:0.2in; display:grid; grid-template-columns: repeat(2, 1fr); gap:0.18in;">
  <div class="sidebar gold">
    <h3 style="font-size:11pt;">Shot-stopper</h3>
    <p style="font-size:8.5pt;">Stays on or near the line. Aims to make the save the shot-stopper <em>can</em> make, not the save the defence <em>expects</em>. Pure reactions. <b>Examples:</b> David De Gea, Emiliano Martínez, Manuel Neuer (in his later years).</p>
  </div>
  <div class="sidebar green">
    <h3 style="font-size:11pt;">Sweeper-keeper</h3>
    <p style="font-size:8.5pt;">Plays 15–25 m off the line, behind a high defensive line. Reads the through-ball before it is played. <b>Examples:</b> Manuel Neuer, Alisson, Ederson (who combines this with build-out).</p>
  </div>
  <div class="sidebar terracotta">
    <h3 style="font-size:11pt;">Aggressive / sweeper-up</h3>
    <p style="font-size:8.5pt;">Charges down one-on-ones before they happen; smothers strikers at the edge of the box. <b>Examples:</b> Marc-André ter Stegen, Diogo Costa, the goalkeeping tradition of the 1990s.</p>
  </div>
  <div class="sidebar navy">
    <h3 style="font-size:11pt;">Distributed / build-out</h3>
    <p style="font-size:8.5pt;">A player-coach’s keeper: reads the press, plays short under pressure, hits long accurate switches. Often the highest-positioned dot on the pitch. <b>Examples:</b> Ederson, Ter Stegen, Aaron Ramsdale.</p>
  </div>
</div>
"""
    return page(41, 'Goalkeeper roles', body_html=body, layout='roles-keepers')


# ---------- Page 42: CB archetypes ----------
def page42():
    # Four CB archetypes arranged across the back line + a defensive-midfielder screening
    players = [
        {'x':18, 'y':50, 'role':'def', 'num':6, 'name':'BP'},
        {'x':18, 'y':28, 'role':'def', 'num':5, 'name':'AS'},
        {'x':18, 'y':72, 'role':'def', 'num':4, 'name':'NN'},
        {'x':24, 'y':50, 'role':'def', 'num':3, 'name':'CS'},
        {'x':4,  'y':50, 'role':'gk',  'num':1, 'name':'GK'},
    ]
    # Archetype chips on right
    extras = [
        arch_chip(70, 12, 'Ball-playing CB',
                  'Starts attacks; central passes.',
                  COL_DEF),
        arch_chip(70, 32, 'Aggressive stopper',
                  'Steps up; wins the first duel.',
                  COL_DEF),
        arch_chip(70, 52, 'Cover-shadow CB',
                  'Sits; sweeps behind the stopper.',
                  COL_DEF),
        arch_chip(70, 72, 'No-nonsense CB',
                  'Marks; clears; rarely crosses halfway.',
                  COL_DEF),
    ]
    # Leader lines from each CB to its chip
    mapping = [
        ((18,50), (70,12)),  # ball-playing
        ((18,28), (70,32)),  # aggressive
        ((24,50), (70,52)),  # cover-shadow
        ((18,72), (70,72)),  # no-nonsense
    ]
    leader_lines = []
    for (sx, sy), (ex, ey) in mapping:
        cx, cy = X(sx), Y(sy)
        ex2, ey2 = X(ex-9), Y(ey)
        leader_lines.append(
            f'<line x1="{cx}" y1="{cy}" x2="{ex2}" y2="{ey2}" '
            f'stroke="{COL_INK}" stroke-width="0.7" stroke-dasharray="3,3" opacity="0.85"/>'
            f'<circle cx="{ex2}" cy="{ey2}" r="2.5" fill="{COL_INK}"/>'
        )
    extras += leader_lines
    diagram = wrap_diagram(
        kicker='The four centre-back archetypes',
        formation_code='CB 1–4',
        svg_body=formation_svg_body(players, extra_svg=''.join(extras)),
        caption='Four ways to play the centre of a back line. Each archetype is a different answer to one question: do you push up to the ball, or sit and read it?'
    )
    body = f"""
<div class="two-col">
  <div>
    <p class="lead">The centre-back position has split into at least four distinct archetypes in the modern game. Every successful back line is, essentially, a <strong>balanced pairing</strong> of these roles — a stopper-sweeper axis, a left-right pairing, or a three in which each role is filled.</p>
    <p>The headline trend is the rise of the <strong>ball-playing CB</strong>: teams that could not build from the back used to concede possession in their own third. Now they don’t — and the ball-playing CB is the player that makes the difference.</p>
    <h3 style="font-family:var(--serif);color:var(--green);font-size:12pt;margin:0.2in 0 0.06in;">On the diagram</h3>
    <p style="font-size:9pt;">The four CB archetypes arranged across the back line. The cover-shadow sits slightly deeper than his aggressive partner; the no-nonsense CB hangs close to the box; the ball-playing CB roams centrally. Dotted leaders connect each to a labelled chip.</p>
  </div>
  <div>{diagram}</div>
</div>

<div style="margin-top:0.2in; display:grid; grid-template-columns: repeat(2, 1fr); gap:0.18in;">
  <div class="sidebar navy">
    <h3 style="font-size:11pt;">Ball-playing CB</h3>
    <p style="font-size:8.5pt;">Comfortable in possession; splits centre-backs and starts the attack with a 10-yard pass into the #6. Often the centre-back who reads the press and the line. <b>Examples:</b> Virgil van Dijk, Rúben Dias, Aymeric Laporte.</p>
  </div>
  <div class="sidebar terracotta">
    <h3 style="font-size:11pt;">Aggressive stopper</h3>
    <p style="font-size:8.5pt;">Front-foot defender; steps into the duel, leads with the body, often wins the ball before the striker can receive. Needs a cover-shadow partner. <b>Examples:</b> Sergio Ramos, Thiago Silva, Kalidou Koulibaly.</p>
  </div>
  <div class="sidebar green">
    <h3 style="font-size:11pt;">Cover-shadow CB</h3>
    <p style="font-size:8.5pt;">Reads play; sits; cleans up after the aggressive stopper’s press. Often slightly smaller, faster, smarter. <b>Examples:</b> Franz Beckenbauer (the original), Gérard Piqué, Matthijs de Ligt.</p>
  </div>
  <div class="sidebar gold">
    <h3 style="font-size:11pt;">No-nonsense CB</h3>
    <p style="font-size:8.5pt;">Old-school: marks the centre-forward, wins the header, clears the line. Rarely crosses the halfway. The late-1980s English-style. <b>Examples:</b> John Terry (early), Marcos Rojo, Bremer.</p>
  </div>
</div>
"""
    return page(42, 'Centre-back archetypes', body_html=body, layout='roles-cb')


# ---------- Page 43: FB evolution ----------
def page43():
    # Three eras of fullbacks, each shown with two dots (LB and RB) at distinct positions
    players = [
        # Traditional fullbacks (1980s) — narrow and deep
        {'x':18, 'y':12, 'role':'def', 'num':3, 'name':'TF'},
        {'x':18, 'y':88, 'role':'def', 'num':2, 'name':'TF'},
        # Modern overlapping fullbacks (1990s-2010s) — push wide
        {'x':22, 'y':3,  'role':'def', 'num':20,'name':'OF'},
        {'x':22, 'y':97, 'role':'def', 'num':5, 'name':'OF'},
        # Inverted fullbacks / wing-backs (2020s) — tuck in or push very high
        {'x':35, 'y':25, 'role':'mid', 'num':11,'name':'IF'},
        {'x':35, 'y':75, 'role':'mid', 'num':7, 'name':'IF'},
    ]
    extras = [
        arch_chip(72, 12, 'Traditional FB',
                  'Narrow and deep. Marks the winger.',
                  COL_DEF),
        arch_chip(72, 32, 'Overlapping FB',
                  'Pushes wide past the winger.',
                  COL_DEF),
        arch_chip(72, 52, 'Inverted FB',
                  'Tucks into midfield; creates overloads.',
                  COL_DEF),
        arch_chip(72, 72, 'Wing-back',
                  'Plays like a winger wearing a defender’s shirt.',
                  COL_DEF),
    ]
    # Leader lines: traditional->first chip, overlapping->second, inverted->third
    mapping = [
        ((18, 12), (72, 12)),
        ((22, 3),  (72, 32)),
        ((35, 25), (72, 52)),
    ]
    leader_lines = []
    for (sx, sy), (ex, ey) in mapping:
        cx, cy = X(sx), Y(sy)
        ex2, ey2 = X(ex-9), Y(ey)
        leader_lines.append(
            f'<line x1="{cx}" y1="{cy}" x2="{ex2}" y2="{ey2}" '
            f'stroke="{COL_INK}" stroke-width="0.7" stroke-dasharray="3,3" opacity="0.85"/>'
            f'<circle cx="{ex2}" cy="{ey2}" r="2.5" fill="{COL_INK}"/>'
        )
    extras += leader_lines
    # A time-line arrow at the bottom showing the evolution direction
    extras.append(
        f'<line x1="{X(10)}" y1="{Y(94)}" x2="{X(60)}" y2="{Y(94)}" '
        f'stroke="{COL_INK}" stroke-width="1.4"/>'
        f'<polygon points="{X(60)},{Y(94)} {X(57)},{Y(92)} {X(57)},{Y(96)}" fill="{COL_INK}"/>'
        f'<text x="{X(10)}" y="{Y(91)}" font-family="\'Inter\',sans-serif" font-size="11" '
        f'fill="{COL_INK}" font-weight="700">1980s</text>'
        f'<text x="{X(32)}" y="{Y(91)}" font-family="\'Inter\',sans-serif" font-size="11" '
        f'fill="{COL_INK}" font-weight="700">2000s</text>'
        f'<text x="{X(55)}" y="{Y(91)}" font-family="\'Inter\',sans-serif" font-size="11" '
        f'fill="{COL_INK}" font-weight="700">2020s</text>'
    )
    diagram = wrap_diagram(
        kicker='The full-back in three eras',
        formation_code='FB EVOLUTION',
        svg_body=formation_svg_body(players, extra_svg=''.join(extras)),
        caption='From a defender who marked the winger to an attacking midfielder wearing a defender’s shirt. Three eras of full-back play, mapped on a single half-pitch.'
    )
    body = f"""
<div class="two-col">
  <div>
    <p class="lead">Forty years, three full-backs. The position has changed more than any other on the pitch — from a narrow defensive marker to an attacker who happens to start in the back line.</p>
    <p>Three eras define the role:</p>
    <p><b>1980s.</b> The traditional full-back. Stays narrow; marks the winger; rarely crosses the halfway line. <b>Examples:</b> <em>Dennis Irwin</em>, <em>Gary Stevens</em>.</p>
    <p><b>2000s.</b> The overlapping full-back. Pushes high and wide past the winger to provide width and crosses. <b>Examples:</b> <em>Roberto Carlos</em>, <em>Cafu</em>, <em>Danny Alves</em>.</p>
    <p><b>2020s.</b> Two new roles: the <strong>inverted full-back</strong> (tucks into midfield to create central overloads) and the <strong>wing-back</strong> (essentially a winger who starts in defence). <b>Examples:</b> <em>João Cancelo</em>, <em>Achraf Hakimi</em>, <em>Trent Alexander-Arnold</em>.</p>
    <div class="callout" style="margin-top:0.25in;">
      <h3 style="font-size:10pt;margin-bottom:0.06in;">Cancelo vs. Alexander-Arnold</h3>
      <p style="font-size:8.5pt; margin:0;">Two opposite answers to the same tactical question. Cancelo (Manchester City 2022) inverted into midfield, leaving the wing for the winger. Alexander-Arnold (Liverpool 2022) pushed into the half-space as a creative passer. Both are full-backs. Neither defends like one.</p>
    </div>
  </div>
  <div>{diagram}</div>
</div>
"""
    return page(43, 'Full-back evolution', body_html=body, layout='roles-fb')


# ---------- Page 44: Midfielder archetypes ----------
def page44():
    # Five midfielder archetypes:
    # - The 6 / regista (deeper, single pivot)
    # - The 8 / box-to-box midfielder
    # - The 10 / trequartista
    # - Mezzala (half-space 8)
    # - The anchor
    players = [
        {'x':30, 'y':50, 'role':'mid', 'num':6, 'name':'RG'},
        {'x':36, 'y':50, 'role':'mid', 'num':8, 'name':'DM'},
        {'x':44, 'y':30, 'role':'mid', 'num':11,'name':'MZ'},
        {'x':44, 'y':70, 'role':'mid', 'num':10,'name':'8'},
        {'x':56, 'y':50, 'role':'mid', 'num':7, 'name':'10'},
    ]
    extras = [
        arch_chip(72, 14, 'Regista',
                  'Deep playmaker; dictates tempo.',
                  COL_MID),
        arch_chip(72, 32, 'The 6 / DM',
                  'Anchor; ball-winner; screens the back four.',
                  COL_MID),
        arch_chip(72, 52, 'Mezzala',
                  'Half-space 8; drifts wide to create.',
                  COL_MID),
        arch_chip(72, 72, 'The 8 (box-to-box)',
                  'Arrives late; covers end-to-end.',
                  COL_MID),
        arch_chip(72, 88, 'The 10 (trequartista)',
                  'Final pass; between the lines.',
                  COL_MID),
    ]
    # Map dots (in order above) to chips
    mapping = [
        ((30, 50), (72, 14)),   # regista
        ((36, 50), (72, 32)),   # the 6
        ((44, 30), (72, 52)),   # mezzala
        ((44, 70), (72, 72)),   # 8 box-to-box
        ((56, 50), (72, 88)),   # 10
    ]
    leader_lines = []
    for (sx, sy), (ex, ey) in mapping:
        cx, cy = X(sx), Y(sy)
        ex2, ey2 = X(ex-9), Y(ey)
        leader_lines.append(
            f'<line x1="{cx}" y1="{cy}" x2="{ex2}" y2="{ey2}" '
            f'stroke="{COL_INK}" stroke-width="0.7" stroke-dasharray="3,3" opacity="0.85"/>'
            f'<circle cx="{ex2}" cy="{ey2}" r="2.5" fill="{COL_INK}"/>'
        )
    extras += leader_lines
    diagram = wrap_diagram(
        kicker='The five midfielder types',
        formation_code='MF 6/8/10',
        svg_body=formation_svg_body(players, extra_svg=''.join(extras)),
        caption='Five midfield roles defined by where they start, where they run, and what they do in the final third. The 6, the 8, the 10 — and the two roles that hide inside each.'
    )
    body = f"""
<div class="two-col">
  <div>
    <p class="lead">A midfield is not one position but a <strong>spectrum of roles</strong>, each defined by where the player starts, the spaces they cover, and what they do in the final third. The old 4-4-2 had two midfielders; the modern 4-3-3 names five distinct roles.</p>
    <p>The numbered system — <strong>6, 8, 10</strong> — has Italian football roots and is now universal. They correspond to:</p>
    <p><b>The 6.</b> The defensive midfielder. Sits in front of the centre-backs, screens, wins the ball, recycles possession. The role of a <em>regista</em> when the 6 is also the team’s deep playmaker.</p>
    <p><b>The 8.</b> The central midfielder. Two sub-roles: the <em>box-to-box</em> (end-to-end, arrives late in the box) and the <em>mezzala</em> (half-space operator, drifts wide to create). Different jobs, same shirt number.</p>
    <p><b>The 10.</b> The attacking midfielder. Plays <em>between the lines</em>, makes the final pass, scores from deep positions. The role of <em>trequartista</em> in Italian tradition.</p>
    <div class="callout" style="margin-top:0.2in;">
      <h3 style="font-size:10pt;margin-bottom:0.06in;">Modern trend</h3>
      <p style="font-size:8.5pt; margin:0;">Since 2018, the <strong>inverted full-back</strong> has done much of the role traditionally played by the 8 — pushing into midfield while the 8 pushes into the 10’s space. The midfield roles shrink year by year as the tactics evolve around them.</p>
    </div>
  </div>
  <div>{diagram}</div>
</div>
"""
    return page(44, 'Midfielder archetypes', body_html=body, layout='roles-mid')


# ============================================================
# WRITE ALL PAGES
# ============================================================
PAGES = [page33(), page34(), page35(), page36(), page37(), page38(),
         page39(), page40(), page41(), page42(), page43(), page44()]

for i, html in enumerate(PAGES, start=33):
    fname = f'{i:02d}-page.html'
    with open(f'{PAGES_DIR}/{fname}', 'w') as f:
        f.write(html)
    print(f'Wrote {fname}')

print(f'\n{len(PAGES)} formation/position pages written to {PAGES_DIR}')
