document.documentElement.classList.add('js');
const search = document.querySelector('#guide-search');
if (search) {
  const cards = [...document.querySelectorAll('[data-search]')];
  search.addEventListener('input', () => {
    const query = search.value.trim().toLocaleLowerCase();
    const words = query.split(/\s+/).filter(Boolean);
    let count = 0;
    cards.forEach(card => {
      const match = words.every(word => (card.textContent + ' ' + card.dataset.search).toLocaleLowerCase().includes(word));
      card.hidden = !match;
      if (match) count++;
    });
    document.querySelector('#no-results').hidden = count !== 0;
    document.querySelector('#search-status').textContent = query ? `${count}件のガイドが見つかりました` : '';
  });
}
document.querySelectorAll('[data-copy]').forEach(button => {
  button.addEventListener('click', async () => {
    const text = button.parentElement.querySelector('code').textContent;
    try {
      await navigator.clipboard.writeText(text);
      button.textContent = 'コピーしました';
    } catch {
      button.textContent = '選択してコピーしてください';
      const selection = window.getSelection();
      const range = document.createRange();
      range.selectNodeContents(button.parentElement.querySelector('code'));
      selection.removeAllRanges(); selection.addRange(range);
    }
    setTimeout(() => { button.textContent = 'コピー'; }, 2500);
  });
});
if ('IntersectionObserver' in window) {
  const links = [...document.querySelectorAll('.toc a[href^="#"]')];
  const observer = new IntersectionObserver(entries => {
    for (const entry of entries) if (entry.isIntersecting) {
      links.forEach(link => link.classList.toggle('active', link.hash === `#${entry.target.id}`));
    }
  }, { rootMargin: '-90px 0px -65% 0px' });
  document.querySelectorAll('.article section[id]').forEach(section => observer.observe(section));
}
