/* Hollywood International Filmmaker — magazine reader
   Wraps the open-source StPageFlip library (MIT, self-hosted in this folder).
   Markup lives in each issue page: a .reader element with data attributes.
   No other scripts, fonts or services are loaded. */
(function () {
  "use strict";

  function init(root) {
    var stage = root.querySelector(".reader-stage");
    var book = root.querySelector(".reader-book");
    var status = root.querySelector(".reader-status");
    var btnPrev = root.querySelector("[data-act=prev]");
    var btnNext = root.querySelector("[data-act=next]");
    var btnFull = root.querySelector("[data-act=full]");
    if (!stage || !book || typeof St === "undefined") { root.classList.add("reader--off"); return; }

    var folder = root.getAttribute("data-folder");
    var count = parseInt(root.getAttribute("data-pages"), 10);
    var pw = parseInt(root.getAttribute("data-w"), 10);
    var ph = parseInt(root.getAttribute("data-h"), 10);
    var title = root.getAttribute("data-title") || "Magazine";

    // Build one page per image. First and last are the covers (hard pages).
    for (var i = 1; i <= count; i++) {
      var p = document.createElement("div");
      p.className = "page";
      if (i === 1 || i === count) p.setAttribute("data-density", "hard");
      var im = document.createElement("img");
      im.src = folder + "/p" + (i < 10 ? "0" : "") + i + ".webp";
      im.width = pw; im.height = ph;
      im.alt = i === 1 ? title + " — front cover" : (i === count ? title + " — back cover" : title + " — page " + i);
      im.decoding = "async";
      im.draggable = false;
      p.appendChild(im);
      book.appendChild(p);
    }

    var flip = new St.PageFlip(book, {
      width: pw, height: ph, size: "stretch",
      minWidth: 260, maxWidth: 900, minHeight: 360, maxHeight: 1300,
      showCover: true, maxShadowOpacity: 0.45, flippingTime: 700,
      mobileScrollSupport: true, usePortrait: true, autoSize: true
    });
    flip.loadFromHTML(book.querySelectorAll(".page"));

    // The library fits the book to the container's WIDTH only. Cap the width so
    // the book also fits the stage's HEIGHT (short windows, phones held sideways).
    var ratio = ph / pw, lastW = 0;
    function fit() {
      var W = stage.clientWidth, H = stage.clientHeight;
      if (!W || !H) return;
      var portrait = W < 520;                       // library switches to one page below 2 x minWidth
      var w = portrait ? Math.min(W, H / ratio) : Math.min(W, (H / ratio) * 2);
      if (!portrait && w < 520) w = 520;
      w = Math.floor(w);
      if (w === lastW) return;
      lastW = w;
      book.style.setProperty("width", w + "px", "important");
      if (flip.update) flip.update();
    }
    fit();
    window.addEventListener("resize", function () { setTimeout(fit, 60); });

    function label() {
      var idx = flip.getCurrentPageIndex();
      var portrait = flip.getOrientation && flip.getOrientation() === "portrait";
      var text;
      if (idx === 0) text = "Front cover";
      else if (idx >= count - 1) text = "Back cover";
      else if (portrait) text = "Page " + (idx + 1) + " of " + count;
      else {
        // With a cover, spreads are (2,3), (4,5)… in 1-based page numbers
        var a = idx + 1;
        if (a % 2 === 1) a -= 1;
        text = "Pages " + a + "–" + Math.min(a + 1, count) + " of " + count;
      }
      if (status) status.textContent = text;
      if (btnPrev) btnPrev.disabled = idx === 0;
      if (btnNext) btnNext.disabled = idx >= count - 1;
    }
    flip.on("flip", label);
    flip.on("changeOrientation", label);
    flip.on("init", label);
    label();

    if (btnPrev) btnPrev.addEventListener("click", function () { flip.flipPrev(); });
    if (btnNext) btnNext.addEventListener("click", function () { flip.flipNext(); });

    // Keyboard: arrows while the reader has focus
    stage.addEventListener("keydown", function (e) {
      if (e.key === "ArrowRight") { flip.flipNext(); e.preventDefault(); }
      else if (e.key === "ArrowLeft") { flip.flipPrev(); e.preventDefault(); }
      else if (e.key === "Home") { flip.turnToPage(0); label(); e.preventDefault(); }
      else if (e.key === "End") { flip.turnToPage(count - 1); label(); e.preventDefault(); }
    });

    // Fullscreen (falls back quietly if the browser has no support)
    if (btnFull) {
      var fsEl = root;
      var canFs = !!(fsEl.requestFullscreen || fsEl.webkitRequestFullscreen);
      if (!canFs) { btnFull.hidden = true; }
      btnFull.addEventListener("click", function () {
        var inFs = document.fullscreenElement || document.webkitFullscreenElement;
        if (inFs) { (document.exitFullscreen || document.webkitExitFullscreen).call(document); }
        else { (fsEl.requestFullscreen || fsEl.webkitRequestFullscreen).call(fsEl); }
      });
      document.addEventListener("fullscreenchange", function () {
        var on = !!document.fullscreenElement;
        root.classList.toggle("is-full", on);
        btnFull.textContent = on ? "Exit full screen" : "Full screen";
        setTimeout(fit, 100);
      });
    }

    // Contents links: <a href="#reader" data-goto="12"> jumps to page 12 (1-based)
    document.querySelectorAll("[data-goto]").forEach(function (a) {
      a.addEventListener("click", function (e) {
        var n = parseInt(a.getAttribute("data-goto"), 10);
        if (!n) return;
        e.preventDefault();
        root.scrollIntoView({ behavior: "smooth", block: "start" });
        setTimeout(function () { flip.flip(Math.max(0, Math.min(count - 1, n - 1))); }, 350);
        stage.focus({ preventScroll: true });
      });
    });

    root.classList.add("reader--ready");
  }

  function boot() {
    var list = document.querySelectorAll(".reader");
    for (var i = 0; i < list.length; i++) init(list[i]);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
