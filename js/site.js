(function () {
  'use strict';
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // entrance: heading, then text, then picture, staggered
  if (!reduce && 'IntersectionObserver' in window) {
    var sel = '.fblock h3,.fblock p,.ask-text h2,.ask-text p,.ask-card,.how-col h2,.ex-lead,.ex-sub,.call,.resp,.qa h2,.qa h3,.qa p,.cta-row,.cta-note';
    var els = document.querySelectorAll(sel);
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -6% 0px' });
    els.forEach(function (el) {
      var p = el.parentElement, i = 0, n = el;
      while ((n = n.previousElementSibling)) i++;
      el.style.setProperty('--d', Math.min(i, 4));
      el.classList.add('pre');
      io.observe(el);
    });
  }

  // features: the pinned screen follows the block being read
  var blocks = document.querySelectorAll('.fblock');
  var imgs = document.querySelectorAll('.fimg');
  if (blocks.length && 'IntersectionObserver' in window) {
    var fo = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var k = en.target.getAttribute('data-img');
        imgs.forEach(function (im) { im.classList.toggle('is-on', im.getAttribute('data-k') === k); });
      });
    }, { rootMargin: '-45% 0px -45% 0px' });
    blocks.forEach(function (b) { fo.observe(b); });
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

  // signature move: the wordmark settles as the first screen leaves
  var wm = document.getElementById('wordmark');
  if (wm && !reduce) {
    var ticking = false;
    var update = function () {
      var y = Math.min(window.scrollY / (window.innerHeight * 0.9), 1);
      wm.style.transform = 'scale(' + (1 - y * 0.06).toFixed(4) + ')';
      ticking = false;
    };
    window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
    update();
  }
})();
