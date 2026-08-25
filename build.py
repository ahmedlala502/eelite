# -*- coding: utf-8 -*-
"""ELITƎ static site builder — shared shell + per-page content."""
import os, io

OUT = os.path.dirname(os.path.abspath(__file__))

NAV = [
    ("index.html",        "Home"),
    ("dashboard.html",    "Dashboard"),
    ("case-studies.html", "Success Stories"),
    ("sponsors.html",     "Our Clients"),
    ("contacts.html",     "Contact Us"),
    ("about.html",        "About Us"),
]

ICONS = {
 "sun":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.5v2M12 19.5v2M2.5 12h2M19.5 12h2M5.2 5.2l1.4 1.4M17.4 17.4l1.4 1.4M18.8 5.2l-1.4 1.4M6.6 17.4l-1.4 1.4"/></svg>',
 "moon":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M20 14.2A8.2 8.2 0 1 1 9.8 4a6.6 6.6 0 0 0 10.2 10.2z"/></svg>',
 "globe":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.6 3.8 9S14.5 18.4 12 21c-2.5-2.6-3.8-5.6-3.8-9S9.5 5.6 12 3z"/></svg>',
 "arrow":'<svg class="ico ico--arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h13M12 5l7 7-7 7"/></svg>',
 "arrowup":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17L17 7M9 7h8v8"/></svg>',
 "play":'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5.5v13l11-6.5z"/></svg>',
 "instagram":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><rect x="3" y="3" width="18" height="18" rx="5.4"/><circle cx="12" cy="12" r="4"/><circle cx="17.4" cy="6.6" r="1.1" fill="currentColor" stroke="none"/></svg>',
 "mail":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="3"/><path d="M4 7l8 6 8-6"/></svg>',
 "menu":'<svg class="ico-open" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M4 8h16M4 16h16"/></svg><svg class="ico-close" style="display:none" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>',
 "users":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M16 20v-1.6a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4V20"/><circle cx="9" cy="7.4" r="3.4"/><path d="M22 20v-1.6a4 4 0 0 0-3-3.87M16.5 4.1a4 4 0 0 1 0 7.4"/></svg>',
 "grid":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><rect x="3.5" y="3.5" width="7" height="7" rx="2"/><rect x="13.5" y="3.5" width="7" height="7" rx="2"/><rect x="3.5" y="13.5" width="7" height="7" rx="2"/><rect x="13.5" y="13.5" width="7" height="7" rx="2"/></svg>',
 "trend":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 17l6-6 4 4 8-8"/><path d="M15 7h6v6"/></svg>',
 "megaphone":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10v4a2 2 0 0 0 2 2h1l9 4V4L7 8H6a2 2 0 0 0-2 2z"/><path d="M19 9.5a3.2 3.2 0 0 1 0 5"/></svg>',
 "search":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="11" cy="11" r="6.5"/><path d="M20 20l-3.6-3.6"/></svg>',
 "target":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.6"/><circle cx="12" cy="12" r="1" fill="currentColor"/></svg>',
 "spark":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"><path d="M12 3l2.2 5.6L20 10.8l-5.8 2.2L12 19l-2.2-6L4 10.8l5.8-2.2z"/></svg>',
 "chart":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M5 19V11M12 19V5M19 19v-6"/></svg>',
 "shield":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"><path d="M12 3l7.5 3v5.4c0 4.5-3 8.3-7.5 9.6-4.5-1.3-7.5-5.1-7.5-9.6V6z"/><path d="M9 12l2.2 2.2L15.4 10"/></svg>',
 "empty":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M3.5 8.5L12 4l8.5 4.5v7L12 20l-8.5-4.5z"/><path d="M3.5 8.5L12 13l8.5-4.5M12 13v7"/></svg>',
 "doc":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h4"/></svg>',
}

LOGO_URL = "assets/img/elite-logo.svg"
WORDMARK = (f'<a class="wordmark" href="index.html" aria-label="Elite — home">'
            f'<span class="wordmark__asset"><img class="wordmark__image" src="{LOGO_URL}" alt="Elite"></span>'
            f'<span class="wordmark__monogram" aria-hidden="true">E</span></a>')


def head(title, desc, page):
    return f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0A0A0B">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Playfair+Display:wght@500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/elite.css">
<link rel="icon" href="{LOGO_URL}">
<script>(function(){{try{{var t=localStorage.getItem('elite-theme')||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}}})();</script>
</head>
<body data-page="{page}">
<a class="skip-link" href="#main">Skip to content</a>
"""


def nav(page, tone="dark"):
    CUR = ' aria-current="page"'
    links = "".join(
        '<li><a class="nav__link" href="%s"%s>%s</a></li>' % (href, CUR if href == page else "", label)
        for href, label in NAV)
    drawer_links = "".join(
        '<a href="%s"%s>%s%s</a>' % (href, CUR if href == page else "", label, ICONS["arrow"])
        for href, label in NAV)
    return f"""
<header class="nav" data-tone="{tone}">
  <div class="nav__inner">
    {WORDMARK}
    <nav aria-label="Primary">
      <ul class="nav__links">{links}</ul>
    </nav>
    <div class="nav__actions">
      <a class="icon-btn icon-btn--text lang-toggle" href="ar/{page}" hreflang="ar" lang="ar" aria-label="Switch language to Arabic">{ICONS['globe']}<span>AR</span></a>
      <button class="icon-btn" type="button" data-theme-toggle aria-label="Switch theme" aria-pressed="false">
        <span class="theme-ico" aria-hidden="true"><span class="theme-ico__moon">{ICONS['moon']}</span><span class="theme-ico__sun">{ICONS['sun']}</span></span>
      </button>
      <a class="btn btn--primary btn--sm nav__cta" href="contacts.html">Start a campaign</a>
      <button class="icon-btn nav__toggle" type="button" data-drawer-toggle aria-expanded="false" aria-controls="drawer" aria-label="Open menu">{ICONS['menu']}</button>
    </div>
  </div>
</header>
<div class="drawer" id="drawer">
  {drawer_links}
  <div class="drawer__foot">
    <a class="btn btn--primary btn--block" href="contacts.html">Start a campaign</a>
  </div>
</div>
"""


FOOTER = f"""
<footer class="footer">
  <div class="container">
    <div class="footer__grid">
      <div>
        <img class="footer__logo-image" src="{LOGO_URL}" alt="Elite — Niche Mastery Redefined">
        <p class="footer__about">Elite is the #1 influencer marketing platform to help you achieve all your marketing goals. We launch and manage your campaigns with 24/7 live support.</p>
        <div class="social mt-6">
          <a href="https://instagram.com" target="_blank" rel="noopener" aria-label="Elite on Instagram">{ICONS['instagram']}</a>
          <a href="contacts.html" aria-label="Email Elite">{ICONS['mail']}</a>
        </div>
      </div>
      <div>
        <h4>Explore</h4>
        <div class="footer__links">
          <a href="index.html">Home</a>
          <a href="case-studies.html">Success Stories</a>
          <a href="sponsors.html">Our Clients</a>
          <a href="dashboard.html">Dashboard</a>
        </div>
      </div>
      <div>
        <h4>Company</h4>
        <div class="footer__links">
          <a href="about.html">About Us</a>
          <a href="contacts.html">Contact Us</a>
          <a href="#privacy" data-modal-open="privacy-modal">Privacy Policy</a>
        </div>
      </div>
      <div>
        <h4>Newsletter</h4>
        <p class="muted" style="font-size:.95rem;margin-bottom:16px">Campaign insights and creator trends, once a month.</p>
        <form class="inline-field" data-validate data-success="You're subscribed. Welcome to Elite.">
          <label class="sr-only" for="nl-email">Email address</label>
          <div class="field" style="width:100%">
            <input class="input" id="nl-email" name="email" type="email" required placeholder="Enter your email">
            <span class="field__error">Enter a valid email address.</span>
          </div>
          <button type="submit" aria-label="Subscribe">{ICONS['arrowup']}</button>
        </form>
      </div>
    </div>
    <div class="footer__bottom">
      <span>Copyright © <span data-year>2026</span> Elite. All rights reserved.</span>
      <span>Niche Mastery Redefined</span>
    </div>
  </div>
</footer>

<div class="modal" id="privacy-modal" role="dialog" aria-modal="true" aria-labelledby="privacy-title">
  <div class="modal__panel">
    <div class="spread" style="align-items:flex-start">
      <h3 id="privacy-title">Privacy Policy</h3>
      <button class="icon-btn" type="button" data-modal-close aria-label="Close">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>
      </button>
    </div>
    <p class="muted mt-6">Elite collects only the information needed to run your campaigns — contact details you submit, and campaign performance data from connected creator accounts. We never sell your data.</p>
    <p class="muted mt-4">For the full policy, or to request deletion of your data, contact us and we will respond within 30 days.</p>
    <a class="btn btn--dark mt-8" href="contacts.html">Contact us</a>
  </div>
</div>

<div class="toast" id="toast" role="status" aria-live="polite"></div>
<script src="assets/js/elite.js" defer></script>
</body>
</html>
"""


def page(filename, title, desc, body, tone="light"):
    html = head(title, desc, filename.replace(".html", "")) + nav(filename, tone) + body + FOOTER
    with io.open(os.path.join(OUT, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", filename, len(html))
