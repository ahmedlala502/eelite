#!/usr/bin/env python3
"""Build and verify the dependency-free Elite static site.

The script intentionally uses only the Python standard library so the same
check works from PowerShell, cmd.exe, Git hooks, and CI without npm installs.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAGES = ("index.html", "about.html", "case-studies.html", "sponsors.html", "contacts.html", "dashboard.html")
AR_PAGES = tuple("ar/" + name for name in PAGES)


class SiteParser(HTMLParser):
    """Standard-library parser used to catch malformed generated markup."""


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def build() -> None:
    # i18n_build.py reads the English output, so it has to run last.
    for source in ("pages_home.py", "pages_rest.py", "i18n_build.py"):
        result = subprocess.run([sys.executable, source], cwd=ROOT, check=False)
        if result.returncode:
            fail(f"{source} failed with exit code {result.returncode}")


def verify() -> None:
    for asset in ("assets/css/elite.css", "assets/js/elite.js"):
        if not (ROOT / asset).is_file():
            fail(f"missing required asset: {asset}")

    for page in PAGES + AR_PAGES:
        path = ROOT / page
        if not path.is_file():
            fail(f"missing generated page: {page}")
        markup = path.read_text(encoding="utf-8")
        arabic = page.startswith("ar/")
        prefix = "../" if arabic else ""
        for asset in ("assets/css/elite.css", "assets/js/elite.js"):
            if prefix + asset not in markup:
                fail(f"{page} does not include {prefix + asset}")
        if arabic:
            # The Arabic pages must actually be Arabic: RTL, the RTL sheet, and
            # copy that is not still English.
            if 'lang="ar"' not in markup or 'dir="rtl"' not in markup:
                fail(f"{page} is not marked lang=ar dir=rtl")
            if "../assets/css/elite-rtl.css" not in markup:
                fail(f"{page} does not include the RTL stylesheet")
            if not any("؀" <= ch <= "ۿ" for ch in markup):
                fail(f"{page} contains no Arabic text")
            if 'href="assets/' in markup:
                fail(f"{page} still points at a top-level assets/ path")
        parser = SiteParser()
        try:
            parser.feed(markup)
            parser.close()
        except Exception as exc:  # HTMLParser's exception varies by Python version.
            fail(f"could not parse {page}: {exc}")

    # Structural parity. The Arabic pages are a translation of the English
    # markup, so the two must carry the same skeleton. This is the check that
    # was missing when ar/ was allowed to be served from a stale snapshot and
    # quietly fell six sections behind the English home page.
    import re as _re0
    for page in PAGES:
        en = (ROOT / page).read_text(encoding="utf-8")
        ar = (ROOT / "ar" / page).read_text(encoding="utf-8")
        for label, pattern in (("section", r"<section"),
                               ("heading", r"<h[1-3]"),
                               ("nav link", r'class="nav__link"')):
            n_en = len(_re0.findall(pattern, en))
            n_ar = len(_re0.findall(pattern, ar))
            if n_en != n_ar:
                fail(f"ar/{page} has {n_ar} {label}(s) but {page} has {n_en} — "
                     "the Arabic page is out of step; re-run i18n_build.py")
        # No English page may exist only in one language.
        for target in sorted(set(_re0.findall(r'href="([a-z0-9-]+\.html)"', ar))):
            if not (ROOT / "ar" / target).is_file():
                fail(f"ar/{page} links to ar/{target}, which does not exist")

    # Every logo referenced by a page has to exist on disk.
    import re as _re
    missing_assets = set()
    for page in PAGES:
        markup = (ROOT / page).read_text(encoding="utf-8")
        for src in _re.findall(r'src="(assets/img/[^"]+)"', markup):
            if not (ROOT / src).is_file():
                missing_assets.add(src)
    if missing_assets:
        fail("referenced images are missing: " + ", ".join(sorted(missing_assets)))

    print(f"Verified {len(PAGES)} English + {len(AR_PAGES)} Arabic pages, "
          f"shared assets and every referenced image.")


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description="Build and verify the Elite static site.")
    cli.add_argument("--build", action="store_true", help="Regenerate pages before verification.")
    args = cli.parse_args()
    if args.build:
        build()
    verify()
