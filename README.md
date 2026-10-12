# Hollywood International Filmmaker — demo site

A static site: plain HTML, one stylesheet, self-hosted fonts. No external scripts, fonts or CDNs.

## Preview
    cd <this folder>
    python3 -m http.server 8000      # then open http://localhost:8000

## Pages
- `index.html` — home (Issue 31 drives it), plus a "From the Archive" strip
- `archive.html` — grid of past issues by year
- `issue-31.html`, `issue-30.html` — one page per recent issue (stories grouped by section)
- `article-willis.html`, `article-stallone.html` — the article template, one current, one archived
- `issue-2018-winter.html`, `issue-2018-fall.html`, `issue-2017-fall.html` — back issues, each with the page-turning reader and a clickable contents list

## The magazine reader
- Replaces DearFlip. It uses the open-source StPageFlip library (MIT licence, a 44 KB file in `assets/js/`), plus a small script, `assets/js/reader.js`. No WordPress, no plugins, no outside services.
- Page images live in `issues/issue-XX/` (`p01.webp` is the front cover, the last page is the back cover, `cover.jpg` is the archive thumbnail).
- To add an issue from a PDF: `python3 tools/pdf_to_pages.py "Issue.pdf" issues/issue-13` (add `--split` for PDFs made of two-page spreads), then copy one of the `issue-20xx-*.html` pages and change the folder, page count and contents.
- The PDFs themselves are not needed on the site. Keep them in the repo's `assets/` folder as source files or move them elsewhere.

## What is placeholder
- **Wordmark** is live text, not the real logo. Swap in Todd's logo file in the `.brand` block.
- **Images** for Issues 30 and 31 are cropped from low-resolution PDFs. Final images should come from Todd's PNGs.
- **Article text** was transcribed from the printed pages and is not proofread.
- **Ad slots** are labeled boxes. The only real creative is the Diamond Sofa page ad. The "advertise" email is the masthead address; replace it.
- **Issue numbers** on the back issues follow the covers (Vol. 3, Issue 004, Issue 005), which differ from the numbers in the PDF file names.
- **Dead links** (`#about`, `#privacy`, social links, Issue 29) point at pages not built yet.
- `<meta name="robots" content="noindex">` is on every page. **Remove it at launch.**

## Hosting notes
Everything uses relative paths, so it works from any folder or host (GitHub Pages, Cloudflare, plain web server).
