/* Interviews carousel: one slide every 4 seconds.
   Pauses on hover, keyboard focus and touch; has a Pause button; stays still if the
   visitor's device asks for reduced motion. Works without JavaScript as a plain list. */
(function () {
  "use strict";
  var INTERVAL = 4000;
  document.querySelectorAll(".carousel").forEach(function (root) {
    var slides = Array.prototype.slice.call(root.querySelectorAll(".slide"));
    if (slides.length < 2) return;
    var ctl = root.querySelector(".carousel-ctl");
    var idx = 0, timer = null, userPaused = false, hover = false;
    var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (reduce) userPaused = true;

    var dots = [];
    slides.forEach(function (s, i) {
      var d = document.createElement("button");
      d.type = "button"; d.className = "dot";
      d.setAttribute("aria-label", "Show interview " + (i + 1) + " of " + slides.length);
      d.addEventListener("click", function () { show(i); restart(); });
      ctl.insertBefore(d, ctl.querySelector(".pause"));
      dots.push(d);
    });
    var pauseBtn = ctl.querySelector(".pause");

    function show(i) {
      idx = (i + slides.length) % slides.length;
      slides.forEach(function (s, n) {
        var on = n === idx;
        s.classList.toggle("is-active", on);
        s.setAttribute("aria-hidden", on ? "false" : "true");
        s.tabIndex = on ? 0 : -1;
        dots[n].setAttribute("aria-current", on ? "true" : "false");
      });
    }
    function stop() { if (timer) { clearInterval(timer); timer = null; } }
    function start() { stop(); if (!userPaused && !hover && !document.hidden) timer = setInterval(function () { show(idx + 1); }, INTERVAL); }
    function restart() { start(); }
    function label() { pauseBtn.textContent = userPaused ? "Play" : "Pause"; pauseBtn.setAttribute("aria-label", userPaused ? "Play the rotation" : "Pause the rotation"); }

    pauseBtn.addEventListener("click", function () { userPaused = !userPaused; label(); start(); });
    root.addEventListener("mouseenter", function () { hover = true; stop(); });
    root.addEventListener("mouseleave", function () { hover = false; start(); });
    root.addEventListener("focusin", function () { hover = true; stop(); });
    root.addEventListener("focusout", function () { hover = false; start(); });
    document.addEventListener("visibilitychange", start);

    // Swipe on touch screens
    var x0 = null;
    root.addEventListener("touchstart", function (e) { x0 = e.touches[0].clientX; hover = true; stop(); }, { passive: true });
    root.addEventListener("touchend", function (e) {
      if (x0 !== null) {
        var dx = e.changedTouches[0].clientX - x0;
        if (Math.abs(dx) > 40) show(idx + (dx < 0 ? 1 : -1));
      }
      x0 = null; hover = false; start();
    }, { passive: true });

    root.classList.add("is-ready");
    show(0); label(); start();
  });
})();
