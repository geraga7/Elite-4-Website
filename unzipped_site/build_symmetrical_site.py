import os

# 1. Base Layout Template
layout = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="keywords" content="Minnesota luxury landscaping, premium hardscape construction, landscape design Minnesota, high-end outdoor living, Elite 4 landscaping, custom stone patios, retaining walls">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Epilogue:wght@700;800;900&amp;family=Manrope:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
<script>
    tailwind.config = {{
        theme: {{
            extend: {{
                colors: {{
                    "primary": "#366549",
                    "primary-fixed": "#c3f7d3",
                    "on-primary": "#ffffff",
                    "secondary": "#575d5a",
                    "tertiary": "#705900",
                    "surface": "#f6f6f5",
                    "surface-container-low": "#f0f1ef",
                    "surface-container-lowest": "#ffffff",
                    "on-surface": "#2d2f2e",
                }},
                fontFamily: {{
                    "display": ["Epilogue"],
                    "body": ["Manrope"]
                }}
            }}
        }}
    }}
</script>
<style>
    .material-symbols-outlined {{ font-variation-settings: 'FILL' 0, 'wght' 300, 'GRAD' 0, 'opsz' 32; }}
    /* Thicker hamburger lines */
    .hamburger-icon {{ font-variation-settings: 'FILL' 1, 'wght' 600, 'GRAD' 0, 'opsz' 48; font-size: 2.5rem; }}
</style>
</head>
<body class="bg-surface text-on-surface font-body overflow-x-hidden antialiased">

<!-- Top Navigation (Minimalist Hamburger) -->
<nav class="fixed top-0 w-full z-50 bg-surface/90 backdrop-blur-xl shadow-sm border-b border-primary/5">
<div class="flex justify-between items-center w-full px-8 md:px-16 py-6 max-w-[1920px] mx-auto">
    <a class="text-2xl font-black tracking-[-0.02em] text-primary uppercase font-display" href="index.html">The Elite 4</a>
    
    <!-- Desktop & Mobile Menu Button (3 Horizontal Lines) -->
    <div class="flex items-center gap-8">
        <a href="contact.html" class="hidden md:inline-block text-secondary font-display font-bold text-xs uppercase tracking-widest border-b-2 border-transparent hover:border-primary transition-colors">
            Start Project
        </a>
        <button id="main-menu-button" class="text-primary hover:text-tertiary transition-colors flex items-center justify-center p-2 rounded-full hover:bg-primary/5">
            <span class="material-symbols-outlined hamburger-icon">menu</span>
        </button>
    </div>
</div>

<!-- Full Screen Menu Overlay -->
<div id="full-menu" class="fixed inset-0 bg-surface z-[100] flex flex-col justify-center items-center gap-10 hidden opacity-0 transition-opacity duration-500">
    <button id="close-menu-button" class="absolute top-8 right-8 md:right-16 text-primary p-4 hover:rotate-90 transition-transform duration-300">
        <span class="material-symbols-outlined hamburger-icon">close</span>
    </button>
    <a class="font-display text-4xl md:text-5xl font-black uppercase tracking-tight text-secondary hover:text-primary hover:scale-105 transition-all" href="index.html">Home</a>
    <a class="font-display text-4xl md:text-5xl font-black uppercase tracking-tight text-secondary hover:text-primary hover:scale-105 transition-all" href="about.html">About Us</a>
    <a class="font-display text-4xl md:text-5xl font-black uppercase tracking-tight text-secondary hover:text-primary hover:scale-105 transition-all" href="services.html">Services</a>
    <a class="font-display text-4xl md:text-5xl font-black uppercase tracking-tight text-secondary hover:text-primary hover:scale-105 transition-all" href="portfolio.html">Portfolio</a>
    <a class="font-display text-4xl md:text-5xl font-black uppercase tracking-tight text-secondary hover:text-primary hover:scale-105 transition-all" href="process.html">Process</a>
    <a class="font-display text-4xl md:text-5xl font-black uppercase tracking-tight text-secondary hover:text-primary hover:scale-105 transition-all" href="journal.html">Journal</a>
    
    <a href="contact.html" class="mt-12 bg-primary text-on-primary px-12 py-5 rounded-sm font-display font-bold text-sm uppercase tracking-widest shadow-xl hover:bg-tertiary hover:-translate-y-2 transition-all text-center">
        Request Consultation
    </a>
</div>
</nav>

<!-- Main Content -->
<main class="w-full pt-28">
{content}
</main>

<!-- Footer -->
<footer class="w-full bg-surface-container-low mt-20 py-24 border-t border-secondary/10">
<div class="max-w-7xl mx-auto px-8 grid grid-cols-1 md:grid-cols-4 gap-12 mb-16 text-center md:text-left">
    <div class="md:col-span-2" data-aos="fade-up">
        <p class="text-3xl font-black font-display text-primary uppercase tracking-tight mb-6">The Elite 4</p>
        <p class="font-body text-sm text-secondary leading-loose max-w-sm mx-auto md:mx-0">
            Minnesota's premier luxury landscape architecture firm. We specialize in high-end hardscape construction, retaining walls, and custom outdoor living transformations. Precision execution guaranteed.
        </p>
    </div>
    <div data-aos="fade-up" data-aos-delay="100">
        <p class="font-body text-xs tracking-[0.2em] uppercase text-tertiary font-black mb-8">Service Areas</p>
        <div class="flex flex-col gap-4 text-secondary text-sm font-bold">
            <span class="hover:text-primary cursor-default">Minneapolis</span>
            <span class="hover:text-primary cursor-default">Saint Paul</span>
            <span class="hover:text-primary cursor-default">Edina</span>
            <span class="hover:text-primary cursor-default">Wayzata</span>
        </div>
    </div>
    <div data-aos="fade-up" data-aos-delay="200">
        <p class="font-body text-xs tracking-[0.2em] uppercase text-tertiary font-black mb-8">Navigation</p>
        <div class="flex flex-col gap-4">
            <a href="contact.html" class="text-sm font-bold text-secondary hover:text-primary transition-colors uppercase tracking-widest">Contact Us</a>
            <a href="faq.html" class="text-sm font-bold text-secondary hover:text-primary transition-colors uppercase tracking-widest">FAQ</a>
            <a href="testimonials.html" class="text-sm font-bold text-secondary hover:text-primary transition-colors uppercase tracking-widest">Testimonials</a>
        </div>
    </div>
</div>
<div class="max-w-7xl mx-auto px-8 text-center border-t border-secondary/10 pt-12">
    <p class="font-body text-xs text-secondary/60 tracking-[0.2em] uppercase font-bold">© 2026 The Elite 4. Premium Landscape Design & Hardscape Construction.</p>
</div>
</footer>

<script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
<script>
    document.addEventListener('DOMContentLoaded', () => {{
        AOS.init({{ duration: 800, once: true, offset: 50 }});
        
        const menuBtn = document.getElementById('main-menu-button');
        const closeBtn = document.getElementById('close-menu-button');
        const fullMenu = document.getElementById('full-menu');

        if(menuBtn && closeBtn && fullMenu) {{
            menuBtn.addEventListener('click', () => {{
                fullMenu.classList.remove('hidden');
                setTimeout(() => fullMenu.classList.remove('opacity-0'), 10);
                document.body.style.overflow = 'hidden';
            }});

            closeBtn.addEventListener('click', () => {{
                fullMenu.classList.add('opacity-0');
                setTimeout(() => fullMenu.classList.add('hidden'), 500);
                document.body.style.overflow = '';
            }});
        }}
    }});
</script>
</body>
</html>"""

def create_hero(subtitle, title, text, image, cta1="View Portfolio", link1="portfolio.html", cta2="Our Process", link2="process.html"):
    return f"""
    <header class="relative min-h-[85vh] flex flex-col md:flex-row mx-4 md:mx-8 mt-4 rounded-3xl overflow-hidden shadow-2xl">
        <div class="w-full md:w-1/2 flex flex-col justify-center px-10 md:px-24 py-24 bg-surface-container-lowest z-10" data-aos="fade-right">
            <div class="max-w-xl mx-auto md:mx-0">
                <span class="font-body text-xs uppercase tracking-[0.2em] text-tertiary font-black mb-6 block">{subtitle}</span>
                <h1 class="font-display text-5xl md:text-7xl font-extrabold text-on-surface leading-[1.05] tracking-tighter mb-10">
                    {title}
                </h1>
                <p class="text-lg text-secondary leading-loose mb-12 font-medium">{text}</p>
                <div class="flex flex-wrap gap-6">
                    <a href="{link1}" class="inline-block bg-primary text-on-primary px-10 py-5 rounded-sm font-display font-black text-xs uppercase tracking-widest hover:bg-tertiary hover:-translate-y-1 transition-all shadow-xl">{cta1}</a>
                    <a href="{link2}" class="inline-block text-primary border-b-2 border-primary/20 hover:border-primary px-2 py-4 font-display font-black text-xs uppercase tracking-widest transition-colors">{cta2}</a>
                </div>
            </div>
        </div>
        <div class="w-full md:w-1/2 relative min-h-[50vh] md:min-h-full bg-black" data-aos="fade-left">
            <img src="{image}" alt="Minnesota Luxury Landscaping and Premium Hardscapes" loading="eager" class="absolute inset-0 w-full h-full object-cover opacity-90 mix-blend-lighten">
        </div>
    </header>
    """

# Extensive SEO Text Content Additions
pages = {}

pages["index.html"] = {
    "title": "The Elite 4 | Premium MN Landscape Design & Luxury Hardscapes",
    "description": "Minnesota's premier landscape architecture and hardscape construction firm. We build custom stone patios, retaining walls, and high-end outdoor living spaces.",
    "content": create_hero("Symmetry in Nature", "Premium Hardscape Construction in <span class='text-primary italic block'>Minnesota.</span>", "Welcome to The Elite 4, the top-rated landscape design and luxury hardscape construction team in Minnesota. We transform residential estates into immaculate, high-value outdoor living sanctuaries using world-class materials and elite architectural execution.", "./hero-pathway.jpg") + 
    """
    <section class="py-32 bg-surface text-center px-8">
        <div class="max-w-4xl mx-auto" data-aos="fade-up">
            <h2 class="font-display text-4xl md:text-5xl font-black mb-10 text-on-surface tracking-tight">The 48-Hour Elite Transformation</h2>
            <p class="text-secondary text-lg leading-loose font-medium">As Minnesota's most exclusive landscaping strike-force, we specialize in high-end, rapid-deployment hardscape installations. Unlike traditional landscaping companies that tear up your yard for weeks, our elite team of craftsmen deploys on Friday evening and completes massive structural retaining walls, custom natural stone patios, and complete outdoor living environments by Monday morning. Perfect symmetry, absolute precision, and zero disruption to your daily life.</p>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-10 mt-24 max-w-7xl mx-auto text-left">
            <div class="bg-surface-container-lowest p-12 rounded-2xl shadow-sm hover:shadow-2xl hover:-translate-y-2 transition-all border border-secondary/5" data-aos="fade-up" data-aos-delay="0">
                <span class="material-symbols-outlined text-6xl text-primary mb-8 block">diamond</span>
                <h3 class="font-display text-2xl font-black mb-6">Tier-1 Luxury Materials</h3>
                <p class="text-secondary leading-loose">We do not compromise. We construct your hardscapes using only the finest premium limestone, imported granite, and high-density architectural concrete available in Minnesota. The result is an heirloom-quality outdoor estate that vastly increases your property value.</p>
            </div>
            <div class="bg-surface-container-lowest p-12 rounded-2xl shadow-sm hover:shadow-2xl hover:-translate-y-2 transition-all border border-secondary/5" data-aos="fade-up" data-aos-delay="100">
                <span class="material-symbols-outlined text-6xl text-primary mb-8 block">speed</span>
                <h3 class="font-display text-2xl font-black mb-6">Rapid Hardscape Strike</h3>
                <p class="text-secondary leading-loose">Time is your most valuable asset. Our weekend-only hardscaping methodology guarantees that your massive landscaping project is finalized within 48 hours. Regain access to your private sanctuary immediately, built to perfection.</p>
            </div>
            <div class="bg-surface-container-lowest p-12 rounded-2xl shadow-sm hover:shadow-2xl hover:-translate-y-2 transition-all border border-secondary/5" data-aos="fade-up" data-aos-delay="200">
                <span class="material-symbols-outlined text-6xl text-primary mb-8 block">architecture</span>
                <h3 class="font-display text-2xl font-black mb-6">Symmetric Design Masters</h3>
                <p class="text-secondary leading-loose">True luxury is found in symmetry and geometric balance. Every custom stone patio, fire pit, and geometric poolscape we design is drafted with strict mathematical precision to ensure aesthetic superiority.</p>
            </div>
        </div>
    </section>
    """
}

pages["about.html"] = {
    "title": "About Us | The Elite 4 Landscaping Founders",
    "description": "Meet the Elite 4, Minnesota's expert hardscape craftsmen and landscape design architects.",
    "content": create_hero("The Strike Force", "Four Craftsmen. One <span class='text-primary italic block'>Symphony.</span>", "The Elite 4 was founded by four of Minnesota's most experienced and highly sought-after landscape architecture professionals. We recognized a massive gap in the luxury landscaping market: high-net-worth homeowners wanted premium outdoor living spaces, but despised the weeks of mud, noise, and contractors loitering on their estates.", "./landscape_team.png", "Our Process", "process.html", "Contact Us", "contact.html") + 
    """
    <section class="py-32 bg-surface-container-lowest text-center px-8">
        <div class="max-w-4xl mx-auto" data-aos="fade-up">
            <h2 class="font-display text-4xl md:text-5xl font-black mb-10 text-on-surface tracking-tight">Precision, Integrity, and Grit</h2>
            <p class="text-secondary text-lg leading-loose font-medium mb-8">We are not a mass-market lawn care company. We are a specialized, four-man crew of master hardscape craftsmen. When you hire The Elite 4, you are hiring the owners of the company to physically build your luxury landscape. We operate as a high-precision military unit, focusing exclusively on one single masterpiece at a time.</p>
            <p class="text-secondary text-lg leading-loose font-medium">By limiting our clientele to select residential estates in Minneapolis, Edina, Wayzata, and Minnetonka, we ensure that every retaining wall, natural stone pathway, and premium fire feature is built with obsessive attention to detail. This is the epitome of high-end landscape design.</p>
        </div>
    </section>
    """
}

pages["services.html"] = {
    "title": "Services | Premium Hardscape Construction Minnesota",
    "description": "We specialize in high-end hardscaping, retaining walls, luxury patios, custom outdoor living environments, and geometric poolscapes in MN.",
    "content": create_hero("Our Capabilities", "Symmetric Hardscape <span class='text-primary italic block'>Mastery.</span>", "We provide comprehensive, high-end landscape architecture and hardscape construction services. Whether you need a massive structural retaining wall engineered for safety, or a breathtaking luxury patio for entertaining, The Elite 4 delivers unmatched quality.", "./modern_pool.png", "View Portfolio", "portfolio.html", "Consultation", "contact.html") + 
    """
    <section class="py-32 bg-surface px-8">
        <div class="max-w-7xl mx-auto space-y-32">
            <!-- Service 1 -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-16 items-center">
                <div data-aos="fade-right" class="order-2 md:order-1">
                    <h2 class="font-display text-4xl font-black mb-8 text-on-surface">Luxury Patio & Outdoor Living Construction</h2>
                    <p class="text-secondary text-lg leading-loose mb-8">Expand your estate's livable square footage with our custom outdoor living spaces. We design and construct premium natural stone patios, modern geometric fire pits, and fully integrated outdoor kitchens. Our patio builders use severe-weather rated materials to ensure your investment easily survives the harshest Minnesota winters without cracking or shifting.</p>
                    <ul class="space-y-4 mb-10 text-secondary font-bold">
                        <li class="flex items-center gap-3"><span class="material-symbols-outlined text-primary">check_circle</span> Premium Bluestone & Travertine Patios</li>
                        <li class="flex items-center gap-3"><span class="material-symbols-outlined text-primary">check_circle</span> Custom Stone Fire Pits & Seating Walls</li>
                        <li class="flex items-center gap-3"><span class="material-symbols-outlined text-primary">check_circle</span> Outdoor Kitchen & Bar Installations</li>
                    </ul>
                    <a href="contact.html" class="inline-block bg-primary text-on-primary px-10 py-5 rounded-sm font-display font-black text-xs uppercase tracking-widest shadow-xl">Get a Quote</a>
                </div>
                <div data-aos="fade-left" class="order-1 md:order-2">
                    <img src="./luxury_patio.png" alt="Luxury Patio Construction Minnesota" loading="lazy" class="w-full h-[600px] object-cover rounded-3xl shadow-2xl">
                </div>
            </div>
            
            <!-- Service 2 -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-16 items-center">
                <div data-aos="fade-right">
                    <img src="./retaining_wall.png" alt="Retaining Wall Construction Minnesota" loading="lazy" class="w-full h-[600px] object-cover rounded-3xl shadow-2xl">
                </div>
                <div data-aos="fade-left">
                    <h2 class="font-display text-4xl font-black mb-8 text-on-surface">Structural Retaining Walls & Grading</h2>
                    <p class="text-secondary text-lg leading-loose mb-8">Erosion control and property levelling are critical for Minnesota homeowners. Our expert landscape engineers design and construct massive, geometrically perfect retaining walls using heavy-duty limestone boulders and premium segmental blocks. We don't just build walls; we engineer permanent structural solutions that enhance your property's aesthetic and symmetry.</p>
                    <ul class="space-y-4 mb-10 text-secondary font-bold">
                        <li class="flex items-center gap-3"><span class="material-symbols-outlined text-primary">check_circle</span> Natural Limestone Boulder Walls</li>
                        <li class="flex items-center gap-3"><span class="material-symbols-outlined text-primary">check_circle</span> Engineered Segmental Block Retaining Walls</li>
                        <li class="flex items-center gap-3"><span class="material-symbols-outlined text-primary">check_circle</span> Comprehensive Grading & Drainage Solutions</li>
                    </ul>
                    <a href="contact.html" class="inline-block bg-primary text-on-primary px-10 py-5 rounded-sm font-display font-black text-xs uppercase tracking-widest shadow-xl">Secure Your Property</a>
                </div>
            </div>
        </div>
    </section>
    """
}

pages["portfolio.html"] = {
    "title": "Portfolio | Minnesota Luxury Landscape Gallery",
    "description": "View our extensive portfolio of luxury Minnesota landscapes, custom stone patios, high-end retaining walls, and geometric poolscapes.",
    "content": create_hero("The Gallery", "Curated Outdoor <span class='text-primary italic block'>Sanctuaries.</span>", "Explore a curated gallery of our finest weekend hardscape transformations. From sprawling Minneapolis estates to private lakeside retreats in Wayzata, The Elite 4 has established the benchmark for high-end landscape construction.", "./luxury_patio.png", "Start Yours", "contact.html", "Our Process", "process.html") + 
    """
    <section class="py-32 bg-surface-container-lowest px-8">
        <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-10">
            <div class="group relative overflow-hidden rounded-3xl shadow-xl" data-aos="fade-up">
                <img src="./retaining_wall.png" alt="Limestone Retaining Wall Hardscape Project" loading="lazy" class="w-full h-[600px] object-cover group-hover:scale-110 group-hover:rotate-1 transition-all duration-1000">
                <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/20 to-transparent flex flex-col justify-end p-12 opacity-90 group-hover:opacity-100 transition-opacity duration-300">
                    <span class="text-tertiary font-display font-black text-xs uppercase tracking-[0.2em] mb-3 block">Edina, MN</span>
                    <h3 class="font-display text-white text-3xl font-black mb-4">Geometric Limestone Retaining Wall</h3>
                    <p class="text-white/80 leading-relaxed max-w-md">A towering, precision-cut limestone retaining wall constructed to tame a steep hillside and create a flat, usable luxury backyard.</p>
                </div>
            </div>
            <div class="group relative overflow-hidden rounded-3xl shadow-xl" data-aos="fade-up" data-aos-delay="150">
                <img src="./modern_pool.png" alt="Modern Poolscape and Landscape Design Project" loading="lazy" class="w-full h-[600px] object-cover group-hover:scale-110 group-hover:-rotate-1 transition-all duration-1000">
                <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/20 to-transparent flex flex-col justify-end p-12 opacity-90 group-hover:opacity-100 transition-opacity duration-300">
                    <span class="text-tertiary font-display font-black text-xs uppercase tracking-[0.2em] mb-3 block">Wayzata, MN</span>
                    <h3 class="font-display text-white text-3xl font-black mb-4">Modern Poolscape Oasis</h3>
                    <p class="text-white/80 leading-relaxed max-w-md">Seamless integration of natural stone hardscaping surrounding a luxury geometric pool, complete with minimalist plantings.</p>
                </div>
            </div>
            <div class="group relative overflow-hidden rounded-3xl shadow-xl md:col-span-2" data-aos="fade-up">
                <img src="./landscape_team.png" alt="Landscape construction team building a patio" loading="lazy" class="w-full h-[700px] object-cover group-hover:scale-105 transition-all duration-1000">
                <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/20 to-transparent flex flex-col justify-end p-16 opacity-90 group-hover:opacity-100 transition-opacity duration-300">
                    <span class="text-tertiary font-display font-black text-xs uppercase tracking-[0.2em] mb-3 block">Minneapolis, MN</span>
                    <h3 class="font-display text-white text-4xl font-black mb-4">The 48-Hour Estate Overhaul</h3>
                    <p class="text-white/80 leading-relaxed max-w-2xl text-lg">Our elite strike-force executing a massive paver patio, fire pit, and seating wall installation over a single weekend. Absolute precision in motion.</p>
                </div>
            </div>
        </div>
    </section>
    """
}

pages["process.html"] = {
    "title": "Our Process | The 48-Hour Hardscape Transformation",
    "description": "Learn about our unique 48-hour luxury hardscape installation process. We build premium retaining walls and patios over a single weekend.",
    "content": create_hero("The 48-Hour Strike", "We Build While <span class='text-primary italic block'>You Rest.</span>", "Traditional landscaping companies are notoriously slow, leaving your property looking like a construction zone for weeks. The Elite 4 has revolutionized the industry with our signature 48-Hour Hardscape Strike.", "./landscape_team.png", "Contact Us", "contact.html", "Read Journal", "journal.html") + 
    """
    <section class="py-32 bg-surface text-center px-8">
        <div class="max-w-5xl mx-auto" data-aos="fade-up">
            <h2 class="font-display text-4xl md:text-5xl font-black mb-10 text-on-surface tracking-tight">The Anatomy of an Elite Deployment</h2>
            <p class="text-secondary text-lg leading-loose font-medium mb-16">Our process is highly orchestrated. Long before we step foot on your property, every stone is pre-measured, every cubic yard of base material is scheduled, and every plant is pre-selected. When Friday arrives, we execute with military precision.</p>
            
            <div class="space-y-8 text-left">
                <div class="bg-surface-container-lowest p-10 rounded-2xl shadow-md border-l-8 border-primary flex flex-col md:flex-row gap-8 items-center" data-aos="fade-up">
                    <div class="text-6xl font-black text-tertiary/20 font-display min-w-[80px]">01</div>
                    <div>
                        <h3 class="font-display text-2xl font-black mb-4 text-primary">The Architectural Consultation (Weeks Prior)</h3>
                        <p class="text-secondary leading-loose">We meet at your estate to discuss your vision. We draft fully symmetrical, 3D luxury landscape designs ensuring exact aesthetic alignment with your home's architecture.</p>
                    </div>
                </div>
                <div class="bg-surface-container-lowest p-10 rounded-2xl shadow-md border-l-8 border-primary flex flex-col md:flex-row gap-8 items-center" data-aos="fade-up">
                    <div class="text-6xl font-black text-tertiary/20 font-display min-w-[80px]">02</div>
                    <div>
                        <h3 class="font-display text-2xl font-black mb-4 text-primary">Friday 5 PM: Site Prep & Excavation</h3>
                        <p class="text-secondary leading-loose">The Elite 4 arrives with heavy machinery. We immediately excavate the site, lay down heavy-duty geotextile fabric, and compact the commercial-grade base rock. By nightfall, the foundation is set.</p>
                    </div>
                </div>
                <div class="bg-surface-container-lowest p-10 rounded-2xl shadow-md border-l-8 border-primary flex flex-col md:flex-row gap-8 items-center" data-aos="fade-up">
                    <div class="text-6xl font-black text-tertiary/20 font-display min-w-[80px]">03</div>
                    <div>
                        <h3 class="font-display text-2xl font-black mb-4 text-primary">Saturday: Structural Construction</h3>
                        <p class="text-secondary leading-loose">The core of the hardscape is built. Retaining walls are stacked, massive stone patios are laid with hairline precision, and outdoor kitchens are framed. Our craftsmanship shines.</p>
                    </div>
                </div>
                <div class="bg-surface-container-lowest p-10 rounded-2xl shadow-md border-l-8 border-primary flex flex-col md:flex-row gap-8 items-center" data-aos="fade-up">
                    <div class="text-6xl font-black text-tertiary/20 font-display min-w-[80px]">04</div>
                    <div>
                        <h3 class="font-display text-2xl font-black mb-4 text-primary">Sunday Sunset: The Reveal</h3>
                        <p class="text-secondary leading-loose">Final polymeric sand is applied, high-end landscape lighting is wired, and premium plantings are installed. We clean the site flawlessly. By Sunday sunset, your luxury sanctuary is complete.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
    """
}

pages["journal.html"] = {
    "title": "The Elite Journal | Landscape Design Insights",
    "description": "Read our field reports and deep dives into luxury landscape architecture, hardscape materials, and retaining wall engineering.",
    "content": create_hero("Field Reports", "Landscaping <span class='text-primary italic block'>Insights.</span>", "Stay informed with the latest developments in luxury landscape architecture. The Elite 4 shares our expertise on hardscape construction, material selection, and high-end outdoor living trends.", "./hero-pathway.jpg", "Subscribe", "contact.html", "View Portfolio", "portfolio.html") + 
    """
    <section class="py-32 bg-surface px-8">
        <div class="max-w-5xl mx-auto grid grid-cols-1 gap-16">
            <article class="bg-surface-container-lowest p-12 rounded-3xl shadow-xl border-t-4 border-tertiary" data-aos="fade-up">
                <span class="font-body text-xs uppercase tracking-widest text-primary font-black mb-4 block">Design Theory • March 2026</span>
                <h3 class="font-display text-4xl font-black mb-6 text-on-surface">The Importance of Symmetry in Luxury Hardscapes</h3>
                <p class="text-secondary text-lg leading-loose mb-8">Why does true luxury rely on geometric precision? In this field report, we explore how mathematical balance and strict symmetry elevate a standard backyard into an elite architectural estate. From perfectly aligned bluestone pavers to mirrored retaining wall curves, the human eye inherently appreciates structured, clean design...</p>
                <a href="contact.html" class="inline-flex items-center gap-2 font-display text-sm font-black text-tertiary uppercase tracking-widest hover:translate-x-2 transition-transform">Read Full Report <span class="material-symbols-outlined">arrow_right_alt</span></a>
            </article>
            <article class="bg-surface-container-lowest p-12 rounded-3xl shadow-xl border-t-4 border-tertiary" data-aos="fade-up">
                <span class="font-body text-xs uppercase tracking-widest text-primary font-black mb-4 block">Material Science • February 2026</span>
                <h3 class="font-display text-4xl font-black mb-6 text-on-surface">Limestone vs. Granite: Choosing the Perfect Retaining Wall</h3>
                <p class="text-secondary text-lg leading-loose mb-8">When engineering a massive structural retaining wall for a steep Minnesota property, material choice dictates both aesthetic value and longevity. We break down the tensile strength, weathering characteristics, and visual impact of premium limestone boulders versus engineered granite blocks...</p>
                <a href="contact.html" class="inline-flex items-center gap-2 font-display text-sm font-black text-tertiary uppercase tracking-widest hover:translate-x-2 transition-transform">Read Full Report <span class="material-symbols-outlined">arrow_right_alt</span></a>
            </article>
        </div>
    </section>
    """
}

pages["contact.html"] = {
    "title": "Contact | Hire The Elite 4 Landscapers",
    "description": "Request a consultation for premium landscape design and luxury hardscape construction in Minnesota.",
    "content": """
    <header class="pt-48 pb-32 bg-surface">
        <div class="max-w-7xl mx-auto px-8 grid grid-cols-1 lg:grid-cols-2 gap-20 items-center">
            <div data-aos="fade-right">
                <span class="font-body text-xs uppercase tracking-[0.2em] text-tertiary font-black mb-6 block">Commission Our Strike-Force</span>
                <h1 class="font-display text-5xl md:text-7xl font-extrabold text-on-surface leading-[1.05] tracking-tighter mb-10">
                    Start Your <span class="text-primary italic block">Transformation.</span>
                </h1>
                <p class="text-lg text-secondary leading-loose mb-12 font-medium">We specialize in luxury weekend execution for discerning homeowners in Minnesota. Fill out the brief below, and an Elite 4 architect will reach out within 24 hours to schedule your private, on-site consultation and hardscape assessment.</p>
                
                <div class="flex items-center gap-6 mb-8 bg-surface-container-lowest p-6 rounded-2xl shadow-sm border border-secondary/10">
                    <div class="bg-primary/10 p-4 rounded-full text-primary">
                        <span class="material-symbols-outlined text-3xl">call</span>
                    </div>
                    <div>
                        <p class="font-display font-black text-xs uppercase tracking-widest text-secondary mb-1">Direct Line</p>
                        <p class="font-display text-2xl font-bold text-on-surface">(612) 555-ELITE</p>
                    </div>
                </div>
            </div>
            
            <div class="bg-surface-container-lowest p-12 rounded-3xl shadow-2xl border-t-8 border-primary" data-aos="fade-left">
                <h3 class="font-display text-3xl font-black mb-8">Project Inquiry</h3>
                <form action="#" method="POST" class="space-y-8">
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                        <div>
                            <label class="block font-body text-xs uppercase tracking-[0.2em] text-secondary font-black mb-3">First Name</label>
                            <input type="text" class="w-full bg-surface border-2 border-surface-container-high px-5 py-4 rounded-lg focus:outline-none focus:border-primary transition-colors font-medium">
                        </div>
                        <div>
                            <label class="block font-body text-xs uppercase tracking-[0.2em] text-secondary font-black mb-3">Last Name</label>
                            <input type="text" class="w-full bg-surface border-2 border-surface-container-high px-5 py-4 rounded-lg focus:outline-none focus:border-primary transition-colors font-medium">
                        </div>
                    </div>
                    <div>
                        <label class="block font-body text-xs uppercase tracking-[0.2em] text-secondary font-black mb-3">Email Address</label>
                        <input type="email" class="w-full bg-surface border-2 border-surface-container-high px-5 py-4 rounded-lg focus:outline-none focus:border-primary transition-colors font-medium">
                    </div>
                    <div>
                        <label class="block font-body text-xs uppercase tracking-[0.2em] text-secondary font-black mb-3">Project Scope (Landscaping / Hardscaping)</label>
                        <select class="w-full bg-surface border-2 border-surface-container-high px-5 py-4 rounded-lg focus:outline-none focus:border-primary transition-colors font-medium text-secondary">
                            <option>Luxury Stone Patio</option>
                            <option>Structural Retaining Wall</option>
                            <option>Complete Outdoor Living Overhaul</option>
                            <option>Geometric Poolscape Design</option>
                        </select>
                    </div>
                    <a href="index.html" class="block w-full text-center bg-primary text-on-primary px-10 py-6 rounded-lg font-display font-black text-sm uppercase tracking-widest hover:bg-tertiary transition-colors shadow-xl shadow-primary/20 mt-4">Submit Executive Inquiry</a>
                </form>
            </div>
        </div>
    </header>
    """
}

pages["faq.html"] = {
    "title": "FAQ | Minnesota Luxury Landscaping Questions",
    "description": "Answers to frequently asked questions about our premium landscaping services, 48-hour installations, and hardscape material costs.",
    "content": create_hero("Common Questions", "Clarity & <span class='text-primary italic block'>Transparency.</span>", "Investing in luxury landscape architecture requires absolute clarity. We operate with complete transparency regarding our timelines, premium materials, and elite construction methods.", "./retaining_wall.png", "Contact Us", "contact.html", "Our Services", "services.html") + 
    """
    <section class="py-32 bg-surface px-8">
        <div class="max-w-4xl mx-auto space-y-10" data-aos="fade-up">
            <div class="bg-surface-container-lowest p-10 rounded-2xl shadow-md border-l-8 border-primary hover:translate-x-2 transition-transform">
                <h3 class="font-display text-2xl font-black mb-4">Do you only perform hardscape construction on weekends?</h3>
                <p class="text-secondary text-lg leading-loose">Yes. Our signature 48-Hour Strike methodology is specifically designed for high-profile clients who require zero disruption during the work week. We deploy on Friday evening and complete your luxury landscaping project by Sunday sunset.</p>
            </div>
            <div class="bg-surface-container-lowest p-10 rounded-2xl shadow-md border-l-8 border-primary hover:translate-x-2 transition-transform">
                <h3 class="font-display text-2xl font-black mb-4">What areas in Minnesota do you serve?</h3>
                <p class="text-secondary text-lg leading-loose">The Elite 4 provides premium landscape architecture and hardscape installation exclusively to select estates in Minneapolis, Saint Paul, Edina, Wayzata, Minnetonka, and the greater Twin Cities metro area.</p>
            </div>
            <div class="bg-surface-container-lowest p-10 rounded-2xl shadow-md border-l-8 border-primary hover:translate-x-2 transition-transform">
                <h3 class="font-display text-2xl font-black mb-4">Do you provide ongoing lawn care or maintenance?</h3>
                <p class="text-secondary text-lg leading-loose">No. We are specialized hardscape architects and construction masters. We focus entirely on high-value structural installations: massive retaining walls, sprawling natural stone patios, and permanent outdoor living environments.</p>
            </div>
        </div>
    </section>
    """
}

pages["testimonials.html"] = {
    "title": "Testimonials | Elite Landscaping Reviews MN",
    "description": "Read reviews and testimonials from our luxury landscaping clients across Minnesota. See why The Elite 4 is the top-rated hardscape firm.",
    "content": create_hero("Client Reverence", "Estates <span class='text-primary italic block'>Transformed.</span>", "Our reputation is built on flawless execution and absolute client satisfaction. Read testimonials from Minnesota homeowners who have experienced the 48-Hour Elite Strike.", "./luxury_patio.png", "View Portfolio", "portfolio.html", "Start Yours", "contact.html") + 
    """
    <section class="py-32 bg-surface-container-low px-8">
        <div class="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-10" data-aos="fade-up">
            <div class="bg-surface-container-lowest p-12 rounded-3xl shadow-xl hover:-translate-y-2 transition-transform border border-secondary/5">
                <div class="flex gap-2 mb-6">
                    <span class="material-symbols-outlined text-tertiary">star</span><span class="material-symbols-outlined text-tertiary">star</span><span class="material-symbols-outlined text-tertiary">star</span><span class="material-symbols-outlined text-tertiary">star</span><span class="material-symbols-outlined text-tertiary">star</span>
                </div>
                <p class="text-secondary text-xl italic leading-loose mb-8">"I was skeptical of the 48-hour promise. They arrived Friday evening with heavy machinery, and by Sunday morning our entire backyard was an architectural masterpiece. True professionals, incredibly clean, and the retaining wall is absolute perfection."</p>
                <p class="font-display font-black text-primary uppercase tracking-[0.2em] text-sm">- The Anderson Estate, Edina MN</p>
            </div>
            <div class="bg-surface-container-lowest p-12 rounded-3xl shadow-xl hover:-translate-y-2 transition-transform border border-secondary/5" data-aos="fade-up" data-aos-delay="100">
                <div class="flex gap-2 mb-6">
                    <span class="material-symbols-outlined text-tertiary">star</span><span class="material-symbols-outlined text-tertiary">star</span><span class="material-symbols-outlined text-tertiary">star</span><span class="material-symbols-outlined text-tertiary">star</span><span class="material-symbols-outlined text-tertiary">star</span>
                </div>
                <p class="text-secondary text-xl italic leading-loose mb-8">"The Elite 4 designed and installed a massive geometric poolscape and custom bluestone patio for our lake house. The symmetry is breathtaking. The fact that the four owners were the ones physically doing the work gave us immense confidence."</p>
                <p class="font-display font-black text-primary uppercase tracking-[0.2em] text-sm">- The Harrison Family, Wayzata MN</p>
            </div>
        </div>
    </section>
    """
}

dest_dir = "/Users/user/Documents/Elite 4"

for page_name, data in pages.items():
    html = layout.format(
        title=data["title"],
        description=data["description"],
        content=data["content"]
    )
    with open(os.path.join(dest_dir, page_name), "w") as f:
        f.write(html)

print("Highly detailed, SEO-rich, minimalist hamburger-menu site generated.")
