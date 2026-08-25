#!/usr/bin/env python3
"""Re-encode the harvested media to sensible delivery sizes.

The files come straight off gc-elite.com's CDN, where they are served at upload
resolution and resized on the fly by Next's image optimizer. A static host does
no such thing, so a 4000px logo would ship as-is. This caps each class of image
at the largest size the layout can actually use and re-encodes it.

Idempotent: an image already at or below its cap is re-encoded only if that makes
it smaller, and never upscaled. Run it after any new asset is added.

    python scripts/optimize_images.py            # report only
    python scripts/optimize_images.py --apply    # rewrite the files
"""
from __future__ import annotations

import argparse
import io
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:  # pragma: no cover - depends on the machine
    print("Pillow is required: python -m pip install Pillow", file=sys.stderr)
    raise SystemExit(2)

ROOT = Path(__file__).resolve().parents[1]
IMG = ROOT / "assets" / "img"

# (directory, longest edge in px, JPEG/WebP quality)
# The hero is full-bleed; service tiles sit in a card column; logos are chips.
RULES = {
    "brand": (2000, 82),
    "services": (1100, 80),
    "brands": (420, 86),
}
RASTER = {".jpg", ".jpeg", ".png", ".webp", ".jfif"}


def optimise(path: Path, cap: int, quality: int, apply: bool):
    before = path.stat().st_size
    try:
        with Image.open(path) as im:
            im.load()
            fmt = (im.format or "").upper()
            w, h = im.size
            scale = min(1.0, cap / max(w, h))
            target = im
            if scale < 1.0:
                target = im.resize((max(1, round(w * scale)), max(1, round(h * scale))),
                                   Image.LANCZOS)

            buf = io.BytesIO()
            if fmt == "PNG":
                # Logos are flat art; palette-quantise when it is safe, else
                # keep RGBA and lean on max compression.
                out = target
                if out.mode not in ("RGBA", "LA", "P"):
                    out = out.convert("RGBA")
                out.save(buf, "PNG", optimize=True, compress_level=9)
            else:
                out = target.convert("RGB")
                out.save(buf, "JPEG", quality=quality, optimize=True, progressive=True)
            data = buf.getvalue()
    except Exception as exc:
        return None, before, before, "skipped (%s)" % exc

    after = len(data)
    if after >= before:
        return None, before, before, "already optimal"
    if apply:
        path.write_bytes(data)
    return (w, h), before, after, "resized" if scale < 1.0 else "re-encoded"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true", help="write the optimised files")
    args = ap.parse_args()

    total_before = total_after = 0
    changed = 0
    for folder, (cap, quality) in RULES.items():
        d = IMG / folder
        if not d.is_dir():
            continue
        for path in sorted(d.iterdir()):
            if path.suffix.lower() not in RASTER:
                continue
            size, before, after, note = optimise(path, cap, quality, args.apply)
            total_before += before
            total_after += after
            if after < before:
                changed += 1
                if before - after > 40_000:
                    print("  %-46s %7.0fKB -> %6.0fKB  %s"
                          % (path.relative_to(ROOT), before / 1024, after / 1024, note))

    saved = total_before - total_after
    print("\n%s: %d file(s), %.2fMB -> %.2fMB (saved %.2fMB)"
          % ("APPLIED" if args.apply else "DRY RUN", changed,
             total_before / 1024 / 1024, total_after / 1024 / 1024, saved / 1024 / 1024))
    if not args.apply and changed:
        print("Re-run with --apply to write these.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
