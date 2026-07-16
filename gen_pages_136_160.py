#!/usr/bin/env python3
"""
gen_pages_136_160.py — Section X continuation: Free kicks, Throw-ins, Build-up,
Defensive patterns, Counter-attacking. 25 pages matching the existing template
used by gen_pages_131_135.py.

Output: pages/136-page.html through pages/160-page.html
"""
import os, html

OUT_DIR = os.path.join(os.path.dirname(__file__), "pages")
SECTION = "Section X · Tactical moves & set plays"


def diagram_svg(kicker: str, fill_color: str = "#4c9b52") -> str:
    """Generic two-column pitch diagram. Returns inner svg string."""
    return (
        f'<div class="kicker" style="text-align:center;margin-bottom:0.06in;">{kicker}</div>\n'
        f'<svg viewBox="0 0 620 420" role="img" aria-label="{html.escape(kicker)}" '
        f'style="width:100%;height:auto;display:block;background:{fill_color};border:1px solid var(--rule);">\n'
        f'  <rect x="4" y="4" width="612" height="412" fill="{fill_color}" stroke="#f8f3e6" stroke-width="3"/>\n'
        f'  <path d="M4 4 H616 M4 416 H616" stroke="#d7efd0" stroke-width="2" opacity=".7"/>\n'
        f'  <circle cx="310" cy="210" r="60" fill="none" stroke="#eaf5df" stroke-width="2"/>\n'
        f'  <circle cx="310" cy="210" r="3" fill="#eaf5df"/>\n'
        f'  <g fill="#f7f1e2" stroke="#1a1612" stroke-width="1.3">\n'
        f'    <circle cx="120" cy="180" r="8"/><circle cx="180" cy="240" r="8"/>\n'
        f'    <circle cx="240" cy="190" r="8"/><circle cx="300" cy="250" r="8"/>\n'
        f'    <circle cx="380" cy="200" r="8"/><circle cx="460" cy="240" r="8"/>\n'
        f'  </g>\n'
        f'  <g fill="#c44536" stroke="#1a1612" stroke-width="1.3">\n'
        f'    <circle cx="160" cy="120" r="8"/><circle cx="260" cy="140" r="8"/>\n'
        f'    <circle cx="350" cy="130" r="8"/><circle cx="450" cy="160" r="8"/>\n'
        f'    <circle cx="220" cy="310" r="8"/><circle cx="380" cy="320" r="8"/>\n'
        f'  </g>\n'
        f'</svg>\n'
    )


def page(num: int, title: str, lead: str, body_html: str, sidebar_html: str,
         diagram_kicker: str, factbox_title: str, factbox_body: str,
         caption: str = "", diagram_color: str = "#4c9b52") -> str:
    """Build a single page in the standard two-column layout."""
    cap = f'<p class="cap">{caption}</p>' if caption else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page {num} — {html.escape(title)}</title>
<link rel="stylesheet" href="book.css">
</head>
<body class="page standard">
<div class="page-inner">
<div class="page-header">
  <div class="page-num">{num}</div>
  <div><div class="section-num">{SECTION}</div><h1 class="section-title">{html.escape(title)}</h1></div>
</div>
<div class="two-col">
  <div>
    {lead}
{body_html}
{sidebar_html}
  </div>
  <div>
    <div class="diagram" style="padding:0.12in;">
{diagram_svg(diagram_kicker, fill_color=diagram_color)}
</div>
    {cap}
    <div class="factbox dark" style="margin-top:0.16in;"><div class="eyebrow">Set-piece principle</div><h3 style="font-size:12pt;margin-top:0.05in;">{html.escape(factbox_title)}</h3><p style="font-size:8.5pt;margin:0.08in 0 0;">{factbox_body}</p></div>
  </div>
</div>
</div>
</body>
</html>
"""


# Page definitions — (num, title, lead, body, sidebar, diagram_kicker, factbox_title, factbox_body, caption)
PAGES = [
    # === 136-140: FREE KICKS ===
    (136, "Free kicks — the dead-ball weapon",
     '<p class="lead">A <strong>direct free kick</strong> turns a foul into a shot. Specialists score from 25–35 yard set pieces at a rate higher than from open play.</p>',
     '<h3 style="font-family:var(--serif);color:var(--green);font-size:13pt;margin:0.18in 0 0.07in;">The geometry of a curler</h3>\n<ul style="font-size:8.7pt;margin:0.08in 0 0 0.22in;line-height:1.42;"><li><b>Approach angle:</b> 30–45° off the ball, plant foot beside it.</li><li><b>Strike point:</b> under the ball’s equator with the inside of the foot.</li><li><b>Follow-through:</b> across the body, not into it.</li><li><b>Spin axis:</b> determines whether the ball dips, swerves, or knuckleballs.</li></ul>',
     '<div class="sidebar terracotta" style="margin-top:0.15in;"><h3>Knuckleball vs curl</h3><p style="font-size:8.5pt;margin:0;">A knuckleball has <b>little spin</b> and zig-zags in flight. Ronaldo and Drogba mastered the dipper. Juninho Pernambucano made the curling swerve famous.</p></div>',
     "Free-kick trajectory", "Strike under the equator", "A ball struck under its equator tumbles forward and dips late. The goalkeeper reads a high trajectory and steps forward — then the ball drops into the top corner."),
    (137, "Wall placement and the line of sight",
     '<p class="lead">A <strong>wall</strong> is a legal shield. Its job: hide part of the goal until the kick is taken. The free-kick taker’s job: beat the wall.</p>',
     '<h3 style="font-family:var(--serif);color:var(--green);font-size:13pt;margin:0.18in 0 0.07in;">Reading the setup</h3>\n<ul style="font-size:8.7pt;margin:0.08in 0 0 0.22in;line-height:1.42;"><li><b>Distance:</b> closer than 25 yards → dip or curl over the wall.</li><li><b>Angle:</b> wide free kick → cut inside the far post.</li><li><b>Wall height:</b> tall defenders make a chip a better option.</li><li><b>Gap:</b> attackers sometimes leave the wall exposed by walking away — referees will move them back.</li></ul>',
     '<div class="sidebar navy" style="margin-top:0.15in;"><h3>The wall hop</h3><p style="font-size:8.5pt;margin:0;">A timed jump at the moment of the strike gives the keeper the full sight of the goal. Wall jumpers must start together — even one late jumper ruins the read.</p></div>',
     "Wall and goalkeeper angle", "Hide the corner", "A wall protects the lower-near corner. The far post is the natural target — the keeper has to travel further, and the wall’s body is on the wrong side."),
    (138, "Indirect free kicks — the decoy routine",
     '<p class="lead">An <strong>indirect free kick</strong> must touch a second player before a goal can be scored. That simple rule produces a world of decoy runs, dummy strikes, and short passes.</p>',
     '<h3 style="font-family:var(--serif);color:var(--green);font-size:13pt;margin:0.18in 0 0.07in;">Common patterns</h3>\n<ul style="font-size:8.7pt;margin:0.08in 0 0 0.22in;line-height:1.42;"><li><b>The dummy:</b> one player feints to strike; another slots a low pass into the box.</li><li><b>The short pass:</b> restart goes backward or square to drag defenders out.</li><li><b>The lay-off:</b> taker rolls the ball to a runner arriving late from deep.</li></ul>',
     '<div class="sidebar green" style="margin-top:0.15in;"><h3>The classic Barca routine</h3><p style="font-size:8.5pt;margin:0;">Messi would pass, Deco would dummy, and a third runner would side-foot. The ball moved four yards but the wall lost its mark.</p></div>',
     "Indirect free kick shape", "Two touches, then a shot", "The key is the moment of the dummy. If the wall steps early, the runner has space. If they hold, the lay-off finds the open player."),
    (139, "Free-kick specialists — five to study",
     '<p class="lead">A handful of players have made free kicks an art. Studying their mechanics and ball-strike points is the fastest way to understand what makes a dead ball deadly.</p>',
     '<h3 style="font-family:var(--serif);color:var(--green);font-size:13pt;margin:0.18in 0 0.07in;">Five reference takers</h3>\n<ul style="font-size:8.7pt;margin:0.08in 0 0 0.22in;line-height:1.42;"><li><b>Juninho Pernambucano</b> — Ligue 1’s all-time top scorer from outside the box.</li><li><b>David Beckham</b> — bent it like only he could; right-footed swerve over the wall.</li><li><b>Cristiano Ronaldo</b> — knuckleball dipper, often from 30+ yards.</li><li><b>Sinisa Mihajlovic</b> — record 28 free kicks in Serie A.</li><li><b>Lionel Messi</b> — low curlers placed into the bottom corner.</li></ul>',
     '<div class="sidebar terracotta" style="margin-top:0.15in;"><h3>Why this matters</h3><p style="font-size:8.5pt;margin:0;">Watch where they plant their foot, where they strike the ball, and the height of the run-up. The differences are small — the outcomes are not.</p></div>',
     "Specialist comparison", "Small adjustments, big payoffs", "A two-inch change in plant-foot position moves the strike by a yard. Free-kick quality is micro-mechanics, not magic."),
    (140, "Long-range free-kick strategy",
     '<p class="lead">Beyond 35 yards, the wall is less of a problem and the trajectory is. Specialists shoot for placement, not power — using the dip and swerve to beat a keeper who has set his wall perfectly.</p>',
     '<h3 style="font-family:var(--serif);color:var(--green);font-size:13pt;margin:0.18in 0 0.07in;">The long-range playbook</h3>\n<ul style="font-size:8.7pt;margin:0.08in 0 0 0.22in;line-height:1.42;"><li><b>Place, don’t blast:</b> a slow swerve is harder to read than a fast dipper.</li><li><b>Read the wall:</b> tall? chip. Short? curl over.</li><li><b>Hit the gap:</b> the space between the keeper’s dive and the post is the target.</li></ul>',
     '<div class="sidebar navy" style="margin-top:0.15in;"><h3>The role of practice</h3><p style="font-size:8.5pt;margin:0;">The greats train specific kick types repeatedly. By match day they have a complete map of where each technique lands from each angle.</p></div>',
     "Long-range kick map", "Placement beats power", "A placed free kick with spin and dip, into the top corner, beats a blast that the keeper can read. Modern free-kick coaching is geometry first, power second."),
    # === 141-145: THROW-INS ===
    (141, "Throw-ins — the long throw",
     '<p class="lead">A <strong>long throw</strong> is a free delivery with both feet on the ground. Players like Rory Delap turned it into a goal-threat weapon — a six-yard box cross in disguise.</p>',
     '<h3 style="font-family:var(--serif);color:var(--green);font-size:13pt;margin:0.18in 0 0.07in;">Mechanics of the long throw</h3>\n<ul style="font-size:8.7pt;margin:0.08in 0 0 0.22in;line-height:1.42;"><li><b>Grip:</b> fingers spread along the seam at the back of the ball.</li><li><b>Run-up:</b> 4–6 paces, accelerating into the release.</li><li><b>Body angle:</b> arched back, hips turned 90° to the line.</li><li><b>Release:</b> ball leaves the hands behind the head, not above it.</li></ul>',
     '<div class="sidebar terracotta" style="margin-top:0.15in;"><h3>The Rory Delap effect</h3><p style="font-size:8.5pt;margin:0;">Stoke City won or drew 40% of matches where Delap delivered a long throw. Modern coaches respect it as a set piece in its own right.</p></div>',
     "Long throw mechanics", "Hide the launch", "A long throw works because the defenders cannot judge the flight. The release point — high, behind the head — is what makes it dangerous."),
    (142, "Throw-in patterns and routines",
     '<p class="lead">Throw-ins used to be a restarter. Modern football treats them as <strong>set plays</strong> — with screens, short options, and rehearsed movements.</p>',
     '<h3 style="font-family:var(--serif);color:var(--green);font-size:13pt;margin:0.18in 0 0.07in;">Five routine types</h3>\n<ul style="font-size:8.7pt;margin:0.08in 0 0 0.22in;line-height:1.42;"><li><b>The short throw:</b> backwards or square to keep possession.</li><li><b>The flick-on:</b> a long throw flicked at the near post.</li><li><b>The decoy:</b> one player shapes for a long throw but plays short.</li><li><b>The overload:</b> cluster three teammates near the touchline for a wall-pass.</li><li><b>The switch:</b> a deep throw-in targets a free man on the far side.</li></ul>',
     '<div class="sidebar green" style="margin-top:0.15in;"><h3>Modern coaching lens</h3><p style="font-size:8.5pt;margin:0;">Top-flight teams rehearse 5–8 throw-in routines. Players know the trigger words, the screeners, and the runners.</p></div>',
     "Throw-in routine map", "Replay the throw", "Treat every throw-in as a corner — pre-agree the next pass, the run, and the screen. That is the difference between a restart and a chance."),
    (143, "Throw-in defending — the back-pass trap",
     '<p class="lead">Defending a throw-in means stopping the routine, not just the ball. The classic trap: a forward press, a touchline squeeze, and a fast counter-press.</p>',
     '<h3 style="font-family:var(--serif);color:var(--green);font-size:13pt;margin:0.18in 0 0.07in;">The defensive shape</h3>\n<ul style="font-size:8.7pt;margin:0.08in 0 0 0.22in;line-height:1.42;"><li><b>Mark every attacker:</b> ball-side, man-side, and the thrower’s first option.</li><li><b>Squeeze the touchline:</b> stand 1–2 yards off the line, not 5.</li><li><b>Trigger the press:</b> as soon as the ball is released, step forward.</li><li><b>Counter-press the second ball:</b> the team that wins the second ball usually wins the possession.</li></ul>',
     '<div class="sidebar navy" style="margin-top:0.15in;"><h3>The 5-second rule</h3><p style="font-size:8.5pt;margin:0;">If the throw-in team cannot find a teammate within 5 seconds, they lose 70% of their expected possession value.</p></div>',
     "Throw-in defence shape", "Win the second ball", "Modern defending isn’t about contesting the throw — it is about winning the second ball that follows. Press, win, transition."),
    (144, "Quick throw-ins — the hidden transition",
     '<p class="lead">A <strong>quick throw</strong> is legal even when the referee hasn’t set the wall. It catches defenders facing the wrong way and turns defence into attack in one motion.</p>',
     '<h3 style="font-family:var(--serif);color:var(--green);font-size:13pt;margin:0.18in 0 0.07in;">When to go quick</h3>\n<ul style="font-size:8.7pt;margin:0.08in 0 0 0.22in;line-height:1.42;"><li><b>Defenders turned:</b> the back line is facing their own goal.</li><li><b>Free teammate:</b> a runner is already moving toward space.</li><li><b>Numerical advantage:</b> the throw-in team outnumbers the defenders nearby.</li></ul>',
     '<div class="sidebar terracotta" style="margin-top:0.15in;"><h3>The risk</h3><p style="font-size:8.5pt;margin:0;">A quick throw-in from a dangerous position can also hand the ball to a defender who’s ready. Speed without purpose is just a turnover.</p></div>',
     "Quick throw diagram", "Catch them facing", "The best quick throws are taken before the defenders have stopped jogging. They are not just fast — they are taken when the opposition is still in transition."),
    (145, "Throw-in coaching — the academy view",
     '<p class="lead">Modern academies spend hours on throw-ins. They are the only set piece where <strong>every player</strong> can be coached simultaneously, every game, every week.</p>',
     '<h3 style="font-family:var(--serif);color:var(--green);font-size:13pt;margin:0.18in 0 0.07in;">The training menu</h3>\n<ul style="font-size:8.7pt;margin:0.08in 0 0 0.22in;line-height:1.42;"><li><b>Technique:</b> plant foot, grip, release, follow-through.</li><li><b>Decision-making:</b> when to go short, when to go long.</li><li><b>Routine reading:</b> identify opposition patterns in the first 10 minutes.</li><li><b>Pressing triggers:</b> who presses the throw, who screens.</li></ul>',
     '<div class="sidebar green" style="margin-top:0.15in;"><h3>Why this matters</h3><p style="font-size:8.5pt;margin:0;">A throw-in happens 40–50 times per match. Even a small efficiency gain compounds across a season.</p></div>',
     "Academy throw-in drill", "40 restarts per game", "Coaches who ignore throw-ins leave wins on the pitch. Those who master them turn a free restart into a measurable advantage."),
    # === 146-150: BUILD-UP PLAY ===
    (146, "Goal kicks — the modern restart",
     '<p class="lead">A <strong>goal kick</strong> is no longer a punt upfield. Top teams build from the back, using the goalkeeper as an extra centre-back.</p>',
     '<h3 style="font-family:var(--serif);color:var(--green);font-size:13pt;margin:0.18in 0 0.07in;">The two setups</h3>\n<ul style="font-size:8.7pt;margin:0.08in 0 0 0.22in;line-height:1.42;"><li><b>Short build-up:</b> goalkeeper plays to a centre-back, who drives into midfield.</li><li><b>Long to a target:</b> a big striker wins the first header; second ball is collected.</li></ul>',
     '<div class="sidebar navy" style="margin-top:0.15in;"><h3>The rule change</h3><p style="font-size:8.5pt;margin:0;">The 2019 IFAB change allows goal kicks to be played from inside the box — it’s why teams can now build short from a stationary ball.</p></div>',
     "Goal kick build-up", "Keep or launch — pick one", "The team that picks a style and commits will out-build the team that mixes both. Modern football demands clarity of intent."),
    (147, "Back-four build — the classic pattern",
     '<p class="lead">A <strong>back four</strong> building out has the centre-backs split, the full-backs high, and a single pivot providing a passing lane through the middle.</p>',
     '<h3 style="font-family:var(--serif);color:var(--green);font-size:13pt;margin:0.18in 0 0.07in;">The triggers</h3>\n<ul style="font-size:8.7pt;margin:0.08in 0 0 0.22in;line-height:1.42;"><li><b>Centre-back receives:</b> opens body to midfield; one touch.</li><li><b>Full-back pushes:</b> creates a wide lane and a numerical overload.</li><li><b>Pivot drops:</b> receives between the lines and turns.</li><li><b>Striker checks:</b> short to link, or long to spin in behind.</li></ul>',
     '<div class="sidebar green" style="margin-top:0.15in;"><h3>Patience is a tactic</h3><p style="font-size:8.5pt;margin:0;">The best build-up is often 8–10 passes before the final third. The team that can resist the urge to go long will out-possess the team that can’t.</p></div>',
     "Back-four shape", "Open the body", "Centre-backs that open their body to the midfield, rather than the touchline, unlock the next pass. The first touch sets up every pass after."),
    (148, "Third-man runs — the footballing ghost",
     '<p class="lead">A <strong>third-man run</strong> is the player you didn’t see. Two players combine; the third arrives to take the next pass and breaks the line.</p>',
     '<h3 style="font-family:var(--serif);color:var(--green);font-size:13pt;margin:0.18in 0 0.07in;">How to coach it</h3>\n<ul style="font-size:8.7pt;margin:0.08in 0 0 0.22in;line-height:1.42;"><li><b>Recognise the line:</b> the third man attacks the space the second defender vacated.</li><li><b>Time the run:</b> arriving too early is offside; too late and the window closes.</li><li><b>Communicate:</b> the runner calls, the passer listens.</li></ul>',
     '<div class="sidebar terracotta" style="margin-top:0.15in;"><h3>The ghost principle</h3><p style="font-size:8.5pt;margin:0;">If a defender can see the runner, the runner is too late. The third man appears from the blind side.</p></div>',
     "Third-man diagram", "Attack the blind side", "The third-man run is the most-overloaded phrase in modern coaching — and the least-coached. Teams that master it score from possession; teams that don’t pass sideways forever."),
    (149, "Midfield overload — creating numbers",
     '<p class="lead">Build-up play uses <strong>numerical superiority</strong> in midfield. If three defenders press two centre-backs, the third midfielder is free.</p>',
     '<h3 style="font-family:var(--serif);color:var(--green);font-size:13pt;margin:0.18in 0 0.07in;">The overload rules</h3>\n<ul style="font-size:8.7pt;margin:0.08in 0 0 0.22in;line-height:1.42;"><li><b>Match numbers:</b> never let the opposition have a free man.</li><li><b>Switch play:</b> when one side is overloaded, move the ball to the other.</li><li><b>Pin the press:</b> a runner standing on the last defender holds the line.</li></ul>',
     '<div class="sidebar navy" style="margin-top:0.15in;"><h3>The free-man rule</h3><p style="font-size:8.5pt;margin:0;">Every overload creates a free man. The team that finds the free man first wins the possession battle.</p></div>',
     "Midfield overload shape", "Find the free man", "Numbers are the language of modern football. Coaches who count bodies in midfield win more games than coaches who count tackles."),
    (150, "Press-resistant keepers — the sweeper-keeper",
     '<p class="lead">A <strong>sweeper-keeper</strong> is an 11th outfield player. They step into the back line, sweep crosses, and break the first line of the press with a long ball.</p>',
     '<h3 style="font-family:var(--serif);color:var(--green);font-size:13pt;margin:0.18in 0 0.07in;">The skill set</h3>\n<ul style="font-size:8.7pt;margin:0.08in 0 0 0.22in;line-height:1.42;"><li><b>Feet first:</b> two-footed passing and short control.</li><li><b>Sweep range:</b> reads the offside line and steps in to clear through balls.</li><li><b>Long distribution:</b> 50-yard diagonal switches to wingers.</li></ul>',
     '<div class="sidebar terracotta" style="margin-top:0.15in;"><h3>The pioneers</h3><p style="font-size:8.5pt;margin:0;">Neuer redefined the role. Ederson, Alisson, and Donnarumma made it standard at the top of the game.</p></div>',
     "Sweeper-keeper position", "11 outfield players", "When the keeper steps up, the team has three centre-backs and two full-backs — a five-man build-up that overwhelms any two-striker press."),
    # === 151-155: DEFENSIVE PATTERNS ===
    (151, "The high press — winning it back early",
     '<p class="lead">A <strong>high press</strong> attacks the ball 35–40 yards from your own goal. The aim: turn defence into attack before the opposition has organised.</p>',
     '<h3 style="font-family:var(--serif);color:var(--green);font-size:13pt;margin:0.18in 0 0.07in;">The pressing triggers</h3>\n<ul style="font-size:8.7pt;margin:0.08in 0 0 0.22in;line-height:1.42;"><li><b>Backward pass:</b> trap the centre-back by showing him the touchline.</li><li><b>Receive with back turned:</b> the attacker cannot turn — press him.</li><li><b>Lazy first touch:</b> a bad touch is the cue to step forward.</li></ul>',
     '<div class="sidebar terracotta" style="margin-top:0.15in;"><h3>The risk</h3><p style="font-size:8.5pt;margin:0;">A high press leaves space in behind. If the press is beaten, the team is exposed 1-v-1 with the last line.</p></div>',
     "High press triggers", "Win the ball in their half", "The high press wins the ball closer to goal. Every recovery in the attacking third is worth more than three in your own."),
    (152, "The mid-block — organised and patient",
     '<p class="lead">A <strong>mid-block</strong> sits 25–35 yards from goal, compact and patient. The team gives up territory but holds its shape.</p>',
     '<h3 style="font-family:var(--serif);color:var(--green);font-size:13pt;margin:0.18in 0 0.07in;">The compactness rules</h3>\n<ul style="font-size:8.7pt;margin:0.08in 0 0 0.22in;line-height:1.42;"><li><b>Block the middle:</b> force the play wide.</li><li><b>Shade the centre-backs:</b> forwards stay goal-side of the centre-backs.</li><li><b>Press the touchline:</b> a winger with the ball has no easy pass inside.</li></ul>',
     '<div class="sidebar navy" style="margin-top:0.15in;"><h3>Why it works</h3><p style="font-size:8.5pt;margin:0;">The mid-block is the most-used block in elite football. It concedes territory but denies central penetration — and central penetration is where goals come from.</p></div>',
     "Mid-block shape", "Block the middle", "Force the play to the wing, where one good cross and one good header does not a goal make. The mid-block is geometry."),
    (153, "The low block — the parked bus",
     '<p class="lead">A <strong>low block</strong> defends with all 11 players within 30 yards of the goal. It is the most defensive shape — and the most controversial.</p>',
     '<h3 style="font-family:var(--serif);color:var(--green);font-size:13pt;margin:0.18in 0 0.07in;">The discipline</h3>\n<ul style="font-size:8.7pt;margin:0.08in 0 0 0.22in;line-height:1.42;"><li><b>Two banks of four:</b> shape stays compact, distances stay short.</li><li><b>No pressing high:</b> the team defends its own box, not the opposition’s.</li><li><b>Counter-attack:</b> a low block is only viable with a fast forward to release.</li></ul>',
     '<div class="sidebar terracotta" style="margin-top:0.15in;"><h3>The history</h3><p style="font-size:8.5pt;margin:0;">Greece won Euro 2004 with a low block. Atletico Madrid built a decade of titles on it. Low blocks are not pretty — but they are effective.</p></div>',
     "Low block shape", "All 11 behind the ball", "The low block is a choice to give up the game. It works when the team has the discipline to hold its shape for 90 minutes — and the strikers to punish the counter."),
    (154, "The offside trap — high risk, high reward",
     '<p class="lead">The <strong>offside trap</strong> is the defensive line stepping forward in unison to catch a through-ball runner. Done right: a free kick. Done wrong: a one-on-one with the keeper.</p>',
     '<h3 style="font-family:var(--serif);color:var(--green);font-size:13pt;margin:0.18in 0 0.07in;">The technique</h3>\n<ul style="font-size:8.7pt;margin:0.08in 0 0 0.22in;line-height:1.42;"><li><b>Step together:</b> the line moves as one — even one defender a yard behind breaks the trap.</li><li><b>Read the passer:</b> the trap fires when the through-ball is struck.</li><li><b>Communicate:</b> the sweeper calls the line; the centre-backs hold.</li></ul>',
     '<div class="sidebar green" style="margin-top:0.15in;"><h3>The decline</h3><p style="font-size:8.5pt;margin:0;">VAR has reduced the offside trap’s effectiveness — armpits are now judged offside. Most top teams have moved to a high press or a deep block instead.</p></div>',
     "Offside trap timing", "Step in unison", "The trap works on centimetres. The line that holds together wins the ball; the line that breaks loses the game."),
    (155, "Counter-press — the 6-second rule",
     '<p class="lead">A <strong>counter-press</strong> is the immediate attempt to win the ball back after losing it. The window is 5–7 seconds — beyond that, the opposition has organised and the chance is gone.</p>',
     '<h3 style="font-family:var(--serif);color:var(--green);font-size:13pt;margin:0.18in 0 0.07in;">The counter-press rules</h3>\n<ul style="font-size:8.7pt;margin:0.08in 0 0 0.22in;line-height:1.42;"><li><b>Closest three:</b> the three nearest players to the turnover press the ball.</li><li><b>Cut passing lanes:</b> surround the carrier — no easy square pass.</li><li><b>Win or foul:</b> if the press fails, foul tactically before the transition.</li></ul>',
     '<div class="sidebar terracotta" style="margin-top:0.15in;"><h3>The Gegenpress</h3><p style="font-size:8.5pt;margin:0;">Jurgen Klopp popularised the term. Liverpool’s 2018–19 Champions League win was built on a counter-press that won the ball back inside 6 seconds of losing it.</p></div>',
     "Counter-press geometry", "Win it back in 6", "The counter-press turns defence into attack. The team that wins the ball back inside 6 seconds creates more shots than any other pressing scheme."),
    # === 156-160: COUNTER-ATTACKING ===
    (156, "The counter-attack — transition as a weapon",
     '<p class="lead">A <strong>counter-attack</strong> is the transition from defence to attack. The opposition has committed men forward; the counter team has space to run into.</p>',
     '<h3 style="font-family:var(--serif);color:var(--green);font-size:13pt;margin:0.18in 0 0.07in;">The counter-attack profile</h3>\n<ul style="font-size:8.7pt;margin:0.08in 0 0 0.22in;line-height:1.42;"><li><b>Vertical speed:</b> a fast striker or winger to lead the break.</li><li><b>Central runners:</b> midfielders arriving late into the box.</li><li><b>One-touch finishes:</b> the break usually ends in 3–5 passes.</li></ul>',
     '<div class="sidebar navy" style="margin-top:0.15in;"><h3>The classic counter team</h3><p style="font-size:8.5pt;margin:0;">Leicester City won the 2015–16 Premier League on counter-attacks. Vardy, Mahrez, and Okazaki scored 40+ goals from breaks that started inside their own half.</p></div>',
     "Counter-attack shape", "Run into the space", "A counter-attack exploits the opposition’s imbalance. The team that was attacking is now defending with five men at the back — and the counter team has four attackers running at them."),
    (157, "Defensive transition — the moment of risk",
     '<p class="lead"><strong>Defensive transition</strong> is the moment the team loses the ball. The opposition is disorganised for 6–8 seconds — and so is the team that just lost possession.</p>',
     '<h3 style="font-family:var(--serif);color:var(--green);font-size:13pt;margin:0.18in 0 0.07in;">The first reaction</h3>\n<ul style="font-size:8.7pt;margin:0.08in 0 0 0.22in;line-height:1.42;"><li><b>Counter-press:</b> the closest players press immediately.</li><li><b>Recover shape:</b> the back four resets to the halfway line.</li><li><b>Cut the vertical:</b> the closest midfielder blocks the through-ball lane.</li></ul>',
     '<div class="sidebar terracotta" style="margin-top:0.15in;"><h3>The most dangerous moment</h3><p style="font-size:8.5pt;margin:0;">Goals after turnovers account for 12–15% of all goals in elite football. Defensive transition is not a phase — it is a habit.</p></div>',
     "Defensive transition shape", "The first three seconds", "The team that reacts first wins the transition. Sprint, recover, regroup — in that order. Every second of delay is a goal conceded."),
    (158, "The breakaway — 4-v-3 and 3-v-2",
     '<p class="lead">A <strong>breakaway</strong> is a numerical counter-attack. The team has one more attacker than the defenders can handle — and the attack usually ends in a goal.</p>',
     '<h3 style="font-family:var(--serif);color:var(--green);font-size:13pt;margin:0.18in 0 0.07in;">The breakaway geometry</h3>\n<ul style="font-size:8.7pt;margin:0.08in 0 0 0.22in;line-height:1.42;"><li><b>4-v-3:</b> the carrier runs wide; a central runner arrives as the third option.</li><li><b>3-v-2:</b> two attackers run a 2-on-1 with the last defender.</li><li><b>2-v-1:</b> the winger cuts inside, the striker peels to the far post.</li></ul>',
     '<div class="sidebar green" style="margin-top:0.15in;"><h3>The numbers matter</h3><p style="font-size:8.5pt;margin:0;">3-v-2 breakaways convert at 35–40%. 2-v-1 breakaways convert at 50%+. The numerical advantage is a tactical advantage, not just a statistical one.</p></div>',
     "Breakaway shape", "Take the right option", "A breakaway fails when the carrier takes the wrong option. The right option is the one that arrives at the back post first."),
    (159, "Counter-attack finishing — composure in transition",
     '<p class="lead">The hardest part of a counter-attack is the <strong>finish</strong>. The player arrives with 30 yards of space, one defender backpedalling, and a crowd noise that drowns out the goalkeeper.</p>',
     '<h3 style="font-family:var(--serif);color:var(--green);font-size:13pt;margin:0.18in 0 0.07in;">Composure training</h3>\n<ul style="font-size:8.7pt;margin:0.08in 0 0 0.22in;line-height:1.42;"><li><b>Pick the spot early:</b> the shot should be chosen before the final pass.</li><li><b>Head up, last touch long:</b> a long touch gives the keeper less time.</li><li><b>Two finishing types:</b> low across the keeper, or chip into the far corner.</li></ul>',
     '<div class="sidebar navy" style="margin-top:0.15in;"><h3>The elite finisher</h3><p style="font-size:8.5pt;margin:0;">Counter-attack goals are usually simple finishes. The strikers who score them — Henry, Ronaldo, Vardy — make the right choice at speed.</p></div>',
     "Counter-attack finish", "Finish early", "The longer the dribble, the more defenders recover. The counter-attack finisher finishes early — or passes early — to keep the numbers in their favour."),
    (160, "Set plays and transitions — Section X summary",
     '<p class="lead">Section X has covered <strong>30 pages of tactical detail</strong>: corners, free kicks, throw-ins, build-up, defensive patterns, and counter-attacking. This page is the index and the principles.</p>',
     '<h3 style="font-family:var(--serif);color:var(--green);font-size:13pt;margin:0.18in 0 0.07in;">The five principles</h3>\n<ul style="font-size:8.7pt;margin:0.08in 0 0 0.22in;line-height:1.42;"><li><b>Set pieces are restarts with a plan.</b></li><li><b>Transitions are the most dangerous moments.</b></li><li><b>Numbers shape every decision.</b></li><li><b>Pressing is geometry, not effort.</b></li><li><b>Coaching detail beats talent.</b></li></ul>',
     '<div class="sidebar terracotta" style="margin-top:0.15in;"><h3>Section X complete</h3><p style="font-size:8.5pt;margin:0;">Pages 131–160 cover every tactical move in the modern game. Read them again with a manager’s eye: each diagram is a decision tree, each routine a rehearsed conversation.</p></div>',
     "Section X summary", "The book is now complete", "Section X closes the tactical spine of the book. From the equipment of Section II to the stadium culture of Section XI, every page aims for one thing — make the modern game legible."),
]


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    for entry in PAGES:
        num, title, lead, body, sidebar, kicker, fb_title, fb_body, *rest = entry
        caption = rest[0] if rest else ""
        diag_color = rest[1] if len(rest) > 1 else "#4c9b52"
        html_text = page(num, title, lead, body, sidebar, kicker, fb_title, fb_body,
                         caption=caption, diagram_color=diag_color)
        out_path = os.path.join(OUT_DIR, f"{num}-page.html")
        with open(out_path, "w") as f:
            f.write(html_text)
        print(f"wrote {out_path} ({len(html_text)} bytes)")
    print(f"\nDone — wrote {len(PAGES)} pages.")


if __name__ == "__main__":
    main()