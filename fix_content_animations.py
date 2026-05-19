import os, glob, re
base = '/Users/user/Documents/Elite 4'

# 1. Unique content for each service card "Read More" subtitle
svc_cards = [
    ('Luxury Patios', 'View Patio & Fire Pit Specs', 'Natural stone, outdoor kitchens & fire features'),
    ('Retaining Walls', 'View Wall Engineering Details', 'Limestone structural grades & drainage systems'),
    ('Geometric Pools', 'View Pool Architecture Plans', 'Infinity edges, LED lighting & filtration specs'),
]

# 2. Unique blog post "Read More" links with distinct subtitles
blog_posts = [
    ('The Importance of Symmetry in Luxury Hardscapes', 'post-symmetry.html', 'Explore Symmetry Principles', '4 min read · Botanical geometry'),
    ('Choosing the right stone for limestone retaining walls', 'post-retaining-walls.html', 'Explore Stone Selection Guide', '5 min read · Material science'),
    ('The right way to build a geometric pool scape', 'portfolio.html', 'Explore Pool Engineering', '3 min read · Hydraulic design'),
    ('Prestige and precision in outdoor environments', 'about.html', 'Explore Precision Standards', '4 min read · Our methodology'),
]

# 3. Animated background CSS + scroll animation CSS
anim_css = '''
<style>
/* Floating Particle Background */
.elite-bg-canvas{position:fixed;top:0;left:0;width:100%;height:100%;z-index:-1;pointer-events:none;overflow:hidden}
.elite-particle{position:absolute;border-radius:50%;opacity:0;animation:eliteFloat linear infinite}
@keyframes eliteFloat{0%{opacity:0;transform:translateY(100vh) scale(0)}10%{opacity:.15}90%{opacity:.15}100%{opacity:0;transform:translateY(-10vh) scale(1)}}
/* Scroll Reveal Animations */
.scroll-reveal{opacity:0;transform:translateY(60px);transition:opacity 0.8s cubic-bezier(.22,1,.36,1),transform 0.8s cubic-bezier(.22,1,.36,1)}
.scroll-reveal.revealed{opacity:1;transform:translateY(0)}
.scroll-reveal-left{opacity:0;transform:translateX(-80px);transition:opacity 0.8s cubic-bezier(.22,1,.36,1),transform 0.8s cubic-bezier(.22,1,.36,1)}
.scroll-reveal-left.revealed{opacity:1;transform:translateX(0)}
.scroll-reveal-right{opacity:0;transform:translateX(80px);transition:opacity 0.8s cubic-bezier(.22,1,.36,1),transform 0.8s cubic-bezier(.22,1,.36,1)}
.scroll-reveal-right.revealed{opacity:1;transform:translateX(0)}
.scroll-reveal-scale{opacity:0;transform:scale(.85);transition:opacity 0.8s cubic-bezier(.22,1,.36,1),transform 0.8s cubic-bezier(.22,1,.36,1)}
.scroll-reveal-scale.revealed{opacity:1;transform:scale(1)}
/* Parallax float */
.parallax-float{transition:transform .15s ease-out}
/* Scroll progress bar */
#scroll-progress{position:fixed;top:0;left:0;height:3px;background:linear-gradient(90deg,#12a638,#0f4a23);z-index:9999;transition:width .1s linear;width:0}
/* Navbar shrink on scroll */
nav.scrolled{backdrop-filter:blur(16px);background:rgba(255,255,255,.92)!important;box-shadow:0 4px 30px rgba(0,0,0,.08)}
/* Counter animation */
.count-up{display:inline-block}
</style>
'''

# 4. Scroll animation + particle background JS
anim_js = '''
<script>
(function(){
  // Scroll progress bar
  const prog=document.getElementById('scroll-progress');
  // Scroll reveal observer
  const obs=new IntersectionObserver((entries)=>{
    entries.forEach(e=>{
      if(e.isIntersecting){e.target.classList.add('revealed');obs.unobserve(e.target)}
    });
  },{threshold:0.12,rootMargin:'0px 0px -40px 0px'});

  function initScrollEffects(){
    // Tag sections for reveal
    document.querySelectorAll('section,header,.grid>div,.bg-white.rounded-2xl,.bg-white.rounded-3xl,.bg-brand-dark.text-white.p-10').forEach((el,i)=>{
      if(!el.classList.contains('scroll-reveal')&&!el.classList.contains('scroll-reveal-left')&&!el.classList.contains('scroll-reveal-scale')){
        const classes=['scroll-reveal','scroll-reveal-left','scroll-reveal-right','scroll-reveal-scale'];
        el.classList.add(classes[i%classes.length]);
        el.style.transitionDelay=(i%4)*0.08+'s';
        obs.observe(el);
      }
    });
    // Parallax float on mouse
    document.querySelectorAll('.blob-shape,.blob-shape-2').forEach(el=>{
      el.classList.add('parallax-float');
    });
    document.addEventListener('mousemove',(e)=>{
      const cx=e.clientX/window.innerWidth-.5;
      const cy=e.clientY/window.innerHeight-.5;
      document.querySelectorAll('.parallax-float').forEach(el=>{
        el.style.transform=`translate(${cx*12}px,${cy*12}px)`;
      });
    });
    // Scroll progress
    window.addEventListener('scroll',()=>{
      if(prog){
        const h=document.documentElement.scrollHeight-window.innerHeight;
        prog.style.width=(window.scrollY/h*100)+'%';
      }
      // Navbar shrink
      const nav=document.querySelector('nav');
      if(nav){nav.classList.toggle('scrolled',window.scrollY>80)}
    });
    // Count-up animation for stat numbers
    document.querySelectorAll('.count-up').forEach(el=>{
      const target=parseInt(el.textContent);
      if(isNaN(target))return;
      const io=new IntersectionObserver(entries=>{
        if(entries[0].isIntersecting){
          let current=0;const step=Math.max(1,Math.floor(target/40));
          const timer=setInterval(()=>{current+=step;if(current>=target){current=target;clearInterval(timer)}el.textContent=current},30);
          io.unobserve(el);
        }
      },{threshold:.5});
      io.observe(el);
    });
  }

  // Particle background
  function initParticles(){
    const canvas=document.createElement('div');
    canvas.className='elite-bg-canvas';
    canvas.setAttribute('aria-hidden','true');
    document.body.prepend(canvas);
    const colors=['#12a638','#0f4a23','#e8f3ec','#a7f3d0'];
    for(let i=0;i<25;i++){
      const p=document.createElement('div');
      p.className='elite-particle';
      const size=Math.random()*6+2;
      p.style.cssText=`width:${size}px;height:${size}px;left:${Math.random()*100}%;background:${colors[i%colors.length]};animation-duration:${Math.random()*12+8}s;animation-delay:${Math.random()*10}s`;
      canvas.appendChild(p);
    }
  }

  if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',()=>{initScrollEffects();initParticles()})}
  else{initScrollEffects();initParticles()}
})();
</script>
'''

for fp in glob.glob(os.path.join(base, '*.html')):
    fn = os.path.basename(fp)
    with open(fp,'r',encoding='utf-8') as f: c = f.read()

    # Fix duplicate service card subtitles
    for title, cta_label, cta_sub in svc_cards:
        old = f'<h3 class="font-heading font-bold text-xl text-brand-dark mb-3">{title}</h3>'
        if old in c:
            # Find the next "Explore Capability Details" after this card title and make it unique
            pat = re.compile(
                re.escape(old) + r'(.*?)<span class="block text-sm font-bold">Explore Capability Details',
                re.DOTALL
            )
            replacement_cta = f'{old}\\1<span class="block text-sm font-bold">{cta_label}'
            c = pat.sub(replacement_cta, c, count=1)
            # Also fix the subtitle line
            old_sub = f'{cta_label} <i class="fas fa-arrow-right ml-1"></i></span><span class="block text-[9px] font-normal uppercase tracking-wider opacity-90 mt-0.5">View materials & structural specs</span>'
            new_sub = f'{cta_label} <i class="fas fa-arrow-right ml-1"></i></span><span class="block text-[9px] font-normal uppercase tracking-wider opacity-90 mt-0.5">{cta_sub}</span>'
            c = c.replace(old_sub, new_sub, 1)

    # Fix duplicate blog "Read More" links with unique content per post
    for title, href, cta_text, cta_sub in blog_posts:
        old_block = f'''<h3 class="font-heading font-bold text-lg text-brand-dark mb-4 leading-tight group-hover:text-brand-primary transition">{title}</h3>
                    <a href="journal.html" class="text-sm font-bold text-brand-dark hover:text-brand-primary flex items-center gap-2 transition">Read More <i class="fas fa-arrow-right"></i></a>'''
        new_block = f'''<h3 class="font-heading font-bold text-lg text-brand-dark mb-4 leading-tight group-hover:text-brand-primary transition">{title}</h3>
                    <a href="{href}" class="text-sm font-bold text-brand-dark hover:text-brand-primary flex items-center gap-2 transition group/cta">
                        <span class="group-hover/cta:translate-x-1 transition-transform">{cta_text} <i class="fas fa-arrow-right ml-1"></i></span>
                    </a>
                    <span class="block text-[9px] text-brand-gray uppercase tracking-wider mt-1">{cta_sub}</span>'''
        c = c.replace(old_block, new_block)

    # Inject scroll progress bar after <body> if not present
    if 'scroll-progress' not in c:
        c = c.replace('<body', '<div id="scroll-progress"></div>\n<body', 1)
        # Actually place it right after <body> tag
        c = c.replace('<div id="scroll-progress"></div>\n<body', '<body', 1)
        c = re.sub(r'(<body[^>]*>)', r'\1\n<div id="scroll-progress"></div>', c, count=1)

    # Inject animation CSS before </head>
    if 'scroll-reveal' not in c:
        c = c.replace('</head>', anim_css + '\n</head>')

    # Inject animation JS before </body> (only the first closing body tag)
    if 'initScrollEffects' not in c:
        c = c.replace('</body>', anim_js + '\n</body>', 1)

    with open(fp,'w',encoding='utf-8') as f: f.write(c)
    print(f"✅ {fn}: unique content, scroll animations & particle background applied")

print("\n🎉 All pages upgraded with unique CTA content, scroll animations & animated background!")
