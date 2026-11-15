"""Builds the Science Over Hype static site. Run: python3 build.py"""
import os

SITE = "https://scienceoverhype.com"
# MailerLite embedded form endpoint (filled in once the MailerLite form exists)
ML_ACTION = os.environ.get("ML_ACTION", "https://assets.mailerlite.com/jsonp/2796942/forms/204186432875529452/subscribe")

HEAD = """<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{site}{path}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:image" content="{site}/assets/og.jpg"><meta property="og:url" content="{site}{path}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/favicon.png"><link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Gloock&family=Instrument+Serif:ital@0;1&family=Geist+Mono&family=Inter:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css">
</head><body>
<header class="site"><div class="wrap">
 <a class="logo" href="/" aria-label="Science Over Hype home"><img src="/assets/logoC-black.png" alt="Science Over Hype"></a>
 <nav><a href="/how-we-work/">How we work</a><a href="/about/">About</a><a class="cta" href="/sleep/">Free guide</a></nav>
</div></header>
"""

FOOT = """<footer class="site"><div class="wrap">
 <div class="row">
  <div><div class="tag">Hype nahi, science.</div><p style="margin-top:10px">Health, mind &amp; body, checked against real studies.</p></div>
  <div>
   <a href="https://www.instagram.com/thescienceoverhype/" target="_blank" rel="noopener">Instagram</a>
   <a href="https://www.youtube.com/@thescienceoverhype" target="_blank" rel="noopener">YouTube</a>
   <a href="https://x.com/scienceoverhype" target="_blank" rel="noopener">X</a>
   <a href="/privacy/">Privacy</a>
  </div>
 </div>
 <p class="fine">© 2026 Science Over Hype. Educational content only, not medical advice. Talk to a qualified doctor before changing medication, diet or supplements, especially if you have a health condition.</p>
</div></footer>
<script>
document.querySelectorAll('form.signup').forEach(function(f){
 f.addEventListener('submit',function(e){
  var action=f.getAttribute('action'); var msg=f.querySelector('.form-msg');
  if(!action||action==='#'){e.preventDefault();msg.textContent='Signups open very soon.';return;}
  e.preventDefault(); var b=f.querySelector('button'); b.disabled=true; b.textContent='Sending…';
  fetch(action,{method:'POST',body:new FormData(f)}).then(function(r){return r.json()}).then(function(d){
   if(d&&d.success){f.querySelectorAll('input,button').forEach(function(x){x.style.display='none'});f.querySelector('label.consent').style.display='none';
    msg.innerHTML='<strong>Almost done. Check your inbox.</strong> Tap the confirm button in our email, and your Sleep Reset arrives right after. (Not there in 2 minutes? Check Promotions or Spam.)';}
   else{b.disabled=false;b.textContent='Send me the free guide';msg.textContent='Something went wrong. Please check your email and try again.';}
  }).catch(function(){b.disabled=false;b.textContent='Send me the free guide';msg.textContent='Something went wrong. Please try again.';});
 });
});
</script>
</body></html>
"""

def form(dark=False):
    return f"""<form class="signup" action="{ML_ACTION or '#'}" method="post">
 <input type="text" name="fields[name]" placeholder="First name" autocomplete="given-name">
 <input type="email" name="fields[email]" placeholder="Email" required autocomplete="email">
 <label class="consent"><input type="checkbox" name="gdpr[]" value="consent" required><span>I agree to receive emails from Science Over Hype. Unsubscribe anytime. See our <a href="/privacy/">privacy policy</a>.</span></label>
 <input type="hidden" name="ml-submit" value="1"><input type="hidden" name="anticsrf" value="true">
 <button type="submit">Send me the free guide</button>
 <div class="form-msg" role="status"></div>
</form>"""

PAGES = {}

PAGES["/"] = ("Science Over Hype | Health, mind & body, checked against real studies",
 "Short, evidence-based health content on sleep, food, blood sugar, habits and supplements. Every claim comes with its source. Hype nahi, science.",
 f"""
<section class="dark hero"><div class="wrap">
 <img class="logo-big" src="/assets/logoC-full-white.png" alt="Science Over Hype">
 <div class="k">What studies say</div>
 <h1 style="margin-top:14px">Health, mind &amp; body,<br><span class="it">checked against real studies.</span></h1>
 <p class="lead">The internet gives you a thousand health tips and very little proof. We read the research on sleep, food, blood sugar, focus, habits and supplements, and turn it into simple things you can actually do. What works, we show you how. What doesn't, we call it hype.</p>
 <a class="btn solid" href="/sleep/">Get the free 7-Day Sleep Reset</a>
 <a class="btn" href="https://www.instagram.com/thescienceoverhype/" target="_blank" rel="noopener">Follow on Instagram</a>
</div></section>

<section><div class="wrap">
 <div class="k">Every week</div>
 <h2 style="margin-top:12px">Three videos. One standard.</h2>
 <div class="grid3">
  <div class="card"><div class="day">MONDAY · VERDICT</div><h3>A viral claim, judged.</h3><p>21 days to build a habit? Detox drinks? We check the studies and stamp it.</p>
   <span class="stamp">SCIENCE</span><span class="stamp">PARTLY</span><span class="stamp">HYPE</span></div>
  <div class="card"><div class="day">WEDNESDAY · GUIDE</div><h3>A real problem, solved.</h3><p>Sleep, focus, blood sugar, stress: why it matters, and the habits the research actually supports.</p></div>
  <div class="card"><div class="day">FRIDAY · SUPPLEMENT FILE</div><h3>One supplement, the full evidence.</h3><p>What it does, who may need it, how strong the evidence is, and when to skip it. Test first, never megadose.</p></div>
 </div>
</div></section>

<section class="dark"><div class="wrap">
 <div class="k">The kind of thing we cover</div>
 <div class="stats">
  <div><div class="big">66</div><p>days on average for a new habit to feel automatic, not 21.</p><div class="src">Lally et al. · Eur J Soc Psychol · 2010</div></div>
  <div><div class="big">4.2×</div><p>more likely to catch a cold when sleeping under 6 hours a night.</p><div class="src">Prather et al. · Sleep · 2015</div></div>
  <div><div class="big">67%</div><p>of Indian adults across 39 studies had low vitamin D (below 20 ng/mL).</p><div class="src">Siddiqee et al. · BMC Public Health · 2021</div></div>
 </div>
</div></section>

<section><div class="wrap split">
 <div>
  <div class="k">Free guide</div>
  <h2 style="margin-top:12px">The 7-Day Sleep Reset</h2>
  <p class="it" style="font-size:24px">One small change a day. Backed by research, not hype.</p>
  <p>Seven habits, each tested in real studies, with a daily tracker and every source listed.</p>
  {form()}
 </div>
 <a href="/sleep/"><img src="/assets/sleep-reset-mockup.png" alt="The 7-Day Sleep Reset guide"></a>
</div></section>
""")

PAGES["/sleep/"] = ("Free 7-Day Sleep Reset | Science Over Hype",
 "7 science-backed sleep habits, one per day. A free guide from Science Over Hype with a daily tracker and every source listed.",
 f"""
<section><div class="wrap split">
 <div>
  <div class="k">Free guide · What studies say</div>
  <h1 style="margin-top:14px">The 7-Day<br>Sleep Reset</h1>
  <p class="it" style="font-size:26px;margin-top:10px">One small change a day. Backed by research, not hype.</p>
  <p style="margin-top:18px">Most of us sleep 6 hours and call it normal. Studies show what that costs: more hunger, weaker immunity and slower thinking, often without you noticing. This free guide gives you <strong>7 habits, one per day</strong>, each one tested in real studies:</p>
  <ul class="ticks">
   <li>The one wake-up rule that anchors your body clock</li>
   <li>The morning habit that makes you sleepy at the right time</li>
   <li>The caffeine cutoff most people get wrong</li>
   <li>What scrolling in bed really does (it's not just blue light)</li>
   <li>A 5-minute trick for a racing mind</li>
  </ul>
  <p>Plus a daily tracker, and every source listed.</p>
  {form()}
  <p style="font-size:13px;color:var(--grey);margin-top:14px">Educational only, not medical advice. We'll never share your email.</p>
 </div>
 <img src="/assets/sleep-reset-mockup.png" alt="Pages from the 7-Day Sleep Reset guide">
</div></section>
""")

PAGES["/how-we-work/"] = ("How we work | Science Over Hype",
 "Our evidence standards: how we read studies, how we give verdicts, and the rules we never break.",
 """
<section><div class="wrap prose">
 <div class="k">Our standards</div>
 <h1 style="margin-top:14px">How we work</h1>
 <p class="it" style="font-size:24px">Every claim gets checked. Every source gets shown.</p>
 <h2>What we make</h2>
 <ul>
  <li><strong>Verdict (Mon):</strong> a viral health claim, judged against the research: SCIENCE, PARTLY or HYPE.</li>
  <li><strong>Guide (Wed):</strong> a real-life problem, why it matters, and the habits the evidence supports.</li>
  <li><strong>Supplement File (Fri):</strong> one supplement: what it does, who may need it, how strong the evidence is, and safety.</li>
  <li><strong>Carousels (Tue, Thu, Sat):</strong> one topic, one point per slide, a source on every slide.</li>
 </ul>
 <h2>How we read research</h2>
 <ul>
  <li>We prefer reviews, meta-analyses and randomised trials in humans over single small studies.</li>
  <li>We say how big an effect is, not just whether one exists. "Modest" and "we don't know yet" are allowed answers.</li>
  <li>We point out when a number depends on a definition (like a deficiency cut-off) or comes from a small or short study.</li>
  <li>Every claim shows its source on screen, and full references are listed.</li>
 </ul>
 <h2>Rules we don't break</h2>
 <ul>
  <li>No disease claims. Food and supplements don't "cure" or "reverse" conditions.</li>
  <li>No fear-selling, no fake urgency, no AI images of real people.</li>
  <li>Honest verdicts even when the evidence is weak, including on things people love.</li>
  <li>If we ever sell our own products, we'll say so clearly, and show the same evidence we'd show for anyone else's.</li>
 </ul>
 <h2>Not medical advice</h2>
 <p>We explain research so you can make better everyday choices. We're not your doctor. If you have a health condition, take medication or are pregnant, talk to a qualified doctor before changing anything.</p>
 <p>Found a mistake? Tell us at <a href="mailto:thescienceoverhype@gmail.com">thescienceoverhype@gmail.com</a>. We correct errors openly.</p>
</div></section>
""")

PAGES["/about/"] = ("About | Science Over Hype",
 "Science Over Hype is run by Nitish Vaibhav: short, evidence-based health content for people who want proof, not hype.",
 """
<section><div class="wrap prose">
 <div class="k">About</div>
 <h1 style="margin-top:14px">Hi, I'm Nitish.</h1>
 <p class="it" style="font-size:24px">Science Over Hype started with my own blood report.</p>
 <p>I moved into a hostel after my 10th standard, and that's where the junk food years began. Through school and then college in Bangalore, I ate whatever was quick and cheap, and never thought about it.</p>
 <p>By 2019, in my mid-twenties, I was constantly low on energy. That's when I got my first proper blood test. The results: <strong>prediabetic, with high cholesterol</strong>. I was young, and I'd assumed this was something that happens to other people, much later.</p>
 <p>So I started experimenting on myself: food, sleep, movement, my mindset. Like many people, I also went looking for a magic supplement. What I found instead was a market full of cheap, overhyped products. So I started importing from trusted international brands, which cost me a fortune once you add import duties and taxes, and I started reading the research papers behind every ingredient.</p>
 <p>Years of trial, error and reading later, my reports are back in the normal range. The biggest lesson surprised me: it wasn't one miracle product. Supplements alone can't fix you from the inside. At best, they fill the gaps in what you're missing. The real change came from simple, consistent habits and the right food, with a few well-chosen supplements filling those gaps, all backed by evidence.</p>
 <p>That's what Science Over Hype is about. We read the research on sleep, food, blood sugar, focus, habits and supplements, and turn it into simple things you can actually do, with every source shown. When something works, we show you how. When it doesn't, we call it hype.</p>
 <p style="font-size:14px;color:var(--grey)">This is my personal story, not a treatment plan. If you have prediabetes, diabetes or high cholesterol, work with your doctor.</p>
 <h2>Where this is going</h2>
 <p>Science Over Hype is building a community of people who want to get healthier with evidence, not marketing. Over time, that means free guides and challenges, deeper long-form videos, and eventually programs and products held to the same standard as everything we publish.</p>
 <p>Follow along on <a href="https://www.instagram.com/thescienceoverhype/" target="_blank" rel="noopener">Instagram</a> and <a href="https://www.youtube.com/@thescienceoverhype" target="_blank" rel="noopener">YouTube</a>, or start with the <a href="/sleep/">free 7-Day Sleep Reset</a>.</p>
 <p style="margin-top:30px">Nitish Vaibhav<br><span class="it" style="font-size:22px">Hype nahi, science.</span></p>
</div></section>
""")

PAGES["/privacy/"] = ("Privacy policy | Science Over Hype",
 "How Science Over Hype collects, uses and protects your personal data.",
 """
<section><div class="wrap prose">
 <div class="k">Last updated: 15 November 2026</div>
 <h1 style="margin-top:14px">Privacy policy</h1>
 <p>This policy explains how Science Over Hype ("we", "us") handles your personal data when you use scienceoverhype.com or sign up for our emails.</p>
 <h2>What we collect</h2>
 <ul>
  <li><strong>When you sign up:</strong> your first name (optional) and email address, plus the date and the page you signed up from.</li>
  <li><strong>When you read our emails:</strong> whether an email was opened and which links were clicked, so we can improve our content.</li>
  <li><strong>When you write to us:</strong> whatever you choose to include in your message.</li>
 </ul>
 <p>We don't collect payment details, health records or sensitive personal data through this website.</p>
 <h2>Why we use it</h2>
 <ul>
  <li>To send you the free guide you asked for and the emails you agreed to receive.</li>
  <li>To understand which content is useful, and to reply when you write to us.</li>
 </ul>
 <p>We use your data only with your consent, which you give by ticking the box when you sign up. You can withdraw it at any time.</p>
 <h2>Who processes it</h2>
 <p>Our email list is managed by MailerLite (MailerLite UAB), which stores and sends emails on our behalf under its own security and privacy standards. We don't sell, rent or share your data with anyone for their own marketing.</p>
 <h2>How long we keep it</h2>
 <p>We keep your data while you're subscribed. If you unsubscribe, we stop emailing you, and you can ask us to delete your data completely.</p>
 <h2>Your rights</h2>
 <ul>
  <li>Unsubscribe anytime using the link at the bottom of every email.</li>
  <li>Ask to see, correct or delete the data we hold about you.</li>
  <li>Raise a concern with us about how your data is handled.</li>
 </ul>
 <h2>Contact</h2>
 <p>Email <a href="mailto:thescienceoverhype@gmail.com">thescienceoverhype@gmail.com</a> for any privacy request. We aim to respond within 7 days.</p>
</div></section>
""")

for path, (title, desc, body) in PAGES.items():
    out = "index.html" if path == "/" else path.strip("/") + "/index.html"
    with open(out, "w") as f:
        f.write(HEAD.format(title=title, desc=desc, site=SITE, path=path) + body + FOOT)
open("CNAME", "w").write("scienceoverhype.com\n")
open("404.html", "w").write(HEAD.format(title="Not found | Science Over Hype", desc="Page not found.", site=SITE, path="/404") +
  '<section><div class="wrap"><div class="k">404</div><h1 style="margin-top:14px">Not found.</h1><p class="it" style="font-size:24px">Unlike most health claims, this one is simply missing.</p><a class="btn solid" href="/">Go home</a></div></section>' + FOOT)
print("built", list(PAGES))
