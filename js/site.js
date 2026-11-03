(function () {
  'use strict';
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // entrance: heading first, then text, then picture
  if (!reduce && 'IntersectionObserver' in window) {
    var sel = '.feat .hd,.fp p,.fm,.ask-text h2,.ask-text p,.ask-card,.how .hd,.ex,.qa > *,.cta-row,.cta-note';
    var els = document.querySelectorAll(sel);
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -5% 0px' });
    els.forEach(function (el) {
      var i = 0, n = el;
      while ((n = n.previousElementSibling)) i++;
      el.style.setProperty('--d', Math.min(i, 4));
      el.classList.add('pre');
      io.observe(el);
    });
  }

  // the real prompt
  var card = document.getElementById('askCard');
  if (card) {
    var out = document.getElementById('askOut');
    var reset = document.getElementById('askReset');
    card.addEventListener('click', function (ev) {
      var b = ev.target.closest('button[data-a]');
      if (!b || card.classList.contains('done')) return;
      var a = b.getAttribute('data-a');
      card.classList.add('done');
      out.textContent = a === 'ok' ? card.dataset.ok : a === 'always' ? card.dataset.always : card.dataset.no;
      out.classList.toggle('ok', a !== 'no');
      reset.hidden = false;
    });
    reset.addEventListener('click', function () {
      card.classList.remove('done');
      out.textContent = card.dataset.wait;
      out.classList.remove('ok');
      reset.hidden = true;
    });
  }

  // copy command
  document.querySelectorAll('.copy').forEach(function (btn) {
    var label = btn.textContent;
    btn.addEventListener('click', function () {
      var t = document.querySelector(btn.getAttribute('data-copy'));
      if (!t) return;
      var done = function () { btn.textContent = btn.getAttribute('data-done'); setTimeout(function () { btn.textContent = label; }, 1600); };
      if (navigator.clipboard) navigator.clipboard.writeText(t.textContent).then(done, done); else done();
    });
  });
})();
