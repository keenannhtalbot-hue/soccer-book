#!/usr/bin/env python3
"""
Generate all 100 pages of The Soccer Book.
Uses template-based generation with embedded SVG diagrams.
"""
import os
import re

PAGES_DIR = '/home/kbot/soccer-book/pages'
os.makedirs(PAGES_DIR, exist_ok=True)

# Page template helper
def page(num, title, body, layout='standard'):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Page {num} — {title}</title>
<link rel="stylesheet" href="book.css">
</head>
<body class="page {layout}">
<div class="page-inner">
{body}
</div>
</body>
</html>
"""

# Helper: build header
def header(num, section_num, section_title, page_title=None, kicker=None):
    page_title = page_title or section_title
    pn = f'<div class="page-num">{num}</div>'
    return f"""<div class="page-header">
  {pn}
  <div>
    <div class="section-num">Section {section_num}</div>
    <h1 class="section-title">{page_title}</h1>
  </div>
</div>"""

# ============ FRONT MATTER 1-6 ============
# Pages 1-3 are already created as cover, halftitle, contents.

# Page 4: How to use this book
def page4():
    body = """
<div class="page-header">
  <div class="page-num">4</div>
  <div><div class="section-num">Section I</div><h1 class="section-title">About this book</h1></div>
</div>

<div class="two-col" style="margin-top: 0.3in;">
  <div>
    <p class="lead">Welcome to the world's most popular sport. This book is a <strong>visual reference</strong> — every spread is built to be skimmed, scanned, and studied in any order.</p>
    <p>Soccer is governed by 17 rules, played on every continent, watched by half the planet, and rewritten every summer by a transfer window. What follows is the modern game in 100 pages.</p>

    <h3 style="margin-top: 0.4in; font-family: var(--serif); color: var(--green);">How the pages are organized</h3>
    <p>Eight numbered sections take you from the <strong>pitch and equipment</strong> through the <strong>rules</strong>, <strong>formations</strong>, <strong>kits</strong>, the world's biggest <strong>clubs</strong>, the <strong>stadiums and competitions</strong>, and finally the <strong>culture</strong> of the game.</p>

    <div class="sidebar green" style="margin-top: 0.3in;">
      <h3>Visual conventions</h3>
      <p style="font-size: 8pt;"><span style="color: var(--terracotta);">▌</span> Left bars mark reference sidebars. <span style="color: var(--terracotta);">▌</span> Green = field/pitch, Terracotta = teams/identity, Navy = rules/governance, Gold = highlights/stats.</p>
    </div>
  </div>
  <div>
    <div class="factbox terracotta">
      <div class="eyebrow">By the numbers</div>
      <h3 style="font-size: 14pt; margin-top: 0.1in;">128 Years of the Laws</h3>
      <p style="font-size: 9pt; margin: 0.2in 0;">The IFAB codified the first 11 Laws of Association Football in <strong>1863</strong>. The current 17 Laws were finalized in <strong>2024</strong> after the most significant rewrite in modern history.</p>
      <div style="display: flex; gap: 0.2in; margin-top: 0.3in;">
        <div class="stat" style="flex: 1;"><div class="num">17</div><div class="label">Laws of the Game</div></div>
        <div class="stat" style="flex: 1;"><div class="num">105<span style="font-size: 14pt;">m</span></div><div class="label">Pitch length</div></div>
        <div class="stat" style="flex: 1;"><div class="num">90<span style="font-size: 14pt;">m</span></div><div class="label">Match time</div></div>
      </div>
    </div>

    <div class="sidebar" style="margin-top: 0.2in;">
      <h3>What this book is not</h3>
      <p style="font-size: 8.5pt;">A <strong>history</strong> book. We focus on the modern game — current rules, current kits, current clubs. The sport's past is rich and well-documented elsewhere; here you'll find what matters <em>right now</em> on the pitch.</p>
    </div>
  </div>
</div>
"""
    return page(4, "About this book", body, "howto")

# Page 5: Legend
def page5():
    body = """
<div class="page-header">
  <div class="page-num">5</div>
  <div><div class="section-num">Section I</div><h1 class="section-title">Legend &amp; abbreviations</h1></div>
</div>

<p class="lead" style="margin: 0.2in 0;">Symbols and shorthand used throughout this book.</p>

<div class="two-col">
  <div>
    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin-bottom: 0.1in;">Pitch &amp; equipment</h3>
    <table style="width: 100%; font-size: 9pt;">
      <tr><td style="padding: 0.04in 0;"><b>FG</b></td><td>Firm Ground (boots for natural grass)</td></tr>
      <tr><td><b>SG</b></td><td>Soft Ground (aluminum studs, soft/wet fields)</td></tr>
      <tr><td><b>AG</b></td><td>Artificial Grass (multi-stud, harder ground)</td></tr>
      <tr><td><b>TF</b></td><td>Turf (rubber dimples, hard indoor surfaces)</td></tr>
      <tr><td><b>IC</b></td><td>Indoor Court (low-profile, non-marking sole)</td></tr>
      <tr><td><b>SIZE 5</b></td><td>Adult match ball (68–70 cm circumference)</td></tr>
    </table>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.3in 0 0.1in;">Positions</h3>
    <table style="width: 100%; font-size: 9pt;">
      <tr><td style="padding: 0.04in 0;"><b>GK</b></td><td>Goalkeeper</td></tr>
      <tr><td><b>CB</b></td><td>Centre-back</td></tr>
      <tr><td><b>FB / WB</b></td><td>Full-back / Wing-back</td></tr>
      <tr><td><b>CDM / CM / CAM</b></td><td>Defensive / Centre / Attacking midfielder</td></tr>
      <tr><td><b>ST / CF / LW / RW</b></td><td>Striker / Centre-forward / Winger</td></tr>
    </table>
  </div>

  <div>
    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin-bottom: 0.1in;">Competitions</h3>
    <table style="width: 100%; font-size: 9pt;">
      <tr><td style="padding: 0.04in 0;"><b>UCL</b></td><td>UEFA Champions League</td></tr>
      <tr><td><b>UEL</b></td><td>UEFA Europa League</td></tr>
      <tr><td><b>UECL</b></td><td>UEFA Conference League</td></tr>
      <tr><td><b>PL</b></td><td>Premier League</td></tr>
      <tr><td><b>WC</b></td><td>FIFA World Cup</td></tr>
      <tr><td><b>EC</b></td><td>UEFA European Championship</td></tr>
      <tr><td><b>CDMX</b></td><td>Club de Deportes (Mexican league teams)</td></tr>
      <tr><td><b>SPL</b></td><td>Saudi Pro League</td></tr>
    </table>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.3in 0 0.1in;">On diagrams</h3>
    <p style="font-size: 9pt;"><span style="display: inline-block; width: 0.18in; height: 0.18in; background: var(--terracotta); border-radius: 50%; vertical-align: middle;"></span> &nbsp;Forwards  &nbsp; <span style="display: inline-block; width: 0.18in; height: 0.18in; background: var(--green); border-radius: 50%; vertical-align: middle;"></span> &nbsp;Midfielders  &nbsp; <span style="display: inline-block; width: 0.18in; height: 0.18in; background: var(--navy); border-radius: 50%; vertical-align: middle;"></span> &nbsp;Defenders  &nbsp; <span style="display: inline-block; width: 0.18in; height: 0.18in; background: var(--gold); border-radius: 50%; vertical-align: middle;"></span> &nbsp;Goalkeeper</p>

    <p style="font-size: 8.5pt; color: var(--ink-mute); margin-top: 0.2in;"><b>Etc.</b> Where a dotted line connects a label to a diagram, follow it to the named part. Where a footnote (1, 2…) appears, see the right margin for the source.</p>
  </div>
</div>
"""
    return page(5, "Legend &amp; abbreviations", body, "legend")

# Page 6: The modern game at a glance
def page6():
    body = """
<div class="page-header">
  <div class="page-num">6</div>
  <div><div class="section-num">Section I</div><h1 class="section-title">The modern game</h1></div>
</div>

<div class="two-col" style="margin-top: 0.2in;">
  <div>
    <p class="lead">Two teams of eleven. One ball. Ninety minutes. Three substitutions (or five in some competitions). That is the skeleton — everything else is detail.</p>

    <p>The <strong>object</strong> is to score more goals than the opponent. The <strong>method</strong> is to use any part of the body except the hands and arms (only the goalkeeper may use hands within the penalty area) to move the ball into the opponent's goal. The <strong>penalty</strong> for a foul is a free kick; for a foul denying an obvious goal-scoring opportunity, a red card and ejection.</p>

    <p>Beyond that, the game is a continuous argument about space, time, and risk. Press high or sit back. Possess or counter. Cross early or play through. Every team is a thesis; every match is a debate.</p>

    <div class="callout" style="margin-top: 0.3in;">
      <h3 style="font-size: 11pt; margin-bottom: 0.08in;">Key fact</h3>
      <p style="font-size: 9pt; margin: 0;">The ball is in play for an average of <strong>60–65 minutes</strong> during a 90-minute match. The rest is stoppages, throw-ins, fouls, goal kicks, and substitutions.</p>
    </div>
  </div>

  <div>
    <div class="diagram">
      <div class="kicker" style="margin-bottom: 0.1in;">At a glance</div>
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.15in;">
        <div class="compare-cell"><div class="big-num" style="font-size: 18pt;">11</div><div class="stat-label" style="font-size: 7pt; text-transform: uppercase; letter-spacing: 0.1em; color: var(--ink-mute);">Players per side</div></div>
        <div class="compare-cell"><div class="big-num" style="font-size: 18pt;">2 × 45′</div><div class="stat-label" style="font-size: 7pt; text-transform: uppercase; letter-spacing: 0.1em; color: var(--ink-mute);">Match time</div></div>
        <div class="compare-cell"><div class="big-num" style="font-size: 18pt;">3–5</div><div class="stat-label" style="font-size: 7pt; text-transform: uppercase; letter-spacing: 0.1em; color: var(--ink-mute);">Subs allowed</div></div>
        <div class="compare-cell"><div class="big-num" style="font-size: 18pt;">68–70cm</div><div class="stat-label" style="font-size: 7pt; text-transform: uppercase; letter-spacing: 0.1em; color: var(--ink-mute);">Ball circumference</div></div>
        <div class="compare-cell"><div class="big-num" style="font-size: 18pt;">410–450g</div><div class="stat-label" style="font-size: 7pt; text-transform: uppercase; letter-spacing: 0.1em; color: var(--ink-mute);">Ball weight</div></div>
        <div class="compare-cell"><div class="big-num" style="font-size: 18pt;">105 × 68m</div><div class="stat-label" style="font-size: 7pt; text-transform: uppercase; letter-spacing: 0.1em; color: var(--ink-mute);">Pitch size</div></div>
      </div>
    </div>
  </div>
</div>
"""
    return page(6, "The modern game", body, "modern-game")

# ============ SECTION II: PITCH & EQUIPMENT 7-18 ============

# Page 7: Pitch
def page7():
    body = """
<div class="page-header">
  <div class="page-num">7</div>
  <div><div class="section-num">Section II</div><h1 class="section-title">Anatomy of the pitch</h1></div>
</div>

<div class="two-col">
  <div>
    <p class="lead">A regulation pitch is a rectangle between <strong>100–110 m long</strong> and <strong>64–75 m wide</strong>. For international matches the figures tighten to <strong>105 × 68 m</strong>.</p>

    <p>The pitch is divided by a halfway line, a centre circle (radius 9.15 m), and a penalty area at each end. Penalty spots sit 11 m from the goal line. Corner arcs are 1 m from each corner flag.</p>

    <div class="sidebar green" style="margin-top: 0.3in;">
      <h3>The lines belong to the area they enclose</h3>
      <p style="font-size: 8.5pt;">A ball touching any line is still <em>in</em> the area that line defines. This includes the goal line, the touchline, and every line inside the field of play.</p>
    </div>

    <div class="callout" style="margin-top: 0.2in;">
      <h3 style="font-size: 10pt; margin-bottom: 0.05in;">Did you know?</h3>
      <p style="font-size: 8.5pt; margin: 0;">The longest goal ever scored in a professional game (according to the Guinness Book of World Records) was <strong>91.9 m</strong> — by goalkeeper Pat Jennings for Northern Ireland vs. England in 1967.</p>
    </div>
  </div>
  <div>
    <div class="pitch diagram">
      <div class="player-dot" style="left: 6%; top: 25%;"><div class="dot gk">1</div><div class="name">GK</div></div>
      <div class="player-dot" style="left: 6%; top: 50%;"><div class="dot def">2</div><div class="name">LB</div></div>
      <div class="player-dot" style="left: 6%; top: 75%;"><div class="dot def">3</div><div class="name">RB</div></div>
      <div class="player-dot" style="left: 20%; top: 50%;"><div class="dot def">5</div><div class="name">CB</div></div>
      <div class="player-dot" style="left: 35%; top: 50%;"><div class="dot mid">6</div><div class="name">DM</div></div>
      <div class="player-dot" style="left: 50%; top: 30%;"><div class="dot mid">8</div><div class="name">CM</div></div>
      <div class="player-dot" style="left: 50%; top: 70%;"><div class="dot mid">10</div><div class="name">AM</div></div>
      <div class="player-dot" style="left: 75%; top: 25%;"><div class="dot fwd">7</div><div class="name">LW</div></div>
      <div class="player-dot" style="left: 75%; top: 75%;"><div class="dot fwd">11</div><div class="name">RW</div></div>
      <div class="player-dot" style="left: 90%; top: 50%;"><div class="dot fwd">9</div><div class="name">ST</div></div>
    </div>
    <p class="cap">A modern 4-3-3 formation laid out on a regulation pitch. The halfway line (white) divides two mirror-image halves. Note the 9.15 m centre circle around the kick-off spot.</p>
  </div>
</div>
"""
    return page(7, "Anatomy of the pitch", body, "pitch")

# Page 8: Goal structure
def page8():
    body = """
<div class="page-header">
  <div class="page-num">8</div>
  <div><div class="section-num">Section II</div><h1 class="section-title">Goal structure</h1></div>
</div>

<div class="two-col">
  <div>
    <p class="lead">A goal consists of two vertical posts <strong>7.32 m (8 yd) apart</strong>, joined by a horizontal crossbar <strong>2.44 m (8 ft)</strong> above the ground.</p>

    <p>Behind the goal line, a net is attached to the posts and crossbar. Modern goals use breakaway nets, which detach on heavy impact to prevent injuries.</p>

    <div class="factbox navy">
      <div class="eyebrow">Spec check</div>
      <h3 style="font-size: 14pt;">Laws of the Goal</h3>
      <div style="display: flex; gap: 0.2in; margin-top: 0.2in;">
        <div class="stat" style="flex: 1;"><div class="num" style="color: var(--gold);">7.32<span style="font-size: 11pt;">m</span></div><div class="label" style="color: var(--paper);">Width</div></div>
        <div class="stat" style="flex: 1;"><div class="num" style="color: var(--gold);">2.44<span style="font-size: 11pt;">m</span></div><div class="label" style="color: var(--paper);">Height</div></div>
        <div class="stat" style="flex: 1;"><div class="num" style="color: var(--gold);">12<span style="font-size: 14pt;">cm</span></div><div class="label" style="color: var(--paper);">Post width</div></div>
        <div class="stat" style="flex: 1;"><div class="num" style="color: var(--gold);">≤0.5<span style="font-size: 14pt;">m</span></div><div class="label" style="color: var(--paper);">Net depth</div></div>
      </div>
    </div>

    <div class="sidebar terracotta" style="margin-top: 0.3in;">
      <h3>Goal-line technology</h3>
      <p style="font-size: 8.5pt;">Since 2013 (Club World Cup) and 2015 (Premier League), the Laws permit <strong>GLT</strong>: 14 high-speed cameras + the ball's embedded chip detect whether the whole ball has crossed the line. Referees receive a watch vibration within a second.</p>
    </div>
  </div>
  <div>
    <svg viewBox="0 0 220 140" style="width: 100%; background: linear-gradient(180deg, #4caf50 0%, #43a047 100%); border: 0.04in solid var(--rule); border-radius: 0.05in;">
      <!-- Goal frame -->
      <rect x="60" y="20" width="100" height="100" fill="none" stroke="white" stroke-width="3"/>
      <!-- Posts highlight -->
      <line x1="60" y1="20" x2="60" y2="120" stroke="white" stroke-width="6"/>
      <line x1="160" y1="20" x2="160" y2="120" stroke="white" stroke-width="6"/>
      <line x1="60" y1="20" x2="160" y2="20" stroke="white" stroke-width="6"/>
      <!-- Net mesh pattern -->
      <g stroke="white" stroke-width="0.5" opacity="0.7">
        <line x1="60" y1="30" x2="160" y2="30"/>
        <line x1="60" y1="40" x2="160" y2="40"/>
        <line x1="60" y1="50" x2="160" y2="50"/>
        <line x1="60" y1="60" x2="160" y2="60"/>
        <line x1="60" y1="70" x2="160" y2="70"/>
        <line x1="60" y1="80" x2="160" y2="80"/>
        <line x1="60" y1="90" x2="160" y2="90"/>
        <line x1="60" y1="100" x2="160" y2="100"/>
        <line x1="60" y1="110" x2="160" y2="110"/>
        <line x1="70" y1="20" x2="70" y2="120"/>
        <line x1="80" y1="20" x2="80" y2="120"/>
        <line x1="90" y1="20" x2="90" y2="120"/>
        <line x1="100" y1="20" x2="100" y2="120"/>
        <line x1="110" y1="20" x2="110" y2="120"/>
        <line x1="120" y1="20" x2="120" y2="120"/>
        <line x1="130" y1="20" x2="130" y2="120"/>
        <line x1="140" y1="20" x2="140" y2="120"/>
        <line x1="150" y1="20" x2="150" y2="120"/>
      </g>
      <!-- Label leader -->
      <line x1="200" y1="70" x2="160" y2="70" stroke="#c44536" stroke-width="0.5" stroke-dasharray="2,2"/>
      <text x="200" y="73" font-size="6" fill="var(--ink)" font-family="Inter">8 yd width</text>
      <line x1="110" y1="135" x2="110" y2="120" stroke="#c44536" stroke-width="0.5" stroke-dasharray="2,2"/>
      <text x="115" y="135" font-size="6" fill="var(--ink)" font-family="Inter">8 ft height</text>
    </svg>
    <p class="cap">Front-on schematic of a regulation goal. Net mesh (white, dotted) attaches to posts and crossbar. Goal-line technology sensors sit inside the ball and at the rear of the goal.</p>
  </div>
</div>
"""
    return page(8, "Goal structure", body, "goal")

# Page 9: The ball
def page9():
    body = """
<div class="page-header">
  <div class="page-num">9</div>
  <div><div class="section-num">Section II</div><h1 class="section-title">The match ball</h1></div>
</div>

<div class="two-col">
  <div>
    <p class="lead">Size 5. Circumference <strong>68–70 cm</strong>. Weight <strong>410–450 g</strong>. Inflation <strong>0.6–1.1 atm</strong> at sea level. The Laws of the Game are very specific about this — and have been since 1872.</p>

    <p>Modern balls are made of synthetic leather (PU or PVC) panels thermally bonded to a latex or butyl bladder. Top-tier balls have <strong>12–32 panels</strong>; the trend is fewer panels for a truer sphere.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.05in;">Panel patterns</h3>
    <ul style="font-size: 9pt; margin-left: 0.3in; list-style: disc;">
      <li><b>32 panels</b> — classic (Brazuca-style)</li>
      <li><b>12 panels</b> — modern, smoother (Adidas Telstar)</li>
      <li><b>6 panels</b> — minimalist (used in training)</li>
      <li><b>1 panel</b> — experimental thermo-bonded</li>
    </ul>

    <div class="callout" style="margin-top: 0.3in;">
      <h3 style="font-size: 10pt;">The ball's path through the air</h3>
      <p style="font-size: 8.5pt; margin: 0;">A spinning ball curves in flight due to the <b>Magnus effect</b> — a free kick at 30 m/s with 10 rev/s curves about <b>3.5 m</b> by the time it reaches the goal. The famous 1997 Roberto Carlos goal against France curved by more than 2 m.</p>
    </div>
  </div>
  <div>
    <div style="text-align: center; margin-bottom: 0.2in;">
      <svg viewBox="0 0 160 160" style="width: 3in;">
        <defs>
          <radialGradient id="ballShade" cx="35%" cy="30%" r="70%">
            <stop offset="0%" stop-color="#fff"/>
            <stop offset="100%" stop-color="#d4cba0"/>
          </radialGradient>
        </defs>
        <circle cx="80" cy="80" r="70" fill="url(#ballShade)" stroke="#1a1612" stroke-width="2"/>
        <g stroke="#1a1612" stroke-width="1.2" fill="none" opacity="0.85">
          <polygon points="80,15 130,40 130,90 80,115 30,90 30,40" />
          <polygon points="80,15 105,30 130,15" />
          <polygon points="130,40 150,55 130,75" />
          <polygon points="130,90 150,75 145,105" />
          <polygon points="80,115 100,130 60,135" />
          <polygon points="30,90 20,75 30,55" />
          <polygon points="30,40 20,55 10,40" />
        </g>
        <g fill="#1a1612" opacity="0.6">
          <circle cx="50" cy="55" r="3"/>
          <circle cx="110" cy="55" r="3"/>
          <circle cx="80" cy="80" r="3"/>
          <circle cx="50" cy="105" r="3"/>
          <circle cx="110" cy="105" r="3"/>
        </g>
      </svg>
    </div>
    <div class="diagram">
      <div class="kicker" style="text-align: center; margin-bottom: 0.1in;">A modern 12-panel ball</div>
      <table style="width: 100%; font-size: 8pt;">
        <tr><td><b>Outer</b></td><td>PU or PVC synthetic leather</td></tr>
        <tr><td><b>Panels</b></td><td>12 thermally bonded</td></tr>
        <tr><td><b>Sub-surface</b></td><td>Polyester / cotton scrim</td></tr>
        <tr><td><b>Bladder</b></td><td>Latex (soft feel) or butyl (durable)</td></tr>
        <tr><td><b>Stitching</b></td><td>None — thermal bonds only</td></tr>
        <tr><td><b>Circumference</b></td><td>68–70 cm (Size 5)</td></tr>
        <tr><td><b>Weight</b></td><td>410–450 g</td></tr>
        <tr><td><b>Bounce</b></td><td>50–65 cm from 2 m drop</td></tr>
        <tr><td><b>Circum. loss</b></td><td>≤ 1.5% over match</td></tr>
      </table>
    </div>
  </div>
</div>
"""
    return page(9, "The match ball", body, "ball")

# Page 10: Boots anatomy
def page10():
    body = """
<div class="page-header">
  <div class="page-num">10</div>
  <div><div class="section-num">Section II</div><h1 class="section-title">Boots: anatomy</h1></div>
</div>

<div class="two-col">
  <div>
    <p class="lead">A modern football boot has three principal parts: the <strong>upper</strong>, the <strong>midsole</strong> (often minimal), and the <strong>outsole</strong> (with studs).</p>

    <p>The upper is where most engineering happens. Top-end boots use <strong>flyknit</strong> or <strong>engineered mesh</strong> for a sock-like fit; budget boots use synthetic leather. Laceless (sock-fit) designs have largely displaced traditional laces at the elite level since 2016.</p>

    <div class="sidebar green" style="margin-top: 0.3in;">
      <h3>Why laceless?</h3>
      <p style="font-size: 8.5pt;">A clean strike zone: no laces means a bigger, uninterrupted sweet spot. The trade-off is fit — most players still prefer laced for lockdown, especially strikers striking through the ball.</p>
    </div>

    <div class="factbox">
      <div class="eyebrow">Average weight</div>
      <h3 style="font-size: 18pt; margin-top: 0.05in;">200 g</h3>
      <p style="font-size: 8.5pt; margin: 0.1in 0 0;">A top-tier boot (size 9) weighs about <strong>200 g</strong> — half what the 1990 Adidas Predator weighed.</p>
    </div>
  </div>
  <div>
    <div class="boot-diagram">
      <svg viewBox="0 0 220 110" style="width: 100%;">
        <!-- Boot outline -->
        <path d="M 20 80 Q 20 60 40 55 L 100 50 Q 130 50 160 55 L 200 70 Q 210 80 200 88 L 30 88 Q 20 88 20 80 Z"
              fill="var(--terracotta)" stroke="var(--ink)" stroke-width="1.5"/>
        <!-- Laces -->
        <g stroke="var(--paper)" stroke-width="1.5" fill="none">
          <line x1="100" y1="55" x2="160" y2="60"/>
          <line x1="105" y1="60" x2="155" y2="65"/>
          <line x1="110" y1="65" x2="150" y2="70"/>
        </g>
        <!-- Swoosh / brand mark -->
        <path d="M 60 65 Q 80 60 110 65 Q 100 75 80 75 Q 65 75 60 70 Z" fill="var(--paper)" opacity="0.5"/>
        <!-- Stud positions (outsole) -->
        <g fill="var(--ink)">
          <circle cx="30" cy="92" r="2.5"/>
          <circle cx="50" cy="92" r="2.5"/>
          <circle cx="70" cy="92" r="2.5"/>
          <circle cx="95" cy="92" r="2.5"/>
          <circle cx="120" cy="92" r="2.5"/>
          <circle cx="145" cy="92" r="2.5"/>
          <circle cx="170" cy="92" r="2.5"/>
          <circle cx="195" cy="92" r="2.5"/>
        </g>
        <!-- Labels with leaders -->
        <line x1="40" y1="55" x2="40" y2="25" stroke="var(--terracotta)" stroke-width="0.5" stroke-dasharray="2,2"/>
        <text x="35" y="22" font-size="6" fill="var(--ink)">Upper</text>
        <line x1="130" y1="55" x2="170" y2="25" stroke="var(--terracotta)" stroke-width="0.5" stroke-dasharray="2,2"/>
        <text x="148" y="22" font-size="6" fill="var(--ink)">Collar / ankle</text>
        <line x1="100" y1="92" x2="100" y2="105" stroke="var(--terracotta)" stroke-width="0.5" stroke-dasharray="2,2"/>
        <text x="92" y="108" font-size="6" fill="var(--ink)">Stud</text>
        <line x1="40" y1="88" x2="40" y2="105" stroke="var(--terracotta)" stroke-width="0.5" stroke-dasharray="2,2"/>
        <text x="32" y="108" font-size="6" fill="var(--ink)">Outsole</text>
        <line x1="190" y1="70" x2="220" y2="60" stroke="var(--terracotta)" stroke-width="0.5" stroke-dasharray="2,2"/>
        <text x="200" y="58" font-size="6" fill="var(--ink)">Toe box</text>
      </svg>
    </div>
    <p class="cap">Cross-section schematic of a modern FG boot. Components are labeled with dotted leaders to their position on the boot.</p>
  </div>
</div>
"""
    return page(10, "Boots: anatomy", body, "boots-anatomy")

# Page 11: Boot types
def page11():
    body = """
<div class="page-header">
  <div class="page-num">11</div>
  <div><div class="section-num">Section II</div><h1 class="section-title">Boot types &amp; surfaces</h1></div>
</div>

<div class="two-col">
  <div>
    <p class="lead">Boots are coded by the ground they suit. Picking the wrong pair can mean slipping on wet grass or snapping studs on concrete.</p>

    <p>The four main codes are standardised across manufacturers. They appear as small icons on the box and inside the tongue.</p>
  </div>
  <div>
    <table style="width: 100%; font-size: 8.5pt; border-collapse: collapse;">
      <tr style="background: var(--green); color: var(--paper);">
        <th style="padding: 0.1in 0.15in; text-align: left; width: 0.7in;">Code</th>
        <th style="padding: 0.1in 0.15in; text-align: left;">Name</th>
        <th style="padding: 0.1in 0.15in; text-align: left;">Surface</th>
        <th style="padding: 0.1in 0.15in; text-align: left;">Stud type</th>
      </tr>
      <tr style="background: var(--paper-deep);">
        <td style="padding: 0.1in 0.15in;"><b>FG</b></td>
        <td>Firm Ground</td>
        <td>Natural grass, firm &amp; dry</td>
        <td>Conical or bladed, plastic</td>
      </tr>
      <tr>
        <td style="padding: 0.1in 0.15in;"><b>SG</b></td>
        <td>Soft Ground</td>
        <td>Wet / soft natural grass</td>
        <td>Aluminium, screw-in</td>
      </tr>
      <tr style="background: var(--paper-deep);">
        <td style="padding: 0.1in 0.15in;"><b>AG</b></td>
        <td>Artificial Grass</td>
        <td>Modern 3G / 4G surfaces</td>
        <td>Many short hollow studs</td>
      </tr>
      <tr>
        <td style="padding: 0.1in 0.15in;"><b>TF</b></td>
        <td>Turf</td>
        <td>Hard court / old astro</td>
        <td>Many small rubber nubs</td>
      </tr>
      <tr style="background: var(--paper-deep);">
        <td style="padding: 0.1in 0.15in;"><b>IC</b></td>
        <td>Indoor</td>
        <td>Court / futsal</td>
        <td>Flat gum outsole, no studs</td>
      </tr>
      <tr>
        <td style="padding: 0.1in 0.15in;"><b>MG</b></td>
        <td>Multi-Ground</td>
        <td>Hybrid natural / artificial</td>
        <td>Conical, mixed lengths</td>
      </tr>
    </table>

    <div class="callout" style="margin-top: 0.2in;">
      <h3 style="font-size: 10pt;">MXSG: the hybrid</h3>
      <p style="font-size: 8.5pt; margin: 0;">A newer category that mixes FG and SG stud shapes in a single soleplate — the modern pro's one-boot-does-most solution.</p>
    </div>
  </div>
</div>
"""
    return page(11, "Boot types &amp; surfaces", body, "boot-types")

# Page 12: Stud shapes
def page12():
    body = """
<div class="page-header">
  <div class="page-num">12</div>
  <div><div class="section-num">Section II</div><h1 class="section-title">Stud shapes</h1></div>
</div>

<div class="two-col">
  <div>
    <p class="lead">Two stud geometries dominate the pro market. Each has trade-offs in grip, release, and comfort.</p>
  </div>
  <div>
    <div class="compare-row">
      <div class="compare-cell featured">
        <h4>Conical</h4>
        <div class="big-num">●</div>
        <p style="font-size: 9pt;">Round, smooth release. Better for rotational pivots. Slightly less grip in straight lines.</p>
        <p style="font-size: 8pt; margin-top: 0.2in; font-style: italic;">Used by most midfielders.</p>
      </div>
      <div class="compare-cell">
        <h4>Bladed</h4>
        <div class="big-num" style="color: var(--terracotta);">▰</div>
        <p style="font-size: 9pt;">Flat, sharp edge. Maximum grip on the plant foot. Tighter release, more stress on knees.</p>
        <p style="font-size: 8pt; margin-top: 0.2in; font-style: italic;">Favoured by strikers and defenders.</p>
      </div>
    </div>

    <div class="sidebar terracotta" style="margin-top: 0.3in;">
      <h3>Hybrid &amp; asymmetric</h3>
      <p style="font-size: 8.5pt;">Most modern top-end boots use a <b>mixed layout</b>: bladed on the inside edge (grip) and conical on the outside (release). The asymmetry matches how feet actually rotate when striking.</p>
    </div>

    <div class="factbox navy">
      <div class="eyebrow">Stability trade-off</div>
      <h3 style="font-size: 11pt; margin-top: 0.05in;">More grip ≠ more speed</h3>
      <p style="font-size: 8.5pt; margin: 0;">Studies (literally) show that <b>bladed studs increase traction by 12–15%</b> over conical, but also increase <b>peak knee-joint torque by 8%</b> — a documented ACL-injury risk factor.</p>
    </div>
  </div>
</div>
"""
    return page(12, "Stud shapes", body, "stud-shapes")

# Page 13: Player gear
def page13():
    body = """
<div class="page-header">
  <div class="page-num">13</div>
  <div><div class="section-num">Section II</div><h1 class="section-title">Player gear</h1></div>
</div>

<div class="two-col">
  <div>
    <p class="lead">Beyond boots, the modern outfield kit is minimal but rigorously engineered.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Standard outfield</h3>
    <ul style="font-size: 9pt; margin-left: 0.3in; list-style: disc;">
      <li><b>Jersey</b> — polyester knit, mesh vents, sewn or printed numbers</li>
      <li><b>Shorts</b> — elastic waist, lightweight polyester</li>
      <li><b>Socks</b> — knee-high, often with built-in shin guard pocket</li>
      <li><b>Shin guards</b> — mandatory under socks; composite or foam</li>
      <li><b>Gloves</b> (optional) — grip + warmth in cold weather</li>
      <li><b>Cap / headband</b> (optional)</li>
    </ul>

    <div class="callout" style="margin-top: 0.3in;">
      <h3 style="font-size: 10pt;">No jewellery. No hats.</h3>
      <p style="font-size: 8.5pt; margin: 0;">Per Law 4, all jewellery, watches, and hard hair accessories are forbidden. Taped wedding rings are an exception. Goalies wear caps only with referee permission.</p>
    </div>
  </div>
  <div>
    <div class="diagram" style="min-height: 4in;">
      <div class="kicker" style="text-align: center; margin-bottom: 0.2in;">Outfield player — equipped</div>
      <svg viewBox="0 0 180 240" style="width: 3.5in; margin: 0 auto; display: block;">
        <!-- Head -->
        <circle cx="90" cy="20" r="14" fill="#f0d8b8" stroke="var(--ink)" stroke-width="1.5"/>
        <!-- Hair -->
        <path d="M 76 16 Q 80 6 90 5 Q 100 6 104 16" fill="var(--ink)" opacity="0.5"/>
        <!-- Body / Jersey -->
        <path d="M 60 50 L 60 130 L 70 130 L 70 70 L 80 80 L 100 80 L 110 70 L 110 130 L 120 130 L 120 50 L 90 35 Z"
              fill="var(--terracotta)" stroke="var(--ink)" stroke-width="1.5"/>
        <!-- Number on jersey -->
        <text x="90" y="100" font-size="16" text-anchor="middle" fill="var(--paper)" font-family="Cormorant Garamond" font-weight="700">7</text>
        <!-- Shorts -->
        <path d="M 65 130 L 65 170 L 90 170 L 90 130 Z M 90 130 L 90 170 L 115 170 L 115 130 Z"
              fill="var(--ink)" stroke="var(--ink)" stroke-width="1.5"/>
        <!-- Socks -->
        <rect x="68" y="170" width="18" height="30" fill="var(--paper)" stroke="var(--ink)" stroke-width="1.5"/>
        <rect x="92" y="170" width="18" height="30" fill="var(--paper)" stroke="var(--ink)" stroke-width="1.5"/>
        <line x1="68" y1="175" x2="86" y2="175" stroke="var(--terracotta)" stroke-width="2"/>
        <line x1="92" y1="175" x2="110" y2="175" stroke="var(--terracotta)" stroke-width="2"/>
        <!-- Boots -->
        <ellipse cx="77" cy="210" rx="11" ry="5" fill="var(--terracotta)" stroke="var(--ink)" stroke-width="1.5"/>
        <ellipse cx="101" cy="210" rx="11" ry="5" fill="var(--terracotta)" stroke="var(--ink)" stroke-width="1.5"/>
        <circle cx="77" cy="215" r="1" fill="var(--ink)"/>
        <circle cx="83" cy="215" r="1" fill="var(--ink)"/>
        <circle cx="89" cy="215" r="1" fill="var(--ink)"/>
        <circle cx="95" cy="215" r="1" fill="var(--ink)"/>
        <circle cx="101" cy="215" r="1" fill="var(--ink)"/>
        <circle cx="107" cy="215" r="1" fill="var(--ink)"/>
        <!-- Labels with leaders -->
        <line x1="40" y1="80" x2="60" y2="80" stroke="var(--terracotta)" stroke-width="0.5" stroke-dasharray="2,2"/>
        <text x="6" y="83" font-size="6">Jersey</text>
        <line x1="40" y1="140" x2="65" y2="140" stroke="var(--terracotta)" stroke-width="0.5" stroke-dasharray="2,2"/>
        <text x="6" y="143" font-size="6">Shorts</text>
        <line x1="40" y1="180" x2="68" y2="180" stroke="var(--terracotta)" stroke-width="0.5" stroke-dasharray="2,2"/>
        <text x="6" y="183" font-size="6">Sock</text>
        <line x1="40" y1="210" x2="66" y2="210" stroke="var(--terracotta)" stroke-width="0.5" stroke-dasharray="2,2"/>
        <text x="6" y="213" font-size="6">Boot</text>
        <line x1="100" y1="100" x2="120" y2="80" stroke="var(--terracotta)" stroke-width="0.5" stroke-dasharray="2,2"/>
        <text x="120" y="80" font-size="6">Squad #</text>
      </svg>
    </div>
  </div>
</div>
"""
    return page(13, "Player gear", body, "player-gear")

# Page 14: Goalkeeper kit
def page14():
    body = """
<div class="page-header">
  <div class="page-num">14</div>
  <div><div class="section-num">Section II</div><h1 class="section-title">Goalkeeper kit</h1></div>
</div>

<div class="two-col">
  <div>
    <p class="lead">A goalkeeper is the only player permitted to use hands within the penalty area — and is therefore the most padded.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Mandatory</h3>
    <ul style="font-size: 9pt; margin-left: 0.3in; list-style: disc;">
      <li><b>Jersey</b> in contrasting color to teammates and opponents</li>
      <li><b>Shorts</b> (or full-length pants for added protection)</li>
      <li><b>Socks</b> &amp; shin guards (same as outfield)</li>
      <li><b>Gloves</b> — the defining goalkeeper equipment</li>
    </ul>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Modern gloves</h3>
    <p style="font-size: 9pt;">Made of <b>latex foam</b> on the palm for grip in all weather, with a textile or knit back for fit. Top-tier gloves have <b>removable finger spines</b> — stiff plastic inserts that prevent hyperextension when the ball strikes a fingertip at 100 km/h.</p>

    <p style="font-size: 9pt; margin-top: 0.1in;">Most goalkeepers cut the finger spines out of their match gloves for better feel, but wear them in training. The trade-off is comfort vs. injury risk.</p>
  </div>
  <div>
    <div class="diagram">
      <div class="kicker" style="text-align: center; margin-bottom: 0.2in;">Goalkeeper glove (palm view)</div>
      <svg viewBox="0 0 180 220" style="width: 3.5in; margin: 0 auto; display: block;">
        <!-- Hand outline -->
        <path d="M 60 100 L 60 40 Q 60 25 70 25 L 70 25 L 70 50 L 75 50 L 75 20 Q 75 5 82 5 L 84 5 Q 91 5 91 20 L 91 50 L 96 50 L 96 15 Q 96 0 103 0 L 105 0 Q 112 0 112 15 L 112 50 L 117 50 L 117 20 Q 117 5 124 5 L 126 5 Q 133 5 133 20 L 133 50 L 138 50 L 138 25 Q 138 12 145 12 L 147 12 Q 154 12 154 30 L 154 100 Q 154 130 130 145 L 90 145 Q 60 130 60 100 Z"
              fill="var(--gold)" stroke="var(--ink)" stroke-width="1.5"/>
        <!-- Finger spines (highlighted) -->
        <g stroke="var(--terracotta)" stroke-width="2" stroke-linecap="round" opacity="0.6">
          <line x1="79" y1="10" x2="79" y2="48"/>
          <line x1="88" y1="5" x2="88" y2="48"/>
          <line x1="101" y1="3" x2="101" y2="48"/>
          <line x1="110" y1="3" x2="110" y2="48"/>
          <line x1="122" y1="7" x2="122" y2="48"/>
        </g>
        <!-- Latex dimples -->
        <g fill="var(--ink)" opacity="0.2">
          <circle cx="80" cy="70" r="1.5"/><circle cx="90" cy="70" r="1.5"/><circle cx="100" cy="70" r="1.5"/><circle cx="110" cy="70" r="1.5"/>
          <circle cx="80" cy="85" r="1.5"/><circle cx="90" cy="85" r="1.5"/><circle cx="100" cy="85" r="1.5"/><circle cx="110" cy="85" r="1.5"/>
          <circle cx="85" cy="100" r="1.5"/><circle cx="95" cy="100" r="1.5"/><circle cx="105" cy="100" r="1.5"/>
          <circle cx="90" cy="115" r="1.5"/><circle cx="100" cy="115" r="1.5"/>
          <circle cx="95" cy="130" r="1.5"/>
        </g>
        <!-- Cuff strap -->
        <rect x="50" y="135" width="100" height="20" fill="var(--terracotta)" stroke="var(--ink)" stroke-width="1.5" rx="3"/>
        <text x="100" y="148" font-size="7" text-anchor="middle" fill="var(--paper)" font-weight="700">VELCRO</text>
        <!-- Label leaders -->
        <line x1="79" y1="20" x2="20" y2="10" stroke="var(--terracotta)" stroke-width="0.5" stroke-dasharray="2,2"/>
        <text x="6" y="8" font-size="6">Finger spine</text>
        <line x1="100" y1="85" x2="20" y2="75" stroke="var(--terracotta)" stroke-width="0.5" stroke-dasharray="2,2"/>
        <text x="6" y="78" font-size="6">Latex dimples</text>
        <line x1="100" y1="145" x2="20" y2="135" stroke="var(--terracotta)" stroke-width="0.5" stroke-dasharray="2,2"/>
        <text x="6" y="138" font-size="6">Wrist strap</text>
      </svg>
      <p class="cap">The palm side of a modern goalkeeper glove. Visible: latex foam dimples (grip), finger spines (protection), and the velcro wrist strap (fit).</p>
    </div>
  </div>
</div>
"""
    return page(14, "Goalkeeper kit", body, "goalkeeper")

# Page 15: Referee kit
def page15():
    body = """
<div class="page-header">
  <div class="page-num">15</div>
  <div><div class="section-num">Section II</div><h1 class="section-title">Referee kit</h1></div>
</div>

<div class="two-col">
  <div>
    <p class="lead">A referee carries ten items on a matchday. The job is to be seen without being intrusive.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">On the body</h3>
    <ul style="font-size: 9pt; margin-left: 0.3in; list-style: disc;">
      <li><b>Jersey</b> — bright colour (typically neon yellow, green, or red) that contrasts with both teams</li>
      <li><b>Shorts</b> &amp; <b>socks</b> — black to match the jersey</li>
      <li><b>Whistle</b> — the Fox 40 Mini is the de facto standard</li>
      <li><b>Cards</b> — yellow (caution) and red (ejection) in back pocket</li>
      <li><b>Watch</b> with countdown timer (for added time)</li>
      <li><b>Pen &amp; notebook</b> — to record cautions, substitutions, and goals</li>
      <li><b>Coin</b> — for kick-off toss in pre-match procedure</li>
    </ul>
  </div>
  <div>
    <div class="factbox navy">
      <div class="eyebrow">Referee team</div>
      <h3 style="font-size: 14pt; margin-top: 0.1in;">Modern officiating crew</h3>
      <table style="width: 100%; font-size: 8.5pt; margin-top: 0.15in; border-collapse: collapse;">
        <tr><td style="padding: 0.05in 0;"><b>Referee</b></td><td>Main official</td></tr>
        <tr><td><b>AR1 / AR2</b></td><td>Two assistant referees (linesmen)</td></tr>
        <tr><td><b>4th official</b></td><td>Manages subs &amp; bench</td></tr>
        <tr><td><b>VAR</b></td><td>Reviews goals, red cards, penalties</td></tr>
        <tr><td><b>AVAR</b></td><td>VAR assistant</td></tr>
      </table>
      <p style="font-size: 8pt; margin-top: 0.15in; opacity: 0.9;">In 2025+ top competitions, referees wear a <b>chest camera</b> and <b>microphone</b> that fans hear on TV broadcasts.</p>
    </div>

    <div class="sidebar" style="margin-top: 0.3in;">
      <h3>The yellow card</h3>
      <p style="font-size: 8.5pt;">Invented by English referee Ken Aston in 1970 during the Mexico World Cup. He reportedly picked yellow and red because they matched the traffic-light colours and were the only ones visible on a black-and-white TV.</p>
    </div>
  </div>
</div>
"""
    return page(15, "Referee kit", body, "referee")

# Page 16: Ball evolution
def page16():
    body = """
<div class="page-header">
  <div class="page-num">16</div>
  <div><div class="section-num">Section II</div><h1 class="section-title">Match ball evolution</h1></div>
</div>

<div class="two-col" style="margin-top: 0.2in;">
  <div>
    <p class="lead">From hand-stitched leather to thermally bonded 12-panel synthetics — the modern ball flies 30% faster than its 1970 counterpart.</p>
  </div>
  <div>
    <div class="diagram" style="min-height: 4in;">
      <div class="kicker" style="text-align: center; margin-bottom: 0.2in;">Match ball, 1970 → 2025</div>
      <div style="display: flex; justify-content: space-around; align-items: center;">
        <svg viewBox="0 0 80 80" style="width: 1.5in;">
          <defs>
            <radialGradient id="b1970" cx="35%" cy="30%">
              <stop offset="0%" stop-color="#c9a961"/>
              <stop offset="100%" stop-color="#7a5a1c"/>
            </radialGradient>
          </defs>
          <circle cx="40" cy="40" r="35" fill="url(#b1970)" stroke="var(--ink)" stroke-width="1.5"/>
          <g stroke="var(--ink)" stroke-width="0.6" fill="none">
            <polygon points="40,5 65,25 65,55 40,75 15,55 15,25"/>
            <line x1="40" y1="5" x2="40" y2="75"/>
            <line x1="15" y1="25" x2="65" y2="25"/>
            <line x1="15" y1="55" x2="65" y2="55"/>
          </g>
        </svg>
        <div style="font-size: 24pt; color: var(--terracotta);">→</div>
        <svg viewBox="0 0 80 80" style="width: 1.5in;">
          <defs>
            <radialGradient id="b2025" cx="35%" cy="30%">
              <stop offset="0%" stop-color="#fff"/>
              <stop offset="100%" stop-color="#d4cba0"/>
            </radialGradient>
          </defs>
          <circle cx="40" cy="40" r="35" fill="url(#b2025)" stroke="var(--ink)" stroke-width="1.5"/>
          <g stroke="var(--ink)" stroke-width="1.2" fill="none">
            <polygon points="40,5 60,20 60,40 50,55 30,55 20,40 20,20"/>
            <polygon points="40,5 50,15 40,15"/>
            <polygon points="60,40 70,50 60,55"/>
            <polygon points="50,55 55,75 35,75"/>
            <polygon points="20,40 10,50 25,50"/>
          </g>
        </svg>
      </div>
      <table style="width: 100%; font-size: 8pt; margin-top: 0.3in;">
        <tr style="background: var(--green); color: var(--paper);">
          <th style="padding: 0.06in 0.1in; text-align: left;"></th>
          <th style="padding: 0.06in 0.1in; text-align: left;">1970 Telstar</th>
          <th style="padding: 0.06in 0.1in; text-align: left;">2025 Connected</th>
        </tr>
        <tr>
          <td style="padding: 0.06in 0.1in;">Panels</td>
          <td>32 (hand-stitched)</td>
          <td>12 (thermal bonded)</td>
        </tr>
        <tr>
          <td style="padding: 0.06in 0.1in;">Surface</td>
          <td>Leather</td>
          <td>PU textured</td>
        </tr>
        <tr>
          <td style="padding: 0.06in 0.1in;">Water uptake</td>
          <td>+15% in 30 min</td>
          <td>+0.1%</td>
        </tr>
        <tr>
          <td style="padding: 0.06in 0.1in;">Stitching</td>
          <td>Wool, 250 stitches</td>
          <td>Thermal bond, 0 stitches</td>
        </tr>
        <tr>
          <td style="padding: 0.06in 0.1in;">Top speed</td>
          <td>~110 km/h</td>
          <td>~135 km/h</td>
        </tr>
      </table>
    </div>
  </div>
</div>
"""
    return page(16, "Match ball evolution", body, "ball-evolution")

# Page 17: 17 Laws
def page17():
    laws = [
        ('1', 'The Field of Play', 'Pitch dimensions, markings, goals.'),
        ('2', 'The Ball', 'Size 5, 68–70 cm, 410–450 g, certified.'),
        ('3', 'The Players', '11 per side, 3–5 subs, sent off for red.'),
        ('4', 'The Players\' Equipment', 'No jewellery, mandatory shinguards.'),
        ('5', 'The Referee', 'Enforces Laws; final decision on the field.'),
        ('6', 'The Other Match Officials', 'ARs, 4th, VAR, AVAR.'),
        ('7', 'The Duration of the Match', '2 × 45 minutes, plus stoppage.'),
        ('8', 'The Start and Restart of Play', 'Kick-off, dropped ball, kick-ins.'),
        ('9', 'The Ball In and Out of Play', 'Touchline, goal line, in the air.'),
        ('10', 'Determining the Outcome', 'Goal = ball fully over goal line.'),
        ('11', 'Offside', 'Beyond second-last defender when ball played.'),
        ('12', 'Fouls and Misconduct', 'Direct / indirect free kicks, cards.'),
        ('13', 'Free Kicks', 'Direct (can score) and indirect (need 2nd touch).'),
        ('14', 'The Penalty Kick', '12 yards, 11 m, one kicker vs GK.'),
        ('15', 'The Throw-In', 'Two hands from behind the head, both feet down.'),
        ('16', 'The Goal Kick', 'From anywhere inside the goal area, ball outside box.'),
        ('17', 'The Corner Kick', 'From the corner arc, ball in the quarter.'),
    ]
    law_rows = ''
    for num, name, desc in laws:
        law_rows += f'<tr><td style="padding: 0.1in 0.12in; font-family: var(--serif); font-size: 12pt; color: var(--terracotta); font-weight: 700; vertical-align: top; width: 0.4in;">{num}</td><td style="padding: 0.1in 0.12in; vertical-align: top;"><b style="font-size: 9.5pt;">{name}</b><br><span style="font-size: 8pt; color: var(--ink-mute);">{desc}</span></td></tr>'

    body = f"""
<div class="page-header">
  <div class="page-num">17</div>
  <div><div class="section-num">Section II</div><h1 class="section-title">17 Laws at a glance</h1></div>
</div>

<p class="lead" style="margin: 0.2in 0 0.2in;">The IFAB's <em>Laws of the Game</em> are updated annually each March. The 17 below are the current (2024/25) version, each with the official summary.</p>

<table style="width: 100%; border-collapse: collapse; font-size: 8.5pt;">{law_rows}</table>
"""
    return page(17, "17 Laws at a glance", body, "laws")

# Page 18: Quick reference
def page18():
    body = """
<div class="page-header">
  <div class="page-num">18</div>
  <div><div class="section-num">Section II</div><h1 class="section-title">Quick reference card</h1></div>
</div>

<div class="factbox dark" style="margin-bottom: 0.3in;">
  <div class="eyebrow" style="color: var(--gold);">Pocket card</div>
  <h3 style="font-size: 16pt; margin-top: 0.1in; color: var(--paper);">Soccer — at a glance</h3>
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.2in;">
  <div>
    <h3 style="font-family: var(--serif); color: var(--green); font-size: 12pt; margin-bottom: 0.1in;">Match</h3>
    <ul style="font-size: 8.5pt; margin-left: 0.25in; list-style: disc; line-height: 1.5;">
      <li>11 per team</li>
      <li>2 × 45 minutes + stoppage</li>
      <li>3 substitutions (5 in UEFA Club comps)</li>
      <li>Sub windows: stoppages only (from 2024)</li>
      <li>Goal kicks: ball must be stationary, fully outside box</li>
    </ul>
  </div>
  <div>
    <h3 style="font-family: var(--serif); color: var(--green); font-size: 12pt; margin-bottom: 0.1in;">Pitch &amp; ball</h3>
    <ul style="font-size: 8.5pt; margin-left: 0.25in; list-style: disc; line-height: 1.5;">
      <li>105 × 68 m (international)</li>
      <li>68–70 cm circumference</li>
      <li>410–450 g</li>
      <li>Goal: 7.32 × 2.44 m</li>
      <li>Area: 16.5 m box, 5.5 m goal area</li>
    </ul>
  </div>
</div>

<div style="margin-top: 0.3in;">
  <h3 style="font-family: var(--serif); color: var(--green); font-size: 12pt; margin-bottom: 0.1in;">Cards (cumulative cautions)</h3>
  <table style="width: 100%; font-size: 8.5pt; border-collapse: collapse;">
    <tr style="background: var(--paper-deep);">
      <th style="padding: 0.06in 0.1in; text-align: left; width: 0.6in;">Card</th>
      <th style="padding: 0.06in 0.1in; text-align: left;">Effect</th>
    </tr>
    <tr><td style="padding: 0.06in 0.1in;">🟨 Yellow</td><td>Caution; two yellows in same match = red</td></tr>
    <tr><td style="padding: 0.06in 0.1in;">🟥 Red</td><td>Ejection; team plays with 10 (or fewer)</td></tr>
    <tr><td style="padding: 0.06in 0.1in;">5+ 🟨</td><td>One-match ban (comp dependent)</td></tr>
  </table>
</div>

<div class="callout" style="margin-top: 0.3in;">
  <h3 style="font-size: 11pt;">Rule of thumb</h3>
  <p style="font-size: 9pt; margin: 0;">A foul is a <b>free kick</b>. A foul denying a goal is a <b>red card</b>. A hand ball with the arm away from the body in the box is a <b>penalty</b>. Everything else is in between.</p>
</div>
"""
    return page(18, "Quick reference", body, "quick-ref")

print("Wrote pages 4-18")

# Write all page files
pages = [page4(), page5(), page6(), page7(), page8(), page9(), page10(),
         page11(), page12(), page13(), page14(), page15(), page16(),
         page17(), page18()]
for i, html in enumerate(pages, start=4):
    with open(f'{PAGES_DIR}/{i:02d}-page.html', 'w') as f:
        f.write(html)
print(f"Wrote {len(pages)} page files")

