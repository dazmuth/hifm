#!/usr/bin/env python3
"""Turn a magazine PDF into the page images the reader needs.

Usage:   python3 tools/pdf_to_pages.py "My Issue.pdf" issues/issue-12 [--split]

Needs:   poppler (pdftoppm) and Pillow  (brew install poppler && pip3 install pillow)
Output:  issues/issue-12/p01.webp, p02.webp ... and cover.jpg (archive thumbnail)

--split  Use when the PDF holds two-page spreads (each PDF page is a wide spread).
         Each spread is cut down the middle into a left and a right page. If every
         spread appears twice in a row (some exports do this), the repeat is skipped.
Page 1 must be the front cover and the last page the back cover.
"""
import subprocess, sys, os, glob, tempfile
from PIL import Image, ImageChops

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    split = "--split" in sys.argv
    if len(args) != 2: sys.exit(__doc__)
    pdf, out = args
    os.makedirs(out, exist_ok=True)
    tmp = tempfile.mkdtemp()
    subprocess.run(["pdftoppm", "-r", "110", "-png", pdf, f"{tmp}/p"], check=True)
    files = sorted(glob.glob(f"{tmp}/p-*.png"))
    pages = []
    if not split:
        pages = [Image.open(f).convert("RGB") for f in files]
    else:
        pages.append(Image.open(files[0]).convert("RGB"))                 # front cover
        inner, prev = files[1:-1], None
        for f in inner:
            im = Image.open(f).convert("RGB")
            if prev is not None and prev.size == im.size and ImageChops.difference(prev.convert("L"), im.convert("L")).getbbox() is None:
                continue                                                  # skip a repeated spread
            prev = im
            mid = im.width // 2
            pages += [im.crop((0, 0, mid, im.height)), im.crop((mid, 0, im.width, im.height))]
        pages.append(Image.open(files[-1]).convert("RGB"))                # back cover
    w = 820
    h = round(pages[0].height * w / pages[0].width)
    for i, im in enumerate(pages, 1):
        im.resize((w, h), Image.LANCZOS).save(f"{out}/p{i:02d}.webp", "WEBP", quality=70, method=6)
    cw = 520; ch = round(pages[0].height * cw / pages[0].width)
    pages[0].resize((cw, ch), Image.LANCZOS).save(f"{out}/cover.jpg", "JPEG", quality=82, optimize=True)
    print(f"{len(pages)} pages written to {out}" + ("  (odd page count: the reader expects an even number)" if len(pages) % 2 else ""))

if __name__ == "__main__":
    main()
