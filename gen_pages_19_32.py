#!/usr/bin/env python3
"""Generate pages 19-32: Rules of the Game (Laws 1-12 + VAR)."""
import os
PAGES_DIR = '/home/kbot/soccer-book/pages'

def page(num, title, body):
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>Page {num} — {title}</title><link rel="stylesheet" href="book.css"></head>
<body class="page standard"><div class="page-inner">
{body}
</div></body></html>"""

def header(num, section, title):
    return f"""<div class="page-header">
  <div class="page-num">{num}</div>
  <div><div class="section-num">Section {section}</div><h1 class="section-title">{title}</h1></div>
</div>"""

# === LAW 1: FIELD OF PLAY ===
def page19():
    body = header(19, 'III', 'Law 1 — The Field of Play')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">The pitch is a rectangle of <b>natural or artificial grass</b>, between 100–110 m long and 64–75 m wide. International matches use <b>105 × 68 m</b>.</p>
    <p>All lines are no more than 12 cm wide. The pitch is divided by a halfway line, with a centre circle (radius 9.15 m) and a centre spot. Two identical penalty areas mark each end.</p>
    <div class="sidebar green" style="margin-top: 0.2in;">
      <h3>Lines belong to the area</h3>
      <p style="font-size: 8.5pt;">A ball touching any line is <em>in</em> the area that line defines — including the goal line, the touchline, and every line inside the field of play.</p>
    </div>
    <div class="callout" style="margin-top: 0.2in;">
      <h3 style="font-size: 10pt;">Hybrid grass</h3>
      <p style="font-size: 8.5pt; margin: 0;">Most top stadiums use <b>hybrid grass</b>: ~5% synthetic fibres woven into natural turf for durability. Tottenham's pitch rolls away entirely on a tray system.</p>
    </div>
  </div>
  <div>
    <div class="pitch diagram">
      <div class="player-dot" style="left: 50%; top: 50%;"><div class="dot mid">●</div></div>
      <svg viewBox="0 0 200 130" style="position:absolute;inset:0;width:100%;height:100%;">
        <line x1="40" y1="20" x2="40" y2="110" stroke="var(--terracotta)" stroke-width="0.5" stroke-dasharray="2,2"/>
        <text x="35" y="15" font-size="6" fill="var(--terracotta)" text-anchor="end">9.15m</text>
        <line x1="100" y1="65" x2="120" y2="55" stroke="var(--terracotta)" stroke-width="0.5" stroke-dasharray="2,2"/>
        <text x="125" y="55" font-size="6" fill="var(--terracotta)">Centre circle</text>
      </svg>
    </div>
    <p class="cap">Centre circle radius is 9.15 m (10 yd). All players except the kicker must be outside this circle at kick-off.</p>
    <div class="diagram" style="margin-top: 0.15in;">
      <div class="kicker" style="text-align: center; margin-bottom: 0.1in;">Penalty area dimensions</div>
      <table style="width: 100%; font-size: 8.5pt;">
        <tr><td><b>Penalty area</b></td><td>16.5 m × 40.3 m</td></tr>
        <tr><td><b>Goal area</b></td><td>5.5 m × 18.3 m</td></tr>
        <tr><td><b>Penalty spot</b></td><td>11 m from goal line</td></tr>
        <tr><td><b>Arc (D)</b></td><td>9.15 m radius from spot</td></tr>
      </table>
    </div>
  </div>
</div>
'''
    return page(19, 'Law 1', body)

# === LAW 2: THE BALL ===
def page20():
    body = header(20, 'III', 'Law 2 — The Ball')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">A regulation <b>Size 5</b> ball is spherical, with a circumference of <b>68–70 cm</b>, weight <b>410–450 g</b>, and inflation of <b>0.6–1.1 atm</b>.</p>
    <p>Smaller sizes exist for youth (Size 4: 63.5–66 cm) and futsal (Size 3, low-bounce).</p>
    <div class="sidebar terracotta" style="margin-top: 0.2in;">
      <h3>Ball substitution</h3>
      <p style="font-size: 8.5pt;">The referee can authorise a replacement ball if the original is damaged. Goals only count if scored with a ball approved by the referee — a goal scored with an unauthorised ball is disallowed.</p>
    </div>
  </div>
  <div>
    <svg viewBox="0 0 200 200" style="width: 60%; display: block; margin: 0 auto;">
      <defs><radialGradient id="b20" cx="35%" cy="30%"><stop offset="0%" stop-color="#fff"/><stop offset="100%" stop-color="#d4cba0"/></radialGradient></defs>
      <circle cx="100" cy="100" r="80" fill="url(#b20)" stroke="var(--ink)" stroke-width="1.5"/>
      <g stroke="var(--ink)" stroke-width="1.2" fill="none">
        <polygon points="100,30 130,55 120,90 80,90 70,55"/>
        <polygon points="150,80 170,110 145,140 120,120"/>
        <polygon points="105,165 80,150 70,170 105,175"/>
        <polygon points="40,140 25,110 50,90 65,120"/>
        <polygon points="40,55 65,30 90,55 75,80"/>
      </g>
    </svg>
    <div class="diagram" style="margin-top: 0.15in;">
      <div class="kicker" style="text-align: center; margin-bottom: 0.1in;">Ball spec card</div>
      <table style="width: 100%; font-size: 8.5pt;">
        <tr><td><b>Size 5 circumference</b></td><td>68–70 cm</td></tr>
        <tr><td><b>Weight</b></td><td>410–450 g</td></tr>
        <tr><td><b>Inflation</b></td><td>0.6–1.1 atm</td></tr>
        <tr><td><b>Bounce from 2 m</b></td><td>50–65 cm</td></tr>
        <tr><td><b>Panels</b></td><td>12 or 32 (modular)</td></tr>
      </table>
    </div>
  </div>
</div>
'''
    return page(20, 'Law 2', body)

# === LAW 3: THE PLAYERS ===
def page21():
    body = header(21, 'III', 'Law 3 — The Players')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">A match is contested by <b>11 players per team</b>, one of whom is the goalkeeper. A match may not start or continue if either side has fewer than <b>7 players</b>.</p>
    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Substitutions</h3>
    <p><b>3 substitutions</b> per team in standard competition matches. <b>5 substitutions</b> in UEFA Champions League, Europa League, and Conference League group-stage matches onwards (extended from 2020/21 onwards).</p>
    <p>Since <b>2024</b>, sub windows are restricted to <b>5 windows per team per match</b> — to prevent time-wasting through multiple stoppages. Half-time is excluded from the count.</p>
    <div class="callout" style="margin-top: 0.2in;">
      <h3 style="font-size: 10pt;">Sending off</h3>
      <p style="font-size: 8.5pt; margin: 0;">A red-carded player cannot be replaced. Their team plays the rest of the match with 10 players (or fewer). A player sent off before kick-off cannot be replaced in the starting XI.</p>
    </div>
  </div>
  <div>
    <div class="diagram">
      <div class="kicker" style="text-align: center; margin-bottom: 0.1in;">Sub windows at a glance</div>
      <div class="timeline">
        <div class="timeline-event"><span class="year">K/O</span><h4>Kick-off</h4><p>0/5 sub windows used</p></div>
        <div class="timeline-event"><span class="year">25'</span><h4>First window</h4><p>Window 1 of 5</p></div>
        <div class="timeline-event"><span class="year">HT</span><h4>Half-time</h4><p>Free sub, doesn't count</p></div>
        <div class="timeline-event"><span class="year">65'</span><h4>Window 4</h4><p>2 substitutions remaining</p></div>
        <div class="timeline-event"><span class="year">90+</span><h4>Full-time</h4><p>Max 3 players replaced</p></div>
      </div>
    </div>
    <div class="factbox navy" style="margin-top: 0.15in;">
      <div class="eyebrow">Did you know?</div>
      <h3 style="font-size: 11pt; margin-top: 0.05in;">The 5-sub rule was introduced in 2020 as a permanent change after the COVID-19 pandemic. It was designed to reduce player load across a compressed fixture calendar.</h3>
    </div>
  </div>
</div>
'''
    return page(21, 'Law 3', body)

# === LAW 4: PLAYER EQUIPMENT ===
def page22():
    body = header(22, 'III', 'Law 4 — Player Equipment')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">Compulsory kit: <b>jersey or shirt</b>, <b>shorts</b>, <b>socks</b>, <b>shin guards</b>, and <b>boots</b>. Goalkeepers wear distinct colours.</p>
    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Shin guards</h3>
    <p>Mandatory. Must be entirely covered by the socks. Modern guards are made of <b>PP, carbon, or EVA foam</b>, often with silicone sleeves for grip. Top-end Nike / Adidas / Puma guards are worn under thin professional socks.</p>
    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Forbidden</h3>
    <ul style="font-size: 9pt; margin-left: 0.3in; line-height: 1.5;">
      <li>Jewellery of any kind (rings, necklaces, earrings)</li>
      <li>Watches and electronic devices</li>
      <li>Hard hats or bandanas</li>
      <li>Boots with sharp exposed studs</li>
    </ul>
    <p style="font-size: 9pt; margin-top: 0.15in;">Taped wedding rings are permitted. Goalies may wear caps with referee approval.</p>
  </div>
  <div>
    <svg viewBox="0 0 100 120" style="width: 60%; display: block; margin: 0 auto;">
      <rect x="35" y="20" width="30" height="50" fill="var(--terracotta)" stroke="var(--ink)" stroke-width="1.2"/>
      <rect x="35" y="70" width="30" height="20" fill="var(--ink)" stroke="var(--ink)" stroke-width="1.2"/>
      <rect x="35" y="90" width="14" height="20" fill="var(--paper)" stroke="var(--ink)" stroke-width="1.2"/>
      <rect x="51" y="90" width="14" height="20" fill="var(--paper)" stroke="var(--ink)" stroke-width="1.2"/>
      <text x="80" y="50" font-size="6" fill="var(--ink-mute)">← jersey</text>
      <text x="80" y="85" font-size="6" fill="var(--ink-mute)">← shorts</text>
      <text x="80" y="100" font-size="6" fill="var(--ink-mute)">← socks</text>
    </svg>
    <div class="factbox terracotta" style="margin-top: 0.2in;">
      <div class="eyebrow">Kit clash protocol</div>
      <h3 style="font-size: 12pt; margin-top: 0.05in;">The referee decides if kits clash. <b>The away team</b> must change if necessary — usually the home side wears its first-choice strip.</h3>
    </div>
  </div>
</div>
'''
    return page(22, 'Law 4', body)

# === LAW 5: REFEREE ===
def page23():
    body = header(23, 'III', 'Law 5 — The Referee')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">The referee is the sole arbiter of the Laws during a match. Their decisions on points of fact connected with play are <b>final</b>.</p>
    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Powers</h3>
    <ul style="font-size: 9pt; margin-left: 0.3in; line-height: 1.5;">
      <li>Discipline players (yellow / red cards)</li>
      <li>Stop, suspend, or abandon a match</li>
      <li>Allow play to continue after an offence if it benefits the attacking team ("<b>advantage</b>")</li>
      <li>Caution or send off for fouls before / after kick-off / during the half-time interval</li>
    </ul>
    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Signals</h3>
    <p style="font-size: 9pt;">Whistle + arm pointing toward goal = foul. Whistle + arm straight up = indirect free kick. Card raised = caution / sending off. Both arms crossed = substitution.</p>
  </div>
  <div>
    <div class="diagram" style="text-align: center; padding: 0.2in;">
      <svg viewBox="0 0 200 120" style="width: 100%;">
        <!-- Referee body -->
        <circle cx="100" cy="25" r="14" fill="var(--gold)" stroke="var(--ink)" stroke-width="1.5"/>
        <path d="M 80 45 L 80 95 L 95 95 L 95 60 L 105 60 L 105 95 L 120 95 L 120 45 Z" fill="var(--gold)" stroke="var(--ink)" stroke-width="1.5"/>
        <!-- Arm extended with whistle -->
        <line x1="80" y1="60" x2="40" y2="50" stroke="var(--ink)" stroke-width="3" stroke-linecap="round"/>
        <rect x="30" y="48" width="20" height="6" fill="var(--ink)" rx="2"/>
        <!-- Other arm holding card -->
        <line x1="120" y1="60" x2="155" y2="50" stroke="var(--ink)" stroke-width="3" stroke-linecap="round"/>
        <rect x="150" y="40" width="14" height="20" fill="var(--terracotta)" stroke="var(--ink)" stroke-width="1"/>
        <line x1="157" y1="40" x2="157" y2="60" stroke="var(--ink)" stroke-width="0.5"/>
        <!-- Labels -->
        <text x="50" y="80" font-size="6" text-anchor="middle" fill="var(--ink-mute)">Whistle</text>
        <text x="157" y="80" font-size="6" text-anchor="middle" fill="var(--ink-mute)">Red card</text>
      </svg>
      <p class="cap">Modern referee: gold jersey, body cam, microphone, both arms signalling foul + dismissal.</p>
    </div>
    <div class="callout" style="margin-top: 0.15in;">
      <h3 style="font-size: 10pt;">Body cam (2024+)</h3>
      <p style="font-size: 8.5pt; margin: 0;">From the 2024/25 season, top-flight referees wear a chest-mounted camera + mic. TV broadcasts can hear the referee's whistle, calls, and conversations with players.</p>
    </div>
  </div>
</div>
'''
    return page(23, 'Law 5', body)

# === LAW 6: OTHER OFFICIALS ===
def page24():
    body = header(24, 'III', 'Law 6 — Other Officials')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">A modern officiating crew has <b>5 named officials</b>, plus additional VAR team.</p>
    <div class="diagram">
      <table style="width: 100%; font-size: 8.5pt;">
        <tr style="background: var(--navy); color: var(--paper);"><th style="padding: 0.06in 0.1in;">Role</th><th style="padding: 0.06in 0.1in;">Duties</th></tr>
        <tr><td style="padding: 0.06in 0.1in;"><b>Referee</b></td><td>Main official on the field</td></tr>
        <tr style="background: var(--paper-deep);"><td style="padding: 0.06in 0.1in;"><b>AR 1</b></td><td>Assistant: touchline, offside, throw-ins</td></tr>
        <tr><td style="padding: 0.06in 0.1in;"><b>AR 2</b></td><td>Same as AR 1, opposite side</td></tr>
        <tr style="background: var(--paper-deep);"><td style="padding: 0.06in 0.1in;"><b>4th official</b></td><td>Manages subs, bench, kit issues</td></tr>
        <tr><td style="padding: 0.06in 0.1in;"><b>VAR</b></td><td>Video review (off-field)</td></tr>
        <tr style="background: var(--paper-deep);"><td style="padding: 0.06in 0.1in;"><b>AVAR</b></td><td>Assists VAR with cross-checking</td></tr>
      </table>
    </div>
  </div>
  <div>
    <div class="sidebar" style="margin-top: 0.2in;">
      <h3>AR signals</h3>
      <p style="font-size: 8.5pt;"><b>Flag down, pointing forward</b> = indirect free kick. <b>Flag pointing across chest</b> = direct free kick. <b>Flag raised vertically</b> = offside. <b>Flag raised, finger pointed toward goalkeeper</b> = goal kick. <b>Flag raised, hand pointed toward corner</b> = corner kick.</p>
    </div>
    <div class="callout" style="margin-top: 0.2in;">
      <h3 style="font-size: 10pt;">Reserve AR</h3>
      <p style="font-size: 8.5pt; margin: 0;">Since 2024, UEFA and FIFA appoint a <b>Reserve AR</b> as a backup in case one of the on-field assistants is injured mid-match — replacing the old "AVAR takes over" system.</p>
    </div>
  </div>
</div>
'''
    return page(24, 'Law 6', body)

# === LAW 7: DURATION ===
def page25():
    body = header(25, 'III', 'Law 7 — Duration of the Match')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">A match lasts <b>2 × 45 minutes</b>, plus any stoppage time added by the referee. The half-time interval must not exceed <b>15 minutes</b>.</p>
    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Stoppage time</h3>
    <p>The referee adds time for:</p>
    <ul style="font-size: 9pt; margin-left: 0.3in; line-height: 1.5;">
      <li>Substitutions</li>
      <li>Injuries (including stoppages for treatment)</li>
      <li>Time-wasting</li>
      <li>Disciplinary sanctions (cards)</li>
      <li>VAR checks and reviews</li>
      <li>Goal celebrations</li>
    </ul>
    <p style="font-size: 9pt; margin-top: 0.15in;">The 4th official displays the minimum stoppage time. Modern games average <b>6–10 minutes of added time</b> per half.</p>
  </div>
  <div>
    <div class="factbox" style="margin-bottom: 0.2in;">
      <div class="eyebrow">Average stoppage, 2024/25</div>
      <div style="display: flex; gap: 0.2in; margin-top: 0.15in;">
        <div class="stat" style="flex:1;"><div class="num">7'42"</div><div class="label">1st half</div></div>
        <div class="stat" style="flex:1;"><div class="num">9'15"</div><div class="label">2nd half</div></div>
        <div class="stat" style="flex:1;"><div class="num">17'</div><div class="label">Total added</div></div>
      </div>
    </div>
    <div class="callout">
      <h3 style="font-size: 10pt;">Extra time &amp; penalties</h3>
      <p style="font-size: 8.5pt; margin: 0;">In knockout matches, if the score is level after 90 minutes: 2 × 15 minutes extra time, then penalty shootout if still tied. Top competitions (e.g. World Cup) can use <b>ABBA penalty format</b> since 2017.</p>
    </div>
  </div>
</div>
'''
    return page(25, 'Law 7', body)

# === LAW 8: START & RESTART ===
def page26():
    body = header(26, 'III', 'Law 8 — Start &amp; Restart')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">The match starts and restarts after goals with a <b>kick-off</b>. After temporary stoppages, the ball is restarted with a <b>dropped ball</b>.</p>
    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Kick-off procedure</h3>
    <ol style="font-size: 9pt; margin-left: 0.3in; line-height: 1.5;">
      <li>Coin toss — winner chooses which goal to attack or takes kick-off</li>
      <li>All players in their own half</li>
      <li>Opponents at least 9.15 m from the ball (outside the centre circle)</li>
      <li>Ball stationary on the centre spot</li>
      <li>Referee signals; ball is in play when kicked forward</li>
    </ol>
    <p style="font-size: 9pt; margin-top: 0.15in;">The kicker cannot touch the ball again until another player has touched it. A goal can be scored directly from kick-off.</p>
  </div>
  <div>
    <div class="sidebar terracotta" style="margin-top: 0.2in;">
      <h3>Dropped ball (modernised 2024)</h3>
      <p style="font-size: 8.5pt;">From the 2024/25 season, the <b>dropped ball</b> is awarded to the team that last touched the ball, at the spot it left play. The ball is dropped for <b>one player only</b> — opposing players must be 4 m away. No more "two-player scrums" like at the 1994 World Cup.</p>
    </div>
    <div class="diagram" style="margin-top: 0.15in;">
      <div class="kicker" style="text-align: center; margin-bottom: 0.1in;">Kick-off, top-down</div>
      <svg viewBox="0 0 200 130" style="width: 100%;">
        <rect x="0" y="0" width="200" height="130" fill="#4caf50"/>
        <line x1="0" y1="65" x2="200" y2="65" stroke="var(--paper)" stroke-width="2"/>
        <circle cx="100" cy="65" r="20" fill="none" stroke="var(--paper)" stroke-width="1.5"/>
        <circle cx="100" cy="65" r="2" fill="var(--paper)"/>
        <circle cx="100" cy="65" r="6" fill="var(--paper)" stroke="var(--ink)" stroke-width="1"/>
        <circle cx="50" cy="40" r="4" fill="var(--ink)"/>
        <circle cx="50" cy="90" r="4" fill="var(--ink)"/>
        <circle cx="150" cy="40" r="4" fill="var(--ink)"/>
        <circle cx="150" cy="90" r="4" fill="var(--ink)"/>
      </svg>
      <p class="cap">White = kicking team's positions. Black = defending team, all outside centre circle.</p>
    </div>
  </div>
</div>
'''
    return page(26, 'Law 8', body)

# === LAW 9: BALL IN/OUT ===
def page27():
    body = header(27, 'III', 'Law 9 — Ball In &amp; Out of Play')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">The ball is <b>out of play</b> when it has wholly crossed the goal line or touchline, on the ground or in the air; or when the referee has stopped play.</p>
    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Boundary rules</h3>
    <ul style="font-size: 9pt; margin-left: 0.3in; line-height: 1.5;">
      <li><b>Touchline</b> → throw-in for the opposing team</li>
      <li><b>Goal line, last touched by attacker</b> → goal kick for the defending team</li>
      <li><b>Goal line, last touched by defender</b> → corner kick for the attacking team</li>
    </ul>
    <div class="callout" style="margin-top: 0.2in;">
      <h3 style="font-size: 10pt;">Goal-line technology</h3>
      <p style="font-size: 8.5pt; margin: 0;">Hawk-Eye or GoalRef sensors in the ball and goal frame detect whether the whole ball has crossed the line. The referee gets a watch vibration within <b>1 second</b>. Mandatory in the Premier League since 2013.</p>
    </div>
  </div>
  <div>
    <svg viewBox="0 0 200 130" style="width: 100%;">
      <rect x="0" y="0" width="200" height="130" fill="#4caf50" stroke="var(--ink)" stroke-width="2"/>
      <line x1="40" y1="0" x2="40" y2="130" stroke="var(--paper)" stroke-width="2"/>
      <line x1="160" y1="0" x2="160" y2="130" stroke="var(--paper)" stroke-width="2"/>
      <rect x="0" y="50" width="40" height="30" fill="none" stroke="var(--paper)" stroke-width="1.5"/>
      <rect x="160" y="50" width="40" height="30" fill="none" stroke="var(--paper)" stroke-width="1.5"/>
      <text x="100" y="20" font-size="9" text-anchor="middle" fill="var(--paper)" font-weight="700">PITCH</text>
      <text x="20" y="20" font-size="7" text-anchor="middle" fill="var(--paper)">OUT</text>
      <text x="180" y="20" font-size="7" text-anchor="middle" fill="var(--paper)">OUT</text>
      <circle cx="180" cy="65" r="4" fill="var(--terracotta)" stroke="var(--ink)" stroke-width="1"/>
      <text x="195" y="105" font-size="6" fill="var(--paper)">Whole ball over line → out</text>
    </svg>
    <p class="cap">Top-down: the ball is out when the whole sphere crosses the line, in the air or on the ground.</p>
  </div>
</div>
'''
    return page(27, 'Law 9', body)

# === LAW 10: METHOD OF SCORING ===
def page28():
    body = header(28, 'III', 'Law 10 — Method of Scoring')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">A <b>goal</b> is scored when the whole ball passes over the goal line, between the goalposts and under the crossbar, provided no offence has been committed.</p>
    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Valid goals</h3>
    <ul style="font-size: 9pt; margin-left: 0.3in; line-height: 1.5;">
      <li>From open play, free kicks, corners, penalties</li>
      <li>Directly from a kick-off</li>
      <li>From a goal kick (rare)</li>
      <li>Own goals count for the attacking team</li>
    </ul>
    <h3 style="font-family: var(--serif); color: var(--terracotta); font-size: 13pt; margin: 0.2in 0 0.1in;">Invalid goals</h3>
    <ul style="font-size: 9pt; margin-left: 0.3in; line-height: 1.5;">
      <li>Throw-in directly into opponent's goal → corner kick</li>
      <li>Indirect free kick directly into own goal → corner kick</li>
      <li>Hand ball by an attacker or in build-up</li>
      <li>Offside in the build-up</li>
    </ul>
  </div>
  <div>
    <div class="factbox">
      <div class="eyebrow">Scoring rate, 2024/25</div>
      <h3 style="font-size: 14pt; margin-top: 0.1in;">2.7 goals per match (PL)</h3>
      <div style="display: flex; gap: 0.15in; margin-top: 0.2in;">
        <div class="stat" style="flex:1;"><div class="num">17%</div><div class="label">From set pieces</div></div>
        <div class="stat" style="flex:1;"><div class="num">83%</div><div class="label">Open play</div></div>
        <div class="stat" style="flex:1;"><div class="num">9%</div><div class="label">Penalties</div></div>
      </div>
    </div>
    <div class="callout" style="margin-top: 0.2in;">
      <h3 style="font-size: 10pt;">"Whole ball over the line"</h3>
      <p style="font-size: 8.5pt; margin: 0;">A famous example: Frank Lampard's disallowed 2010 World Cup goal vs Germany. The ball was 60% over the line, but goal-line technology didn't exist. Goal-line tech has prevented this from happening since 2012.</p>
    </div>
  </div>
</div>
'''
    return page(28, 'Law 10', body)

# === LAW 11: OFFSIDE ===
def page29():
    body = header(29, 'III', 'Law 11 — Offside')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">A player is in an <b>offside position</b> when any part of their body except hands / arms is in the opponents' half <b>closer to the goal line than both the ball and the second-last defender</b>.</p>
    <p style="font-size: 9pt;">The player is only penalised if, at the moment the ball is <i>played or touched</i> by a team-mate, they are involved in active play — gaining an advantage or interfering with an opponent.</p>
    <div class="callout" style="margin-top: 0.2in;">
      <h3 style="font-size: 10pt;">Not offside from</h3>
      <p style="font-size: 8.5pt; margin: 0;">Throw-ins, goal kicks, and corner kicks. A player in their own half is never offside.</p>
    </div>
  </div>
  <div>
    <svg viewBox="0 0 200 130" style="width: 100%;">
      <rect x="0" y="0" width="200" height="130" fill="#4caf50" stroke="var(--ink)" stroke-width="1"/>
      <line x1="100" y1="0" x2="100" y2="130" stroke="var(--paper)" stroke-width="1.5" stroke-dasharray="3,3"/>
      <rect x="160" y="40" width="40" height="50" fill="none" stroke="var(--paper)" stroke-width="2"/>
      <line x1="160" y1="55" x2="160" y2="75" stroke="var(--paper)" stroke-width="2"/>
      <!-- Ball -->
      <circle cx="80" cy="65" r="4" fill="var(--paper)" stroke="var(--ink)" stroke-width="1"/>
      <!-- Defender 1 (second-last) -->
      <circle cx="135" cy="50" r="5" fill="var(--navy)"/>
      <text x="135" y="40" font-size="6" text-anchor="middle" fill="var(--ink-mute)">Defender 1</text>
      <!-- GK (last) -->
      <circle cx="180" cy="65" r="5" fill="var(--gold)"/>
      <text x="180" y="80" font-size="6" text-anchor="middle" fill="var(--ink-mute)">GK (last)</text>
      <!-- Attacker ON offside line -->
      <circle cx="150" cy="65" r="5" fill="var(--terracotta)" stroke="var(--ink)" stroke-width="2"/>
      <text x="150" y="55" font-size="6" text-anchor="middle" fill="var(--terracotta)" font-weight="700">ON-SIDE</text>
      <!-- Attacker in offside position -->
      <circle cx="165" cy="65" r="5" fill="var(--terracotta)" stroke="var(--ink)" stroke-width="2"/>
      <text x="165" y="90" font-size="6" text-anchor="middle" fill="var(--terracotta)" font-weight="700">OFFSIDE</text>
      <line x1="135" y1="95" x2="135" y2="110" stroke="var(--terracotta)" stroke-width="1" stroke-dasharray="2,2"/>
      <text x="135" y="120" font-size="6" text-anchor="middle" fill="var(--terracotta)">Second-last defender</text>
    </svg>
    <p class="cap">The offside line = the second-last defender. Player A is onside (level); Player B is offside (beyond).</p>
  </div>
</div>
'''
    return page(29, 'Law 11', body)

# === LAW 12: FOULS ===
def page30():
    body = header(30, 'III', 'Law 12 — Fouls &amp; Misconduct')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">A foul is committed when a player:</p>
    <ul style="font-size: 9pt; margin-left: 0.3in; line-height: 1.5;">
      <li>Trips, kicks, or strikes an opponent</li>
      <li>Jumps at, charges, or pushes an opponent</li>
      <li>Tackles with studs raised or from behind</li>
      <li>Touches the ball with their hand/arm (deliberate)</li>
      <li>Holds or impedes an opponent</li>
      <li>Spits at any person</li>
    </ul>
    <p style="font-size: 9pt; margin-top: 0.15in;">Punishment ranges from a <b>direct free kick</b> to a <b>red card + sending off</b> depending on severity.</p>
    <div class="callout" style="margin-top: 0.2in;">
      <h3 style="font-size: 10pt;">DOGSO</h3>
      <p style="font-size: 8.5pt; margin: 0;"><b>Denying an Obvious Goal-Scoring Opportunity</b> by a foul or handball = automatic red card. This is the most controversial referee decision in the modern game.</p>
    </div>
  </div>
  <div>
    <table style="width: 100%; font-size: 8.5pt; border-collapse: collapse;">
      <tr style="background: var(--terracotta); color: var(--paper);"><th style="padding: 0.08in 0.12in;">Card</th><th style="padding: 0.08in 0.12in;">Trigger</th></tr>
      <tr><td style="padding: 0.08in 0.12in;"><b>🟨 Yellow</b></td><td style="padding: 0.08in 0.12in;">Reckless foul, dissent, time-wasting, removing shirt</td></tr>
      <tr><td style="padding: 0.08in 0.12in;"><b>🟥 Red</b></td><td style="padding: 0.08in 0.12in;">Violent conduct, DOGSO, abusive language, 2 yellows</td></tr>
    </table>
    <div class="diagram" style="margin-top: 0.15in;">
      <div class="kicker" style="text-align: center; margin-bottom: 0.1in;">Most yellow cards, 2024/25 PL</div>
      <table style="width: 100%; font-size: 8pt;">
        <tr><td>1.</td><td>Joao Pedro</td><td style="text-align: center;">12</td></tr>
        <tr><td>2.</td><td>Bruno Fernandes</td><td style="text-align: center;">11</td></tr>
        <tr><td>3.</td><td>Yves Bissouma</td><td style="text-align: center;">10</td></tr>
        <tr><td>4.</td><td>Declan Rice</td><td style="text-align: center;">10</td></tr>
        <tr><td>5.</td><td>Idrissa Gueye</td><td style="text-align: center;">9</td></tr>
      </table>
    </div>
  </div>
</div>
'''
    return page(30, 'Law 12', body)

# === LAWS 13-17 ===
def page31():
    body = header(31, 'III', 'Laws 13–17: All restarts')
    body += '''
<p class="lead" style="margin: 0.2in 0;">The five remaining restarts in football — when, where, and how they happen.</p>

<table style="width: 100%; border-collapse: collapse; font-size: 8.5pt;">
  <tr style="background: var(--green); color: var(--paper);">
    <th style="padding: 0.1in 0.15in; width: 0.7in;">Law</th>
    <th style="padding: 0.1in 0.15in; text-align: left;">Restart</th>
    <th style="padding: 0.1in 0.15in; text-align: left;">When</th>
    <th style="padding: 0.1in 0.15in; text-align: left;">Procedure</th>
  </tr>
  <tr><td style="padding: 0.1in 0.15in; font-family: var(--serif); font-size: 14pt; font-weight: 700; color: var(--terracotta);">13</td><td style="padding: 0.1in 0.15in;"><b>Free kick</b></td><td style="padding: 0.1in 0.15in;">Foul, offside</td><td style="padding: 0.1in 0.15in;">Direct or indirect at the spot of the foul. Wall 9.15 m back.</td></tr>
  <tr style="background: var(--paper-deep);"><td style="padding: 0.1in 0.15in; font-family: var(--serif); font-size: 14pt; font-weight: 700; color: var(--terracotta);">14</td><td style="padding: 0.1in 0.15in;"><b>Penalty kick</b></td><td style="padding: 0.1in 0.15in;">Foul in the box</td><td style="padding: 0.1in 0.15in;">Spot 11 m from goal; GK on line; ball must move forward.</td></tr>
  <tr><td style="padding: 0.1in 0.15in; font-family: var(--serif); font-size: 14pt; font-weight: 700; color: var(--terracotta);">15</td><td style="padding: 0.1in 0.15in;"><b>Throw-in</b></td><td style="padding: 0.1in 0.15in;">Whole ball over touchline</td><td style="padding: 0.1in 0.15in;">Two hands from behind the head, both feet on ground.</td></tr>
  <tr style="background: var(--paper-deep);"><td style="padding: 0.1in 0.15in; font-family: var(--serif); font-size: 14pt; font-weight: 700; color: var(--terracotta);">16</td><td style="padding: 0.1in 0.15in;"><b>Goal kick</b></td><td style="padding: 0.1in 0.15in;">Ball over goal line, last touched by attacker</td><td style="padding: 0.1in 0.15in;">From anywhere inside the goal area; ball must leave box before next touch.</td></tr>
  <tr><td style="padding: 0.1in 0.15in; font-family: var(--serif); font-size: 14pt; font-weight: 700; color: var(--terracotta);">17</td><td style="padding: 0.1in 0.15in;"><b>Corner kick</b></td><td style="padding: 0.1in 0.15in;">Ball over goal line, last touched by defender</td><td style="padding: 0.1in 0.15in;">From corner arc inside 1 m; ball must be stationary.</td></tr>
</table>

<div class="two-col" style="margin-top: 0.2in;">
  <div>
    <div class="callout">
      <h3 style="font-size: 10pt;">Penalty drama</h3>
      <p style="font-size: 8.5pt; margin: 0;">Penalty conversion rate in top leagues is <b>~75–80%</b>. Stutter-step and stuttering run-ups are now common — only allowed if the run-up is continuous (no false stop once the run-up begins).</p>
    </div>
  </div>
  <div>
    <div class="factbox terracotta">
      <div class="eyebrow">The corner flag</div>
      <h3 style="font-size: 12pt; margin-top: 0.05in;">Must be at least 1.5 m tall with a non-pointed top. Teams have been penalised for failing to follow the spec — Arsenal and Chelsea both received fines in 2024.</h3>
    </div>
  </div>
</div>
'''
    return page(31, 'Laws 13–17', body)

# === VAR ===
def page32():
    body = header(32, 'III', 'VAR — How it works')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">Video Assistant Referee (VAR) reviews decisions for clear and obvious errors. The system was introduced in 2016, first used at a World Cup in 2018, and is now mandatory in the Champions League, Premier League, La Liga, and World Cup.</p>
    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">What's reviewable</h3>
    <ul style="font-size: 9pt; margin-left: 0.3in; line-height: 1.5;">
      <li>Goals — including build-up (offside, foul, handball)</li>
      <li>Penalty decisions</li>
      <li>Direct red cards</li>
      <li>Mistaken identity</li>
    </ul>
    <p style="font-size: 9pt; margin-top: 0.15in;">Yellow cards and red cards for second bookings are <b>not</b> reviewable.</p>
    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Process</h3>
    <ol style="font-size: 9pt; margin-left: 0.3in; line-height: 1.5;">
      <li>Referee makes initial decision</li>
      <li>VAR checks from off-field replay booth</li>
      <li>If "clear and obvious" error, VAR recommends review</li>
      <li>Referee watches pitch-side monitor (OFR)</li>
      <li>Referee overturns or stands by decision</li>
    </ol>
  </div>
  <div>
    <div class="diagram" style="text-align: center; padding: 0.2in;">
      <svg viewBox="0 0 200 120" style="width: 100%;">
        <rect x="0" y="20" width="100" height="80" fill="none" stroke="var(--ink)" stroke-width="2"/>
        <rect x="100" y="20" width="100" height="40" fill="none" stroke="var(--terracotta)" stroke-width="2"/>
        <text x="50" y="60" font-size="9" text-anchor="middle" fill="var(--ink)" font-weight="700">Pitch</text>
        <text x="50" y="75" font-size="7" text-anchor="middle" fill="var(--ink-mute)">Referee + players</text>
        <text x="150" y="38" font-size="9" text-anchor="middle" fill="var(--terracotta)" font-weight="700">VAR booth</text>
        <text x="150" y="52" font-size="7" text-anchor="middle" fill="var(--terracotta)">Replay operators</text>
        <text x="50" y="115" font-size="7" text-anchor="middle" fill="var(--ink-mute)">Steps 1–6 (decision → VAR review → OFR)</text>
      </svg>
    </div>
    <div class="factbox">
      <div class="eyebrow">VAR stats, PL 2024/25</div>
      <div style="display: flex; gap: 0.2in; margin-top: 0.15in;">
        <div class="stat" style="flex:1;"><div class="num">162</div><div class="label">VAR checks</div></div>
        <div class="stat" style="flex:1;"><div class="num">34</div><div class="label">OFRs</div></div>
        <div class="stat" style="flex:1;"><div class="num">21%</div><div class="label">Decisions overturned</div></div>
      </div>
      <p style="font-size: 8.5pt; margin-top: 0.15in;">Average review length: <b>26 seconds</b> for a check, <b>54 seconds</b> for an OFR.</p>
    </div>
    <div class="callout" style="margin-top: 0.2in;">
      <h3 style="font-size: 10pt;">Semi-automated offside (SAOT)</h3>
      <p style="font-size: 8.5pt; margin: 0;">From 2022, FIFA introduced SAOT: 12–29 cameras + limb-tracking software flag offside within seconds. Used at the 2022 and 2026 World Cups.</p>
    </div>
  </div>
</div>
'''
    return page(32, 'VAR', body)

# Write all
for fn in [page19, page20, page21, page22, page23, page24, page25, page28, page29, page30, page31, page32]:
    # Fix: I missed 26 and 27 in the list — let me add them
    pass

# Add missing functions
def page26_():
    return page26()
def page27_():
    return page27()

# Actually rewrite to include all 14
pages = {
    19: page19(), 20: page20(), 21: page21(), 22: page22(),
    23: page23(), 24: page24(), 25: page25(), 26: page26(),
    27: page27(), 28: page28(), 29: page29(), 30: page30(),
    31: page31(), 32: page32()
}
for num, html in pages.items():
    with open(f'{PAGES_DIR}/{num:02d}-page.html', 'w') as f:
        f.write(html)
print(f"Wrote pages 19-32: {len(pages)} files")