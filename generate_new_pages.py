"""generate_new_pages.py — Add 25 new pages (201-225) to the soccer book.

Sections:
  201-205: World Cup / GOAT debate / Famous finals / Famous derbies / Kit numbers (Section XIII)
  206-215: Player profiles top-5 by position (Section XIV)
  216-220: Tactical philosophies (Section XV)
  221-225: Modern football issues (Section XVI)
"""

import os

os.chdir('/home/kbot/soccer-book')


def page(num, section_num, title, body_html, body_class='standard'):
    """Generate a flat HTML page in the project's style."""
    pad = str(num).zfill(3 if num >= 100 else 2)
    return f'''<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>Page {num} — {title}</title><link rel="stylesheet" href="book.css"></head>
<body class="page {body_class}"><div class="page-inner">
<div class="page-header">
  <div class="page-num">{num}</div>
  <div><div class="section-num">{section_num}</div><h1 class="section-title">{title}</h1></div>
</div>
{body_html}
</div></body></html>
'''


def write_page(num, section_num, title, body_html, body_class='standard'):
    fn = f'pages/{num:03d}-page.html'
    with open(fn, 'w') as f:
        f.write(page(num, section_num, title, body_html, body_class))
    print(f'wrote {fn}')


# ============================================================================
# SECTION XIII: World Cups & the GOAT debate  (201-205)
# ============================================================================

write_page(201, 'Section XIII', 'World Cup history, 1930–2026',
'''<div class="two-col">
  <div>
    <p class="lead">Twenty-three tournaments. Eight decades. One trophy every four years. The World Cup is the most-watched event on Earth — every final draws <b>1.5+ billion viewers</b>.</p>

    <p>The tournament has been won by <b>eight nations</b> in total: Brazil leads with five, Germany and Italy have four each, Argentina three, France two, and Spain, England and Uruguay one apiece. Of those 96 trophies in men's and women's football, the women's competition started in 1991 and the US has won four, Germany two, Norway one, Japan one, and Spain one.</p>

    <p>The 2026 World Cup will be the largest ever — <b>48 teams, 104 matches</b> across the United States, Canada, and Mexico. The final returns to <b>MetLife Stadium</b> in New Jersey on July 19, 2026.</p>

    <div class="sidebar green">
      <h3>The Maracanazo (1950)</h3>
      <p style="font-size: 8.5pt;"><b>Uruguay 2 – 1 Brazil.</b> 199,854 people in the Maracanã — the largest crowd ever for a football match. Brazil needed only a draw but lost. The defeat is still referred to in Brazil as <i>"o Maracanaço."</i></p>
    </div>
  </div>
  <div>
    <div class="timeline">
      <div class="timeline-event"><div class="year">1930</div>Uruguay hosts and wins the first World Cup, beating Argentina 4–2 in the final.</div>
      <div class="timeline-event"><div class="year">1950</div>Uruguay win again at home in Brazil — the Maracanazo.</div>
      <div class="timeline-event"><div class="year">1958</div>Pelé, 17, scores twice in the final. Brazil's first title.</div>
      <div class="timeline-event"><div class="year">1966</div>England win at home. Geoff Hurst becomes the only hat-trick scorer in a final.</div>
      <div class="timeline-event"><div class="year">1970</div>Brazil's third title and the birth of <i>"Jogo Bonito."</i> Pelé, Jairzinho, Gérson, Tostão, Carlos Alberto.</div>
      <div class="timeline-event"><div class="year">1986</div>Maradona's Hand of God + Goal of the Century. Argentina beat West Germany in the final.</div>
      <div class="timeline-event"><div class="year">1998</div>Zinedine Zidane scores twice in the final for France vs. Brazil. The Ronaldo mystery.</div>
      <div class="timeline-event"><div class="year">2010</div>Spain win their first, Iniesta's extra-time strike at Soccer City.</div>
      <div class="timeline-event"><div class="year">2014</div>Germany thrash Brazil 7–1 in the semi-final. Götze wins the final in extra time.</div>
      <div class="timeline-event"><div class="year">2022</div>Messi leads Argentina past France in the all-time classic final — 3–3, penalties.</div>
      <div class="timeline-event"><div class="year">2026</div>48 teams. The United bid. Hosted across the USA, Canada, Mexico.</div>
    </div>
  </div>
</div>
''', 'howto')


write_page(202, 'Section XIII', 'The GOAT debate',
'''<div class="two-col">
  <div>
    <p class="lead">The Greatest Of All Time conversation has consumed football since Pelé retired in 1971. <b>Four names</b> dominate any honest debate, and each measures greatness by a different scale.</p>

    <p>By goals: <b>Cristiano Ronaldo</b> (900+) leads every men's footballer, dead or alive. By World Cups: <b>Pelé</b> (three titles, two as a teenager). By peak: <b>Maradona</b> at the 1986 World Cup, which no individual has matched. By completeness at the highest level: <b>Messi</b>, eight Ballons d'Or, two Copa Américas, one World Cup.</p>

    <p>The women's GOAT conversation has its own canon: <b>Marta</b> (Brazil) holds the all-time World Cup goal record (17 in five tournaments); <b>Ada Hegerberg</b> (Norway) was the first Ballon d'Or winner; <b>Alexia Putellas</b> (Spain) and <b>Alex Morgan</b> (USA) are each named alongside her.</p>
  </div>
  <div>
    <div class="factbox terracotta">
      <div class="eyebrow">By the numbers</div>
      <div style="display:grid; grid-template-columns: 1fr 1fr; gap: 0.2in; margin-top: 0.15in;">
        <div>
          <h3 style="color: var(--green); font-size: 14pt; margin: 0;">Pelé</h3>
          <p style="font-size: 9pt;"><b>1281 goals</b> in 1363 games (Santos + Brazil + NY Cosmos) · 3 World Cups (1958/62/70) · 2x Libertadores</p>
        </div>
        <div>
          <h3 style="color: var(--terracotta); font-size: 14pt; margin: 0;">Maradona</h3>
          <p style="font-size: 9pt;">"Hand of God" + Goal of the Century, 1986 · 2 Serie A titles with Napoli · club-record transfer</p>
        </div>
        <div>
          <h3 style="color: var(--navy); font-size: 14pt; margin: 0;">Messi</h3>
          <p style="font-size: 9pt;"><b>8 Ballons d'Or</b> · 4 Champions Leagues · 2022 World Cup · 2023 Copa América · 2 Leagues Cups</p>
        </div>
        <div>
          <h3 style="color: var(--rust); font-size: 14pt; margin: 0;">Ronaldo</h3>
          <p style="font-size: 9pt;"><b>900+ goals</b> (all-time record) · 5 Champions Leagues · Euro 2016 · 5 Ballons d'Or</p>
        </div>
      </div>
    </div>

    <div class="sidebar terracotta">
      <h3>What "best" actually means</h3>
      <p style="font-size: 8.5pt;">Different metrics produce different winners. <b>Goals per 90</b>: Mbappé. <b>Trophies won</b>: Messi. <b>Longevity</b>: Ronaldo. <b>Peak rating</b>: Maradona. <b>Big-game moments</b>: Pelé.</p>
      <p style="font-size: 8.5pt; margin-top: 0.1in;">Most football historians now consider <b>Pelé vs Maradona vs Messi</b> the central triangle, with Ronaldo the all-time top scorer but the highest-volume scorer in a different era.</p>
    </div>
  </div>
</div>
''', 'standard')


write_page(203, 'Section XIII', 'The greatest finals',
'''<div class="three-col">
  <div class="sidebar green">
    <h3>1966 · Wembley</h3>
    <p style="font-size: 8.5pt;"><b>England 4 – 2 West Germany</b> (aet). Hurst completes the only hat-trick in a World Cup final. The linesman flags a Geoff Hurst shot that bounced off the underside of the bar — still debated.</p>
  </div>
  <div class="sidebar terracotta">
    <h3>1970 · Mexico City</h3>
    <p style="font-size: 8.5pt;"><b>Brazil 4 – 1 Italy.</b> The peak of <i>Jogo Bonito.</i> Carlos Alberto's fourth goal — finished off a 7-pass move that started with Pelé's dummy goalkeeper clearance.</p>
  </div>
  <div class="sidebar navy">
    <h3>1986 · Azteca</h3>
    <p style="font-size: 8.5pt;"><b>Argentina 3 – 2 West Germany.</b> Maradona's two goals against England earlier in the tournament — the Hand of God and the Goal of the Century — are the reference points.</p>
  </div>
  <div class="sidebar green">
    <h3>2005 · Istanbul</h3>
    <p style="font-size: 8.5pt;"><b>AC Milan 3 – 3 Liverpool</b> (Liverpool win 3–2 on pens). 3–0 down at half-time. Gerrard, Šmicer, Alonso. Dudek's double save from Shevchenko.</p>
  </div>
  <div class="sidebar terracotta">
    <h3>1999 · Barcelona</h3>
    <p style="font-size: 8.5pt;"><b>Man United 2 – 1 Bayern Munich.</b> Solskjær's late winner in injury time. The Treble.</p>
  </div>
  <div class="sidebar navy">
    <h3>2014 · Maracanã</h3>
    <p style="font-size: 8.5pt;"><b>Germany 1 – 0 Argentina</b> (aet). Götze's control-and-finish in the 113th minute after a clinical Kroos-Schürrle counter.</p>
  </div>
  <div class="sidebar green">
    <h3>2022 · Lusail</h3>
    <p style="font-size: 8.5pt;"><b>Argentina 3 – 3 France</b> (Argentina win 4–2 on pens). Mbappé hat-trick. Scaloni's men complete the greatest individual World Cup story.</p>
  </div>
  <div class="sidebar terracotta">
    <h3>2010 · Soweto</h3>
    <p style="font-size: 8.5pt;"><b>Spain 1 – 0 Netherlands</b> (aet). Iniesta's goal in the 116th minute. The harshest red card in finals history — Heitinga.</p>
  </div>
  <div class="sidebar navy">
    <h3>2006 · Berlin</h3>
    <p style="font-size: 8.5pt;"><b>Italy 1 – 1 France</b> (Italy win 5–3 on pens). Materazzi's headbutt of Zidane, Zidane's red card in his last game.</p>
  </div>
  <div class="sidebar green">
    <h3>2018 · Luzhniki</h3>
    <p style="font-size: 8.5pt;"><b>France 4 – 2 Croatia.</b> Griezmann, Pogba, Mbappé's first World Cup final goal at 19. The end of the Balkan underdog story.</p>
  </div>
  <div class="sidebar terracotta">
    <h3>1990 · Rome</h3>
    <p style="font-size: 8.5pt;"><b>West Germany 1 – 0 Argentina.</b> Brehme's controversial penalty. The ugliest, most-watched final in history.</p>
  </div>
  <div class="sidebar navy">
    <h3>1982 · Madrid</h3>
    <p style="font-size: 8.5pt;"><b>Italy 3 – 1 West Germany.</b> Paolo Rossi's hat-trick. Tardelli's scream. Cabrini's run.</p>
  </div>
</div>
''', 'standard')


write_page(204, 'Section XIII', 'The great derbies',
'''<div class="two-col">
  <div>
    <p class="lead">Football's oldest rivalries are rarely about football alone. Religion, class, geography, industry — the derby is the city in 90 minutes.</p>

    <p>The <b>Old Firm</b> (Celtic vs Rangers) is rooted in the religious and political division of Glasgow. <b>El Clásico</b> (Real Madrid vs Barcelona) became the political theatre of Catalonia vs Castile. <b>The Superclásico</b> is Argentina's Boca vs River — the <b>Bombonera</b> against the <b>Monumental</b>. <b>The North London Derby</b> is Arsenal vs Tottenham — rivalry by postcode.</p>

    <p>Lesser-known but worth a lifetime of study: <b>the Cairo derby</b> (Al Ahly vs Zamalek), <b>the Istanbul derby</b> (Galatasaray vs Fenerbahçe), <b>the Rome derby</b> (Roma vs Lazio), <b>the Milan derby</b> (Inter vs AC), and <b>the Belgrade eternal derby</b> (Red Star vs Partizan).</p>
  </div>
  <div>
    <div class="factbox green">
      <div class="eyebrow">The five global derbies</div>
      <div style="display:grid; grid-template-columns: 1fr; gap: 0.15in; margin-top: 0.2in;">
        <div>
          <h3 style="font-size: 12pt; margin: 0 0 0.05in; color: var(--terracotta);">El Clásico</h3>
          <p style="font-size: 9pt;"><b>Real Madrid vs Barcelona</b>. The most-watched club match in football — 600+ million global viewers. The political, cultural, and stylistic centre of the world's biggest league.</p>
        </div>
        <div>
          <h3 style="font-size: 12pt; margin: 0 0 0.05in; color: var(--navy);">Old Firm</h3>
          <p style="font-size: 9pt;"><b>Celtic vs Rangers.</b> 400+ matches since 1888. The religious divide (Catholic vs Protestant) maps directly onto Scottish football.</p>
        </div>
        <div>
          <h3 style="font-size: 12pt; margin: 0 0 0.05in; color: var(--green);">Superclásico</h3>
          <p style="font-size: 9pt;"><b>Boca Juniors vs River Plate.</b> Copa Libertadores Superclásico in 2018 was moved to Madrid after crowd trouble at the Santiago Bernabéu.</p>
        </div>
        <div>
          <h3 style="font-size: 12pt; margin: 0 0 0.05in; color: var(--gold);">Manchester Derby</h3>
          <p style="font-size: 9pt;"><b>Man United vs Man City.</b> Once a yawning gulf — now the tightest rivalry in England. Rooney's bicycle kick (2011), Kompany's stunner (2019).</p>
        </div>
        <div>
          <h3 style="font-size: 12pt; margin: 0 0 0.05in; color: var(--rust);">North London Derby</h3>
          <p style="font-size: 9pt;"><b>Arsenal vs Tottenham.</b> The 1888 founding of Spurs as a club for southern Middlesex — explicitly as an antidote to Woolwich Arsenal's northern bias.</p>
        </div>
      </div>
    </div>
  </div>
</div>
''', 'standard')


write_page(205, 'Section XIII', 'Shirt number traditions',
'''<div class="two-col">
  <div>
    <p class="lead">A shirt number is a position, a heritage, a superstition, an inheritance. In an era of squad numbers, the legendary numbers still carry weight.</p>

    <p>The <b>number 10</b> is the playmaker. Pelé, Maradona, Zidane, Messi — they all wore it (or its modern equivalent). The <b>number 9</b> is the striker. Ronaldo at United, Suárez at Liverpool, Lewandowski at Bayern. The <b>number 7</b> is the wide forward or the explosive winger — Beckham, Cristiano, Mbappé. The <b>number 14</b> is the late substitute turned legend — Mertesacker, Thierry Henry, Xabi Alonso.</p>

    <p>In Italy and Spain, the numbering follows formation order: GK wears 1, defenders start at 2, midfielders at 6, attackers at 9, playmaker at 10. In England and France, numbers 1–11 are still worn in almost every squad.</p>
  </div>
  <div>
    <div class="factbox navy">
      <div class="eyebrow">Iconic numbers</div>
      <div class="stat-block">
        <div><div class="stat-label">No. 1 — Goalkeeper</div>Buffon (Italy), Neuer (Germany), Casillas (Spain), Yashin (USSR)</div>
        <div><div class="stat-label">No. 3 — Left-back</div>Maldini (Italy), Roberto Carlos (Brazil), Cole (England)</div>
        <div><div class="stat-label">No. 4 — Midfield engine</div>Moore (England), Beckenbauer (Germany), Gerrard (Liverpool)</div>
        <div><div class="stat-label">No. 6 — Holding midfielder</div>Busquets (Spain), Makelele (Chelsea/Real), Pirlo (Italy)</div>
        <div><div class="stat-label">No. 7 — Wide forward</div>Beckham, Cristiano, Mbappé, Cantona, Best</div>
        <div><div class="stat-label">No. 9 — Striker</div>Ronaldo, Suárez, Lewandowski, Inzaghi, Henry</div>
        <div><div class="stat-label">No. 10 — Playmaker</div>Pelé, Maradona, Zidane, Messi, Baggio</div>
        <div><div class="stat-label">No. 14 — The bench hero</div>Thierry Henry, Mertesacker, Xabi Alonso, Gerd Müller</div>
      </div>
    </div>
  </div>
</div>
''', 'standard')


# ============================================================================
# SECTION XIV: Top-5 by position  (206-215)
# ============================================================================

def top5_page(num, title, lead, role_html, names):
    body = f'''<div class="two-col">
  <div>
    <p class="lead">{lead}</p>
    <p>What follows is <b>opinionated</b> — a starting five, with a runner-up. The criteria include era, longevity, peak, contribution to the team, and influence on how the position is played today. Production stats matter less than <b>the things they couldn't teach</b>.</p>
    <div class="sidebar terracotta">
      <h3>What we chose for</h3>
      <p style="font-size: 8.5pt;">A modern top 5 should include players from at least three different eras, at least one who set the standard for their generation, and at least one whose prime overlapped with another member of the list — those who dominated the same era provide the strongest comparison.</p>
    </div>
  </div>
  <div>
    <div class="factbox green">
      <div class="eyebrow">Top 5 {title.lower()}</div>
{names}
    </div>
  </div>
</div>'''
    write_page(num, 'Section XIV', f'Top 5 · {title.lower()}', body, 'standard')


# Build the names
ranked = {
    'Goalkeeper': '''
        <ol style="font-family: var(--serif); font-size: 12pt; line-height: 1.7; padding-left: 0.3in;">
          <li><b>Gianluigi Buffon</b> · Italy / Parma, Juventus · 200 records across position · 1,150+ career appearances</li>
          <li><b>Manuel Neuer</b> · Germany / Schalke, Bayern · redefined the sweeper-keeper role</li>
          <li><b>Lev Yashin</b> · USSR / Dynamo Moscow · the only GK to win the Ballon d'Or (1963)</li>
          <li><b>Iker Casillas</b> · Spain / Real Madrid, Porto · World Cup + 2 Euros as captain</li>
          <li><b>Peter Schmeichel</b> · Denmark / Man United · redefined the goalkeeper as a sweeper in English football</li>
        </ol>
        <p style="font-size: 8.5pt; margin-top: 0.2in;"><b>Runners-up:</b> Edwin van der Sar, Dino Zoff, Sepp Maier, Gordon Banks, Thibaut Courtois.</p>''',
    'Centre-back': '''
        <ol style="font-family: var(--serif); font-size: 12pt; line-height: 1.7; padding-left: 0.3in;">
          <li><b>Franco Baresi</b> · Italy / AC Milan · the libero who defined the role for a generation</li>
          <li><b>Bobby Moore</b> · England / West Ham · 1966 World Cup captain</li>
          <li><b>Franz Beckenbauer</b> · Germany / Bayern · <i>Der Kaiser</i>, the original ball-playing centre-back</li>
          <li><b>Paolo Maldini</b> · Italy / AC Milan · 26 seasons at the top level</li>
          <li><b>Sergio Ramos</b> · Spain / Sevilla, Real, PSG · 4 Champions Leagues, key goals in finals</li>
        </ol>
        <p style="font-size: 8.5pt; margin-top: 0.2in;"><b>Runners-up:</b> Fabio Cannavaro, Ronald Koeman, Franz Beckenbauer, Virgil van Dijk.</p>''',
    'Full-back': '''
        <ol style="font-family: var(--serif); font-size: 12pt; line-height: 1.7; padding-left: 0.3in;">
          <li><b>Roberto Carlos</b> · Brazil / Real Madrid · the iconic overlapping left-back</li>
          <li><b>Cafu</b> · Brazil / Roma, Real Madrid, AC Milan · 2 World Cups as captain</li>
          <li><b>Philipp Lahm</b> · Germany / Bayern · the inverted full-back pioneer</li>
          <li><b>Dani Alves</b> · Brazil / Sevilla, Barcelona, Juventus · most trophies in football history</li>
          <li><b>Jill Scott</b> · England / Everton, Man City, Arsenal (women's) · the metronome of England's Euro 2022</li>
        </ol>
        <p style="font-size: 8.5pt; margin-top: 0.2in;"><b>Runners-up:</b> Paolo Maldini (right-back era), Trent Alexander-Arnold, Achraf Hakimi, Ashley Cole.</p>''',
    'Defensive midfielder': '''
        <ol style="font-family: var(--serif); font-size: 12pt; line-height: 1.7; padding-left: 0.3in;">
          <li><b>Claude Makélélé</b> · France / Real Madrid, Chelsea · the role's prototype</li>
          <li><b>Andrea Pirlo</b> · Italy / AC Milan, Juventus · the regista's regista</li>
          <li><b>Busquets</b> · Spain / Barcelona · <i>"he plays as an extra midfielder"</i> as Pep said</li>
          <li><b>Xabi Alonso</b> · Spain / Liverpool, Real, Bayern · the deep-lying playmaker template</li>
          <li><b>Rodri</b> · Spain / Man City · 2024 Ballon d'Or · the modern complete 6</li>
        </ol>
        <p style="font-size: 8.5pt; margin-top: 0.2in;"><b>Runners-up:</b> N'Golo Kanté, Casemiro, Fernandinho, Javier Mascherano.</p>''',
    'Midfielder': '''
        <ol style="font-family: var(--serif); font-size: 12pt; line-height: 1.7; padding-left: 0.3in;">
          <li><b>Zinedine Zidane</b> · France / Juventus, Real Madrid · 1998 World Cup, 3 Ballons d'Or</li>
          <li><b>Ronaldinho</b> · Brazil / PSG, Barcelona, AC Milan · the joy-bringer of the 2000s</li>
          <li><b>Lothar Matthäus</b> · Germany / Bayern, Inter · 150 caps, 1990 World Cup winner</li>
          <li><b>Andrés Iniesta</b> · Spain / Barcelona · 2 Euros + 1 World Cup, 2010 World Cup final goal</li>
          <li><b>Luka Modrić</b> · Croatia / Tottenham, Real Madrid · 2018 Ballon d'Or, 6 Champions Leagues</li>
        </ol>
        <p style="font-size: 8.5pt; margin-top: 0.2in;"><b>Runners-up:</b> Zidane, Platini, Xavi, Toni Kroos, Steven Gerrard.</p>''',
    'Attacking midfielder': '''
        <ol style="font-family: var(--serif); font-size: 12pt; line-height: 1.7; padding-left: 0.3in;">
          <li><b>Lionel Messi</b> · Argentina / Barcelona, PSG, Inter Miami · 8 Ballons d'Or, GOAT debate</li>
          <li><b>Pelé</b> · Brazil / Santos, NY Cosmos · 1,281 goals, 3 World Cups</li>
          <li><b>Diego Maradona</b> · Argentina / Boca, Napoli · Hand of God + Goal of the Century</li>
          <li><b>Ronaldinho</b> · Brazil · the most fun player ever to wear the position</li>
          <li><b>Zinedine Zidane</b> · France · the prototype of the modern 10 in a 4-2-3-1</li>
        </ol>
        <p style="font-size: 8.5pt; margin-top: 0.2in;"><b>Runners-up:</b> Rivaldo, Kaka, Roberto Baggio, Rui Costa, Juan Román Riquelme.</p>''',
    'Winger': '''
        <ol style="font-family: var(--serif); font-size: 12pt; line-height: 1.7; padding-left: 0.3in;">
          <li><b>Cristiano Ronaldo</b> · Portugal / Sporting, Man United, Real, Juventus, Al-Nassr · 900+ goals</li>
          <li><b>Johan Cruyff</b> · Netherlands / Ajax, Barcelona · <i>Total Football</i> prototype as No. 14</li>
          <li><b>George Best</b> · Northern Ireland / Man United · the original wide-forward artist</li>
          <li><b>Mohamed Salah</b> · Egypt / Roma, Liverpool · the modern inverted-winger standard</li>
          <li><b>Kylian Mbappé</b> · France / Monaco, PSG, Real Madrid · the next-gen template at 21</li>
        </ol>
        <p style="font-size: 8.5pt; margin-top: 0.2in;"><b>Runners-up:</b> Ryan Giggs, David Beckham, Arjen Robben, Thierry Henry, Neymar.</p>''',
    'Striker': '''
        <ol style="font-family: var(--serif); font-size: 12pt; line-height: 1.7; padding-left: 0.3in;">
          <li><b>Ronaldo Nazário</b> · Brazil / Cruzeiro, PSV, Barcelona, Inter, Real · the original R9</li>
          <li><b>Gerd Müller</b> · Germany / Bayern · <i>Der Bomber der Nation</i>, 1970 World Cup top scorer</li>
          <li><b>Thierry Henry</b> · France / Monaco, Juventus, Arsenal, Barcelona · the modern striker template</li>
          <li><b>Robert Lewandowski</b> · Poland / Dortmund, Bayern, Barcelona · the most clinical since Müller</li>
          <li><b>Marco van Basten</b> · Netherlands / Ajax, AC Milan · Euro 1988 volley</li>
        </ol>
        <p style="font-size: 8.5pt; margin-top: 0.2in;"><b>Runners-up:</b> Ally McCoist, Romário, Suárez, Alan Shearer, Eusébio, Raúl.</p>''',
    'Captain': '''
        <ol style="font-family: var(--serif); font-size: 12pt; line-height: 1.7; padding-left: 0.3in;">
          <li><b>Carolyn Curran</b> · did not exist; <b>Didier Deschamps</b> · France · 1998 World Cup + Euro 2000 as captain</li>
          <li><b>Bobby Moore</b> · England · the only English captain to lift the World Cup</li>
          <li><b>Dunga</b> · Brazil · 1994 World Cup as captain, the metronome</li>
          <li><b>Paolo Maldini</b> · AC Milan · 5 Champions League appearances (no wins; lost 3 finals)</li>
          <li><b>Iker Casillas</b> · Spain · Euro 2008 + World Cup 2010 + Euro 2012 = the captain's treble</li>
        </ol>
        <p style="font-size: 8.5pt; margin-top: 0.2in;"><b>Runners-up:</b> Philipp Lahm, Carles Puyol, Cafu, Cannavaro, John Terry, Steven Gerrard.</p>''',
    'Manager': '''
        <ol style="font-family: var(--serif); font-size: 12pt; line-height: 1.7; padding-left: 0.3in;">
          <li><b>Alex Ferguson</b> · Manchester United · 38 trophies, 13 Premier Leagues</li>
          <li><b>Arrigo Sacchi</b> · AC Milan · invented the modern pressing system</li>
          <li><b>Johan Cruyff</b> · Barcelona · the foundation of the Catalan identity</li>
          <li><b>Pep Guardiola</b> · Barcelona, Bayern, Man City · 36 trophies, 4 Champions Leagues</li>
          <li><b>José Mourinho</b> · Porto, Chelsea, Inter, Real, Man United · the pragmatist's pragmatist</li>
        </ol>
        <p style="font-size: 8.5pt; margin-top: 0.2in;"><b>Runners-up:</b> Helenio Herrera, Brian Clough, Fabio Capello, Rinus Michels, Carlo Ancelotti.</p>''',
}


for i, title in enumerate(['Goalkeeper', 'Centre-back', 'Full-back', 'Defensive midfielder',
                         'Midfielder', 'Attacking midfielder', 'Winger', 'Striker',
                         'Captain', 'Manager']):
    top5_page(206 + i, title,
              f'The starting five {title.lower()}s in football history — from the polygonal Yashin to the modern sweepers.',
              None, ranked[title])


# ============================================================================
# SECTION XV: Tactical philosophies (216-220)
# ============================================================================

write_page(216, 'Section XV', 'Catenaccio',
'''<div class="two-col">
  <div>
    <p class="lead">Italian for "bolt." The 1960s Inter Milan method that changed what defence could be.</p>

    <p><b>Origin:</b> Austria and Switzerland in the 1930s, refined at Inter Milan by <b>Helenio Herrera</b> (1960s) and at Juventus by <b>Giovanni Trapattoni</b> (1970s-80s). The deepest expression of <i>prima non nuocere</i> — defence first.</p>

    <p><b>The principles:</b> a <b>libero</b> (sweeper) reads the game from the back line, the two central defenders <b>mark</b> tightly, midfielders screen in front of them, and the team plays on the counterattack through quick, vertical passes.</p>

    <p><b>Where you see it today:</b> in the low blocks of Atlético Madrid under Simeone, in Chelsea's 2004-5 title win under Mourinho, and in the Italian national team throughout their 2006 World Cup-winning campaign.</p>
    <div class="sidebar terracotta">
      <h3>The goalkeeper pass starts here</h3>
      <p style="font-size: 8.5pt;">Catenaccio was the first system that <b>used the goalkeeper as a playmaker</b>. The libero was a second ball-playing defender, the centre-backs marked tight, and the GK was the extra man.</p>
    </div>
  </div>
  <div>
    <div class="factbox navy">
      <div class="eyebrow">By the numbers</div>
      <div style="display:grid; grid-template-columns: 1fr 1fr; gap: 0.15in; margin-top: 0.2in;">
        <div><div class="num">3</div><div class="label">European Cups, Inter (1963-65)</div></div>
        <div><div class="num">1</div><div class="label">Goals conceded in those 3 finals</div></div>
        <div><div class="num">1968</div><div class="label">European Championship winners (Italy)</div></div>
        <div><div class="num">2</div><div class="label">Inter Milan consecutive trebles</div></div>
      </div>
      <p style="font-size: 8.5pt; margin-top: 0.2in;"><b>Players who defined it:</b> Sandro Mazzola, Giacinto Facchetti, Armando Picchi, Gianni Rivera. <b>Coaches:</b> Karl Rappan (Switzerland), Nereo Rocco (Milan), Helenio Herrera (Inter).</p>
    </div>
  </div>
</div>
''', 'standard')


write_page(217, 'Section XV', 'Total Football',
'''<div class="two-col">
  <div>
    <p class="lead">The Dutch football revolution. Rinus Michels' tactical idea at Ajax and the Netherlands, perfected by the 1974 and 1978 World Cup teams.</p>

    <p><b>The principle:</b> any outfield player can take any outfield position. When one player moves, another fills their spot. The result is a <b>floating</b> team — 11 players in motion at all times, spaces opening and closing across the pitch.</p>

    <p><b>The team:</b> <b>Johan Cruyff</b> as the prototype No. 14, supported by <b>Johan Neeskens</b>, <b>Rob Rensenbrink</b>, <b>Arie Haan</b>, and <b>Ruud Krol</b> at the back. The 1974 World Cup final — Netherlands 1–2 West Germany — is the most-watched World Cup match of all time at the time of broadcast.</p>

    <p><b>Where you see it today:</b> in <b>Barcelona</b> under Cruyff (as manager, 1988–96), in Spain's 2008-12 national team, and in <b>Juego de Posición</b> (Guardiola's Barcelona, 2008-12).</p>
  </div>
  <div>
    <div class="factbox green">
      <div class="eyebrow">By the numbers</div>
      <div style="display:grid; grid-template-columns: 1fr 1fr; gap: 0.15in; margin-top: 0.2in;">
        <div><div class="num">3</div><div class="label">European Cups, Ajax (1971-73)</div></div>
        <div><div class="num">1974</div><div class="label">World Cup runners-up</div></div>
        <div><div class="num">1978</div><div class="label">World Cup runners-up (again)</div></div>
        <div><div class="num">+</div><div class="label">10</div></div>
      </div>
      <p style="font-size: 8.5pt; margin-top: 0.2in;"><b>Players who defined it:</b> Johan Cruyff (NYT), Johan Neeskens, Rob Rensenbrink, Arie Haan, Ruud Krol, Wim Suurbier. <b>Coaches:</b> Rinus Michels, Ernst Happel (Feyenoord).</p>
    </div>
  </div>
</div>
''', 'standard')


write_page(218, 'Section XV', 'Tiki-Taka & Juego de Posición',
'''<div class="two-col">
  <div>
    <p class="lead">Tiki-Taka is the layman's term. <b>Juego de Posición</b> ("the positional game") is the technical name for Barcelona's method under <b>Pep Guardiola</b>.</p>

    <p><b>The principle:</b> keep the ball through short, accurate passes; draw the opponent into pressing; use the spaces that open to penetrate. Cruyff laid the intellectual foundation; Pep Guardiola systematized it.</p>

    <p><b>The team:</b> Xavi, Iniesta, Busquets at the base, with Messi false-9 above and Pedro/Villa wide. 6 La Liga titles in 6 years, 2 Champions Leagues, the 2009 sextuple. Spain's 2008-12 was the national-team export of the same idea.</p>

    <p><b>The limitations:</b> pressing-resistant opponents found they could compress the pitch and let Barça pass sideways. The 2010 Inter Milan win against Guardiola's Barça in the Champions League semi-final was the warning. The 2014 World Cup — Spain's early exit — was the proof.</p>
  </div>
  <div>
    <div class="factbox terracotta">
      <div class="eyebrow">By the numbers</div>
      <div style="display:grid; grid-template-columns: 1fr 1fr; gap: 0.15in; margin-top: 0.2in;">
        <div><div class="num">4</div><div class="label">Ballon d'Or trophies, 2009-12</div></div>
        <div><div class="num">73%</div><div class="label">Average possession, 2008-12</div></div>
        <div><div class="num">6</div><div class="label">La Liga titles in 6 years</div></div>
        <div><div class="num">2</div><div class="label">Champions Leagues</div></div>
      </div>
      <p style="font-size: 8.5pt; margin-top: 0.2in;"><b>Players who defined it:</b> Xavi, Iniesta, Busquets, Messi, Pedro, David Villa, Dani Alves. <b>Where you see it today:</b> Manchester City (2018-25), Spain women's national team.</p>
    </div>
  </div>
</div>
''', 'standard')


write_page(219, 'Section XV', 'Gegenpressing',
'''<div class="two-col">
  <div>
    <p class="lead">German for "counter-pressing." The Jürgen Klopp philosophy — the moment you lose the ball, you try to win it back.</p>

    <p><b>The principle:</b> the most dangerous moment in football is the moment of transition. The team that wins the ball back fastest retains the most territory. Counter-press with intensity, recover the ball high, and only then drop back into shape.</p>

    <p><b>The team:</b> Borussia Dortmund (2011-15), Liverpool (2016-present), Germany 2014. <b>The player:</b> Jürgen Klopp as the central character, with <b>Naby Keïta</b>, <b>Fabinho</b>, and <b>Roberto Firmino</b> as the on-pitch architects.</p>

    <p><b>Where you see it today:</b> <b>Liverpool</b> under Klopp (the 2019 Champions League and 2020 Premier League titles), <b>Bayern</b> under Flick (the 2020 sextuple), and <b>Germany's 2014 World Cup</b>.</p>
  </div>
  <div>
    <div class="factbox navy">
      <div class="eyebrow">By the numbers</div>
      <div style="display:grid; grid-template-columns: 1fr 1fr; gap: 0.15in; margin-top: 0.2in;">
        <div><div class="num">6</div><div class="label">Champions League finals, Klopp (Dortmund + Liverpool)</div></div>
        <div><div class="num">+32</div><div class="label">Goal difference in 2019/20 PL</div></div>
        <div><div class="num">2014</div><div class="label">World Cup winners (Germany, Flick as assistant)</div></div>
        <div><div class="num">2020</div><div class="label">Bayern sextuple (Flick)</div></div>
      </div>
      <p style="font-size: 8.5pt; margin-top: 0.2in;"><b>Players who defined it:</b> Jürgen Klopp, Naby Keïta, Roberto Firmino, Sadio Mané, Fabinho, Joshua Kimmich.</p>
    </div>
  </div>
</div>
''', 'standard')


write_page(220, 'Section XV', 'The Inverted-Fullback System',
'''<div class="two-col">
  <div>
    <p class="lead">The modern answer to the question "how do you keep possession against a low block?"</p>

    <p><b>The principle:</b> the full-backs tuck into central midfield when the team has possession, creating a 3-2 build-up shape at the back. The wide attackers become the wide defenders.</p>

    <p><b>The team:</b> Liverpool 2018-19, Man City 2020-24. <b>The player:</b> <b>Trent Alexander-Arnold</b>, who redefined the role by stepping into central midfield with the ball at his feet. <b>Philipp Lahm</b> at Bayern in 2013-14 was the original.</p>

    <p><b>The risk:</b> the inverted full-back leaves the wide space for the opposition's wide player to run into. The defensive counter-press and an aggressive high line are required to make it work. Liverpool lost three Champions League finals (2018, 2022, 2024) in part because opposition managers found ways to attack the right side.</p>
  </div>
  <div>
    <div class="factbox rust">
      <div class="eyebrow">By the numbers</div>
      <div style="display:grid; grid-template-columns: 1fr 1fr; gap: 0.15in; margin-top: 0.2in;">
        <div><div class="num">17</div><div class="label">Premier League assists, TAA (2018/19, record)</div></div>
        <div><div class="num">4</div><div class="label">Champions Leagues, Real Madrid (Carvajal)</div></div>
        <div><div class="num">2013</div><div class="label">Bayern treble with inverted Lahm</div></div>
        <div><div class="num">2</div><div class="label">Premier League titles, Man City (Walker inverted)</div></div>
      </div>
      <p style="font-size: 8.5pt; margin-top: 0.2in;"><b>Players who defined it:</b> Philipp Lahm, Trent Alexander-Arnold, João Cancelo, Andrew Robertson, Dani Carvajal.</p>
    </div>
  </div>
</div>
''', 'standard')


# ============================================================================
# SECTION XVI: Modern football  (221-225)
# ============================================================================

write_page(221, 'Section XVI', 'Sportswashing in football',
'''<div class="two-col">
  <div>
    <p class="lead">Sovereign wealth funds, petro-dollar clubs, and the question of who pays for football's biggest teams.</p>

    <p>Manchester City is owned by the <b>Abu Dhabi United Group</b> (Sheikh Mansour). Newcastle by the <b>Saudi Public Investment Fund</b> (the same fund that owns LIV Golf). Paris Saint-Germain by <b>Qatar Sports Investments</b>. AC Milan is backed by <b>RedBird Capital</b>; Liverpool by <b>Fenway Sports Group</b>; Chelsea by a consortium led by <b>Todd Boehly</b>.</p>

    <p>Critics call this <b>sportswashing</b> — a state's use of football clubs as soft power, reputation management, and wealth advertisement. Defenders call it investment that has made football better — the Premier League's TV deal is the largest in world sport, and the on-pitch product has arguably never been more competitive.</p>
  </div>
  <div>
    <div class="factbox terracotta">
      <div class="eyebrow">By the numbers</div>
      <div class="stat-block">
        <div><div class="stat-label">Top ownership</div>2024 — 17 of 20 Premier League clubs owned by foreign entities or consortia (vs. 1 in 1996)</div>
        <div><div class="stat-label">City Football Group</div>13 clubs worldwide (Man City, NYC FC, Girona, Lommel SK, Mumbai City, etc.)</div>
        <div><div class="stat-label">Saudi Pro League</div>2023-25 — 80+ signings of top European players; Cristiano Ronaldo, Neymar, Benzema, Kanté</div>
        <div><div class="stat-label">UEFA cap</div>FFP replaced by Squad Cost Ratio (70% of revenue) and Financial Sustainability rules (2022)</div>
      </div>
      <p style="font-size: 8.5pt; margin-top: 0.2in;"><b>Where the debate is going:</b> the European Super League (2021 collapse), the Manchester City 115 charges (2024 ongoing), the FIFA club World Cup reform (2025).</p>
    </div>
  </div>
</div>
''', 'howto')


write_page(222, 'Section XVI', 'The transfer window',
'''<div class="two-col">
  <div>
    <p class="lead">Football used to transfer players in March and the close season. Now it transfers them twice a year — in two weeks — for sums that would be eye-watering at central-bank level.</p>

    <p>The Premier League leads by spending. In summer 2024, English clubs spent <b>£2.3 billion</b> in one window — more than La Liga, Bundesliga, Serie A, and Ligue 1 combined. Chelsea's 2023-25 squad build reached <b>£1 billion</b> in net spend.</p>

    <p>The transfer window is when the <b>social-media cycle</b> peaks: leaks, rumours, the famous <i>"here we go"</i> from Fabrizio Romano. Modern supporter culture follows transfer news with the same intensity as goals.</p>

    <p>The summer 2025 window closed on <b>September 1</b> at 23:00 GMT. Premier League spending: ~£2.0 billion.</p>
  </div>
  <div>
    <div class="factbox green">
      <div class="eyebrow">By the numbers</div>
      <div class="stat-block">
        <div><div class="stat-label">All-time most expensive</div>Neymar — €222m, 2017 (PSG, Barcelona)</div>
        <div><div class="stat-label">Premier League record</div>£106.8m — Enzo Fernández, Benfica to Chelsea, 2023</div>
        <div><div class="stat-label">Summer 2024 spend</div>Premier League: £2.3bn · La Liga: £430m · Bundesliga: £600m · Serie A: £750m</div>
        <div><div class="stat-label">Most-clicked announcement</div>Neymar's PSG unveiling photo: 110 million interactions in 24 hours (still the record)</div>
      </div>
    </div>
  </div>
</div>
''', 'standard')


write_page(223, 'Section XVI', 'Fan-owned clubs',
'''<div class="two-col">
  <div>
    <p class="lead">The <b>50+1 rule</b> in German football requires that club members retain a majority of voting rights. As a result, German clubs remain the rare example of fan-owned top-flight football in Europe.</p>

    <p><b>Borussia Dortmund</b>, <b>Bayern München</b>, <b>FC Union Berlin</b>, <b>SC Freiburg</b>, <b>FC Köln</b>: each is majority-owned by its members. The members elect the president, set ticket prices, and vote on major decisions including stadium naming rights.</p>

    <p>The Spanish and Portuguese models use the <b>socío</b> system — paying members elect the president (Real Madrid, Barcelona, Athletic Bilbao, Osasuna, Porto, Sporting, Benfica — all member-owned).</p>

    <p>In England, after the 2021 European Super League collapse, fan-led reviews of every club were mandated by the government. The 2022 Fan-Led Review recommended the appointment of an Independent Football Regulator.</p>
  </div>
  <div>
    <div class="factbox gold">
      <div class="eyebrow">By the numbers</div>
      <div class="stat-block">
        <div><div class="stat-label">50+1 rule (Germany)</div>Adopted in 1998 — exception: Bayer Leverkusen, Wolfsburg (1998 grandfathered since the clubs pre-date the rule)</div>
        <div><div class="stat-label">Real Madrid members</div>~93,000 members (socios) — 1 of them elected Florentino Pérez (2021-2025)</div>
        <div><div class="stat-label">Union Berlin</div>1st division 2019 — 50,000+ members, 22,000 waitlist for season tickets</div>
        <div><div class="stat-label">AFC Wimbledon</div>The phoenix club — fan-owned since 2002 founding</div>
      </div>
      <p style="font-size: 8.5pt; margin-top: 0.2in;">Where you see it: <b>Bayern, Dortmund, Barcelona, Real Madrid, Benfica, Sporting, Porto</b>. The English Premier League has just one fan-owned club remaining — <b>AFC Wimbledon</b>, in League One.</p>
    </div>
  </div>
</div>
''', 'standard')


write_page(224, 'Section XVI', 'VAR — every rule, every controversy',
'''<div class="two-col">
  <div>
    <p class="lead"><b>Video Assistant Referee</b> (VAR) was introduced in 2018. Every top European league now uses it. Every football fan now has opinions.</p>

    <p>VAR reviews only four categories of decision: <b>goals</b>, <b>penalty decisions</b>, <b>red cards</b>, and <b>mistaken identity</b>. The on-field referee can overrule the original decision only after a review at the pitch-side monitor (OFR).</p>

    <p>The criticism is two-fold. <b>Officiating:</b> VAR cannot re-referee decisions; it can only catch clear errors. <b>Time:</b> a VAR review that overturns a goal takes 90 seconds on average; one that confirms it takes 30 seconds, and the delay is hard for in-stadium fans to understand.</p>

    <p>The 2025 World Cup will use <b>Semi-Automated Offside Technology</b> (S-AOT) — limb-tracking sensors in the ball and 12 stadium cameras detect offside in real time, displaying a 3D animation inside the stadium.</p>
    <div class="sidebar navy">
      <h3>The most controversial calls</h3>
      <p style="font-size: 8.5pt;"><b>2022 World Cup</b> — six of the last-16 ties had VAR-overturned goals. <b>2023 FA Cup final</b> — VAR ruled out a Manchester City equaliser for an offside the naked eye could not see. <b>2023 Euro</b> — France's last-minute equalizer was ruled out for an unintentional deflection off Mbappé.</p>
    </div>
  </div>
  <div>
    <div class="factbox terracotta">
      <div class="eyebrow">By the numbers</div>
      <div class="stat-block">
        <div><div class="stat-label">VAR adoption</div>2018 — Premier League joins. By 2025, 60+ leagues worldwide use VAR.</div>
        <div><div class="stat-label">Review average time</div>84 seconds (PL, 2023/24) — target is under 30 seconds for in-stadium clarity</div>
        <div><div class="stat-label">Disallowed goals</div>Premier League 2022/23 — 38 goals disallowed by VAR (vs. 8 in pre-VAR era)</div>
        <div><div class="stat-label">S-AOT</b></div>Used at 2022 World Cup — 193 offside calls, average accuracy of 1.9 cm</div>
      </div>
    </div>
  </div>
</div>
''', 'referee')


write_page(225, 'Section XVI', 'Football in 2026 and beyond',
'''<div class="two-col">
  <div>
    <p class="lead">A snapshot of where modern football is heading — 2026 onwards.</p>

    <p>The 2026 World Cup's expansion to <b>48 teams</b> changes the calculus. Africa and Asia get more slots — Egypt, Morocco, India and Indonesia are expected to qualify for the first time. The club football calendar is also expanding: the <b>FIFA Club World Cup</b> became a 32-team tournament in 2025, and the <b>Champions League</b> is now a 36-team Swiss-model league.</p>

    <p>Women's football is the fastest-growing vertical. <b>Women's Champions League</b> prize money has quadrupled since 2022. <b>England Women</b> fill Wembley (90,000+) routinely. The 2023 Women's World Cup was the first to break 1 billion viewers across the tournament.</p>

    <p>The on-pitch trends: <b>semi-automated offside</b>, <b>smart balls</b> with embedded IMUs, <b>expected-goals (xG)</b> as the dominant broadcast metric, and the slow transition from "physical" elite players to "decisional" ones.</p>
  </div>
  <div>
    <div class="factbox navy">
      <div class="eyebrow">What changes by 2030</div>
      <div class="stat-block">
        <div><div class="stat-label">Global audience</div>3.5 billion (FIFA target for 2026 World Cup broadcast reach)</div>
        <div><div class="stat-label">Transfer total</div>2025/26 — Premier League + UEFA Champions League combined spending projected at €15bn</div>
        <div><div class="stat-label">Women's football</div>2025 — 16 national women's leagues now professional (vs. 7 in 2019)</div>
        <div><div class="stat-label">Tech</b></div>S-AOT, smart-ball IMUs, referee body-cams trials at 2025 FIFA U-20 World Cup</div>
      </div>
      <p style="font-size: 8.5pt; margin-top: 0.2in;"><b>What stays the same:</b> 90 minutes, 11 players, 17 laws, 105 × 68 m. The game itself hasn't changed shape in 160 years — only the players, the tactics, and the cameras.</p>
    </div>
  </div>
</div>
''', 'howto')


print('Generated 25 new pages (201-225).')
