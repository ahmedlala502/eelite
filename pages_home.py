# -*- coding: utf-8 -*-
from build import page, ICONS
from assets_map import SERVICE_IMAGES, BRAND_LOGOS


def _slug(text):
    out = []
    for ch in text.lower():
        out.append(ch if ch.isalnum() else '-')
    return '-'.join(x for x in ''.join(out).split('-') if x)

MARQUEE_A = ["Morini Riyadh","Rüya","Beefbar","ROKA KSA","The Beauty Secrets","Panerai","TAG Heuer",
             "Ted Baker","Maje","Crocs","Coya","Bagatelle"]
MARQUEE_B = ["Jones the Grocer","Sumosan","MNKY HSE","Tashas Cafe","Signor Sassi","San Carlo",
             "MYAZŪ","Urth Caffe","Vero Moda","Kiko","Fred","Solitaire"]

def chips(names):
    # Real brand logos where available; text wordmark fallback otherwise.
    out = []
    for n in names:
        logo = BRAND_LOGOS.get(n)
        if logo:
            out.append(
                f'<span class="logo-chip" role="img" aria-label="{n}" title="{n}">'
                f'<img src="{logo}" alt="{n}" loading="lazy" decoding="async"></span>')
        else:
            out.append(
                f'<span class="logo-chip logo-chip--fallback" role="img" aria-label="{n}" title="{n}">'
                f'<span aria-hidden="true">{n}</span></span>')
    return "".join(out)

SERVICES = [
 ("01","Influencer","Discovery",
  "Tap into our vast network to connect with influencers who perfectly match your brand and audience, boosting engagement and brand affinity.", "search", 1),
 ("02","Campaign","Strategy",
  "Work with our experts to design influencer campaigns aligned with your goals, ensuring impactful results and brand resonance.", "target", 2),
 ("03","Content","Creation",
  "Collaborate with influencers to create compelling content that captivates your audience and drives action.", "spark", 3),
 ("04","Performance","Tracking",
  "Gain actionable insights into campaign performance, optimizing strategies for maximum impact and ROI.", "chart", 4),
]

def service_cards():
    out = []
    for num, top, bottom, copy, icon, art in SERVICES:
        img = SERVICE_IMAGES.get(_slug(top + "-" + bottom))
        visual = (f'<img src="{img}" alt="" loading="lazy" decoding="async">'
                  if img else f'<div class="art art--{art}"></div>')
        out.append(f"""
        <article class="service-card reveal" data-delay="{art}">
          <div class="service-card__visual">
            {visual}
            <span class="service-card__num">{num}</span>
            <span class="service-card__label"><b data-tr="svc.{num}.top">{top}</b><span data-tr="svc.{num}.bottom">{bottom}</span></span>
          </div>
          <div class="service-card__body">
            <p>{copy}</p>
            <a class="link-arrow" href="contacts.html">Talk to us {ICONS['arrow']}</a>
          </div>
        </article>""")
    return "".join(out)

STORIES = [
 ("Mr.Chow","United Arab Emirates","60M","+569", 1),
 ("A.O.K Kitchen","Saudi Arabia","40M","+309", 2),
 ("Enigmaku","Kuwait","24.9M","+186", 3),
]

def story_cards():
    out = []
    for i,(name, place, reach, infl, art) in enumerate(STORIES, start=1):
        out.append(f"""
        <a class="story reveal" data-delay="{i}" href="case-studies.html" aria-label="{name} — success story">
          <div class="story__media"><div class="art art--{art+3}"></div></div>
          <span class="story__play" aria-hidden="true">{ICONS['play']}</span>
          <div class="story__meta">
            <span class="name">{name}</span>
            <span class="place">{place}</span>
            <div class="story__stats">
              <div>Reach<b>{reach}</b></div>
              <div>Creators<b>{infl}</b></div>
            </div>
          </div>
        </a>""")
    return "".join(out)

VALUE = [
 ("shield","A decade of excellence","Over 10 years running influencer campaigns for high-end brands — the playbook is already written."),
 ("globe","Global reach","A presence in more than 52 countries connects your brand with the right audience, wherever it lives."),
 ("users","Elite partnerships","Exclusive relationships with elite creators and premium brands mean access others simply don't have."),
 ("trend","Measurable results","Every campaign is tracked end to end, so growth is something you can see — not something you're told."),
]

def value_cards():
    out=[]
    for i,(icon,title,copy) in enumerate(VALUE, start=1):
        out.append(f"""
        <article class="card card--hover reveal" data-delay="{i}">
          <div class="card__icon">{ICONS[icon]}</div>
          <h3 class="h4 card__title">{title}</h3>
          <p class="muted" style="font-size:.97rem">{copy}</p>
        </article>""")
    return "".join(out)


BODY = f"""
<main id="main">

  <!-- ── HERO ───────────────────────────────────────────────────────────── -->
  <section class="hero noise">
    <div class="hero__media hero__media--generated" aria-hidden="true"></div>
    <div class="hero__scrim" aria-hidden="true"></div>
    <span class="hero__emblem" aria-hidden="true"></span>
    <div class="hero__orbit" aria-hidden="true"><i></i><i></i><i></i></div>
    <div class="container hero__inner">
      <div class="hero__content">
        <span class="eyebrow hero__eyebrow rise"><span class="hero__live-dot"></span>Influencer marketing · 52+ countries</span>
        <h1 class="display rise" data-delay="1">Niche mastery,<br><span class="gold-gradient">redefined.</span></h1>
        <p class="hero__sub rise" data-delay="2">Elite connects premium brands with the creators their audience already trusts — then plans, runs and measures the whole campaign for you.</p>
        <div class="hero__cta rise" data-delay="3">
          <a class="btn btn--primary btn--lg" href="contacts.html">Start a campaign {ICONS['arrow']}</a>
          <a class="btn btn--on-dark btn--lg" href="case-studies.html">See success stories</a>
        </div>
        <div class="hero__meta rise" data-delay="4">
          <div class="stat"><div class="stat__value"><span data-count="52">52</span><span class="unit">+</span></div><div class="stat__label">Countries</div></div>
          <div class="stat"><div class="stat__value"><span data-count="50" data-suffix="B">50B</span><span class="unit">+</span></div><div class="stat__label">Follower reach</div></div>
          <div class="stat"><div class="stat__value"><span data-count="85" data-suffix="K">85K</span><span class="unit">+</span></div><div class="stat__label">Creators</div></div>
          <div class="stat"><div class="stat__value"><span data-count="1500">1500</span><span class="unit">+</span></div><div class="stat__label">Brands served</div></div>
        </div>
      </div>
    </div>
    <span class="hero__scroll" aria-hidden="true">Scroll<i></i></span>
  </section>

  <!-- ── TRUST ──────────────────────────────────────────────────────────── -->
  <section class="trust" aria-labelledby="trust-title">
    <div class="trust__head"><p class="trust__label" id="trust-title">Trusted by category leaders across the Gulf and beyond</p><button class="marquee-control" type="button" data-marquee-toggle aria-pressed="false">Pause logo movement</button></div>
    <div class="marquee">
      <div class="marquee__track" data-loop>{chips(MARQUEE_A)}</div>
    </div>
    <div class="marquee marquee--reverse" style="margin-top:16px">
      <div class="marquee__track" data-loop>{chips(MARQUEE_B)}</div>
    </div>
    <div class="container center mt-10">
      <a class="link-arrow" href="sponsors.html">View all 75 clients {ICONS['arrow']}</a>
    </div>
  </section>

  <!-- ── VALUE ──────────────────────────────────────────────────────────── -->
  <section class="section" aria-labelledby="value-title">
    <div class="container">
      <div class="section-head section-head--center reveal">
        <span class="eyebrow eyebrow--center">Why Elite</span>
        <h2 id="value-title" class="mt-4">Exceptional results need<br>exceptional strategy.</h2>
        <p class="lede">Ten years of relationships with elite influencers and high-end brands, put to work on your campaign.</p>
      </div>
      <div class="grid cols-4 mt-16">{value_cards()}</div>
    </div>
  </section>

  <!-- ── SERVICES ───────────────────────────────────────────────────────── -->
  <section class="section section--sunken" id="services" aria-labelledby="svc-title">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Elite service solutions</span>
        <h2 id="svc-title" class="mt-4">Everything a campaign needs,<br>under one roof.</h2>
        <p class="lede">From finding the right creator to proving the return — four services that run as one process.</p>
      </div>
      <div class="grid cols-4 mt-16">{service_cards()}</div>
    </div>
  </section>

  <!-- ── PROCESS ────────────────────────────────────────────────────────── -->
  <section class="section" aria-labelledby="how-title">
    <div class="container">
      <div class="split">
        <div class="reveal">
          <span class="eyebrow">How it works</span>
          <h2 id="how-title" class="mt-4">Four steps.<br>One clear line to results.</h2>
          <p class="lede">You bring the brand and the goal. We handle discovery, negotiation, production and reporting — and you see every stage as it happens.</p>
          <a class="btn btn--dark mt-10" href="contacts.html">Book a strategy call {ICONS['arrow']}</a>
        </div>
        <div class="steps reveal" data-delay="2">
          <div class="step"><span class="step__num" aria-hidden="true"></span><div><h3 class="h4">Match</h3><p class="muted mt-0" style="font-size:.96rem">We shortlist creators from our network whose audience genuinely overlaps with yours.</p></div></div>
          <div class="step"><span class="step__num" aria-hidden="true"></span><div><h3 class="h4">Plan</h3><p class="muted" style="font-size:.96rem">Objectives, budget, markets and deliverables become a campaign brief everyone signs off.</p></div></div>
          <div class="step"><span class="step__num" aria-hidden="true"></span><div><h3 class="h4">Create</h3><p class="muted" style="font-size:.96rem">Creators produce content in their own voice, reviewed against your brand guidelines.</p></div></div>
          <div class="step"><span class="step__num" aria-hidden="true"></span><div><h3 class="h4">Measure</h3><p class="muted" style="font-size:.96rem">Live coverage tracking and post-campaign reporting show exactly what the spend returned.</p></div></div>
        </div>
      </div>
    </div>
  </section>

  <!-- ── PROOF ──────────────────────────────────────────────────────────── -->
  <section class="section section--sunken" aria-labelledby="proof-title">
    <div class="container">
      <div class="spread reveal">
        <div class="section-head">
          <span class="eyebrow">Success in action</span>
          <h2 id="proof-title" class="mt-4">Stories from our clients.</h2>
        </div>
        <a class="btn btn--ghost" href="case-studies.html">All success stories {ICONS['arrow']}</a>
      </div>
      <div class="grid cols-3 mt-16">{story_cards()}</div>
    </div>
  </section>

  <!-- ── PLATFORM ───────────────────────────────────────────────────────── -->
  <section class="section" aria-labelledby="platform-title">
    <div class="container">
      <div class="split split--reverse">
        <div class="split__media reveal">
          <div class="art art--light"></div>
          <div style="position:absolute;inset:clamp(20px,4vw,40px);display:grid;gap:14px;align-content:center">
            <div class="kpi" style="box-shadow:var(--sh-3)">
              <div class="kpi__top"><span class="kpi__label">Favourite influencers</span><span class="kpi__icon">{ICONS['users']}</span></div>
              <span class="kpi__value" data-count="930">930</span>
              <span class="kpi__delta up">▲ Live from your network</span>
            </div>
            <div class="kpi" style="box-shadow:var(--sh-3)">
              <div class="kpi__top"><span class="kpi__label">Coverage tracked</span><span class="kpi__icon">{ICONS['trend']}</span></div>
              <div class="bar-list" style="margin-top:6px">
                <div class="bar-row"><span class="label">Stories</span><span class="track"><span class="fill" data-pct="76"></span></span><span class="pct">76%</span></div>
                <div class="bar-row"><span class="label">Posts</span><span class="track"><span class="fill" data-pct="58"></span></span><span class="pct">58%</span></div>
                <div class="bar-row"><span class="label">Video</span><span class="track"><span class="fill" data-pct="41"></span></span><span class="pct">41%</span></div>
              </div>
            </div>
          </div>
        </div>
        <div class="reveal" data-delay="1">
          <span class="eyebrow">The Elite dashboard</span>
          <h2 id="platform-title" class="mt-4">Your whole campaign,<br>on one screen.</h2>
          <p class="lede">Branches, favourite creators, campaign stages, coverage and reporting — all in a single workspace, with 24/7 live support behind it.</p>
          <ul class="stack mt-8">
            <li class="row"><span class="gold" aria-hidden="true">—</span><span class="muted">Track every creator from pending to covered</span></li>
            <li class="row"><span class="gold" aria-hidden="true">—</span><span class="muted">Story, post and video coverage counted automatically</span></li>
            <li class="row"><span class="gold" aria-hidden="true">—</span><span class="muted">Wishlists, branches and scanner tools built in</span></li>
          </ul>
          <a class="btn btn--dark mt-10" href="dashboard.html">Explore the dashboard {ICONS['arrow']}</a>
        </div>
      </div>
    </div>
  </section>

  <!-- ── CTA ────────────────────────────────────────────────────────────── -->
  <section class="section section--tight">
    <div class="container">
      <div class="cta-band rise">
        <span class="eyebrow eyebrow--center" style="color:var(--gold-300)">Get in touch</span>
        <h2 class="mt-6">Ready to elevate your brand?</h2>
        <p>Tell us the goal. We'll come back with the creators, the plan and the numbers — wherever in the world you are.</p>
        <div class="row">
          <a class="btn btn--primary btn--lg" href="contacts.html">Start a campaign {ICONS['arrow']}</a>
          <a class="btn btn--on-dark btn--lg" href="about.html">About Elite</a>
        </div>
      </div>
    </div>
  </section>

</main>
"""

page("index.html", "Elite — Niche Mastery Redefined",
     "Elite is the #1 influencer marketing platform: creator discovery, campaign strategy, content creation and performance tracking across 52+ countries.",
     BODY, tone="light")
