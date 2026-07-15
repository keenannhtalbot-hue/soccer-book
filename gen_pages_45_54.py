#!/usr/bin/env python3
"""Generate pages 45-54: Jerseys & Kits."""
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

# Helper: kit SVG
def kit_svg(primary, secondary, sleeve='solid', collar='crew', number='10', label=''):
    """Jersey SVG with collar, sleeves, number."""
    collar_paths = {
        'crew': 'M 60 5 Q 75 12 90 12 Q 105 12 120 5 L 115 8 L 105 5 L 90 8 L 75 5 L 65 8 Z',
        'v': 'M 60 5 L 90 18 L 120 5 L 110 4 L 90 12 L 70 4 Z',
        'polo': 'M 60 5 L 90 5 L 90 18 L 120 5 L 110 4 L 90 12 L 70 4 Z'
    }
    return f'''<svg viewBox="0 0 180 220" style="width: 1in; aspect-ratio: 9/11;">
  <path d="M 35 25 L 55 5 L 75 18 L 105 18 L 125 5 L 145 25 L 165 35 L 165 200 L 15 200 L 15 35 Z"
        fill="{primary}" stroke="var(--ink)" stroke-width="1.5"/>
  <path d="{collar_paths.get(collar, collar_paths['crew'])}" fill="{secondary}"/>
  <text x="90" y="115" font-size="22" text-anchor="middle" fill="{secondary if primary.lower() != secondary.lower() else 'white'}" font-family="Cormorant Garamond" font-weight="700">{number}</text>
  <text x="90" y="200" font-size="6" text-anchor="middle" fill="var(--ink-mute)" font-family="Inter" font-weight="600">{label}</text>
</svg>'''

# === 45: ANATOMY OF A KIT ===
def page45():
    body = header(45, 'V', 'Anatomy of a modern kit')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">A 2025 football kit is engineered for <b>moisture management</b>, <b>lightweight fit</b>, and <b>brand visibility</b>. The materials are a far cry from the heavy cotton shirts of 1990.</p>
    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Components</h3>
    <ul style="font-size: 9pt; margin-left: 0.3in; line-height: 1.5;">
      <li><b>Main fabric:</b> 100% recycled polyester knit (since 2020)</li>
      <li><b>Panels:</b> Engineered knit zones for breathability</li>
      <li><b>Collar:</b> Heat-bonded TPU, no stitching</li>
      <li><b>Sleeves:</b> Laser-cut ventilation</li>
      <li><b>Numbers:</b> Printed with sublimation inks</li>
      <li><b>Sponsor:</b> Heat-pressed vinyl</li>
      <li><b>Badge:</b> Embroidered or woven polymer</li>
    </ul>
  </div>
  <div>
    <svg viewBox="0 0 200 220" style="width: 70%; display: block; margin: 0 auto;">
      <!-- Jersey -->
      <path d="M 35 30 L 60 8 L 75 18 L 125 18 L 140 8 L 165 30 L 185 45 L 185 200 L 15 200 L 15 45 Z"
            fill="var(--terracotta)" stroke="var(--ink)" stroke-width="1.5"/>
      <!-- Knit texture -->
      <g stroke="rgba(0,0,0,0.15)" stroke-width="0.4">
        <line x1="20" y1="60" x2="180" y2="60"/>
        <line x1="20" y1="80" x2="180" y2="80"/>
        <line x1="20" y1="100" x2="180" y2="100"/>
        <line x1="20" y1="120" x2="180" y2="120"/>
        <line x1="20" y1="140" x2="180" y2="140"/>
        <line x1="20" y1="160" x2="180" y2="160"/>
      </g>
      <!-- Collar -->
      <path d="M 60 8 Q 75 16 90 16 Q 105 16 120 8" fill="var(--ink)"/>
      <!-- Badge -->
      <circle cx="155" cy="55" r="10" fill="var(--gold)" stroke="var(--ink)" stroke-width="1"/>
      <text x="155" y="58" font-size="6" text-anchor="middle" fill="var(--ink)" font-weight="700">CREST</text>
      <!-- Number -->
      <text x="100" y="135" font-size="32" text-anchor="middle" fill="white" font-family="Cormorant Garamond" font-weight="700">10</text>
      <!-- Leader labels -->
      <line x1="180" y1="45" x2="220" y2="30" stroke="var(--terracotta)" stroke-width="0.5" stroke-dasharray="2,2"/>
      <text x="225" y="30" font-size="7" fill="var(--ink)">Sleeve hem</text>
      <line x1="155" y1="55" x2="220" y2="55" stroke="var(--terracotta)" stroke-width="0.5" stroke-dasharray="2,2"/>
      <text x="225" y="58" font-size="7" fill="var(--ink)">Club badge</text>
      <line x1="100" y1="160" x2="220" y2="160" stroke="var(--terracotta)" stroke-width="0.5" stroke-dasharray="2,2"/>
      <text x="225" y="163" font-size="7" fill="var(--ink)">Sponsor logo</text>
    </svg>
    <div class="factbox navy" style="margin-top: 0.15in;">
      <div class="eyebrow">Sustainability</div>
      <h3 style="font-size: 11pt; margin-top: 0.05in;">Nike, Adidas, and Puma shirts since 2020 use 100% recycled polyester — sourced from plastic bottles, fishing nets, and textile waste.</h3>
    </div>
  </div>
</div>
'''
    return page(45, 'Kit anatomy', body)

# === 46: PREMIER LEAGUE 24/25 ===
def page46():
    body = header(46, 'V', 'Premier League kits, 2024/25')
    body += '''
<p class="lead" style="margin: 0.2in 0;">Home kits of the 20 Premier League clubs — the standard away-day wardrobe of the global game.</p>

<div class="kit-display">
  <div class="kit-card">' + kit_svg('#DA291C', '#FBE122', label='Man Utd') + '</div>
  <div class="kit-card">' + kit_svg('#C8102E', '#00B2A9', label='Liverpool') + '</div>
  <div class="kit-card">' + kit_svg('#EF0107', '#063672', label='Arsenal') + '</div>
  <div class="kit-card">' + kit_svg('#6CABDD', '#1C2C5B', label='Man City') + '</div>
  <div class="kit-card">' + kit_svg('#034694', '#FFFFFF', label='Chelsea') + '</div>
  <div class="kit-card">' + kit_svg('#132257', '#FFFFFF', label='Tottenham') + '</div>
  <div class="kit-card">' + kit_svg('#003399', '#FFFFFF', label='Everton') + '</div>
  <div class="kit-card">' + kit_svg('#000000', '#E32221', label='Liverpool ' + 'PL') + '</div>
  <div class="kit-card">' + kit_svg('#1B458F', '#FFFFFF', label='Brighton') + '</div>
</div>

<div class="callout" style="margin-top: 0.2in;">
  <h3 style="font-size: 10pt;">Manufacturers</h3>
  <p style="font-size: 8.5pt; margin: 0;">Nike: 6 PL teams. Adidas: 5. Puma: 3. Castore: 4 (Man City, Newcastle, others). Hummel: 1 (Aston Villa).</p>
</div>

<div class="factbox terracotta" style="margin-top: 0.15in;">
  <div class="eyebrow">Shirt sales, 2024/25</div>
  <h3 style="font-size: 11pt;">Top 5 sellers worldwide: Manchester United (3.2m units), Liverpool (2.4m), Arsenal (2.2m), Real Madrid (2.0m), Man City (1.6m).</h3>
</div>
'''
    return page(46, 'Premier League kits', body)

# === 47: LA LIGA 24/25 ===
def page47():
    body = header(47, 'V', 'La Liga kits, 2024/25')
    body += '''
<p class="lead" style="margin: 0.2in 0;">Home kits from Spain's top flight — the most recognisable colour palette in world football.</p>

<div class="kit-display">
  <div class="kit-card">' + kit_svg('#FFFFFF', '#FEBE10', label='Real Madrid') + '</div>
  <div class="kit-card">' + kit_svg('#A50044', '#0C2340', label='Barcelona') + '</div>
  <div class="kit-card">' + kit_svg('#CB3524', '#FFFFFF', label='Atlético') + '</div>
  <div class="kit-card">' + kit_svg('#EE3522', '#1A3A8F', label='Athletic Club') + '</div>
  <div class="kit-card">' + kit_svg('#0067B1', '#FFFFFF', label='Real Sociedad') + '</div>
  <div class="kit-card">' + kit_svg('#FB090B', '#000000', label='Sevilla') + '</div>
  <div class="kit-card">' + kit_svg('#FFB800', '#FFFFFF', label='Villarreal') + '</div>
  <div class="kit-card">' + kit_svg('#FFFFFF', '#006633', label='Real Betis') + '</div>
  <div class="kit-card">' + kit_svg('#BB1F1F', '#FFFFFF', label='Osasuna') + '</div>
</div>

<div class="callout" style="margin-top: 0.2in;">
  <h3 style="font-size: 10pt;">The El Clásico</h3>
  <p style="font-size: 8.5pt; margin: 0;">Two iconic shirts, two famous colour codes. Real Madrid white = <i>la camiseta blanca</i>; Barcelona blaugrana = <i>barça</i>. Both have barely changed in 100 years.</p>
</div>
'''
    return page(47, 'La Liga kits', body)

# === 48: SERIE A 24/25 ===
def page48():
    body = header(48, 'V', 'Serie A kits, 2024/25')
    body += '''
<p class="lead" style="margin: 0.2in 0;">Italian football's home kits — stripes, checks, and the iconic <i>Nerazzurri</i>.</p>

<div class="kit-display">
  <div class="kit-card">' + kit_svg('#FB090B', '#000000', label='AC Milan') + '</div>
  <div class="kit-card">' + kit_svg('#0068A8', '#000000', label='Inter') + '</div>
  <div class="kit-card">' + kit_svg('#FFFFFF', '#000000', label='Juventus') + '</div>
  <div class="kit-card">' + kit_svg('#12A0D7', '#1A4FA0', label='Napoli') + '</div>
  <div class="kit-card">' + kit_svg('#8E1F2F', '#F5A41B', label='AS Roma') + '</div>
  <div class="kit-card">' + kit_svg('#A39161', '#FFFFFF', label='Atalanta') + '</div>
  <div class="kit-card">' + kit_svg('#E50914', '#1F1F1F', label='Bologna') + '</div>
  <div class="kit-card">' + kit_svg('#7A2239', '#FFFFFF', label='Torino') + '</div>
  <div class="kit-card">' + kit_svg('#9C1B2F', '#FFFFFF', label='Fiorentina') + '</div>
</div>

<div class="callout" style="margin-top: 0.2in;">
  <h3 style="font-size: 10pt;">The Milan Derby</h3>
  <p style="font-size: 8.5pt; margin: 0;">The <b>Derby della Madonnina</b> pairs two iconic shirts: AC Milan's <i>Rossoneri</i> red-black stripes vs Inter's <i>Nerazzurri</i> blue-black stripes. Same stadium, very different stories.</p>
</div>
'''
    return page(48, 'Serie A kits', body)

# === 49: BUNDESLIGA 24/25 ===
def page49():
    body = header(49, 'V', 'Bundesliga kits, 2024/25')
    body += '''
<p class="lead" style="margin: 0.2in 0;">Germany's top flight — cleaner designs, simpler palettes, more historic clubs.</p>

<div class="kit-display">
  <div class="kit-card">' + kit_svg('#DC052D', '#0066B2', label='Bayern') + '</div>
  <div class="kit-card">' + kit_svg('#FDE100', '#000000', label='Dortmund') + '</div>
  <div class="kit-card">' + kit_svg('#E32221', '#000000', label='Leverkusen') + '</div>
  <div class="kit-card">' + kit_svg('#DD0741', '#1A1A1A', label='RB Leipzig') + '</div>
  <div class="kit-card">' + kit_svg('#000000', '#FFFFFF', label='Frankfurt') + '</div>
  <div class="kit-card">' + kit_svg('#108060', '#FFFFFF', label='Werder') + '</div>
  <div class="kit-card">' + kit_svg('#003090', '#FFFFFF', label='HSV') + '</div>
  <div class="kit-card">' + kit_svg('#1976D2', '#FFFFFF', label='Hertha') + '</div>
  <div class="kit-card">' + kit_svg('#006F51', '#FFFFFF', label='Wolfsburg') + '</div>
</div>

<div class="callout" style="margin-top: 0.2in;">
  <h3 style="font-size: 10pt;">The Yellow Wall</h3>
  <p style="font-size: 8.5pt; margin: 0;">Dortmund's iconic yellow shirt — paired with the steep Sudtribüne stand — creates one of football's most distinctive match-day images. Every home game sells out within minutes of tickets going on sale.</p>
</div>
'''
    return page(49, 'Bundesliga kits', body)

# === 50: LIGUE 1 24/25 ===
def page50():
    body = header(50, 'V', 'Ligue 1 kits, 2024/25')
    body += '''
<p class="lead" style="margin: 0.2in 0;">French football — one dominant PSG, then everyone else. The kits reflect the league's stylistic range.</p>

<div class="kit-display">
  <div class="kit-card">' + kit_svg('#004170', '#DA291C', label='PSG') + '</div>
  <div class="kit-card">' + kit_svg('#2FAEE0', '#FFFFFF', label='Marseille') + '</div>
  <div class="kit-card">' + kit_svg('#D71920', '#FFFFFF', label='Lille') + '</div>
  <div class="kit-card">' + kit_svg('#C71F2A', '#FFFFFF', label='Lyon') + '</div>
  <div class="kit-card">' + kit_svg('#0066CC', '#FFFFFF', label='Monaco') + '</div>
  <div class="kit-card">' + kit_svg('#FFFFFF', '#1B458F', label='Nice') + '</div>
  <div class="kit-card">' + kit_svg('#006633', '#FFFFFF', label='Saint-Étienne') + '</div>
  <div class="kit-card">' + kit_svg('#FFC20E', '#1B458F', label='Lens') + '</div>
  <div class="kit-card">' + kit_svg('#000000', '#FFD700', label='Rennes') + '</div>
</div>

<div class="callout" style="margin-top: 0.2in;">
  <h3 style="font-size: 10pt;">The Le Classique</h3>
  <p style="font-size: 8.5pt; margin: 0;">PSG vs Marseille — France's biggest fixture. PSG's Hechter stripe vs OM's cyan-white. A rivalry that has occasionally spilled beyond football.</p>
</div>
'''
    return page(50, 'Ligue 1 kits', body)

# === 51: MLS 24/25 ===
def page51():
    body = header(51, 'V', 'MLS kits, 2024/25')
    body += '''
<p class="lead" style="margin: 0.2in 0;">Major League Soccer is now the most-watched football league in the USA, with 30 clubs across the US and Canada.</p>

<div class="kit-display">
  <div class="kit-card">' + kit_svg('#00205B', '#C8102E', label='LAFC') + '</div>
  <div class="kit-card">' + kit_svg('#000000', '#FFFFFF', label='Galaxy') + '</div>
  <div class="kit-card">' + kit_svg('#A6192E', '#FFFFFF', label='Inter Miami') + '</div>
  <div class="kit-card">' + kit_svg('#012169', '#FFFFFF', label='NYCFC') + '</div>
  <div class="kit-card">' + kit_svg('#DC2626', '#FFFFFF', label='Chicago') + '</div>
  <div class="kit-card">' + kit_svg('#3D8BFD', '#FFFFFF', label='Atlanta') + '</div>
  <div class="kit-card">' + kit_svg('#5F1E20', '#FFFFFF', label='Portland') + '</div>
  <div class="kit-card">' + kit_svg('#FCD619', '#01509A', label='Charlotte') + '</div>
  <div class="kit-card">' + kit_svg('#E03A3E', '#012169', label='NE Revs') + '</div>
</div>

<div class="callout" style="margin-top: 0.2in;">
  <h3 style="font-size: 10pt;">The Messi effect</h3>
  <p style="font-size: 8.5pt; margin: 0;">Inter Miami's pink-and-black kit became the most-sold replica shirt in North American sports history after Lionel Messi joined in July 2023 — selling 1.2M units in the first 6 months.</p>
</div>
'''
    return page(51, 'MLS kits', body)

# === 52: WORLD CUP 2026 HOSTS ===
def page52():
    body = header(52, 'V', 'World Cup 2026 host kits')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">The 2026 World Cup host nations — USA, Mexico, Canada — have already revealed their home and away kits for the expanded 48-team tournament.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">USA</h3>
    <p>Nike. Crest redesigned to evoke a shield. White home kit with subtle stars on the sleeves.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Mexico</h3>
    <p>Adidas. Iconic green home kit with a tonal Aztec-style graphic; red away.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Canada</h3>
    <p>Northern Reflections-inspired red home kit with a maple leaf motif and quote from the national anthem.</p>
  </div>
  <div>
    <div class="kit-display">
      <div class="kit-card">' + kit_svg('#FFFFFF', '#002868', label='USA') + '</div>
      <div class="kit-card">' + kit_svg('#168F49', '#FFFFFF', label='Mexico') + '</div>
      <div class="kit-card">' + kit_svg('#FF0000', '#FFFFFF', label='Canada') + '</div>
      <div class="kit-card">' + kit_svg('#002868', '#FFFFFF', label='USA away') + '</div>
      <div class="kit-card">' + kit_svg('#C8102E', '#FFFFFF', label='Mexico away') + '</div>
      <div class="kit-card">' + kit_svg('#000000', '#FFFFFF', label='Canada away') + '</div>
    </div>
    <div class="factbox navy" style="margin-top: 0.15in;">
      <div class="eyebrow">First time</div>
      <h3 style="font-size: 12pt; margin-top: 0.05in;">The 2026 World Cup will be the first ever hosted by three countries, the first with 48 teams, and the first in which the USA, Mexico, and Canada are joint hosts.</h3>
    </div>
  </div>
</div>
'''
    return page(52, 'World Cup 2026 host kits', body)

# === 53: ICONIC RETRO JERSEYS ===
def page53():
    body = header(53, 'V', 'Iconic retro jerseys')
    body += '''
<p class="lead" style="margin: 0.2in 0;">Six shirts that became cultural artefacts — defining decades and players.</p>

<div class="kit-display">
  <div class="kit-card">' + kit_svg('#108060', '#D71920', label='Mexico 1998') + '</div>
  <div class="kit-card">' + kit_svg('#FFFFFF', '#000000', label='Germany 1990') + '</div>
  <div class="kit-card">' + kit_svg('#001489', '#C8102E', label='France 1998') + '</div>
  <div class="kit-card">' + kit_svg('#FCD116', '#009C3B', label='Brazil 2002') + '</div>
  <div class="kit-card">' + kit_svg('#FFFFFF', '#000000', label='Argentina 1986') + '</div>
  <div class="kit-card">' + kit_svg('#FFCD00', '#DA291C', label='Spain 2010') + '</div>
</div>

<div class="two-col" style="margin-top: 0.2in;">
  <div>
    <div class="callout">
      <h3 style="font-size: 10pt;">The Brazil 2002 shirt</h3>
      <p style="font-size: 8.5pt; margin: 0;">Designed for the first World Cup after the Nike Rivalrio lost on penalties in 1998. Yellow base with deep-green hem and oversized Crazilian Football Confederation crest — worn in Ronaldo's three-goal final.</p>
    </div>
  </div>
  <div>
    <div class="factbox terracotta" style="margin-top: 0;">
      <div class="eyebrow">The "Denim" England 1996</h3>
      <h3 style="font-size: 12pt; margin-top: 0.05in;">Euro 96's Umbro England shirt — with the failed denim-collab reverse side — became the most-mocked shirt in English football. Originals sell for £200+ on resale.</h3>
    </div>
  </div>
</div>
'''
    return page(53, 'Iconic retro jerseys', body)

# === 54: KIT ECONOMICS ===
def page54():
    body = header(54, 'V', 'The economics of kit design')
    body += '''
<div class="two-col">
  <div>
    <p class="lead">A modern kit deal is one of the most lucrative commercial contracts in sport. Manchester United's 10-year adidas deal (2015–2025) was worth <b>£750m</b> — the largest kit sponsorship in football history.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">How the money flows</h3>
    <ul style="font-size: 9pt; margin-left: 0.3in; line-height: 1.5;">
      <li><b>Base fee</b> — annual payment (typically 3–8% of club revenue)</li>
      <li><b>Performance bonuses</b> — for winning trophies, qualifying for UCL</li>
      <li><b>Sales royalties</b> — 10–15% of replica kit sales</li>
      <li><b>Sponsor</b> — separate annual fee (shirt sponsor) often bigger than manufacturer</li>
    </ul>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">The big three manufacturers</h3>
    <table style="width: 100%; font-size: 8.5pt; border-collapse: collapse;">
      <tr style="background: var(--green); color: var(--paper);">
        <th style="padding: 0.06in 0.1in;">Brand</th>
        <th style="padding: 0.06in 0.1in;">Football teams</th>
        <th style="padding: 0.06in 0.1in;">Top deal</th>
      </tr>
      <tr><td style="padding: 0.06in 0.1in;"><b>Nike</b></td><td style="padding: 0.06in 0.1in;">~250 clubs + 25 nations</td><td style="padding: 0.06in 0.1in;">Barça €105m/yr</td></tr>
      <tr style="background: var(--paper-deep);"><td style="padding: 0.06in 0.1in;"><b>Adidas</b></td><td style="padding: 0.06in 0.1in;">~200 clubs + 20 nations</td><td style="padding: 0.06in 0.1in;">Man Utd £75m/yr</td></tr>
      <tr><td style="padding: 0.06in 0.1in;"><b>Puma</b></td><td style="padding: 0.06in 0.1in;">~150 clubs + 10 nations</td><td style="padding: 0.06in 0.1in;">Man City £65m/yr</td></tr>
    </table>
  </div>
  <div>
    <div class="factbox navy">
      <div class="eyebrow">Replica kit margins</div>
      <h3 style="font-size: 12pt; margin-top: 0.05in;">A £75 replica shirt costs the manufacturer <b>~£8</b> to produce. The club's 15% royalty is on the <b>£60 wholesale</b>, not the £75 retail — meaning the club makes ~£9 per shirt.</h3>
    </div>
    <div class="callout" style="margin-top: 0.2in;">
      <h3 style="font-size: 10pt;">The release cycle</h3>
      <p style="font-size: 8.5pt; margin: 0;">Top clubs release <b>3 kits per season</b>: home (May), away (June), third kit (September). Each kit's lifecycle is just <b>14 months</b> — a window designed to maximise replica sales.</p>
    </div>
    <div class="sidebar terracotta" style="margin-top: 0.2in;">
      <h3>Counterfeits</h3>
      <p style="font-size: 8.5pt;">Football is the most counterfeited product in sport. An estimated <b>1 in 5 replica shirts sold worldwide</b> is fake — Interpol seized €440M worth in 2024 alone.</p>
    </div>
  </div>
</div>
'''
    return page(54, 'Kit economics', body)

# Write all
pages = {
    45: page45(), 46: page46(), 47: page47(), 48: page48(),
    49: page49(), 50: page50(), 51: page51(), 52: page52(),
    53: page53(), 54: page54()
}
for num, html in pages.items():
    with open(f'{PAGES_DIR}/{num:02d}-page.html', 'w') as f:
        f.write(html)
print(f"Wrote pages 45-54: {len(pages)} files")