#!/usr/bin/env python3
"""Fix pages 45-54: properly call kit_svg() and emit rendered SVGs."""
import os

PAGES_DIR = '/home/kbot/soccer-book/pages'

# Pre-rendered kit SVG (jersey with collar, sleeves, number)
def kit_svg(primary, secondary, number='10', label=''):
    label_color = secondary if primary.lower() != secondary.lower() else 'white'
    return f'''<svg viewBox="0 0 180 220" style="width: 1in; aspect-ratio: 9/11;">
  <path d="M 35 25 L 55 5 L 75 18 L 105 18 L 125 5 L 145 25 L 165 35 L 165 200 L 15 200 L 15 35 Z" fill="{primary}" stroke="var(--ink)" stroke-width="1.5"/>
  <path d="M 60 5 Q 75 12 90 12 Q 105 12 120 5 L 115 8 L 105 5 L 90 8 L 75 5 L 65 8 Z" fill="{secondary}"/>
  <text x="90" y="115" font-size="22" text-anchor="middle" fill="{label_color}" font-family="Cormorant Garamond" font-weight="700">{number}</text>
  <text x="90" y="200" font-size="6" text-anchor="middle" fill="var(--ink-mute)" font-family="Inter" font-weight="600">{label}</text>
</svg>'''

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

def kit_card(primary, secondary, label):
    return f'<div class="kit-card">{kit_svg(primary, secondary, label=label)}</div>'

# === PAGE 45: ANATOMY ===
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
      <path d="M 35 30 L 60 8 L 75 18 L 125 18 L 140 8 L 165 30 L 185 45 L 185 200 L 15 200 L 15 45 Z" fill="var(--terracotta)" stroke="var(--ink)" stroke-width="1.5"/>
      <g stroke="rgba(0,0,0,0.15)" stroke-width="0.4">
        <line x1="20" y1="60" x2="180" y2="60"/><line x1="20" y1="80" x2="180" y2="80"/>
        <line x1="20" y1="100" x2="180" y2="100"/><line x1="20" y1="120" x2="180" y2="120"/>
        <line x1="20" y1="140" x2="180" y2="140"/><line x1="20" y1="160" x2="180" y2="160"/>
      </g>
      <path d="M 60 8 Q 75 16 90 16 Q 105 16 120 8" fill="var(--ink)"/>
      <circle cx="155" cy="55" r="10" fill="var(--gold)" stroke="var(--ink)" stroke-width="1"/>
      <text x="155" y="58" font-size="6" text-anchor="middle" fill="var(--ink)" font-weight="700">CREST</text>
      <text x="100" y="135" font-size="32" text-anchor="middle" fill="white" font-family="Cormorant Garamond" font-weight="700">10</text>
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

# === PAGE 46: PL KITS ===
def page46():
    body = header(46, 'V', 'Premier League kits, 2024/25')
    body += '''
<p class="lead" style="margin: 0.2in 0;">Home kits of the 20 Premier League clubs — the standard away-day wardrobe of the global game.</p>

<div class="kit-display">
''' + kit_card('#DA291C', '#FBE122', 'Man Utd') + kit_card('#C8102E', '#00B2A9', 'Liverpool') + kit_card('#EF0107', '#063672', 'Arsenal') + '''
''' + kit_card('#6CABDD', '#1C2C5B', 'Man City') + kit_card('#034694', '#FFFFFF', 'Chelsea') + kit_card('#132257', '#FFFFFF', 'Tottenham') + '''
''' + kit_card('#003399', '#FFFFFF', 'Everton') + kit_card('#000000', '#E32221', 'Aston Villa') + kit_card('#1B458F', '#FFFFFF', 'Brighton') + '''
''' + kit_card('#006FB7', '#FFFFFF', 'Newcastle') + kit_card('#EE2737', '#FFFFFF', 'Nottm Forest') + kit_card('#005CAB', '#FFFFFF', 'Crystal Palace') + '''
''' + kit_card('#FDB913', '#1D428A', 'Wolves') + kit_card('#D71920', '#FFFFFF', 'Brentford') + kit_card('#FFCD00', '#000000', 'Watford') + '''
''' + kit_card('#BD1F23', '#F4A91D', 'Brentford') + kit_card('#D00027', '#FFFFFF', 'Ipswich') + kit_card('#1A1A1A', '#FFFFFF', 'Fulham') + '''
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

# === PAGE 47: LA LIGA ===
def page47():
    body = header(47, 'V', 'La Liga kits, 2024/25')
    body += '''
<p class="lead" style="margin: 0.2in 0;">Home kits from Spain's top flight — the most recognisable colour palette in world football.</p>

<div class="kit-display">
''' + kit_card('#FFFFFF', '#FEBE10', 'Real Madrid') + kit_card('#A50044', '#0C2340', 'Barcelona') + kit_card('#CB3524', '#FFFFFF', 'Atlético') + '''
''' + kit_card('#EE3522', '#1A3A8F', 'Athletic') + kit_card('#0067B1', '#FFFFFF', 'R Sociedad') + kit_card('#FB090B', '#000000', 'Sevilla') + '''
''' + kit_card('#FFB800', '#FFFFFF', 'Villarreal') + kit_card('#FFFFFF', '#006633', 'R Betis') + kit_card('#BB1F1F', '#FFFFFF', 'Osasuna') + '''
''' + kit_card('#0E2D5F', '#FFFFFF', 'Espanyol') + kit_card('#7B1F2A', '#FFFFFF', 'Mallorca') + kit_card('#003DA5', '#FFFFFF', 'Deportivo') + '''
</div>

<div class="callout" style="margin-top: 0.2in;">
  <h3 style="font-size: 10pt;">The El Clásico</h3>
  <p style="font-size: 8.5pt; margin: 0;">Two iconic shirts, two famous colour codes. Real Madrid white = <i>la camiseta blanca</i>; Barcelona blaugrana = <i>barça</i>. Both have barely changed in 100 years.</p>
</div>
'''
    return page(47, 'La Liga kits', body)

# === PAGE 48: SERIE A ===
def page48():
    body = header(48, 'V', 'Serie A kits, 2024/25')
    body += '''
<p class="lead" style="margin: 0.2in 0;">Italian football's home kits — stripes, checks, and the iconic <i>Nerazzurri</i>.</p>

<div class="kit-display">
''' + kit_card('#FB090B', '#000000', 'AC Milan') + kit_card('#0068A8', '#000000', 'Inter') + kit_card('#FFFFFF', '#000000', 'Juventus') + '''
''' + kit_card('#12A0D7', '#1A4FA0', 'Napoli') + kit_card('#8E1F2F', '#F5A41B', 'AS Roma') + kit_card('#A39161', '#FFFFFF', 'Atalanta') + '''
''' + kit_card('#E50914', '#1F1F1F', 'Bologna') + kit_card('#7A2239', '#FFFFFF', 'Torino') + kit_card('#9C1B2F', '#FFFFFF', 'Fiorentina') + '''
''' + kit_card('#003F7F', '#FFFFFF', 'Lazio') + kit_card('#FFC72C', '#1A1A1A', 'Genoa') + kit_card('#FFC20E', '#1B458F', 'Lecce') + '''
</div>

<div class="callout" style="margin-top: 0.2in;">
  <h3 style="font-size: 10pt;">The Milan Derby</h3>
  <p style="font-size: 8.5pt; margin: 0;">The <b>Derby della Madonnina</b> pairs two iconic shirts: AC Milan's <i>Rossoneri</i> red-black stripes vs Inter's <i>Nerazzurri</i> blue-black stripes. Same stadium, very different stories.</p>
</div>
'''
    return page(48, 'Serie A kits', body)

# === PAGE 49: BUNDESLIGA ===
def page49():
    body = header(49, 'V', 'Bundesliga kits, 2024/25')
    body += '''
<p class="lead" style="margin: 0.2in 0;">Germany's top flight — cleaner designs, simpler palettes, more historic clubs.</p>

<div class="kit-display">
''' + kit_card('#DC052D', '#0066B2', 'Bayern') + kit_card('#FDE100', '#000000', 'Dortmund') + kit_card('#E32221', '#000000', 'Leverkusen') + '''
''' + kit_card('#DD0741', '#1A1A1A', 'RB Leipzig') + kit_card('#000000', '#FFFFFF', 'Frankfurt') + kit_card('#108060', '#FFFFFF', 'Werder') + '''
''' + kit_card('#003090', '#FFFFFF', 'HSV') + kit_card('#1976D2', '#FFFFFF', 'Hertha') + kit_card('#006F51', '#FFFFFF', 'Wolfsburg') + '''
''' + kit_card('#009FE3', '#000000', 'Hoffenheim') + kit_card('#E30613', '#FFFFFF', 'Stuttgart') + kit_card('#D71920', '#000000', 'Freiburg') + '''
</div>

<div class="callout" style="margin-top: 0.2in;">
  <h3 style="font-size: 10pt;">The Yellow Wall</h3>
  <p style="font-size: 8.5pt; margin: 0;">Dortmund's iconic yellow shirt — paired with the steep Sudtribüne stand — creates one of football's most distinctive match-day images. Every home game sells out within minutes of tickets going on sale.</p>
</div>
'''
    return page(49, 'Bundesliga kits', body)

# === PAGE 50: LIGUE 1 ===
def page50():
    body = header(50, 'V', 'Ligue 1 kits, 2024/25')
    body += '''
<p class="lead" style="margin: 0.2in 0;">French football — one dominant PSG, then everyone else. The kits reflect the league's stylistic range.</p>

<div class="kit-display">
''' + kit_card('#004170', '#DA291C', 'PSG') + kit_card('#2FAEE0', '#FFFFFF', 'Marseille') + kit_card('#D71920', '#FFFFFF', 'Lille') + '''
''' + kit_card('#C71F2A', '#FFFFFF', 'Lyon') + kit_card('#0066CC', '#FFFFFF', 'Monaco') + kit_card('#FFFFFF', '#1B458F', 'Nice') + '''
''' + kit_card('#006633', '#FFFFFF', 'St-Étienne') + kit_card('#FFC20E', '#1B458F', 'Lens') + kit_card('#000000', '#FFD700', 'Rennes') + '''
''' + kit_card('#7B1F2A', '#FFFFFF', 'Strasbourg') + kit_card('#FFFFFF', '#000000', 'Nantes') + kit_card('#1A1A1A', '#F08080', 'Reims') + '''
</div>

<div class="callout" style="margin-top: 0.2in;">
  <h3 style="font-size: 10pt;">The Le Classique</h3>
  <p style="font-size: 8.5pt; margin: 0;">PSG vs Marseille — France's biggest fixture. PSG's Hechter stripe vs OM's cyan-white. A rivalry that has occasionally spilled beyond football.</p>
</div>
'''
    return page(50, 'Ligue 1 kits', body)

# === PAGE 51: MLS ===
def page51():
    body = header(51, 'V', 'MLS kits, 2024/25')
    body += '''
<p class="lead" style="margin: 0.2in 0;">Major League Soccer is now the most-watched football league in the USA, with 30 clubs across the US and Canada.</p>

<div class="kit-display">
''' + kit_card('#00205B', '#C8102E', 'LAFC') + kit_card('#000000', '#FFFFFF', 'Galaxy') + kit_card('#A6192E', '#FFFFFF', 'Inter Miami') + '''
''' + kit_card('#012169', '#FFFFFF', 'NYCFC') + kit_card('#DC2626', '#FFFFFF', 'Chicago') + kit_card('#3D8BFD', '#FFFFFF', 'Atlanta') + '''
''' + kit_card('#5F1E20', '#FFFFFF', 'Portland') + kit_card('#FCD619', '#01509A', 'Charlotte') + kit_card('#E03A3E', '#012169', 'NE Revs') + '''
''' + kit_card('#FFFFFF', '#00843D', 'Seattle') + kit_card('#B3001B', '#006F51', 'Toronto') + kit_card('#0085CA', '#FFFFFF', 'Vancouver') + '''
</div>

<div class="callout" style="margin-top: 0.2in;">
  <h3 style="font-size: 10pt;">The Messi effect</h3>
  <p style="font-size: 8.5pt; margin: 0;">Inter Miami's pink-and-black kit became the most-sold replica shirt in North American sports history after Lionel Messi joined in July 2023 — selling 1.2M units in the first 6 months.</p>
</div>
'''
    return page(51, 'MLS kits', body)

# === PAGE 52: WC 2026 HOSTS ===
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
''' + kit_card('#FFFFFF', '#002868', 'USA') + kit_card('#168F49', '#FFFFFF', 'Mexico') + kit_card('#FF0000', '#FFFFFF', 'Canada') + '''
''' + kit_card('#002868', '#FFFFFF', 'USA away') + kit_card('#C8102E', '#FFFFFF', 'Mexico away') + kit_card('#000000', '#FFFFFF', 'Canada away') + '''
    </div>
    <div class="factbox navy" style="margin-top: 0.15in;">
      <div class="eyebrow">First time</div>
      <h3 style="font-size: 12pt; margin-top: 0.05in;">The 2026 World Cup will be the first ever hosted by three countries, the first with 48 teams, and the first in which the USA, Mexico, and Canada are joint hosts.</h3>
    </div>
  </div>
</div>
'''
    return page(52, 'World Cup 2026 host kits', body)

# === PAGE 53: ICONIC RETRO ===
def page53():
    body = header(53, 'V', 'Iconic retro jerseys')
    body += '''
<p class="lead" style="margin: 0.2in 0;">Six shirts that became cultural artefacts — defining decades and players.</p>

<div class="kit-display">
''' + kit_card('#108060', '#D71920', 'Mexico 1998') + kit_card('#FFFFFF', '#000000', 'Germany 1990') + kit_card('#001489', '#C8102E', 'France 1998') + '''
''' + kit_card('#FCD116', '#009C3B', 'Brazil 2002') + kit_card('#FFFFFF', '#000000', 'Argentina 1986') + kit_card('#FFCD00', '#DA291C', 'Spain 2010') + '''
''' + kit_card('#005CAB', '#E3000F', 'France 2018') + kit_card('#8C2633', '#FFFFFF', 'Portugal 2016') + kit_card('#FFB300', '#00843D', 'Netherlands 1974') + '''
</div>

<div class="two-col" style="margin-top: 0.2in;">
  <div>
    <div class="callout">
      <h3 style="font-size: 10pt;">The Brazil 2002 shirt</h3>
      <p style="font-size: 8.5pt; margin: 0;">Designed for the first World Cup after the <i>Rivaldo</i>-led Brazil lost on penalties in 1998. Yellow base with deep-green hem and oversized Crazilian Football Confederation crest — worn in Ronaldo's three-goal final.</p>
    </div>
  </div>
  <div>
    <div class="factbox terracotta" style="margin-top: 0;">
      <div class="eyebrow">The "Denim" England 1996</div>
      <h3 style="font-size: 12pt; margin-top: 0.05in;">Euro 96's Umbro England shirt — with the failed denim-collab reverse side — became the most-mocked shirt in English football. Originals sell for £200+ on resale.</h3>
    </div>
  </div>
</div>
'''
    return page(53, 'Iconic retro jerseys', body)

# === PAGE 54: KIT ECONOMICS ===
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
    print(f"Wrote page {num}")

# Verify
import subprocess
result = subprocess.run(['grep', '-c', 'kit_svg(', f'{PAGES_DIR}/46-page.html'], capture_output=True, text=True)
print(f"\n'kit_svg(' literal count in 46-page.html: {result.stdout.strip()} (should be 0)")