# -*- coding: utf-8 -*-
"""Generate the Arabic site into ar/ from the English pages.

The English HTML is the single source of layout: this script only swaps the copy,
flips the document to RTL, repoints relative asset paths one level up, and turns
the language toggle around. Nothing about the design changes, so the two
languages cannot drift apart.

Run after pages_home.py / pages_rest.py:

    python i18n_build.py

It prints any string it could not translate, so the dictionary can be completed.
"""
import io
import os
import re
import sys
from html.parser import HTMLParser

from i18n_ar import AR, KEEP, AR_KEYED
from pages_rest import CLIENTS

# Client names stay in Latin script, exactly as gc-elite.com renders them.
KEEP = set(KEEP) | {name for name, _ in CLIENTS} | {
    "width=device-width, initial-scale=1, viewport-fit=cover",
    "Morini Riyadh", "ROKA", "Enigmaku", "Beit El Sabban", "Tashas Cafe",
}

HERE = os.path.dirname(os.path.abspath(__file__))
AR_DIR = os.path.join(HERE, "ar")
PAGES = ["index.html", "dashboard.html", "case-studies.html",
         "sponsors.html", "contacts.html", "about.html"]

# data-success is the text of the toast a form shows on success, so it is
# reader-facing copy like any other string on the page.
ATTRS = ("alt", "title", "placeholder", "aria-label", "content", "value",
         "data-success")
SKIP_TAGS = {"script", "style"}
NOISE = re.compile(r"^[\s\d%+.,:;/|()\[\]{}<>—–\-·•★☆©®™→←↑↓&#*'\"@!?~^$=_\\]*$")
METRIC = re.compile(r"^\+?\d+(?:\.\d+)?[KMB]$")
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}

# Tajawal carries the Arabic UI (it is geometric, like Plus Jakarta Sans on the
# Latin side); Almarai is a little more compact and takes the display slot
# that Playfair Display holds in English.
ARABIC_FONT = (
    '<link href="https://fonts.googleapis.com/css2?'
    'family=Tajawal:wght@300;400;500;700;800&'
    'family=Almarai:wght@400;700;800&display=swap" rel="stylesheet">'
)


class Translator(HTMLParser):
    """Rewrites text nodes and reader-facing attributes; leaves markup alone."""

    def __init__(self, page):
        super().__init__(convert_charrefs=True)
        self.page = page
        self.out = []
        self.stack = []
        self.missing = []
        # Set when the tag just opened carries data-tr; consumed by the text node
        # inside it, so a word can differ by context.
        self.pending_key = None

    # -- helpers ---------------------------------------------------------
    def tr(self, text):
        stripped = text.strip()
        if not stripped or NOISE.match(stripped) or METRIC.match(stripped) or stripped in KEEP:
            return text
        # "<Brand> — success story": the brand keeps its Latin spelling, the
        # descriptor is translated. Brands come from the CMS, so this must not
        # depend on the name being listed in KEEP.
        story_suffix = " — success story"
        if stripped.endswith(story_suffix):
            return text.replace(stripped, stripped[:-len(story_suffix)] + " — قصة نجاح")
        if stripped in AR:
            return text.replace(stripped, AR[stripped])
        self.missing.append(stripped)
        return text

    @staticmethod
    def repath(value):
        """assets/… lives one directory up from ar/."""
        if value.startswith("assets/"):
            return "../" + value
        return value

    # -- parser hooks ----------------------------------------------------
    def _tag(self, tag, attrs, self_closing):
        parts = ["<" + tag]
        for name, value in attrs:
            if value is None:
                parts.append(" " + name)
                continue
            v = value
            if name in ("href", "src"):
                v = self.repath(v)
            if name in ATTRS:
                if name == "content" and not re.search(r"[A-Za-z]{3}", v):
                    pass
                else:
                    v = self.tr(v)
            parts.append(' %s="%s"' % (name, v.replace("&", "&amp;").replace('"', "&quot;")))
        parts.append("/>" if self_closing else ">")
        self.out.append("".join(parts))

    def handle_starttag(self, tag, attrs):
        self.pending_key = dict(attrs).get("data-tr")
        self._tag(tag, attrs, tag in VOID)
        if tag not in VOID:
            self.stack.append(tag)

    def handle_startendtag(self, tag, attrs):
        self._tag(tag, attrs, True)

    def handle_endtag(self, tag):
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        self.out.append("</%s>" % tag)

    @staticmethod
    def esc(text):
        return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    def handle_data(self, data):
        if self.stack and self.stack[-1] in SKIP_TAGS:
            self.out.append(data)
            return
        key, self.pending_key = self.pending_key, None
        if key and key in AR_KEYED and data.strip():
            self.out.append(self.esc(data.replace(data.strip(), AR_KEYED[key])))
            return
        self.out.append(self.esc(self.tr(data)))

    def handle_comment(self, data):
        self.out.append("<!--%s-->" % data)

    def handle_decl(self, decl):
        self.out.append("<!%s>" % decl)

    def result(self):
        return "".join(self.out)


def arabicise(html, page):
    t = Translator(page)
    t.feed(html)
    out = t.result()

    # Document direction and language.
    out = out.replace('<html lang="en" data-theme="light">',
                      '<html lang="ar" dir="rtl" data-theme="light">', 1)
    # Arabic face alongside the Latin one, and the RTL stylesheet.
    # The translator emits void elements self-closing, so match either spelling.
    out = re.sub(
        r'<link rel="stylesheet" href="\.\./assets/css/elite\.css"\s*/?>',
        (ARABIC_FONT + '\n<link rel="stylesheet" href="../assets/css/elite.css"/>'
         '\n<link rel="stylesheet" href="../assets/css/elite-rtl.css"/>'),
        out, count=1)
    # The toggle points back to English from here.
    out = re.sub(
        r'<a class="icon-btn icon-btn--text lang-toggle" href="ar/([^"]+)" hreflang="ar" lang="ar" aria-label="[^"]*">',
        lambda m: ('<a class="icon-btn icon-btn--text lang-toggle" href="../%s" hreflang="en" lang="en" '
                   'aria-label="Switch language to English">' % m.group(1)),
        out)
    out = re.sub(r'(<a class="icon-btn icon-btn--text lang-toggle"[^>]*>.*?<span>)AR(</span>)',
                 r'\1EN\2', out, flags=re.S)
    # Search engines: declare the pair both ways.
    alt = ('<link rel="alternate" hreflang="en" href="../%s">\n'
           '<link rel="alternate" hreflang="ar" href="%s">\n' % (page, page))
    out = out.replace("</head>", alt + "</head>", 1)
    return out


def add_en_alternates(html, page):
    alt = ('<link rel="alternate" hreflang="en" href="%s">\n'
           '<link rel="alternate" hreflang="ar" href="ar/%s">\n' % (page, page))
    if 'rel="alternate"' in html:
        return html
    return html.replace("</head>", alt + "</head>", 1)


def main():
    # Windows terminals often default to cp1252. Missing-copy diagnostics must
    # never crash the build when a brand contains characters such as Ū or Ō.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="backslashreplace")
    os.makedirs(AR_DIR, exist_ok=True)
    missing = []
    for page in PAGES:
        src = os.path.join(HERE, page)
        if not os.path.exists(src):
            print("skip (not generated yet):", page)
            continue
        html = io.open(src, encoding="utf-8").read()

        # Keep the English page in step: declare its Arabic twin.
        io.open(src, "w", encoding="utf-8").write(add_en_alternates(html, page))

        t = Translator(page)
        t.feed(html)
        out = arabicise(html, page)
        missing.extend(t.missing)
        io.open(os.path.join(AR_DIR, page), "w", encoding="utf-8").write(out)
        print("wrote ar/%s  %d bytes" % (page, len(out.encode("utf-8"))))

    uniq = []
    seen = set()
    for m in missing:
        if m not in seen:
            seen.add(m)
            uniq.append(m)
    if uniq:
        io.open(os.path.join(HERE, "_harvest", "untranslated.txt"), "w",
                encoding="utf-8").write("\n".join(uniq))
        print("\nUNTRANSLATED: %d string(s) — see _harvest/untranslated.txt" % len(uniq))
        for m in uniq[:25]:
            print("   ", m[:100])
        return 1
    print("\nEvery string translated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
