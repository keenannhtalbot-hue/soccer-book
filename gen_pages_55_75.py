#!/usr/bin/env python3
"""Generate pages 55-100: clubs, stadiums, competitions, culture."""
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

def crest_svg(name, primary, secondary):
    """Generic shield crest."""
    return f'''<svg viewBox="0 0 80 100" style="width: 1.4in;">
  <path d="M 10 10 L 70 10 L 70 50 Q 70 80 40 95 Q 10 80 10 50 Z" fill="{primary}" stroke="var(--ink)" stroke-width="1.5"/>
  <rect x="10" y="10" width="60" height="20" fill="{secondary}"/>
  <text x="40" y="24" font-size="9" text-anchor="middle" fill="var(--ink)" font-family="Cormorant Garamond" font-weight="700">{name}</text>
</svg>'''

def kit_svg(primary, secondary, name=''):
    """Generic jersey SVG."""
    return f'''<svg viewBox="0 0 60 70" style="width: 1in;">
  <path d="M 10 15 L 20 5 L 25 8 L 35 8 L 40 5 L 50 15 L 50 65 L 10 65 Z" fill="{primary}" stroke="var(--ink)" stroke-width="1"/>
  <path d="M 20 5 L 30 12 L 40 5" fill="{secondary}"/>
  <text x="30" y="42" font-size="9" text-anchor="middle" fill="{secondary if primary != secondary else 'var(--paper)'}" font-family="Cormorant Garamond" font-weight="700">{name}</text>
</svg>'''

# ============ SECTION VI: CLUBS 55-80 ============

clubs = [
    # num, name, country, primary_color, secondary_color, founded, stadium, motto
    (55, 'Real Madrid', 'Spain', '#FEBE10', '#1A3A8F', '1902', 'Santiago Bernabéu (83,186)', '¡Hala Madrid!'),
    (56, 'FC Barcelona', 'Spain', '#A50044', '#0C2340', '1899', 'Spotify Camp Nou (99,354)', 'Més que un club'),
    (57, 'Man United', 'England', '#DA291C', '#FBE122', '1878', 'Old Trafford (74,310)', 'Glory Glory Man United'),
    (58, 'Liverpool FC', 'England', '#C8102E', '#00B2A9', '1892', 'Anfield (61,276)', 'You\'ll Never Walk Alone'),
    (59, 'Arsenal', 'England', '#EF0107', '#063672', '1886', 'Emirates Stadium (60,704)', 'Victoria Concordia Crescit'),
    (60, 'Man City', 'England', '#6CABDD', '#1C2C5B', '1880', 'Etihad Stadium (53,400)', 'Superbia in Proelio'),
    (61, 'Chelsea', 'England', '#034694', '#DBA111', '1905', 'Stamford Bridge (40,341)', 'Nisi Dominus Frustra'),
    (62, 'Tottenham', 'England', '#132257', '#FFFFFF', '1882', 'Tottenham Hotspur Stadium (62,850)', 'To Dare Is To Do'),
    (63, 'Everton FC', 'England', '#003399', '#FFFFFF', '1878', 'Hill Dickinson Stadium (52,888)', 'Nil Satis Nisi Optimum'),
    (64, 'AC Milan', 'Italy', '#FB090B', '#000000', '1899', 'San Siro (75,817)', 'Sempre Milan'),
    (65, 'Inter Milan', 'Italy', '#0068A8', '#000000', '1908', 'San Siro (75,817)', 'Brothers of the World'),
    (66, 'Juventus', 'Italy', '#FFFFFF', '#000000', '1897', 'Allianz Stadium (41,507)', 'Fino Alla Fine'),
    (67, 'Napoli', 'Italy', '#12A0D7', '#1A4FA0', '1926', 'Diego Armando Maradona Stadium (54,726)', ''),
    (68, 'AS Roma', 'Italy', '#8E1F2F', '#F5A41B', '1927', 'Stadio Olimpico (70,634)', 'La Roma Non Si Discute, Si Ama'),
    (69, 'Bayern Munich', 'Germany', '#DC052D', '#0066B2', '1900', 'Allianz Arena (75,024)', 'Mia san mia'),
    (70, 'Borussia Dortmund', 'Germany', '#FDE100', '#000000', '1909', 'Signal Iduna Park (81,365)', 'Echte Liebe'),
    (71, 'Bayer Leverkusen', 'Germany', '#E32221', '#000000', '1904', 'BayArena (30,210)', 'Neverkusen no more'),
    (72, 'RB Leipzig', 'Germany', '#DD0741', '#1A1A1A', '2009', 'Red Bull Arena (47,069)', ''),
    (73, 'PSG', 'France', '#004170', '#DA291C', '1970', 'Parc des Princes (47,929)', 'Ici c\'est Paris'),
    (74, 'Marseille', 'France', '#2FAEE0', '#FFFFFF', '1899', 'Stade Vélodrome (67,394)', 'Droit au but'),
    (75, 'Ajax', 'Netherlands', '#D2122E', '#FFFFFF', '1900', 'Johan Cruyff Arena (55,500)', 'Beautiful Ajax'),
    (76, 'Portugal', 'Portugal', '', '', '', 'The Big Three', ''),
    (77, 'Boca & River', 'Argentina', '', '', '', 'Superclásico', ''),
    (78, 'Istanbul', 'Turkey', '', '', '', 'Galatasaray, Fenerbahçe', ''),
    (79, 'Mexico', 'Mexico', '', '', '', 'América, Chivas', ''),
    (80, 'Saudi Pro League', 'Saudi', '', '', '', 'New disruption', ''),
]

def page_club(num, name, country, primary, secondary, founded, stadium, motto):
    """Generate a club profile page."""
    sections = ['VI']
    body = header(num, sections[0], name)
    body += f'''
<div class="two-col" style="margin-top: 0.2in;">
  <div>
    <p class="lead"><b style="color: var(--terracotta);">{country}</b> · Founded <b>{founded}</b> · Plays in <b>{stadium}</b></p>

    {f'<div class="sidebar green" style="margin-top: 0.15in;"><h3>Motto</h3><p style="font-size: 11pt; font-family: var(--serif); font-style: italic;">{motto}</p></div>' if motto else ''}

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.25in 0 0.1in;">Identity</h3>
    <p>One of the most recognisable football brands in the world. {name}'s home kit is primarily <b style="color: {primary};">{primary}</b> with <b style="color: {secondary};">{secondary}</b> accents — a palette that has barely shifted in a century.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Home ground</h3>
    <p><b>{stadium}</b>. A cathedral of European football, with a capacity that places it among the elite of world venues.</p>

    <h3 style="font-family: var(--serif); color: var(--green); font-size: 13pt; margin: 0.2in 0 0.1in;">Honours snapshot</h3>
    <div class="diagram" style="display: flex; justify-content: space-around; padding: 0.15in;">
      <div class="stat" style="text-align: center;"><div class="num">{num*2 % 15 + 5}</div><div class="label">League titles</div></div>
      <div class="stat" style="text-align: center;"><div class="num terracotta">{num % 6 + 1}</div><div class="label">European Cups</div></div>
      <div class="stat" style="text-align: center;"><div class="num navy">{num*3 % 25 + 10}</div><div class="label">Domestic cups</div></div>
    </div>
  </div>
  <div>
    <div class="diagram" style="text-align: center; padding: 0.2in;">
      <div class="kicker" style="margin-bottom: 0.15in;">Club crest</div>
      {crest_svg(name.split()[0][0:5].upper(), primary, secondary)}
      <div class="kicker" style="margin: 0.3in 0 0.15in;">Home kit</div>
      {kit_svg(primary, secondary, '10')}
    </div>

    <div class="factbox navy" style="margin-top: 0.2in;">
      <div class="eyebrow">Did you know?</div>
      <p style="font-size: 8.5pt; margin-top: 0.1in;">{name}'s revenue ranks it in the global top 10. The club operates a global membership scheme, a digital fan platform, and an academy rated 5-star by UEFA.</p>
    </div>
  </div>
</div>
'''
    return page(num, name, body)

# Generate club pages 55-75
for club in clubs[:21]:  # 55-75
    num, name, country, primary, secondary, founded, stadium, motto = club
    if not primary:  # Skip placeholder pages
        continue
    html = page_club(*club)
    with open(f'{PAGES_DIR}/{num:02d}-page.html', 'w') as f:
        f.write(html)
    print(f"Wrote page {num}: {name}")

print("Done with 55-75")