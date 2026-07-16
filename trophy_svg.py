"""trophy_svg.py — A small World Cup trophy SVG for section dividers."""


def trophy(width=80):
    """Build a stylized World Cup trophy SVG."""
    return f'''<svg viewBox="0 0 100 120" width="{width}" xmlns="http://www.w3.org/2000/svg">
  <circle cx="50" cy="28" r="16" fill="#c9a961" stroke="#1a1612" stroke-width="1.5"/>
  <path d="M 36 22 Q 50 14 64 22" stroke="#1a1612" stroke-width="1" fill="none"/>
  <path d="M 36 34 Q 50 42 64 34" stroke="#1a1612" stroke-width="1" fill="none"/>
  <line x1="50" y1="14" x2="50" y2="42" stroke="#1a1612" stroke-width="1"/>
  <path d="M 44 44 L 56 44 L 54 56 L 46 56 Z" fill="#c9a961" stroke="#1a1612" stroke-width="1"/>
  <path d="M 36 56 L 64 56 L 68 64 L 64 72 L 36 72 L 32 64 Z" fill="#c9a961" stroke="#1a1612" stroke-width="1"/>
  <rect x="36" y="72" width="28" height="6" fill="#c9a961" stroke="#1a1612" stroke-width="1"/>
  <rect x="30" y="78" width="40" height="8" fill="#c9a961" stroke="#1a1612" stroke-width="1.5"/>
  <rect x="30" y="86" width="40" height="3" fill="#1a1612" opacity="0.3"/>
  <path d="M 26 89 L 74 89 L 76 94 L 24 94 Z" fill="#c9a961" stroke="#1a1612" stroke-width="1.5"/>
  <rect x="34" y="80" width="32" height="5" fill="#1a1612"/>
  <text x="50" y="84" text-anchor="middle" fill="#c9a961" font-family="Inter, sans-serif" font-size="3.5" font-weight="900">WORLD CUP</text>
  <path d="M 30 28 Q 26 22 30 14" stroke="#1a1612" stroke-width="2" fill="none"/>
  <path d="M 70 28 Q 74 22 70 14" stroke="#1a1612" stroke-width="2" fill="none"/>
</svg>'''
