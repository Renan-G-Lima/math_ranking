document.addEventListener('DOMContentLoaded', () => {
  const buttons = document.querySelectorAll('.lb-tab-btn');
  const panels  = document.querySelectorAll('.lb-panel');

  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      const target = btn.dataset.target;

      buttons.forEach(b => b.classList.toggle('active', b === btn));
      panels.forEach(p => p.classList.toggle('active', p.classList.contains(target)));
    });
  });
});
