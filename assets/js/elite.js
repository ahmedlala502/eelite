/* ELITƎ — interaction layer. No dependencies. */
(function () {
  'use strict';

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Locale --------------------------------------------------
     The Arabic pages are the same markup with Arabic copy, so every string
     this file injects at runtime has to follow the document's language or
     English leaks back into ar/. */
  var LANG = (document.documentElement.getAttribute('lang') || 'en').slice(0, 2);
  var STRINGS = {
    ar: {
      'Switch to light theme': 'التبديل إلى الوضع الفاتح',
      'Switch to dark theme': 'التبديل إلى الوضع الداكن',
      'Please complete the highlighted fields.': 'يرجى استكمال الحقول المحددة.',
      'Sending…': 'جارٍ الإرسال…',
      'Thank you — we will be in touch shortly.': 'شكرًا لك — سنتواصل معك قريبًا.',
      'Play logo movement': 'تشغيل حركة الشعارات',
      'Pause logo movement': 'إيقاف حركة الشعارات',
      'pieces': 'قطعة محتوى',
      'Summer launch · Riyadh': 'إطلاق الصيف · الرياض',
      'Always-on growth · GCC': 'نمو مستمر · دول الخليج',
      'New location · Jeddah': 'فرع جديد · جدة',
      '01–30 Jun 2026': '1–30 يونيو 2026',
      '01 Jul–30 Sep 2026': '1 يوليو–30 سبتمبر 2026',
      '14–28 Aug 2026': '14–28 أغسطس 2026',
      'Summer launch': 'إطلاق الصيف',
      'The Beauty Edit': 'مختارات الجمال',
      'Night Market': 'سوق الليل',
      'Always-on growth': 'نمو مستمر',
      'Weekend edit': 'مختارات نهاية الأسبوع',
      'New collection': 'التشكيلة الجديدة',
      'Jeddah opening': 'افتتاح جدة',
      'VIP preview': 'معاينة كبار الضيوف',
      'Founder dinner': 'عشاء المؤسسين',
      'In progress': 'قيد التنفيذ',
      'Coverage live': 'التغطية جارية',
      'Brief approved': 'اعتُمد الموجز',
      'Ready to launch': 'جاهزة للإطلاق',
      'Confirmed': 'مؤكدة',
      'Riyadh · 48 creators': 'الرياض · 48 صانع محتوى',
      'Jeddah · 26 creators': 'جدة · 26 صانع محتوى',
      'Al Khobar · 18 creators': 'الخبر · 18 صانع محتوى',
      'GCC · 72 creators': 'دول الخليج · 72 صانع محتوى',
      'Dubai · 32 creators': 'دبي · 32 صانع محتوى',
      'Kuwait · 24 creators': 'الكويت · 24 صانع محتوى',
      'Jeddah · 35 creators': 'جدة · 35 صانع محتوى',
      'Jeddah · 14 creators': 'جدة · 14 صانع محتوى',
      'Jeddah · 9 creators': 'جدة · 9 صانع محتوى'
    }
  };
  function t(key) {
    var table = STRINGS[LANG];
    return (table && table[key]) || key;
  }

  /* ---------- Theme -------------------------------------------------- */
  var THEME_KEY = 'elite-theme';
  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    var themeColor = document.querySelector('meta[name="theme-color"]');
    if (themeColor) themeColor.setAttribute('content', theme === 'dark' ? '#0A0A0B' : '#FFFFFF');
    document.querySelectorAll('[data-theme-toggle]').forEach(function (b) {
      b.setAttribute('aria-label', theme === 'dark' ? t('Switch to light theme') : t('Switch to dark theme'));
      b.setAttribute('aria-pressed', String(theme === 'dark'));
    });
  }
  var stored = null;
  try { stored = localStorage.getItem(THEME_KEY); } catch (e) {}
  applyTheme(stored || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'));

  document.addEventListener('click', function (e) {
    var t = e.target.closest('[data-theme-toggle]');
    if (!t) return;
    var next = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    applyTheme(next);
    try { localStorage.setItem(THEME_KEY, next); } catch (err) {}
  });

  /* ---------- Sticky nav --------------------------------------------- */
  var nav = document.querySelector('.nav');
  if (nav) {
    var onScroll = function () {
      nav.classList.toggle('is-stuck', window.scrollY > 24);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ---------- Mobile drawer ------------------------------------------ */
  var drawer = document.getElementById('drawer');
  var toggle = document.querySelector('[data-drawer-toggle]');
  function setDrawer(open) {
    if (!drawer || !toggle) return;
    drawer.classList.toggle('is-open', open);
    toggle.setAttribute('aria-expanded', String(open));
    document.body.classList.toggle('is-locked', open);
    toggle.querySelector('.ico-open').style.display = open ? 'none' : 'block';
    toggle.querySelector('.ico-close').style.display = open ? 'block' : 'none';
  }
  if (toggle) {
    toggle.addEventListener('click', function () {
      setDrawer(!drawer.classList.contains('is-open'));
    });
    drawer.addEventListener('click', function (e) { if (e.target.closest('a')) setDrawer(false); });
  }
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    if (drawer && drawer.classList.contains('is-open')) setDrawer(false);
    document.querySelectorAll('.modal.is-open').forEach(function (m) { closeModal(m); });
  });
  window.addEventListener('resize', function () {
    if (window.innerWidth > 1024 && drawer && drawer.classList.contains('is-open')) setDrawer(false);
  });

  /* ---------- Scroll reveal ------------------------------------------ */
  var revealables = document.querySelectorAll('.reveal, .rise');
  if (reduced || !('IntersectionObserver' in window)) {
    revealables.forEach(function (el) { el.classList.add('is-in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    revealables.forEach(function (el) { io.observe(el); });
  }

  /* ---------- Count-up numbers --------------------------------------- */
  var counters = document.querySelectorAll('[data-count]');
  function runCount(el) {
    var target = parseFloat(el.getAttribute('data-count'));
    var suffix = el.getAttribute('data-suffix') || '';
    var prefix = el.getAttribute('data-prefix') || '';
    var dec = (el.getAttribute('data-dec') | 0);
    if (reduced) { el.textContent = prefix + target.toFixed(dec) + suffix; return; }
    var start = performance.now(), dur = 1400;
    (function tick(now) {
      var p = Math.min(1, (now - start) / dur);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = prefix + (target * eased).toFixed(dec) + suffix;
      if (p < 1) requestAnimationFrame(tick);
    })(start);
  }
  if ('IntersectionObserver' in window) {
    var cio = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { runCount(e.target); cio.unobserve(e.target); } });
    }, { threshold: 0.5 });
    counters.forEach(function (c) { cio.observe(c); });
  } else counters.forEach(runCount);

  /* ---------- Animated bars ------------------------------------------ */
  var bars = document.querySelectorAll('.bar-row .fill[data-pct]');
  if ('IntersectionObserver' in window) {
    var bio = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.style.width = e.target.getAttribute('data-pct') + '%';
        bio.unobserve(e.target);
      });
    }, { threshold: 0.4 });
    bars.forEach(function (b) { bio.observe(b); });
  } else bars.forEach(function (b) { b.style.width = b.getAttribute('data-pct') + '%'; });

  /* ---------- Accordion ---------------------------------------------- */
  document.querySelectorAll('.acc__trigger').forEach(function (trg) {
    trg.addEventListener('click', function () {
      var panel = document.getElementById(trg.getAttribute('aria-controls'));
      var open = trg.getAttribute('aria-expanded') === 'true';
      var group = trg.closest('.accordion');
      if (group && group.hasAttribute('data-single') && !open) {
        group.querySelectorAll('.acc__trigger[aria-expanded="true"]').forEach(function (o) {
          var op = document.getElementById(o.getAttribute('aria-controls'));
          o.setAttribute('aria-expanded', 'false');
          op.style.height = op.scrollHeight + 'px';
          requestAnimationFrame(function () { op.style.height = '0px'; });
        });
      }
      trg.setAttribute('aria-expanded', String(!open));
      if (open) {
        panel.style.height = panel.scrollHeight + 'px';
        requestAnimationFrame(function () { panel.style.height = '0px'; });
      } else {
        panel.style.height = panel.scrollHeight + 'px';
        panel.addEventListener('transitionend', function te() {
          panel.style.height = 'auto';
          panel.removeEventListener('transitionend', te);
        });
      }
    });
  });

  /* ---------- Tabs / segmented --------------------------------------- */
  document.querySelectorAll('[role="tablist"]').forEach(function (list) {
    var tabs = [].slice.call(list.querySelectorAll('[role="tab"]'));
    function select(tab) {
      tabs.forEach(function (t) {
        var on = t === tab;
        t.setAttribute('aria-selected', String(on));
        t.tabIndex = on ? 0 : -1;
        var p = document.getElementById(t.getAttribute('aria-controls'));
        if (p) p.hidden = !on;
      });
    }
    list.addEventListener('click', function (e) {
      var t = e.target.closest('[role="tab"]'); if (t) select(t);
    });
    list.addEventListener('keydown', function (e) {
      var i = tabs.indexOf(document.activeElement);
      if (i < 0) return;
      var n = e.key === 'ArrowRight' ? i + 1 : e.key === 'ArrowLeft' ? i - 1 : -1;
      if (n < 0) return;
      e.preventDefault();
      var next = tabs[(n + tabs.length) % tabs.length];
      next.focus(); select(next);
    });
  });

  /* ---------- Filter chips ------------------------------------------- */
  document.querySelectorAll('[data-filter-group]').forEach(function (group) {
    var targetSel = group.getAttribute('data-filter-target');
    var items = document.querySelectorAll(targetSel + ' [data-cat]');
    var empty = document.querySelector(group.getAttribute('data-filter-empty') || '#nothing');
    group.addEventListener('click', function (e) {
      var chip = e.target.closest('.chip'); if (!chip) return;
      group.querySelectorAll('.chip').forEach(function (c) { c.setAttribute('aria-pressed', String(c === chip)); });
      var val = chip.getAttribute('data-value');
      var shown = 0;
      items.forEach(function (it) {
        var ok = val === 'all' || it.getAttribute('data-cat').split('|').indexOf(val) > -1;
        it.hidden = !ok; if (ok) shown++;
      });
      if (empty) empty.hidden = shown !== 0;
    });
  });

  /* ---------- Client search ------------------------------------------ */
  var search = document.querySelector('[data-search]');
  if (search) {
    var scope = document.querySelectorAll(search.getAttribute('data-search') + ' [data-name]');
    var searchEmpty = document.querySelector('#search-empty');
    search.addEventListener('input', function () {
      var q = search.value.trim().toLowerCase();
      var shown = 0;
      scope.forEach(function (el) {
        var ok = !q || el.getAttribute('data-name').toLowerCase().indexOf(q) > -1;
        el.hidden = !ok; if (ok) shown++;
      });
      if (searchEmpty) searchEmpty.hidden = shown !== 0;
    });
  }

  /* ---------- Modal --------------------------------------------------- */
  var lastFocus = null;
  function openModal(m) {
    lastFocus = document.activeElement;
    m.classList.add('is-open');
    document.body.classList.add('is-locked');
    var f = m.querySelector('button, [href], input, select, textarea');
    if (f) f.focus();
  }
  function closeModal(m) {
    m.classList.remove('is-open');
    document.body.classList.remove('is-locked');
    if (lastFocus) lastFocus.focus();
  }
  document.addEventListener('click', function (e) {
    var open = e.target.closest('[data-modal-open]');
    if (open) { var m = document.getElementById(open.getAttribute('data-modal-open')); if (m) { e.preventDefault(); openModal(m); } return; }
    var close = e.target.closest('[data-modal-close]');
    if (close) { closeModal(close.closest('.modal')); return; }
    if (e.target.classList.contains('modal')) closeModal(e.target);
  });

  /* ---------- Toast --------------------------------------------------- */
  function toast(msg) {
    var t = document.getElementById('toast');
    if (!t) return;
    t.textContent = msg;
    t.classList.add('is-visible');
    clearTimeout(t._timer);
    t._timer = setTimeout(function () { t.classList.remove('is-visible'); }, 3200);
  }
  window.eliteToast = toast;

  /* ---------- Forms (client-side validation demo) --------------------- */
  document.querySelectorAll('form[data-validate]').forEach(function (form) {
    form.setAttribute('novalidate', '');
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var ok = true;
      form.querySelectorAll('[required]').forEach(function (input) {
        var field = input.closest('.field');
        var valid = input.checkValidity() && input.value.trim() !== '';
        if (field) field.classList.toggle('is-invalid', !valid);
        if (!valid && ok) { input.focus(); ok = false; }
      });
      if (!ok) { toast(t('Please complete the highlighted fields.')); return; }
      var btn = form.querySelector('[type="submit"]');
      if (btn) { btn.setAttribute('aria-disabled', 'true'); btn.dataset.label = btn.textContent; btn.textContent = t('Sending…'); }
      setTimeout(function () {
        if (btn) { btn.removeAttribute('aria-disabled'); btn.textContent = btn.dataset.label; }
        form.reset();
        toast(form.getAttribute('data-success') || t('Thank you — we will be in touch shortly.'));
      }, 900);
    });
    form.querySelectorAll('[required]').forEach(function (i) {
      i.addEventListener('input', function () {
        var f = i.closest('.field'); if (f) f.classList.remove('is-invalid');
      });
    });
  });

  /* ---------- Dashboard demo ---------------------------------------- */
  function initDashboardDemo() {
    var demo = document.querySelector('[data-dashboard-demo]');
    if (!demo) return;
    var datasets = {
      launch: {
        campaign: 'Summer launch · Riyadh', period: '01–30 Jun 2026',
        kpis: { branches: 4, creators: 128, campaigns: 7, coverage: 346 },
        stages: { pending: 12, confirmed: 28, visited: 24, delivered: 19, 'post-creation': 16, shared: 14, covered: 11 },
        coverage: { story: 201, post: 82, video: 63 },
        campaigns: [['Summer launch', 'Riyadh · 48 creators', 'In progress'], ['The Beauty Edit', 'Jeddah · 26 creators', 'Coverage live'], ['Night Market', 'Al Khobar · 18 creators', 'Brief approved']]
      },
      growth: {
        campaign: 'Always-on growth · GCC', period: '01 Jul–30 Sep 2026',
        kpis: { branches: 6, creators: 214, campaigns: 11, coverage: 589 },
        stages: { pending: 18, confirmed: 42, visited: 37, delivered: 31, 'post-creation': 29, shared: 25, covered: 21 },
        coverage: { story: 344, post: 141, video: 104 },
        campaigns: [['Always-on growth', 'GCC · 72 creators', 'In progress'], ['Weekend edit', 'Dubai · 32 creators', 'Coverage live'], ['New collection', 'Kuwait · 24 creators', 'Ready to launch']]
      },
      opening: {
        campaign: 'New location · Jeddah', period: '14–28 Aug 2026',
        kpis: { branches: 2, creators: 76, campaigns: 4, coverage: 184 },
        stages: { pending: 8, confirmed: 17, visited: 15, delivered: 13, 'post-creation': 10, shared: 8, covered: 6 },
        coverage: { story: 112, post: 43, video: 29 },
        campaigns: [['Jeddah opening', 'Jeddah · 35 creators', 'In progress'], ['VIP preview', 'Jeddah · 14 creators', 'Coverage live'], ['Founder dinner', 'Jeddah · 9 creators', 'Confirmed']]
      }
    };
    function setValue(el, value) {
      if (!el) return;
      var current = Number(el.textContent.replace(/[^0-9.]/g, '')) || 0;
      if (reduced) { el.textContent = value; return; }
      var start = performance.now(), duration = 420;
      (function tick(now) {
        var p = Math.min(1, (now - start) / duration);
        el.textContent = Math.round(current + (value - current) * (1 - Math.pow(1 - p, 3)));
        if (p < 1) requestAnimationFrame(tick);
      })(start);
    }
    function render(key) {
      var data = datasets[key];
      demo.querySelectorAll('[data-demo-view]').forEach(function (button) {
        button.setAttribute('aria-pressed', String(button.getAttribute('data-demo-view') === key));
      });
      document.querySelectorAll('[data-demo-kpi]').forEach(function (el) { setValue(el, data.kpis[el.getAttribute('data-demo-kpi')]); });
      document.querySelectorAll('[data-demo-stage]').forEach(function (el) { setValue(el, data.stages[el.getAttribute('data-demo-stage')]); });
      document.querySelectorAll('[data-demo-bar]').forEach(function (bar) {
        var name = bar.getAttribute('data-demo-bar'), value = data.coverage[name];
        bar.style.width = (value / data.kpis.coverage * 100) + '%';
      });
      document.querySelectorAll('[data-demo-pct]').forEach(function (el) { el.textContent = data.coverage[el.getAttribute('data-demo-pct')]; });
      var title = document.querySelector('[data-demo-campaign]'), period = document.querySelector('[data-demo-period]'), total = document.querySelector('[data-demo-total]'), list = document.querySelector('[data-demo-campaigns]');
      if (title) title.textContent = t(data.campaign);
      if (period) period.textContent = t(data.period);
      if (total) total.textContent = data.kpis.coverage + ' ' + t('pieces');
      if (list) list.innerHTML = data.campaigns.map(function (item) {
        return '<div class="demo-campaign"><span class="demo-campaign__mark" aria-hidden="true"></span><div><b>' + t(item[0]) + '</b><span>' + t(item[1]) + '</span></div><em>' + t(item[2]) + '</em></div>';
      }).join('');
    }
    demo.addEventListener('click', function (e) {
      var button = e.target.closest('[data-demo-view]');
      if (button) render(button.getAttribute('data-demo-view'));
    });
    render('launch');
  }
  initDashboardDemo();

  /* ---------- Marquee duplication ------------------------------------- */
  document.querySelectorAll('.marquee__track[data-loop]').forEach(function (track) {
    Array.prototype.slice.call(track.children).forEach(function (item) {
      var clone = item.cloneNode(true);
      clone.setAttribute('aria-hidden', 'true');
      track.appendChild(clone);
    });
  });
  document.querySelectorAll('[data-marquee-toggle]').forEach(function (button) {
    button.addEventListener('click', function () {
      var region = button.closest('.trust');
      if (!region) return;
      var paused = region.classList.toggle('is-marquee-paused');
      button.setAttribute('aria-pressed', String(paused));
      button.textContent = paused ? t('Play logo movement') : t('Pause logo movement');
    });
  });


  /* ---------- Campaign films -------------------------------------------
     Muted, looping, preload="none". Only one plays at a time; hover previews
     on precise pointers, the badge is the control everywhere else. */
  var playingVideo = null;

  function stopFilm(v) {
    if (!v) return;
    v.pause();
    var card = v.closest('.story') || v.closest('.reel__row');
    var btn = card && card.querySelector('[data-video-toggle]');
    if (btn) btn.setAttribute('aria-pressed', 'false');
    if (playingVideo === v) playingVideo = null;
  }

  function startFilm(v) {
    if (!v || playingVideo === v) return;
    stopFilm(playingVideo);
    var p = v.play();
    if (p && p.catch) p.catch(function () { stopFilm(v); });
    playingVideo = v;
    var card = v.closest('.story') || v.closest('.reel__row');
    var btn = card && card.querySelector('[data-video-toggle]');
    if (btn) btn.setAttribute('aria-pressed', 'true');
  }

  document.querySelectorAll('[data-video-toggle]').forEach(function (btn) {
    var card = btn.closest('.story') || btn.closest('.reel__row');
    var video = card && card.querySelector('video');
    if (!video) return;

    btn.addEventListener('click', function (e) {
      e.preventDefault();
      e.stopPropagation();
      if (video.paused) startFilm(video); else stopFilm(video);
    });

    // Hover preview on the grid cards only; the reel rows are large enough
    // that the badge is the right control.
    if (!reduced && card.classList.contains('story') &&
        window.matchMedia('(hover:hover) and (pointer:fine)').matches) {
      card.addEventListener('mouseenter', function () { startFilm(video); });
      card.addEventListener('mouseleave', function () { stopFilm(video); video.currentTime = 0; });
    }
  });

  if ('IntersectionObserver' in window) {
    var filmObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (!e.isIntersecting) stopFilm(e.target); });
    }, { threshold: 0 });
    document.querySelectorAll('video.story__video').forEach(function (v) { filmObserver.observe(v); });
  }
  document.addEventListener('visibilitychange', function () {
    if (document.hidden) stopFilm(playingVideo);
  });

  /* ---------- Current year -------------------------------------------- */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
