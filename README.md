# Hollywood International Filmmaker — demo site (v2)

Plain HTML, one stylesheet, three small scripts, self-hosted fonts. No outside scripts, fonts or services.

## Preview on your computer
    cd <this folder>
    python3 -m http.server 8000      # then open http://localhost:8000

## Pages
- `index.html` — home: Interviews carousel + right column, The Latest Issue, Back Cover (with the Diamond Sofa ad), From the Archive, Advertise with Us, footer
- `archive.html` — every issue; click a cover to open its PDF, or "Download PDF"
- `story-*.html` — eight story pages: willis, godfather, willsmith, taylor, farrell, rudd, curtis, backcover. Each has a BACK button at the top and bottom.

## Change each issue in one place: `assets/js/site-info.js`
Four lines: issue number, season/year, monthly catchphrase (under 20 words), and the PDF that "Read this Issue" opens.
(The same defaults are also written in the HTML, so the pages still work with JavaScript off.)

## Archive PDFs
Files live in `archive/` and are named `Issue 031.pdf` (3-digit issue number). To add an issue: drop the PDF in, add one line to the `ARCHIVE` list in `tools/build_v2.py` (or copy a card in `archive.html`), and add its cover to `assets/img/`.
- **Issue numbers 9, 11 and 12 are provisional** (taken from Todd's file names). Assign the real ones, then rename the files and update the list.
- Largest file today: 12.6 MB. Keep each under 20 MB (Cloudflare's limit is 25 MiB per file).

## Carousel
Rotates every 4 seconds, pauses on hover/focus/touch and with the Pause button, stays still if the visitor's device asks for reduced motion, and shows as a plain list with JavaScript off. The caption is the interviewee's name only.

## What is placeholder
- **Logo**: `assets/img/hi-logo.png` (the low-res file). Replace with the official logo when it arrives; navy/gold colors stay until then.
- **Images** are cropped from the PDFs you have (72 dpi), so they are soft. Final images should come from Todd's originals.
- **Ad slots**: the top leaderboard is a labeled box. Diamond Sofa is the only real ad. The advertising email is the masthead address; replace it.
- **Footer links** (About, Team, Submit a Story, social, Privacy, Terms, F.A.Q.) go nowhere yet. Issue 29 is a placeholder card.
- `<meta name="robots" content="noindex">` is on every page. **Remove it at launch.**

## Proofing notes (text was transcribed from the printed pages)
- Paul Rudd interview, question 4: the printed answer begins with two sentences pasted from the Farrell interview ("I did find myself being surprisingly reflective. It caught…"). Kept as printed; fix with Todd, in `tools/build_v2.py`.
- Printed spellings kept as they are: "Russel Crowe", "Guiness", "a little tricker". Jamie Lee Curtis's "head bitch in charge" quote is as printed.

## Parked
`_parked/` holds the page-turning magazine reader (StPageFlip, MIT) and the script that converted PDFs to page images. Not used by the site; kept in case it's wanted later.

## Hosting
Relative paths everywhere, so it works from any folder or host (GitHub Pages, Cloudflare Pages). GitHub Pages needs a `CNAME` file containing `hi.zylrxxy.site`.
