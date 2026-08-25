# ELITƎ — Premium UI/UX Rebuild

A complete front-end rebuild of gc-elite.com: same pages, same content, same
routes — rebuilt on one design system with an Apple-inspired composition,
spacing and motion language, while keeping Elite's black + gold identity and
the reversed-E wordmark.

## Run it locally

```powershell
.\scripts\build-site.ps1
py -3 -m http.server 8080
# open http://localhost:8080
```

Nothing to install. No build step required to view the site.

### Windows-friendly build commands

The source files generate the HTML pages, so use one of the wrappers before
committing or sharing a build:

```powershell
# PowerShell: generate all pages, then verify them
.\scripts\build-site.ps1

# Verify the existing generated pages only
.\scripts\build-site.ps1 -VerifyOnly
```

```cmd
:: cmd.exe: generate all pages, then verify them
scripts\build-site.cmd
```

Both wrappers use the Python launcher (`py -3`) when it is available and fall
back to `python`. They run only standard-library code; there are no package or
shell-specific dependencies.

If this folder is initialized as a Git repository, enable the included guard:

```bash
git config core.hooksPath .githooks
```

The hook verifies that every generated page still includes the shared CSS and
JavaScript, and that each Arabic page still matches the structure of its English
twin. It deliberately does not rewrite files during a commit.

## Structure

```
index.html          Home        (redesigned most aggressively)
dashboard.html      Dashboard   (marketing preview of the product)
case-studies.html   Success Stories
sponsors.html       Our Clients
contacts.html       Contact Us
about.html          About Us
assets/css/elite.css   the whole design system (tokens → components → responsive)
assets/js/elite.js     nav, drawer, theme, reveal, counters, tabs, accordion,
                       filters, search, modal, toast, form validation
build.py               shared shell (head / nav / footer / modal)
pages_home.py          homepage content
pages_rest.py          all other page content
```

### Regenerating the HTML

The HTML files are generated so the nav/footer never drift between pages:

```bash
python3 pages_home.py && python3 pages_rest.py
```

Edit `build.py` for anything shared, the `pages_*.py` files for page content,
then re-run. If you prefer to hand-edit the HTML directly, you can — just
delete the Python files and keep the output.

## Design system

Everything is driven by CSS custom properties in `:root` (and overridden under
`[data-theme="dark"]`):

| Group      | Tokens |
|------------|--------|
| Brand gold | `--gold-100 … --gold-700` (`--gold-500` = primary) |
| Neutrals   | `--ink-050 … --ink-900` |
| Semantic   | `--bg`, `--bg-sunken`, `--bg-raised`, `--text`, `--text-muted`, `--border`, `--accent` |
| Radius     | `--r-xs … --r-2xl`, `--r-pill` |
| Elevation  | `--sh-1 … --sh-4`, `--sh-gold` |
| Spacing    | `--s-1 … --s-40` (4pt scale) + `--section-y`, `--gutter`, `--container` |
| Motion     | `--ease`, `--ease-out`, `--dur-1 … --dur-4` |

Change the brand gold in one place and the entire site follows.

Components: `.btn` (primary / dark / ghost / quiet / on-dark, sm–lg, block),
`.card`, `.service-card`, `.story`, `.kpi`, `.stat`, `.nav`, `.drawer`,
`.input/.select/.textarea/.check/.segmented`, `.tabs`, `.chips`, `.accordion`,
`.modal`, `.toast`, `.state` (empty / loading / error), `.marquee`,
`.logo-chip`, `.cta-band`, `.footer`.

## Behaviour

- **Dark mode** — real second theme, persisted to `localStorage`, respects
  `prefers-color-scheme` on first visit.
- **Motion** — scroll reveals, count-ups, animated bars, logo marquee, hover
  depth. All of it collapses under `prefers-reduced-motion: reduce`.
- **Accessibility** — semantic landmarks, skip link, visible branded focus
  rings, `aria-current` on nav, real tab/accordion ARIA with arrow-key support,
  labelled fields, live-region toast, `hidden` handled correctly.
- **Responsive** — layouts are reconsidered per breakpoint (nav collapses to a
  full-screen drawer, grids re-flow, hero re-stacks), not just shrunk. Verified
  at 1440 and 390 with no horizontal overflow on any page.

## Real media

Every image on the site is the real asset, downloaded from gc-elite.com and
re-encoded for static delivery:

| Folder | What | Count |
|---|---|---|
| `assets/img/brand/` | Elite logo, hero photograph, banners | 5 |
| `assets/img/services/` | the four service tiles | 4 |
| `assets/img/brands/` | client logos, one per brand | 39 |

`assets_map.py` maps the `CLIENTS` names in `pages_rest.py` to those files and is
generated, not hand-written. A brand missing from the map falls back to the
original text chip, so the grid never breaks — `odachi` is the one such case,
because its source image 404s on the live site too.

`scripts/optimize_images.py` caps each class of image at the largest size the
layout can use and re-encodes it (`--apply` to write; no argument for a dry run).
It is idempotent, so it is safe to re-run after adding an asset.

## Arabic

The site ships in English and Arabic. `ar/` holds a full RTL twin of every page.

```bash
python i18n_build.py      # after the English pages are generated
```

- `i18n_ar.py` is the dictionary. Where gc-elite.com already publishes Arabic
  (About, the contact intro, the footer, the navigation) that wording is
  reproduced verbatim; the rest is translated in the same register.
- The English HTML is the only source of layout. `i18n_build.py` swaps copy,
  flips the document to `lang="ar" dir="rtl"`, repoints `assets/` one level up
  and turns the language toggle around — so the two languages cannot drift.
- `assets/css/elite-rtl.css` is the RTL layer: type stack, mirrored positioning,
  flipped arrows. It changes no colour, size or spacing, so Arabic is the same
  design read the other way.
- A word that means different things in different places (`Influencer` is a
  service on the home page and a form option on the contact page) is
  disambiguated with `data-tr` and `AR_KEYED`.
- Any string without a translation fails the build loudly and is listed in
  `_harvest/untranslated.txt`.
- `assets/js/elite.js` carries its own small `STRINGS` table, keyed off
  `<html lang>`. Anything the JavaScript injects at runtime — toasts, the
  submit label, the marquee toggle, the dashboard demo dataset — has to be in
  it, or English leaks back into `ar/` after the page loads.
- **`ar/` is generated output. Never hand-edit it and never check a fetched
  copy of the deployed site back into it** — that is exactly how the Arabic
  home page ended up six sections behind the English one. `scripts/verify_site.py`
  now compares the section, heading and nav-link counts of each pair and fails
  the build if they diverge.

## Still to wire

1. **Dashboard figures** — the dashboard shows clearly labelled illustrative
   data. It is a public preview, not the authenticated app; replace the demo
   dataset in `assets/js/elite.js` when a real dashboard API exists.
2. **Forms** — `data-validate` handles client-side validation and the success
   toast. Point the `submit` handler in `elite.js` at your real endpoint.
3. **Success-story media** — `.story__media` still uses generated `.art`
   artwork; swap for `<img>` when the campaign stills are available.
4. **Client categories** — `data-cat` on `.logo-chip` and `.story` is a working
   sample mapping. Point it at the real CMS field; the filter JS needs no change.
