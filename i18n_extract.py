# -*- coding: utf-8 -*-
"""List every translatable string in the generated English pages.

Text nodes plus the attributes that surface to a reader (alt/title/placeholder/
aria-label/content). Script and style contents are skipped. Output is a stable,
de-duplicated list so the Arabic dictionary can be checked for coverage.
"""
import io
import json
import os
import re
from html.parser import HTMLParser

HERE = os.path.dirname(os.path.abspath(__file__))
PAGES = ["index.html", "dashboard.html", "case-studies.html",
         "sponsors.html", "contacts.html", "about.html"]
ATTRS = ("alt", "title", "placeholder", "aria-label", "content", "value", "data-suffix")
SKIP_TAGS = {"script", "style"}
# Pure punctuation, numbers, or single characters carry nothing to translate.
NOISE = re.compile(r"^[\s\d%+.,:;/|()\[\]{}<>—–\-·•★☆©®™→←↑↓&#*'\"@!?~^$=_\\]*$")


class Collector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.found = []

    def handle_starttag(self, tag, attrs):
        self.stack.append(tag)
        for name, value in attrs:
            if name in ATTRS and value and not NOISE.match(value):
                if name == "content" and not re.search(r"[A-Za-z]{3}", value):
                    continue
                self.found.append(value.strip())

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.stack.pop()

    def handle_endtag(self, tag):
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()

    def handle_data(self, data):
        if self.stack and self.stack[-1] in SKIP_TAGS:
            return
        text = data.strip()
        if text and not NOISE.match(text):
            self.found.append(text)


def collect():
    per_page = {}
    order = []
    seen = set()
    for name in PAGES:
        path = os.path.join(HERE, name)
        if not os.path.exists(path):
            continue
        parser = Collector()
        parser.feed(io.open(path, encoding="utf-8").read())
        per_page[name] = parser.found
        for s in parser.found:
            if s not in seen:
                seen.add(s)
                order.append(s)
    return order, per_page


if __name__ == "__main__":
    strings, per_page = collect()
    io.open(os.path.join(HERE, "_harvest", "strings.json"), "w", encoding="utf-8").write(
        json.dumps(strings, ensure_ascii=False, indent=1))
    total_chars = sum(len(s) for s in strings)
    print("unique strings: %d  (%d chars)" % (len(strings), total_chars))
    for name in PAGES:
        if name in per_page:
            print("  %-20s %4d" % (name, len(per_page[name])))
    longest = sorted(strings, key=len, reverse=True)[:5]
    print("\nlongest:")
    for s in longest:
        print("  %d chars: %s..." % (len(s), s[:90]))
