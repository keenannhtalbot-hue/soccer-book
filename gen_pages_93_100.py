#!/usr/bin/env python3
"""Generate pages 93-100: tactics, set pieces, analytics, transfers, stadiums future, social media, glossary, index."""
import os

PAGES_DIR = '/home/kbot/soccer-book/pages'

def page(num, title, body):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Page {num} — {title}</title>
<link rel="stylesheet" href="book.css">
</head>
<body class="page standard">
<div class="page-inner">
{body}
</div>
</body>
</html>
"""

def header(num, section, title):
    return f"""<div class="page-header">
  <div class="page-num">{num}</div>
  <div><div class="section-num">Section {section}</div><h1 class="section-title">{title}</h1></div>
</div>"""

# Page 93: Tactics 101
def page93():
    body = header(93, 'VIII', 'Tactics 101')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">Three tactical philosophies dominate the modern game. Most top teams blend elements of all three.</p>

    <div class="callout" style="margin-top: 0.2in;">
      <h3 style="font-size: 11pt;">Possession</h3>
      <p style="font-size: 9pt; margin: 0;"><i>"The ball is our life."</i> Barcelona, Manchester City, Spain 2008–12. Build from the back, control tempo through short passing, suffocate opponents with territorial dominance.</p>
    </div>

    <div class="callout" style="margin-top: 0.15in;">
      <h3 style="font-size: 11pt;">Gegenpressing</h3>
      <p style="font-size: 9pt; margin: 0;"><i>"Win the ball back within 6 seconds."</i> Jürgen Klopp's Liverpool, Borussia Dortmund. High press, intense vertical runs, transition goals. Famously coined by Rangnick.</p>
    </div>

    <div class="callout" style="margin-top: 0.15in;">
      <h3 style="font-size: 11pt;">Low block / counter-attack</h3>
      <p style="font-size: 9pt; margin: 0;"><i>"Let them have the ball."</i> Simeone's Atlético Madrid, Italian catenaccio. Compact shape, deep defending, vertical pace on the break.</p>
    </div>
  </div>
  <div>
    <div class="diagram">
      <div class="kicker" style="text-align: center; margin-bottom: 0.15in;">Three pressing zones</div>
      <svg viewBox="0 0 200 220" style="width: 100%; max-width: 2.8in;">
        <!-- High press -->
        <rect x="20" y="20" width="160" height="50" fill="#4caf50" stroke="var(--ink)" stroke-width="1"/>
        <text x="100" y="50" font-size="9" text-anchor="middle" fill="var(--paper)" font-weight="700">HIGH PRESS</text>
        <text x="100" y="62" font-size="7" text-anchor="middle" fill="var(--paper)">Attack the ball in final ⅓</text>
        <!-- Mid block -->
        <rect x="20" y="80" width="160" height="50" fill="#fbc02d" stroke="var(--ink)" stroke-width="1"/>
        <text x="100" y="110" font-size="9" text-anchor="middle" fill="var(--ink)" font-weight="700">MID BLOCK</text>
        <text x="100" y="122" font-size="7" text-anchor="middle" fill="var(--ink)">Squeeze the centre of the pitch</text>
        <!-- Low block -->
        <rect x="20" y="140" width="160" height="50" fill="#c44536" stroke="var(--ink)" stroke-width="1"/>
        <text x="100" y="170" font-size="9" text-anchor="middle" fill="var(--paper)" font-weight="700">LOW BLOCK</text>
        <text x="100" y="182" font-size="7" text-anchor="middle" fill="var(--paper)">Compact 25m, wait for the break</text>
        <!-- Ball -->
        <circle cx="40" cy="55" r="6" fill="var(--ink)"/>
        <text x="40" y="200" font-size="7" text-anchor="middle" fill="var(--ink-mute)" font-style="italic">Ball position determines block</text>
      </svg>
    </div>
    <div class="sidebar terracotta" style="margin-top: 0.2in;">
      <h3>The PPDA metric</h3>
      <p style="font-size: 8.5pt;">Pressures Per Defensive Action — the average number of opposition passes allowed before a defensive action. <b>Liverpool under Klopp: 8.4</b> (elite high press). <b>Burnley under Dyche: 19.2</b> (elite low block).</p>
    </div>
  </div>
</div>
'''
    return page(93, 'Tactics 101', body)

# Page 94: Set pieces
def page94():
    body = header(94, 'VIII', 'Set pieces')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">Set pieces decide matches. Studies by analysts at <i>The Athletic</i> and <i>FiveThirtyEight</i> show <b>25–30% of goals</b> come from dead-ball situations — a share that has barely changed in 30 years.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Corners</h3>
    <p>Inswinging vs outswinging. Near post flick-ons, edge-of-box lay-offs, short corners. Modern coaches plan 5–6 corner routines, each named (e.g. "Corner A — Japan").</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Free kicks</h3>
    <p>Direct (shoot) vs indirect (pass). Famous specialists: Messi, Ronaldo, Ward-Prowse, James Ward-Prowse held the PL record with 17 direct free kicks before being matched by Ronaldo.</p>
  </div>
  <div>
    <div class="diagram">
      <div class="kicker" style="text-align: center; margin-bottom: 0.15in;">Goals from set pieces, % of total</div>
      <table style="width: 100%; font-size: 9pt; border-collapse: collapse;">
        <tr style="background: var(--navy); color: var(--paper);">
          <th style="padding: 0.08in 0.12in;">Competition</th>
          <th style="padding: 0.08in 0.12in;">% from set pieces</th>
          <th style="padding: 0.08in 0.12in;">% from open play</th>
        </tr>
        <tr style="background: var(--paper-deep);"><td style="padding: 0.08in 0.12in;">PL 2023/24</td><td style="text-align: center; color: var(--terracotta); font-weight: 700;">28%</td><td style="text-align: center;">72%</td></tr>
        <tr><td style="padding: 0.08in 0.12in;">La Liga 2023/24</td><td style="text-align: center; color: var(--terracotta); font-weight: 700;">26%</td><td style="text-align: center;">74%</td></tr>
        <tr style="background: var(--paper-deep);"><td style="padding: 0.08in 0.12in;">Serie A 2023/24</td><td style="text-align: center; color: var(--terracotta); font-weight: 700;">32%</td><td style="text-align: center;">68%</td></tr>
        <tr><td style="padding: 0.08in 0.12in;">World Cup 2022</td><td style="text-align: center; color: var(--terracotta); font-weight: 700;">31%</td><td style="text-align: center;">69%</td></tr>
      </table>
    </div>
    <div class="callout" style="margin-top: 0.2in;">
      <h3 style="font-size: 10pt;">The throw-in renaissance</h3>
      <p style="font-size: 8.5pt; margin: 0;">From 2023, throw-ins became a tactical weapon. Coaches like Thomas Frank (Brentford), Roberto De Zerbi, and Roberto Martinez now design multi-player throw-in routines — including the famous <b>"long-throw"</b> of players like Rory Delap or modern specialists like Brentford's Christian Nørgaard.</p>
    </div>
  </div>
</div>
'''
    return page(94, 'Set pieces', body)

# Page 95: Data & analytics
def page95():
    body = header(95, 'VIII', 'Data &amp; analytics')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">Football has become a data sport. Every pass, tackle, sprint, and shot is now recorded, catalogued, and analysed.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Key metrics</h3>
    <table style="width: 100%; font-size: 8.5pt;">
      <tr><td style="padding: 0.04in 0;"><b>xG</b></td><td>Expected Goals — probability a shot becomes a goal.</td></tr>
      <tr><td><b>xA</b></td><td>Expected Assists — quality of the pass leading to a shot.</td></tr>
      <tr><td><b>xT</b></td><td>Expected Threat — value added to a possession by an action.</td></tr>
      <tr><td><b>PPDA</b></td><td>Passes Per Defensive Action (see page 93).</td></tr>
      <tr><td><b>Press %</b></td><td>% of opposition passes that are pressured within 2s.</td></tr>
      <tr><td><b>Field tilt</b></td><td>% of final-third passes in your team's favour.</td></tr>
    </table>

    <div class="callout" style="margin-top: 0.2in;">
      <h3 style="font-size: 10pt;">Who tracks the data?</h3>
      <p style="font-size: 8.5pt; margin: 0;">Top clubs hire <b>10–40 data scientists</b>. Most use <b>StatsBomb</b> or <b>Opta</b> event data, plus <b>TRACAB</b> or <b>Hawk-Eye</b> tracking (60Hz position data, 3D joint locations). Liverpool's data team includes a former physicist and an astrophysicist.</p>
    </div>
  </div>
  <div>
    <div class="diagram">
      <div class="kicker" style="text-align: center; margin-bottom: 0.15in;">xG explained</div>
      <svg viewBox="0 0 200 130" style="width: 100%; max-width: 3.5in;">
        <!-- Goal -->
        <rect x="20" y="20" width="160" height="40" fill="none" stroke="var(--paper)" stroke-width="2"/>
        <!-- Net -->
        <g stroke="var(--paper)" stroke-width="0.4" opacity="0.7">
          <line x1="40" y1="20" x2="40" y2="60"/>
          <line x1="60" y1="20" x2="60" y2="60"/>
          <line x1="80" y1="20" x2="80" y2="60"/>
          <line x1="100" y1="20" x2="100" y2="60"/>
          <line x1="120" y1="20" x2="120" y2="60"/>
          <line x1="140" y1="20" x2="140" y2="60"/>
          <line x1="160" y1="20" x2="160" y2="60"/>
          <line x1="20" y1="30" x2="180" y2="30"/>
          <line x1="20" y1="40" x2="180" y2="40"/>
          <line x1="20" y1="50" x2="180" y2="50"/>
        </g>
        <!-- Shot from center -->
        <line x1="100" y1="100" x2="100" y2="40" stroke="var(--terracotta)" stroke-width="2" marker-end="url(#arrow)"/>
        <defs>
          <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 0 L 10 5 L 0 10 z" fill="var(--terracotta)"/>
          </marker>
        </defs>
        <!-- Probability circles (size = xG) -->
        <circle cx="170" cy="40" r="20" fill="var(--green)" opacity="0.6"/>
        <text x="170" y="44" font-size="8" text-anchor="middle" fill="var(--paper)" font-weight="700">0.85</text>
        <circle cx="100" cy="40" r="14" fill="var(--gold)" opacity="0.6"/>
        <text x="100" y="44" font-size="7" text-anchor="middle" fill="var(--ink)" font-weight="700">0.55</text>
        <circle cx="35" cy="40" r="8" fill="var(--terracotta)" opacity="0.7"/>
        <text x="35" y="44" font-size="6" text-anchor="middle" fill="var(--paper)" font-weight="700">0.15</text>
        <!-- Player -->
        <circle cx="100" cy="100" r="8" fill="var(--terracotta)" stroke="var(--ink)" stroke-width="1"/>
        <text x="100" y="125" font-size="7" text-anchor="middle" fill="var(--ink-mute)">Player shooting</text>
      </svg>
    </div>
    <p class="cap">xG by shot location. A clear shot from inside the 6-yard box: ~0.85. A shot from the penalty spot: ~0.55. A tight angle from a wide position: ~0.15. xG is the sum of these probabilities — the higher the team's xG, the better their chances.</p>

    <div class="factbox navy" style="margin-top: 0.2in;">
      <div class="eyebrow">Modern signing</div>
      <h3 style="font-size: 12pt;">In 2025, Liverpool signed a 19-year-old based almost entirely on data — scouts saw him play just twice before the bid. <b>Recruitment is now led by data, not traditional scouting.</b></h3>
    </div>
  </div>
</div>
'''
    return page(95, 'Data &amp; analytics', body)

# Page 96: Transfers
def page96():
    body = header(96, 'VIII', 'The transfer market')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">The 2024/25 transfer window saw European clubs spend <b>€9.9 billion</b> in a single summer. The market is now larger than the entire GDP of Barbados.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">How transfers work</h3>
    <p>The buying club and selling club agree a fee. The player then agrees personal terms with the buying club. The buying club pays the fee in instalments (typically 3 over 3 years). The selling club pays the player a <b>training compensation</b> to their academy for any player aged 12–21.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Key windows</h3>
    <ul style="font-size: 9pt; margin-left: 0.3in; line-height: 1.5;">
      <li><b>Summer:</b> June–August in Europe (main window)</li>
      <li><b>Winter:</b> January in Europe (smaller)</li>
      <li><b>Saudi:</b> September in Saudi Arabia (synchronised with their season)</li>
    </ul>
  </div>
  <div>
    <div class="diagram">
      <div class="kicker" style="text-align: center; margin-bottom: 0.15in;">All-time transfer fees (€ million)</div>
      <table style="width: 100%; font-size: 8.5pt; border-collapse: collapse;">
        <tr style="background: var(--terracotta); color: var(--paper);">
          <th style="padding: 0.08in 0.12in;">Player</th>
          <th style="padding: 0.08in 0.12in;">From → To</th>
          <th style="padding: 0.08in 0.12in;">Fee</th>
          <th style="padding: 0.08in 0.12in;">Year</th>
        </tr>
        <tr><td style="padding: 0.08in 0.12in;"><b>Neymar</b></td><td style="padding: 0.08in 0.12in;">Barça → PSG</td><td style="text-align: center; color: var(--terracotta); font-weight: 700;">222</td><td style="text-align: center;">2017</td></tr>
        <tr style="background: var(--paper-deep);"><td style="padding: 0.08in 0.12in;"><b>Mbappé</b></td><td style="padding: 0.08in 0.12in;">Monaco → PSG</td><td style="text-align: center; color: var(--terracotta); font-weight: 700;">180</td><td style="text-align: center;">2018</td></tr>
        <tr><td style="padding: 0.08in 0.12in;"><b>Coutinho</b></td><td style="padding: 0.08in 0.12in;">Liverpool → Barça</td><td style="text-align: center; color: var(--terracotta); font-weight: 700;">145</td><td style="text-align: center;">2018</td></tr>
        <tr style="background: var(--paper-deep);"><td style="padding: 0.08in 0.12in;"><b>Joao Félix</b></td><td style="padding: 0.08in 0.12in;">Benfica → Atlético</td><td style="text-align: center; color: var(--terracotta); font-weight: 700;">126</td><td style="text-align: center;">2019</td></tr>
        <tr><td style="padding: 0.08in 0.12in;"><b>Antony</b></td><td style="padding: 0.08in 0.12in;">Ajax → Man Utd</td><td style="text-align: center; color: var(--terracotta); font-weight: 700;">95</td><td style="text-align: center;">2022</td></tr>
        <tr style="background: var(--paper-deep);"><td style="padding: 0.08in 0.12in;"><b>Bellingham</b></td><td style="padding: 0.08in 0.12in;">Dortmund → Real</td><td style="text-align: center; color: var(--terracotta); font-weight: 700;">103</td><td style="text-align: center;">2023</td></tr>
      </table>
    </div>
    <div class="callout" style="margin-top: 0.2in;">
      <h3 style="font-size: 10pt;">Free transfers</h3>
      <p style="font-size: 8.5pt; margin: 0;">Players out of contract can sign for free with any club. <b>Messi → PSG (2021)</b> and <b>Mbappé → Real Madrid (2024)</b> were both free transfers — yet the headline value of those signings (wages, signing bonus) eclipsed any outright purchase.</p>
    </div>
  </div>
</div>
'''
    return page(96, 'The transfer market', body)

# Page 97: Stadiums of the future
def page97():
    body = header(97, 'VIII', 'Stadiums of the future')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">European football is undergoing a <b>€15 billion stadium building boom</b>. The new grounds are entertainment campuses, not just sports venues.</p>

    <div class="callout" style="margin: 0.2in 0;">
      <h3 style="font-size: 11pt;">What's driving the boom</h3>
      <p style="font-size: 9pt; margin: 0;">Matchday revenue is the single biggest income for most clubs. New stadiums typically generate <b>2–3× more matchday revenue</b> than old ones — through corporate boxes, hospitality, naming rights, concerts, conferences, and restaurants.</p>
    </div>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Trends</h3>
    <ul style="font-size: 9pt; margin-left: 0.3in; line-height: 1.5;">
      <li><b>Retractable pitches</b> — real grass rolls away for concerts and events (Tottenham, Madrid)</li>
      <li><b>360° LED facades</b> — programmable exteriors (Allianz Arena, Santiago Bernabéu)</li>
      <li><b>Steep stands</b> — fans closer to the action (Everton's Hill Dickinson, Atlanta United's MBS)</li>
      <li><b>Bars &amp; breweries</b> — stadium-as-destination (Atlanta, Tottenham)</li>
      <li><b>Hotels, residential, retail</b> — the "mixed-use campus" model (Chelsea, Roma, Liverpool)</li>
    </ul>
  </div>
  <div>
    <div class="diagram">
      <div class="kicker" style="text-align: center; margin-bottom: 0.15in;">New stadiums opening 2025–2030</div>
      <table style="width: 100%; font-size: 8.5pt; border-collapse: collapse;">
        <tr style="background: var(--green); color: var(--paper);">
          <th style="padding: 0.08in 0.12in;">Club</th>
          <th style="padding: 0.08in 0.12in;">Stadium</th>
          <th style="padding: 0.08in 0.12in;">Cap.</th>
          <th style="padding: 0.08in 0.12in;">Open</th>
        </tr>
        <tr><td style="padding: 0.08in 0.12in;"><b>FC Barcelona</b></td><td style="padding: 0.08in 0.12in;">Spotify Camp Nou</td><td style="text-align: center;">105k</td><td style="text-align: center;">2026</td></tr>
        <tr style="background: var(--paper-deep);"><td style="padding: 0.08in 0.12in;"><b>Everton</b></td><td style="padding: 0.08in 0.12in;">Hill Dickinson</td><td style="text-align: center;">52,888</td><td style="text-align: center;">2025</td></tr>
        <tr><td style="padding: 0.08in 0.12in;"><b>AC Milan / Inter</b></td><td style="padding: 0.08in 0.12in;">New San Siro</td><td style="text-align: center;">71,500</td><td style="text-align: center;">2030</td></tr>
        <tr style="background: var(--paper-deep);"><td style="padding: 0.08in 0.12in;"><b>Chelsea</b></td><td style="padding: 0.08in 0.12in;">New Stamford Bridge</td><td style="text-align: center;">TBD</td><td style="text-align: center;">2030</td></tr>
        <tr><td style="padding: 0.08in 0.12in;"><b>Roma</b></td><td style="padding: 0.08in 0.12in;">Stadio della Roma</td><td style="text-align: center;">55,000</td><td style="text-align: center;">2027</td></tr>
        <tr style="background: var(--paper-deep);"><td style="padding: 0.08in 0.12in;"><b>Man Utd</b></td><td style="padding: 0.08in 0.12in;">New Trafford</td><td style="text-align: center;">90,000</td><td style="text-align: center;">2030</td></tr>
      </table>
    </div>
    <div class="factbox navy" style="margin-top: 0.2in;">
      <div class="eyebrow">Stadium-as-bond</div>
      <h3 style="font-size: 12pt; margin-top: 0.05in;">Everton's Hill Dickinson was financed in part by a £200m bond issue on the London Stock Exchange. The bond pays 6.5% interest, secured against future matchday and naming-rights revenue — a new model of stadium finance.</h3>
    </div>
  </div>
</div>
'''
    return page(97, 'Stadiums of the future', body)

# Page 98: Social media & fan culture
def page98():
    body = header(98, 'VIII', 'Football &amp; social media')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">Football is the world's most-engaged-with subject on social media. The top 10 accounts include 6 footballers, 3 clubs, and 1 league.</p>

    <div class="callout" style="margin: 0.2in 0;">
      <h3 style="font-size: 11pt;">The numbers</h3>
      <p style="font-size: 9pt; margin: 0;">Combined Instagram, X, TikTok, Facebook, YouTube:</p>
      <ul style="font-size: 9pt; margin: 0.15in 0 0 0.3in; line-height: 1.5;">
        <li><b>Real Madrid:</b> 480M followers</li>
        <li><b>FC Barcelona:</b> 410M</li>
        <li><b>Manchester United:</b> 240M</li>
        <li><b>Premier League:</b> 200M</li>
        <li><b>Cristiano Ronaldo:</b> 920M (most of any human)</li>
      </ul>
    </div>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">The new fan economy</h3>
    <p>Clubs now stream matches directly on their own apps. Players have personal brands worth hundreds of millions. The fan creates content (memes, fan cams, tactical analysis) that often outpaces official media. Football has become the first truly <b>creator-led sport</b>.</p>
  </div>
  <div>
    <div class="diagram">
      <div class="kicker" style="text-align: center; margin-bottom: 0.15in;">The football creator economy</div>
      <div style="display: flex; flex-direction: column; gap: 0.1in;">
        <div style="display: flex; justify-content: space-between; padding: 0.06in 0.12in; background: var(--paper-deep);"><b>Direct-to-consumer apps</b> <span style="color: var(--terracotta);">130M+ downloads (PL)</span></div>
        <div style="display: flex; justify-content: space-between; padding: 0.06in 0.12in;"><b>TikTok hashtags</b> <span style="color: var(--terracotta);">#football · 56B views</span></div>
        <div style="display: flex; justify-content: space-between; padding: 0.06in 0.12in; background: var(--paper-deep);"><b>YouTube channels</b> <span style="color: var(--terracotta);">FreeFootball: 12M subs</span></div>
        <div style="display: flex; justify-content: space-between; padding: 0.06in 0.12in;"><b>Fantasy football</b> <span style="color: var(--terracotta);">11M+ Premier League players</span></div>
        <div style="display: flex; justify-content: space-between; padding: 0.06in 0.12in; background: var(--paper-deep);"><b>NFT / digital collectibles</b> <span style="color: var(--terracotta);">Sorare: 3M+ users</span></div>
        <div style="display: flex; justify-content: space-between; padding: 0.06in 0.12in;"><b>Discord communities</b> <span style="color: var(--terracotta);">Football Twitter (X) · 4M+ DAU</span></div>
      </div>
    </div>
    <div class="factbox terracotta" style="margin-top: 0.2in;">
      <div class="eyebrow">Meme culture</div>
      <h3 style="font-size: 12pt;">The "Dump Truck" goal celebration has its own TikTok soundtrack. The "Xavi simulation" is a reaction GIF. <b>Memes are now a fixture of football coverage</b> — from Ballon d'Or voting to World Cup draw reactions.</h3>
    </div>
  </div>
</div>
'''
    return page(98, 'Football &amp; social media', body)

# Page 99: Glossary
def page99():
    body = header(99, 'VIII', 'Glossary')
    body += '''
<p class="lead" style="margin: 0.2in 0;">Terms used throughout this book.</p>

<div class="two-col" style="font-size: 8.5pt; line-height: 1.5;">
  <div>
    <h3 style="font-family: var(--serif); color: var(--green); font-size: 12pt; margin-bottom: 0.1in;">A–F</h3>
    <p><b>Assist</b> — final pass leading directly to a goal.</p>
    <p><b>Bicycle kick</b> — overhead kick, both feet off the ground.</p>
    <p><b>Box-to-box</b> — midfielder who covers the full length of the pitch.</p>
    <p><b>Cap</b> — each senior international appearance.</p>
    <p><b>Clean sheet</b> — match in which the team concedes zero goals.</p>
    <p><b>Coefficient</b> — UEFA ranking that determines competition entries.</p>
    <p><b>Counter-attack</b> — fast transition from defence to attack.</p>
    <p><b>Cross</b> — long pass from wide area into the box.</p>
    <p><b>Dummy</b> — feint or feint pass to deceive an opponent.</p>
    <p><b>False nine</b> — striker who drops deep, leaving defenders unsure.</p>
    <p><b>Finishing</b> — the act of converting chances into goals.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 12pt; margin: 0.2in 0 0.1in;">G–L</h3>
    <p><b>Ghosting</b> — running off the ball to create space.</p>
    <p><b>Golden Boot</b> — award for top scorer in a tournament.</p>
    <p><b>Hat-trick</b> — three goals by one player in a single match.</p>
    <p><b>Holding midfielder</b> — defensive shield in front of defence.</p>
    <p><b>Injury time</b> — additional minutes added to the end of a half.</p>
    <p><b>Inverted fullback</b> — fullback who tucks into midfield in possession.</p>
    <p><b>Libero</b> — sweeper behind the defensive line (rare in modern football).</p>
  </div>
  <div>
    <h3 style="font-family: var(--serif); color: var(--green); font-size: 12pt; margin-bottom: 0.1in;">M–R</h3>
    <p><b>Man of the Match</b> — best-performing player award.</p>
    <p><b>Match ball</b> — the official ball used in a specific game.</p>
    <p><b>Nutmeg</b> — putting the ball between an opponent's legs.</p>
    <p><b>Own goal</b> — when a player puts the ball into their own net.</p>
    <p><b>Penalty shootout</b> — tiebreaker with alternating spot kicks.</p>
    <p><b>Playmaker</b> — creative midfielder who dictates tempo.</p>
    <p><b>Press</b> — collective defensive pressure on the ball.</p>
    <p><b>Promotion</b> — moving up to a higher division.</p>
    <p><b>Relegation</b> — moving down to a lower division.</p>
    <p><b>Rotation</b> — squad changes between matches to manage fitness.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 12pt; margin: 0.2in 0 0.1in;">S–Z</h3>
    <p><b>Set piece</b> — any restart: corner, free kick, throw-in, goal kick.</p>
    <p><b>Shadow striker</b> — second striker playing off the main striker.</p>
    <p><b>Six-yard box</b> — small goal-area rectangle.</p>
    <p><b>Sweeper-keeper</b> — goalkeeper who plays high and acts as a sweeper.</p>
    <p><b>Tifo</b> — large choreographed display by ultras in the stands.</p>
    <p><b>Through ball</b> — pass played into space behind the defence.</p>
    <p><b>VAR</b> — Video Assistant Referee.</p>
    <p><b>Volley</b> — striking the ball before it touches the ground.</p>
    <p><b>Winger</b> — wide attacker who stays close to the touchline.</p>
  </div>
</div>
'''
    return page(99, 'Glossary', body)

# Page 100: Index
def page100():
    body = header(100, 'VIII', 'Index &amp; credits')
    body += '''
<div class="two-col">
  <div>
    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin-bottom: 0.1in;">Index by section</h3>
    <ul style="font-size: 8.5pt; line-height: 1.5; margin-left: 0.2in; list-style: none;">
      <li><b>Front matter</b> · 4–6</li>
      <li><b>Pitch &amp; equipment</b> · 7–18</li>
      <li><b>Rules of the game</b> · 19–32</li>
      <li><b>Formations &amp; positions</b> · 33–44</li>
      <li><b>Jerseys &amp; kits</b> · 45–54</li>
      <li><b>The biggest clubs</b> · 55–80</li>
      <li><b>Stadiums &amp; competitions</b> · 81–92</li>
      <li><b>Modern football culture</b> · 93–100</li>
    </ul>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.3in 0 0.1in;">Index by club</h3>
    <ul style="font-size: 8.5pt; line-height: 1.5; columns: 2; column-gap: 0.3in;">
      <li>Ajax · 75</li>
      <li>América (Mexico) · 79</li>
      <li>Arsenal · 59</li>
      <li>Atalanta · 80</li>
      <li>Atlético Madrid · 80</li>
      <li>Bayer Leverkusen · 71</li>
      <li>Bayern Munich · 69</li>
      <li>Benfica · 76</li>
      <li>Boca Juniors · 77</li>
      <li>Borussia Dortmund · 70</li>
      <li>Chelsea · 61</li>
      <li>Chivas · 79</li>
      <li>Everton · 63</li>
      <li>Fenerbahçe · 78</li>
      <li>Galatasaray · 78</li>
      <li>Inter Milan · 65</li>
      <li>Juventus · 66</li>
      <li>Liverpool · 58</li>
      <li>Man City · 60</li>
      <li>Man United · 57</li>
      <li>Marseille · 74</li>
      <li>AC Milan · 64</li>
      <li>Napoli · 67</li>
      <li>PSG · 73</li>
      <li>Porto · 76</li>
      <li>RB Leipzig · 72</li>
      <li>Real Madrid · 55</li>
      <li>River Plate · 77</li>
      <li>AS Roma · 68</li>
      <li>Sporting CP · 76</li>
      <li>Tottenham · 62</li>
      <li>FC Barcelona · 56</li>
    </ul>
  </div>
  <div>
    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin-bottom: 0.1in;">Credits</h3>
    <p style="font-size: 8.5pt;">Editor: <b>Forge</b></p>
    <p style="font-size: 8.5pt;">Design: <b>Forge Editions</b></p>
    <p style="font-size: 8.5pt;">Imprint: <b>Forge Editions · 2025</b></p>
    <p style="font-size: 8.5pt;">Edition: 1.0</p>
    <p style="font-size: 8.5pt;">ISBN: 978-0-00000-000-0 (placeholder)</p>

    <div class="factbox dark" style="margin-top: 0.3in;">
      <div class="eyebrow" style="color: var(--gold);">A note on currency</div>
      <h3 style="font-size: 14pt; margin-top: 0.1in; color: var(--paper);">All figures current to October 2025.</h3>
      <p style="font-size: 9pt; margin: 0.1in 0 0; color: var(--paper);">Transfer fees, attendance figures, and league revenues reflect the most recent season for which reliable data is available. Statistics will drift; the framework in this book will hold.</p>
    </div>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.4in 0 0.1in;">Further reading</h3>
    <ul style="font-size: 8.5pt; line-height: 1.5; margin-left: 0.2in; list-style: disc;">
      <li><i>The Numbers Game</i> — Chris Anderson &amp; David Sally</li>
      <li><i>Inverting the Pyramid</i> — Jonathan Wilson</li>
      <li><i>The Ball is Round</i> — David Goldblatt</li>
      <li><i>Football Hackers</i> — Christoph Biermann</li>
      <li><i>Leading</i> — Sir Alex Ferguson &amp; Michael Moritz</li>
    </ul>

    <div class="callout" style="margin-top: 0.3in; text-align: center;">
      <h3 style="font-size: 12pt; font-family: var(--serif-display); font-style: italic;">Thank you for reading</h3>
      <p style="font-size: 8pt; margin: 0; color: var(--ink-soft);">This is the end of the book — but not of the game.</p>
    </div>
  </div>
</div>
'''
    return page(100, 'Index &amp; credits', body)

# Write
for fn in [page93, page94, page95, page96, page97, page98, page99, page100]:
    n = int(fn.__name__.replace('page', ''))
    with open(f'{PAGES_DIR}/{n:02d}-page.html', 'w') as f:
        f.write(fn())
    print(f"Wrote page {n}")
print("Done 93-100")