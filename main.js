
document.addEventListener('DOMContentLoaded', ()=>{
  const btn = document.getElementById('load-more');
  if(!btn) return;
  btn.addEventListener('click', async ()=>{
    const page = btn.getAttribute('data-page') || '2';
    btn.disabled = true;
    try{
      const res = await fetch(`/api/load-more/?page=${page}`);
      const data = await res.json();
      const container = document.getElementById('posts');
      data.results.forEach(r=>{
        const art = document.createElement('article');
        art.className='post';
        art.innerHTML = `<h2>${r.title}</h2><p class="meta">By ${r.author} — ${r.timestamp}</p><div class="excerpt">${r.excerpt}...</div><a href="/blog/${r.id}/">Read More</a>`;
        container.appendChild(art);
      });
      if(data.has_next){
        btn.setAttribute('data-page', Number(page)+1);
        btn.disabled = false;
      } else {
        btn.style.display='none';
      }
    }catch(e){
      console.error(e);
      btn.disabled = false;
    }
  });
});
