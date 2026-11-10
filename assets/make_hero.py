"""Generate the profile header (dark and light).

Run:  python3 assets/make_hero.py
Writes assets/hero-dark.svg and assets/hero-light.svg. No dependencies.

The backgrounds match GitHub's own page colours, so the header sits flush
with the page instead of reading as a boxed image.
"""

from pathlib import Path

THEMES = {
    "dark": dict(bg="#0d1117", text="#f0f6fc", muted="#9198a1", rule="#3d444d", accent="#4493f8"),
    "light": dict(bg="#ffffff", text="#1f2328", muted="#59636e", rule="#d1d9e0", accent="#0969da"),
}

SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"

W, H = 1200, 300

FACTS = [
    ("Building", "Conductor"),
    ("Open source", "precedent, portparity"),
    ("Clients", "US, UK, EU, Australia"),
    ("Based", "Lahore, remote"),
]


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;")


def svg(t: dict) -> str:
    o = []
    a = o.append
    a(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
      f'role="img" aria-label="Muhammad Burhan Mujahid, Systems Architect for founders and business leaders.">')
    a(f'<rect width="{W}" height="{H}" fill="{t["bg"]}"/>')
    a(f'<g font-family="{SANS}">')

    # Left column
    a(f'<rect x="0" y="72" width="28" height="3" fill="{t["accent"]}"/>')
    a(f'<text x="0" y="140" font-size="50" font-weight="600" letter-spacing="-1.2" '
      f'fill="{t["text"]}">Muhammad Burhan Mujahid</text>')
    a(f'<text x="1" y="184" font-size="23" fill="{t["muted"]}">'
      f'Systems Architect for founders and business leaders.</text>')
    a(f'<text x="1" y="214" font-size="23" fill="{t["muted"]}">'
      f'AI agents, automation and custom software that hold up.</text>')

    # Divider
    a(f'<rect x="770" y="72" width="1" height="156" fill="{t["rule"]}"/>')

    # Right column: facts
    y = 92
    for k, v in FACTS:
        a(f'<text x="806" y="{y}" font-size="15" font-weight="600" letter-spacing="1.1" '
          f'fill="{t["muted"]}">{esc(k.upper())}</text>')
        a(f'<text x="946" y="{y}" font-size="21" fill="{t["text"]}">{esc(v)}</text>')
        y += 42

    # Bottom hairline
    a(f'<rect x="0" y="{H - 1}" width="{W}" height="1" fill="{t["rule"]}"/>')
    a("</g></svg>")
    return "\n".join(o) + "\n"


if __name__ == "__main__":
    here = Path(__file__).parent
    for name, theme in THEMES.items():
        (here / f"hero-{name}.svg").write_text(svg(theme), encoding="utf-8")
        print(f"wrote hero-{name}.svg")
