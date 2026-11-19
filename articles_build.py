"""Renders /research/ pages, the research index, sitemap.xml and robots.txt."""
import json, os, html
from research import ARTICLES, AUTHOR

def esc(s): return html.escape(s, quote=True)
def human(d):
    import datetime as dt
    return dt.date.fromisoformat(d).strftime("%-d %b %Y")

STAMP = {"SCIENCE": "SCIENCE", "PARTLY": "PARTLY", "HYPE": "HYPE", "WHAT HELPS": "WHAT HELPS"}

def related_cards(a, by_slug):
    out = []
    for r in a["related"]:
        if r == "7-day-sleep-reset":
            continue
        b = by_slug.get(r)
        if b: out.append(f'<a class="rel" href="/research/{b["slug"]}/"><span class="k">{b["series"]} · #{b["num"]}</span><span class="rt">{esc(b["title"])}</span></a>')
    return "".join(out)

def ld(a, site):
    url = f"{site}/research/{a['slug']}/"
    graph = [
      {"@type": "Article", "@id": url + "#article", "headline": a["title"], "description": a["desc"],
       "datePublished": a["reviewed"], "dateModified": a["reviewed"], "inLanguage": "en-IN",
       "mainEntityOfPage": url, "image": site + "/assets/og.jpg", "keywords": ", ".join(a["keywords"]),
       "author": {"@type": "Person", "@id": site + "/about/#nitish", "name": AUTHOR["name"], "url": site + AUTHOR["url"]},
       "publisher": {"@id": site + "/#org"},
       "citation": [u for _, u in a["sources"] if u]},
      {"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": ans}} for q, ans in a["faq"]]},
      {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": site + "/"},
        {"@type": "ListItem", "position": 2, "name": "Research", "item": site + "/research/"},
        {"@type": "ListItem", "position": 3, "name": a["title"], "item": url}]},
      {"@type": "Organization", "@id": site + "/#org", "name": "Science Over Hype", "url": site + "/",
       "logo": site + "/assets/logo-black.png"},
    ]
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": graph}) + "</script>\n"

def page(a, by_slug, form):
    secs = "".join(f"<h2>{esc(h)}</h2>{body}" for h, body in a["sections"])
    faq = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(ans)}</p></details>" for q, ans in a["faq"])
    srcs = "".join(f'<li>{esc(t)}' + (f' <a href="{u}" target="_blank" rel="noopener">Link ↗</a>' if u else "") + "</li>" for t, u in a["sources"])
    rel = related_cards(a, by_slug)
    return f"""
<article class="research"><div class="wrap prose">
 <div class="crumbs k"><a href="/research/">Research</a> · {a["series"]} · #{a["num"]}</div>
 <h1>{esc(a['title'])}</h1>
 <p class="meta">By <a href="{AUTHOR['url']}">{AUTHOR['name']}</a> · Last reviewed {human(a['reviewed'])} · Educational, not medical advice</p>
 <div class="verdict"><div class="vlabel k">The short answer</div><span class="stamp">{STAMP[a['verdict']]}</span><p>{esc(a['verdict_text'])}</p></div>
 {secs}
 <h2>Frequently asked questions</h2>
 <div class="faq">{faq}</div>
 <h2>Sources</h2>
 <ol class="sources">{srcs}</ol>
 <div class="author"><div class="k">About the author</div><p><strong><a href="{AUTHOR['url']}">{AUTHOR['name']}</a></strong>: {esc(AUTHOR['bio'])}</p></div>
 <div class="cta-box"><div class="k">Free guide</div><h3>The 7-Day Sleep Reset</h3><p>One small change a day, every one backed by a study.</p>{form()}</div>
 {('<h2>Read next</h2><div class="rels">' + rel + '</div>') if rel else ''}
</div></article>
"""

def index(arts):
    cards = "".join(
        f'<a class="card rcard" href="/research/{a["slug"]}/"><div class="day">{a["series"].upper()} · #{a["num"]}</div>'
        f'<h3>{esc(a["title"])}</h3><span class="stamp small">{STAMP[a["verdict"]]}</span><p>{esc(a["desc"])}</p></a>'
        for a in sorted(arts, key=lambda a: a["num"], reverse=True))
    return f"""
<section><div class="wrap">
 <div class="k">Research</div>
 <h1 style="margin-top:12px">Health claims,<br><span class="it">checked against real studies.</span></h1>
 <p class="lead-dark" style="max-width:640px;margin-top:18px">Every video we make gets a full write-up here: the short answer first, then what the studies found, their limits, and links to every source.</p>
 <div class="grid3">{cards}</div>
</div></section>
"""

def build(HEAD, FOOT, SITE, form, static_paths):
    by_slug = {a["slug"]: a for a in ARTICLES}
    for a in ARTICLES:
        path = f"/research/{a['slug']}/"
        os.makedirs(path.strip("/"), exist_ok=True)
        with open(path.strip("/") + "/index.html", "w") as f:
            f.write(HEAD.format(title=f"{a['title']} | Science Over Hype", desc=esc(a["desc"]), site=SITE, path=path, extra=ld(a, SITE))
                    + page(a, by_slug, form) + FOOT)
    os.makedirs("research", exist_ok=True)
    with open("research/index.html", "w") as f:
        f.write(HEAD.format(title="Research: health claims checked against real studies | Science Over Hype",
                            desc="Evidence write-ups on sleep, blood sugar, habits and supplements, with a short answer first and every source linked.",
                            site=SITE, path="/research/", extra="") + index(ARTICLES) + FOOT)
    # sitemap + robots
    urls = [(p, None) for p in static_paths] + [("/research/", None)] + [(f"/research/{a['slug']}/", a["reviewed"]) for a in ARTICLES]
    items = "".join(f"<url><loc>{SITE}{p}</loc>" + (f"<lastmod>{d}</lastmod>" if d else "") + "</url>" for p, d in urls)
    open("sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + items + "</urlset>\n")
    open("robots.txt", "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
