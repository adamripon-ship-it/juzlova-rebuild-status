"""Cocoa product page blocks — sensory radar, applications, nutrition."""
import html as H
import math


def esc(s):
    return H.escape(str(s), quote=True)


def cocoa_sensory_html(show):
    axes = show.get("axes") or []
    if not axes:
        return ""
    n = len(axes)
    cx = cy = 140
    r_max = 86
    rings = []
    for frac in (0.28, 0.55, 0.82, 1.0):
        rings.append(
            f'<circle class="ring" cx="{cx}" cy="{cy}" r="{r_max * frac:.1f}"/>')
    spokes = []
    labels = []
    pts = []
    legend = []
    for i, ax in enumerate(axes):
        name, val = ax["label"], ax["value"]
        ang = -math.pi / 2 + i * 2 * math.pi / n
        cos_a, sin_a = math.cos(ang), math.sin(ang)
        spokes.append(
            f'<line class="spoke" x1="{cx}" y1="{cy}" '
            f'x2="{cx + r_max * cos_a:.1f}" y2="{cy + r_max * sin_a:.1f}"/>')
        rr = r_max * (max(0, min(val, 100)) / 100)
        pts.append(f"{cx + rr * cos_a:.1f},{cy + rr * sin_a:.1f}")
        lx = cx + (r_max + 26) * cos_a
        ly = cy + (r_max + 26) * sin_a
        anchor = "middle"
        if cos_a > 0.35:
            anchor = "start"
        elif cos_a < -0.35:
            anchor = "end"
        labels.append(
            f'<text class="axis" text-anchor="{anchor}" x="{lx:.1f}" y="{ly:.1f}">'
            f'{esc(name)}</text>')
        legend.append(
            f'<li><span>{esc(name)}</span><strong>{val}</strong></li>')
    poly = " ".join(pts)
    return f"""<section class="cocoa-block cocoa-sense rv" data-cocoa-anim aria-labelledby="cocoa-sense-h">
<h2 id="cocoa-sense-h">{esc(show.get("sensory_h", ""))}</h2>
<p class="cocoa-lead">{esc(show.get("sensory_lead", ""))}</p>
<div class="cocoa-sense-grid">
<figure class="cocoa-radar" aria-hidden="true">
<svg viewBox="0 0 280 280" width="280" height="280" focusable="false">
<g class="grid">{"".join(rings)}{"".join(spokes)}</g>
<polygon class="poly" points="{poly}"/>
<circle class="hub" cx="{cx}" cy="{cy}" r="4"/>
{"".join(labels)}
</svg>
</figure>
<ul class="cocoa-legend">{"".join(legend)}</ul>
</div>
</section>"""


def cocoa_apps_html(show):
    apps = show.get("apps") or []
    if not apps:
        return ""
    cards = "".join(
        f'<li class="cocoa-app"><h3>{esc(a["title"])}</h3><p>{esc(a["text"])}</p></li>'
        for a in apps)
    return f"""<section class="cocoa-block cocoa-apps rv" aria-labelledby="cocoa-apps-h">
<h2 id="cocoa-apps-h">{esc(show.get("apps_h", ""))}</h2>
<ul class="cocoa-app-grid">{cards}</ul>
</section>"""


def cocoa_nutrition_html(show):
    bars = show.get("bars") or []
    if not bars:
        return ""
    rows = ""
    for b in bars:
        pct = max(0, min(int(b["pct"]), 100))
        rows += (
            f'<div class="cocoa-nbar" style="--w:{pct}%">'
            f'<div class="cocoa-nbar-top"><span>{esc(b["label"])}</span>'
            f'<strong>{esc(b["text"])}</strong></div>'
            f'<div class="cocoa-nbar-track" role="meter" aria-label="{esc(b["label"])}" '
            f'aria-valuemin="0" aria-valuemax="100" aria-valuenow="{pct}">'
            f'<i class="fill"></i></div></div>'
        )
    extras = ""
    if show.get("nutri_extra"):
        extras = f'<p class="cocoa-extra">{esc(show["nutri_extra"])}</p>'
    note = ""
    if show.get("nutri_note"):
        note = f'<p class="cocoa-note">{esc(show["nutri_note"])}</p>'
    return f"""<section class="cocoa-block cocoa-nutri rv" data-cocoa-anim aria-labelledby="cocoa-nutri-h">
<h2 id="cocoa-nutri-h">{esc(show.get("nutri_h", ""))}</h2>
<p class="cocoa-lead">{esc(show.get("nutri_lead", ""))}</p>
<div class="cocoa-bars">{rows}</div>
{extras}{note}
</section>"""


def cocoa_facts_html(show):
    facts = show.get("facts") or []
    if not facts:
        return ""
    items = "".join(
        f'<li><span>{esc(f["label"])}</span><strong>{esc(f["value"])}</strong></li>'
        for f in facts)
    return f"""<section class="cocoa-block cocoa-facts rv" aria-labelledby="cocoa-facts-h">
<h2 id="cocoa-facts-h">{esc(show.get("facts_h", ""))}</h2>
<ul class="cocoa-fact-grid">{items}</ul>
</section>"""
