#!/usr/bin/env python3
"""Generate pages 81-92: stadiums & competitions."""
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

def stadium_svg(name, capacity, primary):
    return f'''<div class="diagram" style="text-align: center; padding: 0.2in;">
  <svg viewBox="0 0 200 130" style="width: 100%; max-width: 3.5in;">
    <ellipse cx="100" cy="65" rx="85" ry="50" fill="{primary}" stroke="var(--ink)" stroke-width="1.5"/>
    <ellipse cx="100" cy="65" rx="60" ry="35" fill="none" stroke="var(--paper)" stroke-width="1"/>
    <ellipse cx="100" cy="65" rx="40" ry="22" fill="none" stroke="var(--paper)" stroke-width="1"/>
    <ellipse cx="100" cy="65" rx="3" ry="3" fill="var(--paper)"/>
    <text x="100" y="125" font-size="7" text-anchor="middle" fill="var(--ink-mute)">CAPACITY · {capacity}</text>
  </svg>
  <div class="kicker" style="margin-top: 0.1in;">{name}</div>
</div>'''

# Page 81: El Clásico arenas
def page81():
    body = header(81, 'VII', 'El Clásico arenas')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">Two stadiums, one rivalry, the two largest football clubs in the world by revenue.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Santiago Bernabéu (Real Madrid)</h3>
    <p><b>Opened 1947.</b> Under renovation since 2019. New retractable roof, 360° LED scoreboard, retractable pitch system (a real lawn slides into storage for non-football events). Capacity: <b>83,186</b>. Hosted the 1982 World Cup final and the 2010 Champions League final.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Spotify Camp Nou (FC Barcelona)</h3>
    <p><b>Opened 1957.</b> Currently undergoing Espai Barça renovation — expected completion 2026. Will return to its <b>99,354 capacity</b>, regain its position as Europe's largest stadium.</p>

    <div class="callout" style="margin-top: 0.2in;">
      <h3 style="font-size: 10pt;">Two identities, one city</h3>
      <p style="font-size: 8.5pt; margin: 0;">The Bernabéu sits in the affluent Chamartín district of north Madrid; Camp Nou on the western fringes of Barcelona. The stadiums reflect the clubs — institutional power vs. cultural identity.</p>
    </div>
  </div>
  <div>
    <div class="compare-row" style="margin-top: 0.2in;">
''' + stadium_svg('Bernabéu', '83,186', '#1A3A8F') + '''
''' + stadium_svg('Camp Nou', '99,354', '#A50044') + '''
    </div>
    <div class="diagram" style="margin-top: 0.2in;">
      <div class="kicker" style="text-align: center; margin-bottom: 0.15in;">El Clásico all-time</div>
      <table style="width: 100%; font-size: 9pt; border-collapse: collapse;">
        <tr style="background: var(--terracotta); color: var(--paper);">
          <th style="padding: 0.08in 0.12in;">Statistic</th>
          <th style="padding: 0.08in 0.12in;">Real Madrid</th>
          <th style="padding: 0.08in 0.12in;">Barcelona</th>
        </tr>
        <tr style="background: var(--paper-deep);"><td style="padding: 0.08in 0.12in;">La Liga titles</td><td style="text-align: center; color: var(--terracotta); font-weight: 700;">36</td><td style="text-align: center;">27</td></tr>
        <tr><td style="padding: 0.08in 0.12in;">Champions League</td><td style="text-align: center; color: var(--terracotta); font-weight: 700;">15</td><td style="text-align: center;">5</td></tr>
        <tr style="background: var(--paper-deep);"><td style="padding: 0.08in 0.12in;">El Clásico wins (all)</td><td style="text-align: center; color: var(--terracotta); font-weight: 700;">102</td><td style="text-align: center;">99</td></tr>
        <tr><td style="padding: 0.08in 0.12in;">El Clásico draws</td><td style="text-align: center;">52</td><td style="text-align: center;">52</td></tr>
        <tr style="background: var(--paper-deep);"><td style="padding: 0.08in 0.12in;">Ballon d'Or winners</td><td style="text-align: center; color: var(--terracotta); font-weight: 700;">12</td><td style="text-align: center;">8</td></tr>
      </table>
    </div>
  </div>
</div>
'''
    return page(81, 'El Clásico arenas', body)

# Page 82: English cathedrals
def page82():
    body = header(82, 'VII', 'English cathedrals')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">Old Trafford and Anfield — two stadiums that have been in continuous use for nearly a century, both bearing the scars and glories of English football history.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Old Trafford (Manchester United)</h3>
    <p><b>Opened 1910.</b> Capacity <b>74,310</b>. The largest club stadium in the United Kingdom. Famously dubbed the "Theatre of Dreams" by Bobby Charlton. Bombed in WWII and rebuilt between 1945 and 1949.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Anfield (Liverpool FC)</h3>
    <p><b>Opened 1884.</b> Capacity <b>61,276</b>. The Kop — the single-tier standing-end-turned-seated stand behind the goal — is the spiritual home of English football support. Site of four European Cup / Champions League triumphs celebrated under the night sky.</p>

    <div class="callout" style="margin-top: 0.2in;">
      <h3 style="font-size: 10pt;">North-west rivalry</h3>
      <p style="font-size: 8.5pt; margin: 0;">The clubs are separated by 35 miles on the M62. Both cities were defined by the Industrial Revolution; both clubs by European competition; both grounds by fans whose loyalty is generational.</p>
    </div>
  </div>
  <div>
    <div class="compare-row" style="margin-top: 0.2in;">
''' + stadium_svg('Old Trafford', '74,310', '#DA291C') + '''
''' + stadium_svg('Anfield', '61,276', '#C8102E') + '''
    </div>
    <div class="diagram" style="margin-top: 0.2in;">
      <div class="kicker" style="text-align: center; margin-bottom: 0.15in;">North-west giants, all-time</div>
      <table style="width: 100%; font-size: 9pt; border-collapse: collapse;">
        <tr style="background: var(--green); color: var(--paper);">
          <th style="padding: 0.08in 0.12in;">Statistic</th>
          <th style="padding: 0.08in 0.12in;">Man Utd</th>
          <th style="padding: 0.08in 0.12in;">Liverpool</th>
        </tr>
        <tr style="background: var(--paper-deep);"><td style="padding: 0.08in 0.12in;">PL titles</td><td style="text-align: center; color: var(--terracotta); font-weight: 700;">20</td><td style="text-align: center; color: var(--terracotta); font-weight: 700;">19</td></tr>
        <tr><td style="padding: 0.08in 0.12in;">European Cups</td><td style="text-align: center;">3</td><td style="text-align: center; color: var(--terracotta); font-weight: 700;">6</td></tr>
        <tr style="background: var(--paper-deep);"><td style="padding: 0.08in 0.12in;">FA Cups</td><td style="text-align: center; color: var(--terracotta); font-weight: 700;">13</td><td style="text-align: center;">8</td></tr>
      </table>
    </div>
  </div>
</div>
'''
    return page(82, 'English cathedrals', body)

# Page 83: European temples
def page83():
    body = header(83, 'VII', 'European temples')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">Two continental cathedrals — one shared by two clubs, one purpose-built.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">San Siro / Stadio Giuseppe Meazza</h3>
    <p><b>Opened 1926.</b> Capacity <b>75,817</b>. Home to <b>both AC Milan and Inter Milan</b> — one of the few major stadiums in the world shared by two top-division clubs. Distinctive red girders spiral up the towers at each corner. Slated to be replaced by a new 71,500-seat stadium by 2030.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Allianz Arena (Bayern Munich)</h3>
    <p><b>Opened 2005.</b> Capacity <b>75,024</b>. The ETFE plastic exterior is illuminated by 3,000 lights — the stadium can glow in any color (red for Bayern, blue for TSV 1860 during shared-tenant days, white for German national team, green for St Patrick's day).</p>
  </div>
  <div>
    <div class="compare-row">
''' + stadium_svg('San Siro', '75,817', '#FB090B') + '''
''' + stadium_svg('Allianz Arena', '75,024', '#DC052D') + '''
    </div>
    <div class="callout" style="margin-top: 0.3in;">
      <h3 style="font-size: 10pt;">Architectural notes</h3>
      <p style="font-size: 8.5pt; margin: 0;">San Siro's most recent renovation (1989, by Giancarlo Ragazzi and Enrico Hoffer) added the iconic third ring — making it the first all-seater stadium in Italy. Allianz Arena was designed by Herzog &amp; de Meuron, the same firm that designed the Beijing National Stadium.</p>
    </div>
  </div>
</div>
'''
    return page(83, 'European temples', body)

# Page 84: National stadiums
def page84():
    body = header(84, 'VII', 'National stadiums')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">Two stadiums where national identity is the architecture.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Wembley (England)</h3>
    <p><b>New Wembley opened 2007</b> on the site of the 1923 original. Capacity <b>90,000</b> — the largest stadium in the United Kingdom. The 134m-tall arch is the longest unsupported roof span in the world. Hosts every FA Cup final, every England home international, plus NFL, boxing, and concerts.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Maracanã (Brazil)</h3>
    <p><b>Opened 1950</b> for the World Cup that Brazil lost to Uruguay in the deciding match. Capacity reduced from 199,854 (then world record) to <b>78,838</b> after renovations for the 2014 World Cup. Hosted the 1950 and 2014 World Cup finals — only stadium in the world to do so.</p>

    <div class="callout" style="margin-top: 0.2in;">
      <h3 style="font-size: 10pt;">A stadium of two cathedrals</h3>
      <p style="font-size: 8.5pt; margin: 0;">The Maracanã was named after the Rio Maracanã river, which in turn comes from a Tupi word meaning "similar to a rattle" — a reference to the parrots that once flocked to the area.</p>
    </div>
  </div>
  <div>
    <div class="compare-row">
''' + stadium_svg('Wembley', '90,000', '#FFFFFF') + '''
''' + stadium_svg('Maracanã', '78,838', '#FBC02D') + '''
    </div>
    <div class="factbox navy" style="margin-top: 0.3in;">
      <div class="eyebrow">By the numbers</div>
      <h3 style="font-size: 13pt; margin-top: 0.05in;">Maracanã 1950 World Cup final</h3>
      <p style="font-size: 9pt; margin: 0;">Official attendance: <b>199,854</b>. Realistic estimate: ~210,000 (only 90,850 paid; the rest squeezed in unofficially). Uruguay 2–1 Brazil.</p>
    </div>
  </div>
</div>
'''
    return page(84, 'National stadiums', body)

# Page 85: Champions League
def page85():
    body = header(85, 'VII', 'Champions League format')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">From 2024/25, the Champions League is a <b>36-team league phase</b> — every team plays 8 matches (4 home, 4 away) against seeded opponents, ranked 1–36.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">The league phase (2024/25–)</h3>
    <ol style="font-size: 9pt; margin-left: 0.3in; line-height: 1.5;">
      <li>36 clubs qualify (4 entry spots: league position, UCL holder, UEL/UECL holders)</li>
      <li>Each plays 8 matches — 4 home, 4 away against 8 different opponents</li>
      <li>Top 8 advance directly to Round of 16</li>
      <li>9th–24th play knockout playoff for remaining 8 spots</li>
      <li>25th–36th are eliminated (no drop to UEL)</li>
      <li>Knockout rounds: R16, QF, SF, Final — single-legged from QF onward</li>
    </ol>

    <div class="callout" style="margin-top: 0.2in;">
      <h3 style="font-size: 10pt;">The "Swiss model"</h3>
      <p style="font-size: 8.5pt; margin: 0;">Replaces the old group stage (8 groups of 4 → 125 matches). The new league phase plays 144 matches — 19 more than before, but with more matches for the big clubs, and a more reliable strength-of-schedule balance.</p>
    </div>
  </div>
  <div>
    <div class="diagram">
      <div class="kicker" style="text-align: center; margin-bottom: 0.15in;">Champions League timeline 2024/25</div>
      <div class="timeline" style="padding-left: 0.4in;">
        <div class="timeline-event"><span class="year">Sep</span><h4>Matchday 1–3</h4><p>First 3 of 8 league phase games.</p></div>
        <div class="timeline-event"><span class="year">Oct–Nov</span><h4>Matchday 4–6</h4><p>Back-to-back home and away against seeded opponents.</p></div>
        <div class="timeline-event"><span class="year">Jan</span><h4>Matchday 7–8</h4><p>Final league phase games. Top 8 decided.</p></div>
        <div class="timeline-event"><span class="year">Feb</span><h4>Knockout playoffs</h4><p>9–16 host 17–24 in two-leg ties.</p></div>
        <div class="timeline-event"><span class="year">Mar–Apr</span><h4>Quarter-finals</h4><p>8 → 4 in two legs.</p></div>
        <div class="timeline-event"><span class="year">Apr–May</span><h4>Semi-finals</h4><p>4 → 2 in two legs.</p></div>
        <div class="timeline-event"><span class="year">May</span><h4>Final</h4><p>Single match at a neutral venue (2025: Munich).</p></div>
      </div>
    </div>
  </div>
</div>
'''
    return page(85, 'Champions League format', body)

# Page 86: Europa & Conference
def page86():
    body = header(86, 'VII', 'Europa &amp; Conference')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">UEFA runs three club competitions. The Champions League is the crown jewel; the Europa and Conference Leagues feed into it through coefficient-based promotion.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">UEFA Europa League</h3>
    <p>The second tier — 36 teams in a 2024-format league phase. The UEL winner earns a UCL spot for the next season. Born in 1971 as the UEFA Cup, rebranded 2009. Used to be the stage where Premier League giants would tinker; now a serious route to elite European football.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">UEFA Conference League</h3>
    <p>UEFA's third competition, launched in 2021 to give smaller clubs a European stage. Often dubbed "the Irn-Bru Cup" by British fans — but it has produced memorable runs (Roma 2022, West Ham 2023). The Conference winner also earns a UCL spot if they finish outside qualifying places.</p>
  </div>
  <div>
    <div class="diagram">
      <div class="kicker" style="text-align: center; margin-bottom: 0.15in;">UEFA club competitions 2024/25</div>
      <table style="width: 100%; font-size: 9pt; border-collapse: collapse;">
        <tr style="background: var(--navy); color: var(--paper);">
          <th style="padding: 0.08in 0.12in;">Competition</th>
          <th style="padding: 0.08in 0.12in;">Teams</th>
          <th style="padding: 0.08in 0.12in;">Format</th>
        </tr>
        <tr><td style="padding: 0.08in 0.12in;"><b>Champions League</b></td><td style="text-align: center;">36</td><td style="text-align: center;">League + knockout</td></tr>
        <tr style="background: var(--paper-deep);"><td style="padding: 0.08in 0.12in;"><b>Europa League</b></td><td style="text-align: center;">36</td><td style="text-align: center;">League + knockout</td></tr>
        <tr><td style="padding: 0.08in 0.12in;"><b>Conference League</b></td><td style="text-align: center;">36</td><td style="text-align: center;">League + knockout</td></tr>
        <tr style="background: var(--paper-deep);"><td style="padding: 0.08in 0.12in;"><b>Youth League</b></td><td style="text-align: center;">32</td><td style="text-align: center;">Group + knockout</td></tr>
        <tr><td style="padding: 0.08in 0.12in;"><b>Super Cup</b></td><td style="text-align: center;">2</td><td style="text-align: center;">Single match (Aug)</td></tr>
      </table>
    </div>
    <div class="callout" style="margin-top: 0.2in;">
      <h3 style="font-size: 10pt;">Promotion &amp; relegation</h3>
      <p style="font-size: 8.5pt; margin: 0;">The new format removes the old group → knockout split. Instead, all 36 teams enter one league. Promotion from UECL → UEL is automatic for the winners of certain knockout playoff rounds; from UEL → UCL is reserved for the UEL winner only.</p>
    </div>
  </div>
</div>
'''
    return page(86, 'Europa &amp; Conference', body)

# Page 87: World Cup 2026
def page87():
    body = header(87, 'VII', 'World Cup 2026')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">The 2026 FIFA World Cup in the <b>USA, Mexico, and Canada</b> will be the largest in history — <b>48 teams, 104 matches, 11 host cities</b> over 39 days.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Tournament structure</h3>
    <ul style="font-size: 9pt; margin-left: 0.3in; line-height: 1.5;">
      <li><b>12 groups of 4</b> (was 8 groups of 4)</li>
      <li>Top 2 + 8 best 3rd-placed teams → <b>32-team knockout</b></li>
      <li>New round of 32 added before the Round of 16</li>
      <li><b>Final at MetLife Stadium</b>, East Rutherford, NJ, 19 July 2026</li>
    </ul>

    <div class="callout" style="margin-top: 0.2in;">
      <h3 style="font-size: 10pt;">A 104-match marathon</h3>
      <p style="font-size: 8.5pt; margin: 0;">This is the same number of matches as the 1998, 2002, 2006, 2010, 2014, and 2018 World Cups combined — except distributed across 3 host nations and 11 cities.</p>
    </div>
  </div>
  <div>
    <div class="diagram">
      <div class="kicker" style="text-align: center; margin-bottom: 0.15in;">11 host cities</div>
      <table style="width: 100%; font-size: 8.5pt; border-collapse: collapse;">
        <tr style="background: var(--terracotta); color: var(--paper);">
          <th style="padding: 0.06in 0.1in;">Country</th>
          <th style="padding: 0.06in 0.1in;">City</th>
          <th style="padding: 0.06in 0.1in;">Stadium</th>
        </tr>
        <tr><td rowspan="3" style="padding: 0.06in 0.1in; background: var(--paper-deep); text-align: center;"><b>USA</b></td><td style="padding: 0.06in 0.1in;">Atlanta</td><td style="padding: 0.06in 0.1in;">Mercedes-Benz Stadium</td></tr>
        <tr><td style="padding: 0.06in 0.1in;">Boston</td><td style="padding: 0.06in 0.1in;">Gillette Stadium</td></tr>
        <tr><td style="padding: 0.06in 0.1in;">Dallas</td><td style="padding: 0.06in 0.1in;">AT&T Stadium</td></tr>
        <tr><td style="padding: 0.06in 0.1in; background: var(--paper-deep);"><b>USA</b></td><td style="padding: 0.06in 0.1in;">Houston</td><td style="padding: 0.06in 0.1in;">NRG Stadium</td></tr>
        <tr><td style="padding: 0.06in 0.1in;"><b>USA</b></td><td style="padding: 0.06in 0.1in;">Kansas City</td><td style="padding: 0.06in 0.1in;">Arrowhead Stadium</td></tr>
        <tr><td style="padding: 0.06in 0.1in; background: var(--paper-deep);"><b>USA</b></td><td style="padding: 0.06in 0.1in;">Los Angeles</td><td style="padding: 0.06in 0.1in;">SoFi Stadium</td></tr>
        <tr><td style="padding: 0.06in 0.1in;"><b>USA</b></td><td style="padding: 0.06in 0.1in;">Miami</td><td style="padding: 0.06in 0.1in;">Hard Rock Stadium</td></tr>
        <tr><td style="padding: 0.06in 0.1in; background: var(--paper-deep);"><b>USA</b></td><td style="padding: 0.06in 0.1in;">New York / NJ</td><td style="padding: 0.06in 0.1in;">MetLife Stadium (Final)</td></tr>
        <tr><td style="padding: 0.06in 0.1in;"><b>USA</b></td><td style="padding: 0.06in 0.1in;">Philadelphia</td><td style="padding: 0.06in 0.1in;">Lincoln Financial Field</td></tr>
        <tr><td style="padding: 0.06in 0.1in; background: var(--paper-deep);"><b>USA</b></td><td style="padding: 0.06in 0.1in;">San Francisco</td><td style="padding: 0.06in 0.1in;">Levi's Stadium</td></tr>
        <tr><td style="padding: 0.06in 0.1in;"><b>USA</b></td><td style="padding: 0.06in 0.1in;">Seattle</td><td style="padding: 0.06in 0.1in;">Lumen Field</td></tr>
        <tr><td style="padding: 0.06in 0.1in; background: var(--paper-deep);"><b>Mexico</b></td><td style="padding: 0.06in 0.1in;">Guadalajara</td><td style="padding: 0.06in 0.1in;">Estadio Akron</td></tr>
        <tr><td style="padding: 0.06in 0.1in;"><b>Mexico</b></td><td style="padding: 0.06in 0.1in;">Mexico City</td><td style="padding: 0.06in 0.1in;">Estadio Azteca</td></tr>
        <tr><td style="padding: 0.06in 0.1in; background: var(--paper-deep);"><b>Mexico</b></td><td style="padding: 0.06in 0.1in;">Monterrey</td><td style="padding: 0.06in 0.1in;">Estadio BBVA</td></tr>
        <tr><td style="padding: 0.06in 0.1in;"><b>Canada</b></td><td style="padding: 0.06in 0.1in;">Toronto</td><td style="padding: 0.06in 0.1in;">BMO Field</td></tr>
        <tr><td style="padding: 0.06in 0.1in; background: var(--paper-deep);"><b>Canada</b></td><td style="padding: 0.06in 0.1in;">Vancouver</td><td style="padding: 0.06in 0.1in;">BC Place</td></tr>
      </table>
    </div>
  </div>
</div>
'''
    return page(87, 'World Cup 2026', body)

# Page 88: Premier League
def page88():
    body = header(88, 'VII', 'Premier League')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">The richest domestic football competition in the world. <b>20 clubs</b>, <b>38 matchdays</b>, <b>380 matches per season</b>, and a global TV audience measured in the billions.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">How it works</h3>
    <ul style="font-size: 9pt; margin-left: 0.3in; line-height: 1.5;">
      <li>Each club plays every other home and away (2 × 19 = 38 games)</li>
      <li>3 points for a win, 1 for a draw, 0 for a loss</li>
      <li>Top 4 qualify for Champions League</li>
      <li>5th qualifies for Europa League, FA Cup winner also qualifies</li>
      <li>Conference League playoff for 6th–7th</li>
      <li>Bottom 3 <b>relegated</b> to the Championship</li>
      <li>Top 2 Championship teams + playoff winner promoted</li>
    </ul>

    <div class="callout" style="margin-top: 0.2in;">
      <h3 style="font-size: 10pt;">Promotion / relegation</h3>
      <p style="font-size: 8.5pt; margin: 0;">The 3 relegated teams each receive ~<b>£100m parachute payments</b> over 3 years. This is one of the most generous parachute systems in world football — designed to soften the financial shock of relegation and ensure parachute clubs are competitive in the Championship.</p>
    </div>
  </div>
  <div>
    <div class="diagram">
      <div class="kicker" style="text-align: center; margin-bottom: 0.15in;">Premier League season</div>
      <div class="timeline">
        <div class="timeline-event"><span class="year">Aug</span><h4>Season start</h4><p>First matchday, usually a Friday night.</p></div>
        <div class="timeline-event"><span class="year">Sep</span><h4>International break</h4><p>First FIFA window of the season.</p></div>
        <div class="timeline-event"><span class="year">Dec</span><h4>Festive fixtures</h4><p>3 matches in 8 days — a uniquely English tradition.</p></div>
        <div class="timeline-event"><span class="year">Jan</span><h4>Transfer window</h4><p>Major signings, season-defining deals.</p></div>
        <div class="timeline-event"><span class="year">May</span><h4>Season end</h4><p>All 380 matches complete; title, European spots, relegation decided.</p></div>
      </div>
    </div>
    <div class="factbox navy" style="margin-top: 0.2in;">
      <div class="eyebrow">The trophy</div>
      <h3 style="font-size: 13pt; margin-top: 0.05in;">Officially the "Barclays Premier League Trophy" but always called "the Premier League trophy" — silver, with a silk-and-leather ribbon in the league's colours: purple, blue, red, white, gold.</h3>
    </div>
  </div>
</div>
'''
    return page(88, 'Premier League', body)

# Page 89: Big-5 leagues
def page89():
    body = header(89, 'VII', 'Big-5 leagues')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">The five permanent members of UEFA's coefficient top — the leagues with the most Champions League and Europa League entrants, and the highest transfer fees.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Compared</h3>
    <p>Total annual revenue of the Big-5 is over <b>€17 billion</b> — roughly equal to the entire GDP of Iceland. They dominate European football through financial muscle, drawing the world's best players.</p>

    <div class="callout" style="margin-top: 0.2in;">
      <h3 style="font-size: 10pt;">Beyond the Big-5</h3>
      <p style="font-size: 8.5pt; margin: 0;">The Portuguese Liga, Dutch Eredivisie, Belgian Pro League, Turkish Süper Lig, and Brazilian Série A all punch above their weight in talent production — but their clubs can rarely afford to keep their best players.</p>
    </div>
  </div>
  <div>
    <div class="diagram">
      <div class="kicker" style="text-align: center; margin-bottom: 0.15in;">Big-5 leagues at a glance</div>
      <table style="width: 100%; font-size: 8pt; border-collapse: collapse;">
        <tr style="background: var(--navy); color: var(--paper);">
          <th style="padding: 0.06in 0.08in;">League</th>
          <th style="padding: 0.06in 0.08in;">Teams</th>
          <th style="padding: 0.06in 0.08in;">Relegated</th>
          <th style="padding: 0.06in 0.08in;">UCL spots</th>
          <th style="padding: 0.06in 0.08in;">Revenue €bn</th>
        </tr>
        <tr><td style="padding: 0.06in 0.08in;"><b>Premier League</b></td><td style="text-align: center;">20</td><td style="text-align: center;">3</td><td style="text-align: center;">4</td><td style="text-align: center; color: var(--terracotta); font-weight: 700;">7.4</td></tr>
        <tr style="background: var(--paper-deep);"><td style="padding: 0.06in 0.08in;"><b>La Liga</b></td><td style="text-align: center;">20</td><td style="text-align: center;">3</td><td style="text-align: center;">4</td><td style="text-align: center;">4.0</td></tr>
        <tr><td style="padding: 0.06in 0.08in;"><b>Bundesliga</b></td><td style="text-align: center;">18</td><td style="text-align: center;">2 + playoff</td><td style="text-align: center;">4</td><td style="text-align: center;">3.8</td></tr>
        <tr style="background: var(--paper-deep);"><td style="padding: 0.06in 0.08in;"><b>Serie A</b></td><td style="text-align: center;">20</td><td style="text-align: center;">3</td><td style="text-align: center;">4</td><td style="text-align: center;">2.7</td></tr>
        <tr><td style="padding: 0.06in 0.08in;"><b>Ligue 1</b></td><td style="text-align: center;">18</td><td style="text-align: center;">2 + playoff</td><td style="text-align: center;">3-4</td><td style="text-align: center;">2.2</td></tr>
      </table>
    </div>
    <div class="factbox terracotta" style="margin-top: 0.2in;">
      <div class="eyebrow">Revenue gap</div>
      <h3 style="font-size: 12pt; margin-top: 0.05in;">The Premier League earns <b>3.5× more than Ligue 1</b> — even though both have roughly the same number of teams. TV rights inequality is the single biggest factor.</h3>
    </div>
  </div>
</div>
'''
    return page(89, 'Big-5 leagues', body)

# Page 90: Libertadores & Club World Cup
def page90():
    body = header(90, 'VII', 'Libertadores &amp; Club WC')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">South America's premier club competition and the new Club World Cup that crowns the global champion.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Copa Libertadores</h3>
    <p>Est. 1960. Run by CONMEBOL. 47 clubs from 10 South American nations enter. The trophy — a silver urn topped by a globe — is the most coveted prize in South American club football. The <b>Superclásico</b> final has happened three times (1976, 1977, 1978, all Boca); the 2018 final was River Plate–Boca Juniors, the most-watched club match in history.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">FIFA Club World Cup</h3>
    <p>The new 32-team Club World Cup launched in summer 2025 in the USA. Six confederations, 32 clubs, 63 matches over 29 days. Replaces the old 7-team annual tournament. Format mirrors the World Cup (12 groups of 4 + 32-team knockout).</p>
  </div>
  <div>
    <div class="diagram">
      <div class="kicker" style="text-align: center; margin-bottom: 0.15in;">Copa Libertadores: most titles</div>
      <table style="width: 100%; font-size: 9pt; border-collapse: collapse;">
        <tr style="background: var(--terracotta); color: var(--paper);">
          <th style="padding: 0.08in 0.12in;">Club</th>
          <th style="padding: 0.08in 0.12in;">Country</th>
          <th style="padding: 0.08in 0.12in;">Titles</th>
        </tr>
        <tr style="background: var(--paper-deep);"><td style="padding: 0.08in 0.12in;"><b>Alianza Lima</b></td><td style="padding: 0.08in 0.12in;">Peru</td><td style="text-align: center;">—</td></tr>
        <tr><td style="padding: 0.08in 0.12in;"><b>Peñarol</b></td><td style="padding: 0.08in 0.12in;">Uruguay</td><td style="text-align: center; color: var(--terracotta); font-weight: 700;">5</td></tr>
        <tr style="background: var(--paper-deep);"><td style="padding: 0.08in 0.12in;"><b>River Plate</b></td><td style="padding: 0.08in 0.12in;">Argentina</td><td style="text-align: center; color: var(--terracotta); font-weight: 700;">4</td></tr>
        <tr><td style="padding: 0.08in 0.12in;"><b>Boca Juniors</b></td><td style="padding: 0.08in 0.12in;">Argentina</td><td style="text-align: center; color: var(--terracotta); font-weight: 700;">4</td></tr>
        <tr style="background: var(--paper-deep);"><td style="padding: 0.08in 0.12in;"><b>Santos</b></td><td style="padding: 0.08in 0.12in;">Brazil</td><td style="text-align: center;">3</td></tr>
        <tr><td style="padding: 0.08in 0.12in;"><b>Independiente</b></td><td style="padding: 0.08in 0.12in;">Argentina</td><td style="text-align: center; color: var(--terracotta); font-weight: 700;">7</td></tr>
        <tr style="background: var(--paper-deep);"><td style="padding: 0.08in 0.12in;"><b>São Paulo</b></td><td style="padding: 0.08in 0.12in;">Brazil</td><td style="text-align: center;">3</td></tr>
      </table>
    </div>
    <div class="callout" style="margin-top: 0.2in;">
      <h3 style="font-size: 10pt;">Independiente — the "Rey de Copas"</h3>
      <p style="font-size: 8.5pt; margin: 0;">With 7 Libertadores trophies, Independiente has more than any other club — the most successful Libertadores side of all time, despite having never won a Copa América. Their Avellaneda stadium is nicknamed <b>"La Doble Visera"</b> for its distinctive double-canopy roof.</p>
    </div>
  </div>
</div>
'''
    return page(90, 'Libertadores &amp; Club WC', body)

# Page 91: Internationals
def page91():
    body = header(91, 'VII', 'International tournaments')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">Every two years (or so), the world stops to watch the continental championships. Here are the four biggest.</p>

    <div class="compare-row">
      <div class="compare-cell featured">
        <h4 style="font-size: 14pt;">Euro</h4>
        <div class="big-num">24</div>
        <p style="font-size: 9pt;">UEFA European Championship. Held every 4 years (since 1960). 24 teams, 51 matches.</p>
      </div>
      <div class="compare-cell">
        <h4 style="font-size: 14pt;">Copa América</h4>
        <div class="big-num" style="color: var(--terracotta);">16</div>
        <p style="font-size: 9pt;">CONMEBOL. Held every 4 years (since 1916 — the oldest continental comp). 16 teams.</p>
      </div>
    </div>

    <div class="compare-row" style="margin-top: 0.15in;">
      <div class="compare-cell">
        <h4 style="font-size: 14pt;">AFCON</h4>
        <div class="big-num" style="color: var(--terracotta);">24</div>
        <p style="font-size: 9pt;">Africa Cup of Nations. CAF. Held every 2 years. 24 teams, last held in Côte d'Ivoire (2024).</p>
      </div>
      <div class="compare-cell featured">
        <h4 style="font-size: 14pt;">Asian Cup</h4>
        <div class="big-num">24</div>
        <p style="font-size: 9pt;">AFC. Held every 4 years. 24 teams, last held in Qatar (2023).</p>
      </div>
    </div>

    <div class="callout" style="margin-top: 0.2in;">
      <h3 style="font-size: 10pt;">The Nations League revolution</h3>
      <p style="font-size: 8.5pt; margin: 0;">From 2018, UEFA replaced most friendlies with the Nations League — a 55-team league phase (4 divisions) that culminates in a Final Four. The competition has dramatically reduced pointless international friendlies across European football.</p>
    </div>
  </div>
  <div>
    <div class="diagram">
      <div class="kicker" style="text-align: center; margin-bottom: 0.15in;">International competitions calendar</div>
      <div class="timeline">
        <div class="timeline-event"><span class="year">June</span><h4>International windows</h4><p>Most club football pauses for 1 week each March, June, September, October, November.</p></div>
        <div class="timeline-event"><span class="year">Even years</span><h4>World Cup cycle</h4><p>The 32-team (2022) or 48-team (2026) tournament held every 4 years.</p></div>
        <div class="timeline-event"><span class="year">2024</span><h4>Euro / Copa</h4><p>UEFA Euro 2024 in Germany, Copa América 2024 in USA.</p></div>
        <div class="timeline-event"><span class="year">2025</span><h4>AFCON</h4><p>Africa Cup of Nations in Morocco.</p></div>
        <div class="timeline-event"><span class="year">2026</span><h4>World Cup</h4><p>First 48-team World Cup — USA, Mexico, Canada.</p></div>
      </div>
    </div>
  </div>
</div>
'''
    return page(91, 'International tournaments', body)

# Page 92: Women's football
def page92():
    body = header(92, 'VII', 'Women\'s football')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">The women's game has grown 8× since 2015. Revenue, viewership, and pay are all on a sharp upward curve.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Big-5 women's leagues</h3>
    <ul style="font-size: 9pt; margin-left: 0.3in; line-height: 1.5;">
      <li><b>WSL</b> (Women's Super League, England) — 12 clubs, Barclays sponsor since 2021</li>
      <li><b>Liga F</b> (Spain) — 16 clubs, professional since 2021</li>
      <li><b>Frauen-Bundesliga</b> (Germany) — 12 clubs, oldest professional league (1990)</li>
      <li><b>Première Ligue</b> (France) — 12 clubs</li>
      <li><b>NWSL</b> (USA) — 14 clubs, growing fast on the back of the 2019 World Cup win</li>
    </ul>

    <div class="callout" style="margin-top: 0.2in;">
      <h3 style="font-size: 10pt;">The 2023 World Cup effect</h3>
      <p style="font-size: 8.5pt; margin: 0;">Spain's 2023 World Cup win — combined with the <i>Las 15</i> player mutiny against the federation — accelerated structural change. Players now have a collective bargaining agreement, professional contracts, and 15 days of paid leave.</p>
    </div>
  </div>
  <div>
    <div class="diagram">
      <div class="kicker" style="text-align: center; margin-bottom: 0.15in;">Women's World Cup — winners</div>
      <table style="width: 100%; font-size: 9pt; border-collapse: collapse;">
        <tr style="background: var(--green); color: var(--paper);">
          <th style="padding: 0.08in 0.12in;">Year</th>
          <th style="padding: 0.08in 0.12in;">Winner</th>
          <th style="padding: 0.08in 0.12in;">Runner-up</th>
        </tr>
        <tr style="background: var(--paper-deep);"><td style="padding: 0.08in 0.12in;">2015</td><td>USA</td><td>Japan</td></tr>
        <tr><td style="padding: 0.08in 0.12in;">2019</td><td>USA</td><td>Netherlands</td></tr>
        <tr style="background: var(--paper-deep);"><td style="padding: 0.08in 0.12in;">2023</td><td>Spain</td><td>England</td></tr>
        <tr><td style="padding: 0.08in 0.12in; background: var(--gold);"><b>2027</b></td><td><b>Brazil</b></td><td><b>TBD</b></td></tr>
        <tr style="background: var(--paper-deep);"><td style="padding: 0.08in 0.12in;"><b>2031</b></td><td><b>USA</b></td><td><b>TBD</b></td></tr>
      </table>
    </div>
    <div class="factbox terracotta" style="margin-top: 0.2in;">
      <div class="eyebrow">By the numbers</div>
      <h3 style="font-size: 13pt; margin-top: 0.05in;">The 2023 WWC final (Spain vs England) drew <b>1.9 billion</b> global viewers — the most-watched women's football match ever. Prize money: <b>$110m</b> — 10× the 2015 total.</h3>
    </div>
  </div>
</div>
'''
    return page(92, "Women's football", body)

# Write
for fn in [page81, page82, page83, page84, page85, page86, page87, page88, page89, page90, page91, page92]:
    n = int(fn.__name__.replace('page', ''))
    with open(f'{PAGES_DIR}/{n:02d}-page.html', 'w') as f:
        f.write(fn())
    print(f"Wrote page {n}")
print("Done 81-92")