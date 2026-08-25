# -*- coding: utf-8 -*-
from build import page, ICONS

def pagehead(title, tag, lede="", actions=""):
    return f"""
  <section class="pagehead">
    <div class="container">
      <div class="pagehead__title rise">
        <h1 class="tracked">{title}</h1>
        <p class="tag">{tag}</p>
        {f'<p class="lede mt-6" style="max-width:62ch;margin-inline:auto">{lede}</p>' if lede else ''}
        {f'<div class="row" style="justify-content:center" >{actions}</div>' if actions else ''}
      </div>
    </div>
  </section>"""

# ═══════════════════════════════════════════════════════════ ABOUT ══════
WHY = [
 ("shield","Decade of excellence","With over 10 years of experience in the industry, GC Elite brings a wealth of knowledge and expertise to every campaign we undertake."),
 ("globe","Global reach","Our presence in over 52 countries enables us to connect brands with influencers and audiences on a global scale, ensuring maximum reach and impact."),
 ("users","Elite partnerships","We pride ourselves on our exclusive partnerships with high-end brands and elite influencers, ensuring that our clients have access to the best talent and opportunities worldwide."),
 ("trend","Measurable results","We're committed to delivering measurable results that drive real business growth and ROI for our clients, no matter where they are in the world."),
 ("spark","Exceptional quality","From campaign conception to execution, we maintain the highest standards of quality and professionalism in everything we do."),
]

def why_cards():
    return "".join(f"""
      <article class="card card--hover reveal" data-delay="{i}">
        <div class="card__icon">{ICONS[ic]}</div>
        <h3 class="h4 card__title">{t}</h3>
        <p class="muted" style="font-size:.96rem">{c}</p>
      </article>""" for i,(ic,t,c) in enumerate(WHY, start=1))

ABOUT = f"""
<main id="main">
  {pagehead("ABOUT US","Niche Mastery Redefined",
    "Your premier destination for cutting-edge influencer marketing solutions.")}

  <section class="section section--tight">
    <div class="container">
      <div class="split">
        <div class="split__media reveal"><div class="art art--2"></div><span class="emblem" aria-hidden="true"></span></div>
        <div class="reveal" data-delay="1">
          <span class="eyebrow">Who we are</span>
          <h2 class="mt-4">A decade of influence,<br>in more than 52 countries.</h2>
          <p class="lede">Welcome to Elite. With over a decade of experience in the industry and a global presence spanning more than 52 countries, Elite has established itself as a trusted leader in the world of influencer marketing. Our extensive experience and international reach empower us to deliver unparalleled results for brands seeking to maximize their impact on a global scale.</p>
          <div class="grid cols-3 mt-10">
            <div class="stat"><div class="stat__value"><span data-count="10">10</span><span class="unit">+</span></div><div class="stat__label">Years</div></div>
            <div class="stat"><div class="stat__value"><span data-count="52">52</span><span class="unit">+</span></div><div class="stat__label">Countries</div></div>
            <div class="stat"><div class="stat__value"><span data-count="50" data-suffix="B">50B</span><span class="unit">+</span></div><div class="stat__label">Follower reach</div></div>
            <div class="stat"><div class="stat__value"><span data-count="85" data-suffix="K">85K</span><span class="unit">+</span></div><div class="stat__label">Creators</div></div>
            <div class="stat"><div class="stat__value"><span data-count="1500">1500</span><span class="unit">+</span></div><div class="stat__label">Brands served</div></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--sunken">
    <div class="container">
      <div class="grid cols-2" style="gap:clamp(28px,5vw,72px)">
        <div class="reveal">
          <span class="eyebrow">Our mission</span>
          <h2 class="mt-4">Simple, yet powerful.</h2>
          <p class="lede">To empower brands with tailored influencer marketing strategies that amplify their message and drive tangible results. We are committed to leveraging our decade-long expertise and global network to create impactful campaigns that resonate with audiences around the world.</p>
        </div>
        <div class="reveal" data-delay="2">
          <span class="eyebrow">What sets us apart</span>
          <h2 class="mt-4">Exceptional strategies.</h2>
          <p class="lede">At Elite, we understand that exceptional results require exceptional strategies. That's why we've spent over 10 years cultivating relationships with elite influencers and high-end brands, ensuring that our clients have access to the best talent and opportunities across the globe — bespoke campaigns that transcend borders and resonate with diverse audiences.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head section-head--center reveal">
        <span class="eyebrow eyebrow--center">Why choose Elite</span>
        <h2 class="mt-4">Five reasons brands stay.</h2>
      </div>
      <div class="grid cols-auto-md mt-16">{why_cards()}</div>
    </div>
  </section>

  <section class="section section--tight">
    <div class="container">
      <div class="cta-band rise">
        <span class="eyebrow eyebrow--center" style="color:var(--gold-300)">Get in touch</span>
        <h2 class="mt-6">Let's talk about your next campaign.</h2>
        <p>Ready to elevate your brand with the power of influencer marketing on a global scale? Get in touch today to learn more about our services and how we can help you achieve your marketing goals.</p>
        <div class="row"><a class="btn btn--primary btn--lg" href="contacts.html">Contact us {ICONS['arrow']}</a></div>
      </div>
    </div>
  </section>
</main>
"""
page("about.html","About Us — Elite","Over a decade of influencer marketing across more than 52 countries. Elite's mission, approach and reasons brands stay.",ABOUT,tone="dark")


# ═══════════════════════════════════════════════════ SUCCESS STORIES ═════
# Campaign records come from case_studies.py, generated by import_case_studies.py
# from the scraped export in assets/. Films were captured from the live site.
import case_studies

PAUSE_ICON = ('<svg class="ico-pause" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M7 5h3.2v14H7zM13.8 5H17v14h-3.2z"/></svg>')


def _handle(url):
    """Instagram handle out of an avatar filename."""
    return url.rsplit("/", 1)[-1].rsplit("_", 1)[0]


def story_media(rec, art):
    """Campaign film, campaign still, or the generated artwork as a fallback."""
    name = rec["name"]
    if rec.get("video"):
        poster = ' poster="%s"' % rec["shots"][0] if rec.get("shots") else ""
        return ('<video class="story__video" muted loop playsinline preload="none"%s '
                'aria-label="%s campaign film"><source src="%s" type="video/mp4"></video>'
                % (poster, name, rec["video"]))
    src = rec.get("still") or (rec["shots"][0] if rec.get("shots") else None)
    if src:
        return '<img src="%s" alt="%s campaign still" loading="lazy" decoding="async">' % (src, name)
    return '<div class="art art--%s"></div>' % art


def story_crew(rec):
    """Avatar stack of the creators who actually ran the campaign."""
    if not rec.get("avatars"):
        return ""
    pics = "".join(
        '<img class="crew__face" src="%s" alt="" width="30" height="30" loading="lazy" decoding="async">'
        % u for u in rec["avatars"][:3]
    )
    more = '<span class="crew__more">+%d</span>' % rec["more"] if rec.get("more") else ""
    return '<div class="crew"><div class="crew__faces">%s%s</div></div>' % (pics, more)


def story_grid():
    out = []
    for i, rec in enumerate(case_studies.WITH_MEDIA, start=1):
        art = (i % 6) + 1
        # An article, not a link: there is no per-story page to open, and the
        # play control cannot legally sit inside an anchor.
        play = ('<button class="story__play" type="button" data-video-toggle aria-pressed="false" '
                'aria-label="Play the %s film">%s%s</button>'
                % (rec["name"], ICONS["play"], PAUSE_ICON)) if rec.get("video") else ""
        logo = ('<img class="story__logo" src="%s" alt="" loading="lazy" decoding="async">'
                % rec["logo"]) if rec.get("logo") else ""
        out.append(f"""
      <article class="story reveal" data-delay="{i}" data-cat="{rec['category']}" data-name="{rec['name']}">
        <div class="story__media">{story_media(rec, art)}</div>
        {logo}{play}
        <div class="story__meta">
          <span class="name">{rec['name']}</span><span class="place">{rec['market']}</span>
          <div class="story__stats">
            <div>Followers<b>{rec['followers']}</b></div><div>Influencers<b>{rec['influencers']}</b></div>
          </div>
          {story_crew(rec)}
        </div>
      </article>""")
    return "".join(out)


CASES = f"""
<main id="main">
  {pagehead("SUCCESS IN ACTION","Stories From Our Clients",
    "Real campaigns, real creators, real numbers. Filter by category to find work close to yours.")}

  <section class="section section--tight">
    <div class="container">
      <div class="spread reveal" style="gap:var(--s-4)">
        <div class="field" style="flex:1 1 280px;max-width:380px">
          <label class="sr-only" for="story-search">Search success stories</label>
          <input class="input" id="story-search" type="search" placeholder="Search stories…" data-search="#story-list">
        </div>
        <!-- Categories below are wired client-side; swap for live data from the Elite API. -->
        <div class="chips" data-filter-group data-filter-target="#story-list" data-filter-empty="#story-empty">
          <button class="chip" type="button" data-value="all" aria-pressed="true">All</button>
          <button class="chip" type="button" data-value="Restaurant" aria-pressed="false">Restaurant</button>
          <button class="chip" type="button" data-value="Cafe" aria-pressed="false">Café</button>
          <button class="chip" type="button" data-value="Fashion" aria-pressed="false">Fashion</button>
        </div>
      </div>

      <div class="grid cols-4 mt-12" id="story-list">{story_grid()}</div>

      <div class="state mt-8" id="story-empty" hidden>
        <span class="state__icon">{ICONS['empty']}</span>
        <div><h3 class="h4">No stories in this category yet</h3>
        <p class="muted mt-4">Try another filter, or tell us what you're looking for and we'll share relevant work directly.</p></div>
        <a class="btn btn--ghost" href="contacts.html">Request case studies</a>
      </div>
      <div class="state mt-8" id="search-empty" hidden>
        <span class="state__icon">{ICONS['search']}</span>
        <div><h3 class="h4">Nothing matched that search</h3>
        <p class="muted mt-4">Check the spelling, or clear the search to see every story.</p></div>
      </div>

      <div class="center mt-16 reveal">
        <a class="btn btn--dark btn--lg" href="contacts.html">Get a campaign like these {ICONS['arrow']}</a>
      </div>
    </div>
  </section>

  <section class="section section--sunken">
    <div class="container">
      <div class="section-head section-head--center reveal">
        <span class="eyebrow eyebrow--center">Questions</span>
        <h2 class="mt-4">How a campaign runs.</h2>
      </div>
      <div class="accordion mt-12" data-single>
        <div class="acc__item">
          <button class="acc__trigger" aria-expanded="false" aria-controls="faq1">How do you pick the creators?<span class="acc__icon" aria-hidden="true"></span></button>
          <div class="acc__panel" id="faq1"><div>We shortlist from our network based on genuine audience overlap with your brand — market, category, age profile and engagement quality — not follower count alone.</div></div>
        </div>
        <div class="acc__item">
          <button class="acc__trigger" aria-expanded="false" aria-controls="faq2">How long does a campaign take?<span class="acc__icon" aria-hidden="true"></span></button>
          <div class="acc__panel" id="faq2"><div>It depends on scope and market, but most campaigns move from brief to first published content within a few weeks. We'll give you a schedule before anything is signed.</div></div>
        </div>
        <div class="acc__item">
          <button class="acc__trigger" aria-expanded="false" aria-controls="faq3">What do you report back?<span class="acc__icon" aria-hidden="true"></span></button>
          <div class="acc__panel" id="faq3"><div>Coverage by creator and format — stories, posts and video — plus reach and campaign-level performance, all visible live in the Elite dashboard.</div></div>
        </div>
        <div class="acc__item">
          <button class="acc__trigger" aria-expanded="false" aria-controls="faq4">Which markets do you cover?<span class="acc__icon" aria-hidden="true"></span></button>
          <div class="acc__panel" id="faq4"><div>Elite has a presence in more than 52 countries, with the deepest creator networks across Saudi Arabia, Kuwait, the UAE, Qatar and Bahrain.</div></div>
        </div>
      </div>
    </div>
  </section>
</main>
"""
page("case-studies.html","Success Stories — Elite","Success in action: influencer campaigns Elite has run for premium brands, with reach and creator counts.",CASES,tone="dark")


# ══════════════════════════════════════════════════════ OUR CLIENTS ══════
CLIENTS = [
 # Category is the build's sample mapping and covers the original forty; the
 # rest stay uncategorised until the CMS field is wired, so they answer to
 # "All" and to search but not to a category chip.
 ("odachi","Restaurant"), ("Nawader Aloud","Perfume"), ("Crocs","Fashion"), ("BHPC KSA","Fashion"),
 ("Urth Caffe","Cafe"), ("Morini Riyadh","Restaurant"), ("Rüya","Restaurant"), ("Beefbar","Restaurant"),
 ("ROKA KSA","Restaurant"), ("The Beauty Secrets","Beauty"), ("Swaikhat & Tanoor","Restaurant"), ("The Back Burner","Restaurant"),
 ("Maryool","Restaurant"), ("Coya","Restaurant"), ("A.O.K Kitchen","Restaurant"), ("elct.sa","Fashion"),
 ("Opt Coffee KW","Cafe"), ("ROBATA","Restaurant"), ("Signor Sassi","Restaurant"), ("San Carlo","Restaurant"),
 ("MYAZŪ","Restaurant"), ("Agio","Restaurant"), ("Beit El Sabban","Restaurant"), ("Vero Moda","Fashion"),
 ("Enigmaku","Fashion"), ("Clap","Restaurant"), ("Jones the Grocer","Cafe"), ("Iris","Restaurant"),
 ("Brute","Restaurant"), ("Bagatelle","Restaurant"), ("Sumosan","Restaurant"), ("MNKY HSE","Restaurant"),
 ("Tashas Cafe","Cafe"), ("Solitaire","Fashion"), ("Panerai","Fashion"), ("Fred","Fashion"),
 ("Kiko","Beauty"), ("Maje","Fashion"), ("Ted Baker","Fashion"), ("TAG Heuer","Fashion"),
 ("Nicoli",""), ("Skechers",""), ("Dani by Daniel K",""), ("Rituals Cosmetics",""),
 ("Rowleys",""), ("Saiddal",""), ("Keycafe",""), ("DayDayGame",""),
 ("Jadeel",""), ("Crêpes des Alpes",""), ("Flamingo Room",""), ("Splash Spectrum",""),
 ("MAREEZ",""), ("Pizza Bar",""), ("tabl.to",""), ("Brunch & Cake",""),
 ("Hamra Tower",""), ("Zuma",""), ("Mr.Chow",""), ("KAYZŌ",""),
 ("Il Baretto",""), ("Crazy Pizza",""), ("St. Regis Hotels",""), ("Gia",""),
 ("Black Tap",""), ("Sobhy Kaber",""), ("Jon & Vinny's",""), ("Million Riyal Menu",""),
 ("ISISPHARMA",""), ("Lina's & Dina's",""), ("ShieldMe",""), ("Maserati",""),
 ("Tom Tom Coffee",""), ("Mana",""), ("Lavenue","Restaurant"),
]

def client_grid():
    return "".join(
      f'<span class="logo-chip logo-chip--fallback" role="img" aria-label="{n}" title="{n}" data-cat="{c}" data-name="{n}"><span aria-hidden="true">{n}</span></span>' for n,c in CLIENTS)

CAT_BARS = [("Restaurant",58.82),("Fashion",10.29),("Café",10.29),("Perfume",4.41),("Cosmetics / Beauty",2.94)]
REG_BARS = [("Saudi Arabia",71.74),("Kuwait",15.22),("United Arab Emirates",4.35),("Qatar",4.35),("Bahrain",2.17)]

def bars(rows):
    return "".join(f"""
      <div class="bar-row"><span class="label">{l}</span>
      <span class="track"><span class="fill" data-pct="{v}"></span></span>
      <span class="pct">{v}%</span></div>""" for l,v in rows)

SPONSORS = f"""
<main id="main">
  {pagehead("OUR CLIENTS","Niche Mastery Redefined",
    "Seventy-five brands across seven countries and twelve categories choose Elite to reach their audience.")}

  <section class="section section--tight">
    <div class="container">
      <div class="kpi-grid reveal">
        <div class="kpi"><div class="kpi__top"><span class="kpi__label">Featured clients</span><span class="kpi__icon">{ICONS['users']}</span></div><span class="kpi__value" data-count="75">75</span></div>
        <div class="kpi"><div class="kpi__top"><span class="kpi__label">Countries</span><span class="kpi__icon">{ICONS['globe']}</span></div><span class="kpi__value" data-count="7">7</span></div>
        <div class="kpi"><div class="kpi__top"><span class="kpi__label">Categories</span><span class="kpi__icon">{ICONS['grid']}</span></div><span class="kpi__value" data-count="12">12</span></div>
        
      </div>

      <div class="grid cols-2 mt-8">
        <div class="card reveal">
          <h3 class="h4">Clients by category</h3>
          <div class="bar-list mt-8">{bars(CAT_BARS)}</div>
        </div>
        <div class="card reveal" data-delay="1">
          <h3 class="h4">Clients by region</h3>
          <div class="bar-list mt-8">{bars(REG_BARS)}</div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--sunken">
    <div class="container">
      <div class="spread reveal">
        <div class="section-head">
          <span class="eyebrow">The roster</span>
          <h2 class="mt-4">Brands we work with.</h2>
        </div>
        <div class="field" style="flex:1 1 260px;max-width:340px">
          <label class="sr-only" for="client-search">Search clients</label>
          <input class="input" id="client-search" type="search" placeholder="Search clients…" data-search="#client-list">
        </div>
      </div>

      <!-- Category tags are a working sample mapping; point data-cat at the CMS field in production. -->
      <div class="chips mt-8 reveal" data-filter-group data-filter-target="#client-list" data-filter-empty="#client-empty">
        <button class="chip" type="button" data-value="all" aria-pressed="true">All <span class="count">{len(CLIENTS)}</span></button>
        <button class="chip" type="button" data-value="Restaurant" aria-pressed="false">Restaurant</button>
        <button class="chip" type="button" data-value="Cafe" aria-pressed="false">Café</button>
        <button class="chip" type="button" data-value="Fashion" aria-pressed="false">Fashion</button>
        <button class="chip" type="button" data-value="Beauty" aria-pressed="false">Cosmetics / Beauty</button>
        <button class="chip" type="button" data-value="Perfume" aria-pressed="false">Perfume</button>
      </div>

      <div class="logo-grid mt-8 reveal" id="client-list">{client_grid()}</div>

      <div class="state mt-8" id="client-empty" hidden>
        <span class="state__icon">{ICONS['empty']}</span>
        <div><h3 class="h4">No clients in this category yet</h3><p class="muted mt-4">Pick another category to keep browsing.</p></div>
      </div>
      <div class="state mt-8" id="search-empty" hidden>
        <span class="state__icon">{ICONS['search']}</span>
        <div><h3 class="h4">No match for that name</h3><p class="muted mt-4">Clear the search to see the full roster.</p></div>
      </div>

      <p class="center subtle mt-10" style="font-size:.88rem">Showing all {len(CLIENTS)} clients</p>
    </div>
  </section>

  <section class="section section--tight">
    <div class="container">
      <div class="cta-band rise">
        <h2>Your brand belongs here.</h2>
        <p>Join seventy-five brands running influencer campaigns with Elite across the Gulf and beyond.</p>
        <div class="row"><a class="btn btn--primary btn--lg" href="contacts.html">Become a client {ICONS['arrow']}</a></div>
      </div>
    </div>
  </section>
</main>
"""
page("sponsors.html","Our Clients — Elite","Seventy-five brands across seven countries and twelve categories partner with Elite for influencer marketing.",SPONSORS,tone="dark")


# ═════════════════════════════════════════════════════════ CONTACT ═══════
CONTACT = f"""
<main id="main">
  {pagehead("CONTACT US","Niche Mastery Redefined",
    "Stay connected with us! Whether you have a question, suggestion, or just want to say hello, we're here to help. Don't hesitate to reach out — we'd love to hear from you.")}

  <section class="section section--tight">
    <div class="container">
      <div class="split split--form">
        <div class="card reveal" style="padding:clamp(24px,4vw,48px)">
          <div class="segmented" role="tablist" aria-label="I am a">
            <button role="tab" id="tab-inf" aria-controls="panel-inf" aria-selected="true" type="button" data-tr="who.creator">Influencer</button>
            <button role="tab" id="tab-brand" aria-controls="panel-brand" aria-selected="false" tabindex="-1" type="button" data-tr="who.brand">Brand</button>
          </div>

          <div id="panel-inf" role="tabpanel" aria-labelledby="tab-inf">
            <p class="muted mt-6" style="font-size:.96rem">Join the Elite network and work with the region's premium brands.</p>
            <form class="grid cols-2 mt-8" data-validate data-success="Thanks — an Elite partner manager will be in touch.">
              <div class="field"><label class="field__label" for="i-name">Name <span class="req">*</span></label>
                <input class="input" id="i-name" name="name" required placeholder="Your full name"><span class="field__error">Please enter your name.</span></div>
              <div class="field"><label class="field__label" for="i-country">Country</label>
                <select class="select" id="i-country" name="country">
                  <option value="">Select country</option><option>Saudi Arabia</option><option>Kuwait</option>
                  <option>United Arab Emirates</option><option>Qatar</option><option>Bahrain</option><option>Egypt</option><option>Other</option>
                </select></div>
              <div class="field"><label class="field__label" for="i-email">Email <span class="req">*</span></label>
                <input class="input" id="i-email" name="email" type="email" required placeholder="you@example.com"><span class="field__error">Enter a valid email address.</span></div>
              <div class="field"><label class="field__label" for="i-phone">Phone number</label>
                <input class="input" id="i-phone" name="phone" type="tel" placeholder="+966 …"></div>
              <div style="grid-column:1/-1"><label class="check"><input type="checkbox" name="whatsapp" checked><span>WhatsApp is active on this number</span></label></div>
              <div class="field" style="grid-column:1/-1"><label class="field__label" for="i-msg">Message</label>
                <textarea class="textarea" id="i-msg" name="message" placeholder="Tell us about your audience and the brands you'd like to work with."></textarea></div>
              <div style="grid-column:1/-1"><button class="btn btn--primary btn--lg btn--block" type="submit">Send message</button></div>
            </form>
          </div>

          <div id="panel-brand" role="tabpanel" aria-labelledby="tab-brand" hidden>
            <p class="muted mt-6" style="font-size:.96rem">Tell us the goal and we'll come back with creators, a plan and a budget.</p>
            <form class="grid cols-2 mt-8" data-validate data-success="Thanks — we'll reply with a campaign outline shortly.">
              <div class="field"><label class="field__label" for="b-name">Name <span class="req">*</span></label>
                <input class="input" id="b-name" name="name" required placeholder="Your full name"><span class="field__error">Please enter your name.</span></div>
              <div class="field"><label class="field__label" for="b-brand">Brand <span class="req">*</span></label>
                <input class="input" id="b-brand" name="brand" required placeholder="Brand name"><span class="field__error">Please enter your brand.</span></div>
              <div class="field"><label class="field__label" for="b-email">Email <span class="req">*</span></label>
                <input class="input" id="b-email" name="email" type="email" required placeholder="you@company.com"><span class="field__error">Enter a valid email address.</span></div>
              <div class="field"><label class="field__label" for="b-country">Country</label>
                <select class="select" id="b-country" name="country">
                  <option value="">Select country</option><option>Saudi Arabia</option><option>Kuwait</option>
                  <option>United Arab Emirates</option><option>Qatar</option><option>Bahrain</option><option>Egypt</option><option>Other</option>
                </select></div>
              <div class="field"><label class="field__label" for="b-phone">Phone number</label>
                <input class="input" id="b-phone" name="phone" type="tel" placeholder="+966 …"></div>
              <div class="field"><label class="field__label" for="b-cat">Category</label>
                <select class="select" id="b-cat" name="category">
                  <option value="">Select category</option><option>Restaurant</option><option>Café</option><option>Fashion</option>
                  <option>Cosmetics / Beauty</option><option>Perfume</option><option>Hotel</option><option>Other</option>
                </select></div>
              <div style="grid-column:1/-1"><label class="check"><input type="checkbox" name="whatsapp" checked><span>WhatsApp is active on this number</span></label></div>
              <div class="field" style="grid-column:1/-1"><label class="field__label" for="b-msg">Message</label>
                <textarea class="textarea" id="b-msg" name="message" placeholder="What are you launching, and what does success look like?"></textarea></div>
              <div style="grid-column:1/-1"><button class="btn btn--primary btn--lg btn--block" type="submit">Send message</button></div>
            </form>
          </div>
        </div>

        <aside class="stack reveal" data-delay="1">
          <div class="card card--sunken">
            <div class="card__icon">{ICONS['spark']}</div>
            <h3 class="h4">What happens next</h3>
            <ol class="stack mt-6" style="counter-reset:c">
              <li class="muted" style="font-size:.95rem"><b class="gold">1 —</b> We read your brief and check creator fit.</li>
              <li class="muted" style="font-size:.95rem"><b class="gold">2 —</b> You get a shortlist, a plan and a budget.</li>
              <li class="muted" style="font-size:.95rem"><b class="gold">3 —</b> We run the campaign and report live.</li>
            </ol>
          </div>
          <div class="card card--sunken">
            <div class="card__icon">{ICONS['globe']}</div>
            <h3 class="h4">Where we work</h3>
            <p class="muted mt-4" style="font-size:.95rem">Saudi Arabia · Kuwait · United Arab Emirates · Qatar · Bahrain — and 52+ countries worldwide.</p>
          </div>
          <div class="card card--sunken">
            <div class="card__icon">{ICONS['users']}</div>
            <h3 class="h4">24/7 live support</h3>
            <p class="muted mt-4" style="font-size:.95rem">Campaigns don't keep office hours. Neither do we.</p>
          </div>
        </aside>
      </div>
    </div>
  </section>
</main>
"""
page("contacts.html","Contact Us — Elite","Talk to Elite about an influencer campaign, or join the network as a creator. 24/7 live support.",CONTACT,tone="dark")


# ═══════════════════════════════════════════════════════ DASHBOARD ═══════
STAGES = ["Pending","Confirmed","Visited","Delivered","Post creation","Shared","Covered"]

DASH = f"""
<main id="main">
  {pagehead("DASHBOARD","One workspace for every campaign",
    "Branches, creators, campaign stages and coverage — the Elite platform gives you a comprehensive overview of all influencer marketing activities.",
    '<a class="btn btn--primary btn--lg" href="https://gc-elite.com/dashboard">Sign in to your dashboard '+ICONS['arrow']+'</a><a class="btn btn--ghost btn--lg" href="contacts.html">Request a demo</a>')}

  <section class="section section--tight">
    <div class="container">
      <div class="dashboard-demo reveal" data-dashboard-demo>
        <div class="dashboard-demo__head">
          <div><span class="eyebrow">Interactive preview</span><p class="dashboard-demo__note">Illustrative campaign data — switch a view to explore the workspace.</p></div>
          <div class="segmented dashboard-demo__switch" role="group" aria-label="Choose a dashboard demo campaign">
            <button type="button" data-demo-view="launch" aria-pressed="true">Summer launch</button>
            <button type="button" data-demo-view="growth" aria-pressed="false">Always-on growth</button>
            <button type="button" data-demo-view="opening" aria-pressed="false">New location</button>
          </div>
        </div>
        <div class="dashboard-demo__campaign"><span class="dashboard-demo__pulse" aria-hidden="true"></span><span data-demo-campaign>Summer launch · Riyadh</span><span class="dashboard-demo__period" data-demo-period>01–30 Jun 2026</span></div>
      </div>
      <div class="kpi-grid reveal">
        <div class="kpi"><div class="kpi__top"><span class="kpi__label">Branches</span><span class="kpi__icon">{ICONS['grid']}</span></div><span class="kpi__value" data-demo-kpi="branches" data-count="4">4</span><span class="kpi__delta">Per location reporting</span></div>
        <div class="kpi"><div class="kpi__top"><span class="kpi__label">Favourite influencers</span><span class="kpi__icon">{ICONS['users']}</span></div><span class="kpi__value" data-demo-kpi="creators" data-count="128">128</span><span class="kpi__delta">Your saved network</span></div>
        <div class="kpi"><div class="kpi__top"><span class="kpi__label">Campaigns</span><span class="kpi__icon">{ICONS['megaphone']}</span></div><span class="kpi__value" data-demo-kpi="campaigns" data-count="7">7</span><span class="kpi__delta">Live and scheduled</span></div>
        <div class="kpi"><div class="kpi__top"><span class="kpi__label">Coverage</span><span class="kpi__icon">{ICONS['trend']}</span></div><span class="kpi__value" data-demo-kpi="coverage" data-count="346">346</span><span class="kpi__delta">Stories · posts · video</span></div>
      </div>
    </div>
  </section>

  <section class="section section--sunken">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Influencer overview</span>
        <h2 class="mt-4">Every creator, every stage.</h2>
        <p class="lede">Follow each influencer from first contact to published coverage, without chasing anyone for an update.</p>
      </div>
      <div class="stages mt-12 reveal" aria-label="Creator campaign stages">
        {"".join(f'<div class="kpi"><span class="kpi__label">{n}</span><span class="kpi__value" data-demo-stage="{n.lower().replace(" ", "-")}">0</span></div>' for n in STAGES)}
      </div>

      <div class="grid cols-2 mt-8">
        <div class="card reveal dashboard-list-card">
          <div class="spread"><div><span class="eyebrow">Live workspace</span><h3 class="h4 mt-4">Recent campaigns</h3></div><a class="link-arrow" href="contacts.html">View all {ICONS['arrow']}</a></div>
          <div class="demo-campaigns mt-6" data-demo-campaigns></div>
        </div>
        <div class="card reveal" data-delay="1">
          <div class="spread"><h3 class="h4">Coverage details</h3><span class="demo-total" data-demo-total>346 pieces</span></div>
          <div class="bar-list mt-8">
            <div class="bar-row"><span class="label">Story</span><span class="track"><span class="fill" data-demo-bar="story" data-pct="58"></span></span><span class="pct" data-demo-pct="story">201</span></div>
            <div class="bar-row"><span class="label">Post</span><span class="track"><span class="fill" data-demo-bar="post" data-pct="24"></span></span><span class="pct" data-demo-pct="post">82</span></div>
            <div class="bar-row"><span class="label">Video</span><span class="track"><span class="fill" data-demo-bar="video" data-pct="18"></span></span><span class="pct" data-demo-pct="video">63</span></div>
          </div>
          <p class="subtle mt-8" style="font-size:.85rem">Coverage is grouped by format and updates with the selected demo campaign.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head section-head--center reveal">
        <span class="eyebrow eyebrow--center">Inside the platform</span>
        <h2 class="mt-4">Built for people running campaigns.</h2>
      </div>
      <div class="grid cols-3 mt-16">
        <article class="card card--hover reveal"><div class="card__icon">{ICONS['users']}</div><h3 class="h4 card__title">Influencers &amp; wishlist</h3><p class="muted" style="font-size:.96rem">Browse the network, save favourites and build shortlists your whole team can see.</p></article>
        <article class="card card--hover reveal" data-delay="1"><div class="card__icon">{ICONS['grid']}</div><h3 class="h4 card__title">Branches</h3><p class="muted" style="font-size:.96rem">Run multi-location brands with coverage and check-ins tracked per branch.</p></article>
        <article class="card card--hover reveal" data-delay="2"><div class="card__icon">{ICONS['search']}</div><h3 class="h4 card__title">Scanner</h3><p class="muted" style="font-size:.96rem">Verify creator check-ins on site with a quick scan — no paperwork.</p></article>
        <article class="card card--hover reveal" data-delay="3"><div class="card__icon">{ICONS['megaphone']}</div><h3 class="h4 card__title">Campaigns</h3><p class="muted" style="font-size:.96rem">Brief, approve and monitor every campaign stage in one timeline.</p></article>
        <article class="card card--hover reveal" data-delay="4"><div class="card__icon">{ICONS['chart']}</div><h3 class="h4 card__title">Reporting</h3><p class="muted" style="font-size:.96rem">Coverage by format and creator, ready to share with stakeholders.</p></article>
        <article class="card card--hover reveal" data-delay="5"><div class="card__icon">{ICONS['shield']}</div><h3 class="h4 card__title">24/7 support</h3><p class="muted" style="font-size:.96rem">A live team behind the platform whenever a campaign needs a hand.</p></article>
      </div>
    </div>
  </section>

  <section class="section section--tight">
    <div class="container">
      <div class="cta-band rise">
        <h2>See it with your own campaign.</h2>
        <p>Sign in to your workspace, or ask us for a walkthrough with your brand's data.</p>
        <div class="row">
          <a class="btn btn--primary btn--lg" href="https://gc-elite.com/dashboard">Sign in {ICONS['arrow']}</a>
          <a class="btn btn--on-dark btn--lg" href="contacts.html">Request a demo</a>
        </div>
      </div>
    </div>
  </section>
</main>
"""
page("dashboard.html","Dashboard — Elite","One workspace for branches, creators, campaign stages and coverage reporting.",DASH,tone="dark")
