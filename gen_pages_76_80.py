#!/usr/bin/env python3
"""Generate pages 76-100: Portuguese three, Boca/River, Istanbul, Mexico, SPL, stadiums, competitions, culture."""
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

# Page 76: Portuguese three
def page76():
    body = header(76, 'VI', 'Portuguese three')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">Portugal's big three clubs — Benfica, Porto, Sporting — have between them won <b>87 Primeira Liga titles</b> (out of 90 total awarded since 1934).</p>

    <div class="sidebar terracotta" style="margin: 0.2in 0;">
      <h3>The O Clássico</h3>
      <p style="font-size: 9pt;">The rivalry between <b>Benfica</b> and <b>Porto</b> is one of the most watched in world football — often called the "war of the roosters" after each club's mascot.</p>
    </div>

    <div class="callout">
      <h3 style="font-size: 11pt;">The Three Pillars</h3>
      <p style="font-size: 9pt; margin: 0;"><b>Benfica</b> (1904, 38 titles) plays at the Estádio da Luz. <b>Porto</b> (1893, 30 titles) at Estádio do Dragão. <b>Sporting</b> (1906, 20 titles) at Estádio José Alvalade. All three stadiums were rebuilt for Euro 2004.</p>
    </div>
  </div>
  <div>
    <div class="diagram">
      <div class="kicker" style="text-align: center; margin-bottom: 0.15in;">Primeira Liga, all-time</div>
      <table style="width: 100%; font-size: 9pt; border-collapse: collapse;">
        <tr style="background: var(--terracotta); color: var(--paper);">
          <th style="padding: 0.08in 0.12in; text-align: left;">Club</th>
          <th style="padding: 0.08in 0.12in; text-align: center;">Founded</th>
          <th style="padding: 0.08in 0.12in; text-align: center;">Titles</th>
          <th style="padding: 0.08in 0.12in; text-align: center;">UCL</th>
        </tr>
        <tr style="background: var(--paper-deep);">
          <td style="padding: 0.08in 0.12in;"><b>Benfica</b></td><td style="text-align: center;">1904</td><td style="text-align: center; color: var(--terracotta); font-weight: 700;">38</td><td style="text-align: center;">2</td>
        </tr>
        <tr>
          <td style="padding: 0.08in 0.12in;"><b>Porto</b></td><td style="text-align: center;">1893</td><td style="text-align: center; color: var(--terracotta); font-weight: 700;">30</td><td style="text-align: center;">2</td>
        </tr>
        <tr style="background: var(--paper-deep);">
          <td style="padding: 0.08in 0.12in;"><b>Sporting CP</b></td><td style="text-align: center;">1906</td><td style="text-align: center; color: var(--terracotta); font-weight: 700;">20</td><td style="text-align: center;">0</td>
        </tr>
      </table>
    </div>
    <div class="factbox navy" style="margin-top: 0.2in;">
      <div class="eyebrow">Producing talent</div>
      <h3 style="font-size: 11pt;">Cristiano Ronaldo, Luís Figo, João Félix, Bernardo Silva, Bruno Fernandes, Gonçalo Ramos, Rúben Dias, João Cancelo, Pedro Neto — the conveyor belt of Portuguese football is unmatched for a country of 10 million.</h3>
    </div>
  </div>
</div>
'''
    return page(76, 'Portuguese three', body)

# Page 77: Boca & River
def page77():
    body = header(77, 'VI', 'Boca &amp; River')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">The <b>Superclásico</b> between Boca Juniors and River Plate is, by many accounts, the most passionate football fixture on earth.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Boca Juniors</h3>
    <p><b>Founded 1905</b> · <b>Estadio Alberto J. Armando</b> ("La Bombonera", 54,000) · <b>34 Argentine titles</b> · 6 Copa Libertadores. Wearing blue and yellow stripes.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">River Plate</h3>
    <p><b>Founded 1901</b> · <b>Estadio Más Monumental</b> (84,567, largest in South America) · <b>38 Argentine titles</b> · 4 Copa Libertadores. The famous white shirt with a red diagonal sash.</p>

    <div class="callout" style="margin-top: 0.2in;">
      <h3 style="font-size: 10pt;">A working-class rivalry</h3>
      <p style="font-size: 8.5pt; margin: 0;">Boca fans come from the dock neighbourhood of La Boca; River fans from the wealthier Núñez district. The class divide is real — and reflected in the violence that has occasionally punctuated the fixture.</p>
    </div>
  </div>
  <div>
    <div class="diagram" style="padding: 0.3in; text-align: center;">
      <div class="kicker" style="margin-bottom: 0.2in;">La Bombonera</div>
      <svg viewBox="0 0 200 130" style="width: 100%; max-width: 3in;">
        <!-- Stadium cross section -->
        <path d="M 20 110 L 20 60 Q 20 30 60 25 L 140 25 Q 180 30 180 60 L 180 110 Z" fill="#c4b89a" stroke="var(--ink)" stroke-width="1.5"/>
        <!-- Tier rows -->
        <rect x="20" y="40" width="160" height="20" fill="#D2122E"/>
        <rect x="20" y="62" width="160" height="20" fill="#1A3A8F"/>
        <rect x="20" y="84" width="160" height="20" fill="#D2122E"/>
        <!-- Pitch -->
        <ellipse cx="100" cy="118" rx="80" ry="6" fill="#4caf50" stroke="var(--ink)" stroke-width="0.5"/>
        <!-- Yellow seats -->
        <text x="100" y="55" font-size="9" text-anchor="middle" fill="#FDE100" font-weight="700">BOCA JUNIORS</text>
        <text x="100" y="77" font-size="9" text-anchor="middle" fill="#FFFFFF" font-weight="700">XENEIZE</text>
        <text x="100" y="99" font-size="9" text-anchor="middle" fill="#FDE100" font-weight="700">LA 12</text>
      </svg>
      <p class="cap">The iconic flat-on-one-side profile of La Bombonera — the steep stands behind the goal create the famous acoustic resonance when fans leap together.</p>
    </div>
  </div>
</div>
'''
    return page(77, 'Boca &amp; River', body)

# Page 78: Istanbul giants
def page78():
    body = header(78, 'VI', 'Istanbul giants')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">Two clubs, one city, one of the loudest derbies in the world. Galatasaray and Fenerbahçe have shared <b>63 Süper Lig titles</b> between them.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Galatasaray</h3>
    <p><b>Founded 1905</b> · <b>Rams Park</b> (52,223) · <b>24 league titles</b> · Only Turkish club to win the UEFA Cup (2000). Yellow and red halves, with red trim.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Fenerbahçe</h3>
    <p><b>Founded 1907</b> · <b>Şükrü Saracoğlu Stadium</b> (50,530) · <b>19 league titles</b> · Yellow and navy stripes, the most-nicknamed kit in world football.</p>

    <div class="callout" style="margin-top: 0.2in;">
      <h3 style="font-size: 10pt;">Welcome to hell</h3>
      <p style="font-size: 8.5pt; margin: 0;">Sir Alex Ferguson called Galatasaray's home a "welcome to hell" after a Champions League night in 1993. The Turkish flag is waved from the stands during European nights — a tradition started by Fenerbahçe fans and adopted across the country.</p>
    </div>
  </div>
  <div>
    <div class="diagram">
      <div class="kicker" style="text-align: center; margin-bottom: 0.15in;">Süper Lig titles, all-time (top 5)</div>
      <table style="width: 100%; font-size: 9pt; border-collapse: collapse;">
        <tr style="background: var(--terracotta); color: var(--paper);">
          <th style="padding: 0.08in 0.12in; text-align: left;">Club</th>
          <th style="padding: 0.08in 0.12in; text-align: center;">Titles</th>
          <th style="padding: 0.08in 0.12in; text-align: center;">Years</th>
        </tr>
        <tr style="background: var(--paper-deep);">
          <td style="padding: 0.08in 0.12in;"><b>Galatasaray</b></td>
          <td style="text-align: center; color: var(--terracotta); font-weight: 700;">24</td>
          <td style="text-align: center;">1961–present</td>
        </tr>
        <tr>
          <td style="padding: 0.08in 0.12in;"><b>Fenerbahçe</b></td>
          <td style="text-align: center; color: var(--terracotta); font-weight: 700;">19</td>
          <td style="text-align: center;">1959–present</td>
        </tr>
        <tr style="background: var(--paper-deep);">
          <td style="padding: 0.08in 0.12in;"><b>Beşiktaş</b></td>
          <td style="text-align: center; color: var(--terracotta); font-weight: 700;">16</td>
          <td style="text-align: center;">1957–present</td>
        </tr>
        <tr>
          <td style="padding: 0.08in 0.12in;"><b>Trabzonspor</b></td>
          <td style="text-align: center; color: var(--terracotta); font-weight: 700;">7</td>
          <td style="text-align: center;">1975–present</td>
        </tr>
      </table>
    </div>
    <div class="factbox navy" style="margin-top: 0.2in;">
      <div class="eyebrow">Foreign backing</div>
      <h3 style="font-size: 11pt; margin-top: 0.05in;">Three of the four Istanbul giants have been bought or invested in by foreign owners in the past decade — a story playing out across Turkish football.</h3>
    </div>
  </div>
</div>
'''
    return page(78, 'Istanbul giants', body)

# Page 79: Mexican giants
def page79():
    body = header(79, 'VI', 'Mexican giants')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">Club América and Chivas — the Liga MX equivalent of Boca vs River. <b>Together they have won 30 of the 78 Liga MX titles</b> on offer.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Club América</h3>
    <p><b>Founded 1916</b> · <b>Estadio Azteca</b> (87,000) · <b>15 Liga MX titles</b> · 7 CONCACAF Champions League. Yellow shirt, blue shorts, the most valuable club in Mexico.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Chivas de Guadalajara</h3>
    <p><b>Founded 1906</b> · <b>Estadio Akron</b> (48,071) · <b>12 Liga MX titles</b> · One of two Liga MX clubs to field only Mexican players — an explicit identity choice.</p>

    <div class="callout" style="margin-top: 0.2in;">
      <h3 style="font-size: 10pt;">Super Clásico</h3>
      <p style="font-size: 8.5pt; margin: 0;">First played in 1925. América fans call themselves "azulcremas" and Chivas fans "chiveros". A match that regularly draws Mexico's largest TV audience of any fixture.</p>
    </div>
  </div>
  <div>
    <div class="diagram">
      <div class="kicker" style="text-align: center; margin-bottom: 0.15in;">Liga MX, all-time</div>
      <table style="width: 100%; font-size: 9pt; border-collapse: collapse;">
        <tr style="background: var(--green); color: var(--paper);">
          <th style="padding: 0.08in 0.12in; text-align: left;">Club</th>
          <th style="padding: 0.08in 0.12in; text-align: center;">Titles</th>
          <th style="padding: 0.08in 0.12in; text-align: center;">Founded</th>
        </tr>
        <tr style="background: var(--paper-deep);">
          <td style="padding: 0.08in 0.12in;"><b>América</b></td><td style="text-align: center; color: var(--terracotta); font-weight: 700;">15</td><td style="text-align: center;">1916</td>
        </tr>
        <tr>
          <td style="padding: 0.08in 0.12in;"><b>Chivas</b></td><td style="text-align: center; color: var(--terracotta); font-weight: 700;">12</td><td style="text-align: center;">1906</td>
        </tr>
        <tr style="background: var(--paper-deep);">
          <td style="padding: 0.08in 0.12in;"><b>Toluca</b></td><td style="text-align: center; color: var(--terracotta); font-weight: 700;">11</td><td style="text-align: center;">1917</td>
        </tr>
        <tr>
          <td style="padding: 0.08in 0.12in;"><b>Cruz Azul</b></td><td style="text-align: center; color: var(--terracotta); font-weight: 700;">9</td><td style="text-align: center;">1927</td>
        </tr>
        <tr style="background: var(--paper-deep);">
          <td style="padding: 0.08in 0.12in;"><b>Pumas UNAM</b></td><td style="text-align: center; color: var(--terracotta); font-weight: 700;">7</td><td style="text-align: center;">1954</td>
        </tr>
      </table>
    </div>
    <div class="factbox terracotta" style="margin-top: 0.2in;">
      <div class="eyebrow">Estadio Azteca</div>
      <h3 style="font-size: 11pt; margin-top: 0.05in;">The only stadium to host two World Cup finals (1970, 1986). Pelé and Maradona both won their last World Cup titles there.</h3>
    </div>
  </div>
</div>
'''
    return page(79, 'Mexican giants', body)

# Page 80: Saudi Pro League
def page80():
    body = header(80, 'VI', 'Saudi Pro League')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">In 2023, the Saudi Public Investment Fund began signing dozens of Europe's biggest names — Cristiano Ronaldo, Neymar, Karim Benzema, N'Golo Kanté — to the Saudi Pro League.</p>

    <p>The <b>PIF</b> owns four of the league's biggest clubs directly (Al-Ittihad, Al-Ahli, Al-Hilal, Al-Nassr) and is the league's majority sponsor. Total spending in 2023–25 exceeded <b>€2.5 billion</b>.</p>

    <div class="callout" style="margin-top: 0.2in;">
      <h3 style="font-size: 10pt;">Vision 2030</h3>
      <p style="font-size: 8.5pt; margin: 0;">The Saudi Pro League is the most visible piece of Crown Prince Mohammed bin Salman's national plan to diversify the economy away from oil. Football is the marketing funnel; the actual investments are in tourism, infrastructure, and lifestyle.</p>
    </div>
  </div>
  <div>
    <div class="diagram">
      <div class="kicker" style="text-align: center; margin-bottom: 0.15in;">Saudi Pro League — top 4 (PIF-owned)</div>
      <table style="width: 100%; font-size: 9pt; border-collapse: collapse;">
        <tr style="background: var(--terracotta); color: var(--paper);">
          <th style="padding: 0.08in 0.12in; text-align: left;">Club</th>
          <th style="padding: 0.08in 0.12in; text-align: center;">Titles</th>
          <th style="padding: 0.08in 0.12in; text-align: left;">Star signing</th>
        </tr>
        <tr style="background: var(--paper-deep);">
          <td style="padding: 0.08in 0.12in;"><b>Al-Hilal</b></td><td style="text-align: center;">19</td><td style="padding: 0.08in 0.12in;">Neymar, Mitrović</td>
        </tr>
        <tr>
          <td style="padding: 0.08in 0.12in;"><b>Al-Ittihad</b></td><td style="text-align: center;">9</td><td style="padding: 0.08in 0.12in;">Benzema, Kanté</td>
        </tr>
        <tr style="background: var(--paper-deep);">
          <td style="padding: 0.08in 0.12in;"><b>Al-Ahli</b></td><td style="text-align: center;">3</td><td style="padding: 0.08in 0.12in;">Mahrez, Firmino</td>
        </tr>
        <tr>
          <td style="padding: 0.08in 0.12in;"><b>Al-Nassr</b></td><td style="text-align: center;">9</td><td style="padding: 0.08in 0.12in;">Ronaldo, Mané</td>
        </tr>
      </table>
    </div>
    <div class="factbox dark" style="margin-top: 0.2in;">
      <div class="eyebrow">Counterpoint</div>
      <h3 style="font-size: 11pt;">Players cite: 5× the European wage, zero income tax, climate, infrastructure. Critics cite: sporting merit, human rights, league competitiveness, post-Ronaldo cliff.</h3>
    </div>
  </div>
</div>
'''
    return page(80, 'Saudi Pro League', body)

# Write all
for fn in [page76, page77, page78, page79, page80]:
    n = int(fn.__name__.replace('page', ''))
    with open(f'{PAGES_DIR}/{n:02d}-page.html', 'w') as f:
        f.write(fn())
    print(f"Wrote page {n}")

print("Done 76-80")