"""Generate the profile hero banners (dark and light).

Run:  python3 assets/make_hero.py
Writes assets/hero-dark.svg and assets/hero-light.svg. No dependencies.
"""

from pathlib import Path

THEMES = {
    "dark": dict(
        bg="#0d1117", panel="#161b22", grid="#21262d", border="#30363d",
        text="#e6edf3", muted="#8b949e", accent="#58a6ff",
        act="#3fb950", wait="#d29922", stop="#f85149", glow="0.35",
    ),
    "light": dict(
        bg="#ffffff", panel="#f6f8fa", grid="#eaeef2", border="#d0d7de",
        text="#1f2328", muted="#59636e", accent="#0969da",
        act="#1a7f37", wait="#9a6700", stop="#cf222e", glow="0.18",
    ),
}

SANS = "ui-sans-serif, -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"

TOOLS = ["Shopify", "Slack", "Notion", "CRM", "Gmail"]
OUTCOMES = [("ACT", "act"), ("NEEDS APPROVAL", "wait"), ("ESCALATE", "stop")]

W, H = 1200, 400
HUB_X, HUB_Y = 905, 200


def svg(t: dict) -> str:
    out = []
    a = out.append
    a(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
      f'role="img" aria-label="Muhammad Burhan Mujahid. Systems Architect. I build AI agents, '
      f'automation and custom software, and fix the systems slowing your business down.">')
    a("<defs>")
    a(f'<pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">'
      f'<path d="M32 0H0V32" fill="none" stroke="{t["grid"]}" stroke-width="1"/></pattern>')
    a(f'<radialGradient id="glow" cx="0.76" cy="0.5" r="0.45">'
      f'<stop offset="0" stop-color="{t["accent"]}" stop-opacity="{t["glow"]}"/>'
      f'<stop offset="1" stop-color="{t["accent"]}" stop-opacity="0"/></radialGradient>')
    a(f'<linearGradient id="fade" x1="0" x2="1"><stop offset="0" stop-color="{t["bg"]}"/>'
      f'<stop offset="0.55" stop-color="{t["bg"]}" stop-opacity="0.92"/>'
      f'<stop offset="1" stop-color="{t["bg"]}" stop-opacity="0"/></linearGradient>')
    a("</defs>")
    a("<style>"
      "@keyframes spin{to{transform:rotate(360deg)}}"
      ".ring{transform-origin:%dpx %dpx;animation:spin 18s linear infinite}"
      "@keyframes blink{0%%,49%%{opacity:1}50%%,100%%{opacity:0}}"
      ".caret{animation:blink 1.1s step-end infinite}"
      "@media (prefers-reduced-motion:reduce){*{animation:none!important}}"
      "</style>" % (HUB_X, HUB_Y))

    # Background
    a(f'<rect width="{W}" height="{H}" rx="18" fill="{t["bg"]}"/>')
    a(f'<rect width="{W}" height="{H}" rx="18" fill="url(#grid)"/>')
    a(f'<rect width="{W}" height="{H}" rx="18" fill="url(#glow)"/>')
    a(f'<rect width="660" height="{H}" rx="18" fill="url(#fade)"/>')
    a(f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="18" fill="none" stroke="{t["border"]}"/>')

    # Left: identity
    a(f'<g font-family="{SANS}">')
    a(f'<text x="64" y="96" font-family="{MONO}" font-size="14" letter-spacing="2.4" '
      f'fill="{t["accent"]}">SYSTEMS ARCHITECT  /  FOUNDER, CONDUCTOR</text>')
    a(f'<text x="62" y="152" font-size="42" font-weight="700" fill="{t["text"]}" '
      f'letter-spacing="-0.8">Muhammad Burhan Mujahid</text>')
    a(f'<text x="64" y="200" font-size="20" fill="{t["muted"]}">'
      f'I build AI agents, automation and custom software,</text>')
    a(f'<text x="64" y="228" font-size="20" fill="{t["muted"]}">'
      f'and fix the systems slowing your business down.</text>')

    # Terminal line
    a(f'<g font-family="{MONO}" font-size="15">')
    a(f'<rect x="64" y="262" width="392" height="40" rx="8" fill="{t["panel"]}" stroke="{t["border"]}"/>')
    a(f'<text x="82" y="287" fill="{t["muted"]}">$ <tspan fill="{t["text"]}">ship</tspan> '
      f'--scope honest --handover clean</text>')
    a(f'<rect class="caret" x="434" y="273" width="9" height="18" fill="{t["accent"]}"/>')
    a("</g>")

    # Pills
    x = 64
    a(f'<g font-size="13" font-weight="600">')
    for label in ["Lahore, Pakistan", "Remote worldwide", "Clients in US, UK, EU, AU"]:
        w = int(len(label) * 7.6) + 28
        a(f'<rect x="{x}" y="326" width="{w}" height="28" rx="14" fill="none" stroke="{t["border"]}"/>')
        a(f'<text x="{x + w/2}" y="345" text-anchor="middle" fill="{t["muted"]}">{label}</text>')
        x += w + 10
    a("</g></g>")

    # Right: systems diagram
    a(f'<g font-family="{MONO}" font-size="13" font-weight="600">')
    tool_x, tool_w, tool_h = 690, 104, 32
    ys = [88 + i * 56 for i in range(len(TOOLS))]
    for i, (name, y) in enumerate(zip(TOOLS, ys)):
        cy = y + tool_h / 2
        d = f"M{tool_x + tool_w} {cy} C {tool_x + tool_w + 60} {cy}, {HUB_X - 90} {HUB_Y}, {HUB_X - 50} {HUB_Y}"
        a(f'<path id="in{i}" d="{d}" fill="none" stroke="{t["border"]}" stroke-width="1.5"/>')
        a(f'<circle r="3.5" fill="{t["accent"]}"><animateMotion dur="{2.6 + i*0.35:.2f}s" '
          f'begin="{i*0.5:.1f}s" repeatCount="indefinite"><mpath href="#in{i}"/></animateMotion></circle>')
        a(f'<rect x="{tool_x}" y="{y}" width="{tool_w}" height="{tool_h}" rx="7" fill="{t["panel"]}" stroke="{t["border"]}"/>')
        a(f'<text x="{tool_x + tool_w/2}" y="{y + 21}" text-anchor="middle" fill="{t["text"]}">{name}</text>')

    out_x, out_w, out_h = 1010, 160, 32
    oys = [124, 184, 244]
    for i, ((label, key), y) in enumerate(zip(OUTCOMES, oys)):
        cy = y + out_h / 2
        d = f"M{HUB_X + 50} {HUB_Y} C {HUB_X + 80} {HUB_Y}, {out_x - 40} {cy}, {out_x} {cy}"
        a(f'<path id="out{i}" d="{d}" fill="none" stroke="{t["border"]}" stroke-width="1.5"/>')
        a(f'<circle r="3.5" fill="{t[key]}"><animateMotion dur="2.2s" begin="{1 + i*0.7:.1f}s" '
          f'repeatCount="indefinite"><mpath href="#out{i}"/></animateMotion></circle>')
        a(f'<rect x="{out_x}" y="{y}" width="{out_w}" height="{out_h}" rx="16" fill="{t["bg"]}" stroke="{t[key]}" stroke-width="1.5"/>')
        a(f'<circle cx="{out_x + 18}" cy="{cy}" r="4.5" fill="{t[key]}"/>')
        a(f'<text x="{out_x + 32}" y="{y + 21}" fill="{t[key]}" letter-spacing="0.6">{label}</text>')

    # Hub
    a(f'<circle class="ring" cx="{HUB_X}" cy="{HUB_Y}" r="62" fill="none" stroke="{t["accent"]}" '
      f'stroke-width="1.5" stroke-dasharray="4 9" opacity="0.8"/>')
    a(f'<circle cx="{HUB_X}" cy="{HUB_Y}" r="48" fill="{t["panel"]}" stroke="{t["accent"]}" stroke-width="2"/>')
    a(f'<text x="{HUB_X}" y="{HUB_Y - 3}" text-anchor="middle" font-size="15" fill="{t["text"]}">agent</text>')
    a(f'<text x="{HUB_X}" y="{HUB_Y + 16}" text-anchor="middle" font-size="10" font-weight="500" '
      f'fill="{t["muted"]}">+ policy gate</text>')
    a(f'<text x="930" y="378" text-anchor="middle" font-size="11" font-weight="500" '
      f'letter-spacing="1.5" fill="{t["muted"]}">YOUR TOOLS  ->  ONE SYSTEM  ->  SAFE ACTIONS</text>')
    a("</g>")

    a("</svg>")
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    here = Path(__file__).parent
    for name, theme in THEMES.items():
        (here / f"hero-{name}.svg").write_text(svg(theme), encoding="utf-8")
        print(f"wrote hero-{name}.svg")
