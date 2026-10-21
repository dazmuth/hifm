/* Shared behaviour: header details, mobile menu, BACK buttons. No libraries. */
(function () {
  "use strict";
  var info = window.HIFM_INFO || {};

  // 1. Fill in issue details from site-info.js (the page already shows the same text without JavaScript)
  function setText(sel, text) {
    if (!text) return;
    var els = document.querySelectorAll(sel);
    for (var i = 0; i < els.length; i++) els[i].textContent = text;
  }
  setText("[data-info=issue]", info.issue ? "Issue " + info.issue : "");
  setText("[data-info=season]", info.season);
  setText("[data-info=catchphrase]", info.catchphrase);
  if (info.issue && info.season) setText("[data-info=issue-line]", "Issue " + info.issue + " · " + info.season);
  if (info.currentPdf) {
    var links = document.querySelectorAll("[data-info=pdf]");
    for (var j = 0; j < links.length; j++) links[j].setAttribute("href", encodeURI(info.currentPdf));
  }

  // 2. Mobile menu
  var b = document.querySelector(".nav-toggle"), l = document.getElementById("nav-links");
  if (b && l) {
    b.addEventListener("click", function () {
      var o = l.classList.toggle("open");
      b.setAttribute("aria-expanded", o ? "true" : "false");
    });
    l.addEventListener("click", function (e) {
      if (e.target.tagName === "A") { l.classList.remove("open"); b.setAttribute("aria-expanded", "false"); }
    });
  }

  // 3. BACK buttons: go back in the same window; if the visitor arrived directly, go to the home page
  var backs = document.querySelectorAll("[data-back]");
  for (var k = 0; k < backs.length; k++) {
    backs[k].addEventListener("click", function (e) {
      try {
        if (document.referrer && new URL(document.referrer).origin === location.origin && history.length > 1) {
          e.preventDefault();
          history.back();
        }
      } catch (err) { /* follow the normal link */ }
    });
  }
})();
