import os

tailwind_config = """<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<script id="tailwind-config">
tailwind.config = {
    darkMode: "class",
    theme: {
        extend: {
            "colors": {
                "surface-container-high": "#e1e3e1",
                "primary-fixed-dim": "#b5e9c5",
                "primary-dim": "#2a593e",
                "surface-tint": "#366549",
                "on-primary-fixed-variant": "#3b6a4e",
                "on-tertiary": "#fff1d4",
                "on-secondary-fixed-variant": "#575d5a",
                "on-secondary-container": "#4d5350",
                "on-surface-variant": "#5a5c5b",
                "secondary-fixed-dim": "#d0d6d2",
                "surface-container-lowest": "#ffffff",
                "outline-variant": "#acadac",
                "on-primary-fixed": "#1e4d33",
                "secondary-fixed": "#dee4e0",
                "secondary-dim": "#4b514e",
                "background": "#f6f6f5",
                "inverse-on-surface": "#9c9d9c",
                "primary-fixed": "#c3f7d3",
                "on-secondary-fixed": "#3b413e",
                "surface": "#f6f6f5",
                "on-tertiary-container": "#584500",
                "surface-dim": "#d3d5d3",
                "on-error": "#ffefee",
                "error": "#b31b25",
                "on-tertiary-fixed": "#413200",
                "tertiary-fixed-dim": "#e6c047",
                "error-container": "#fb5151",
                "surface-container-low": "#f0f1ef",
                "outline": "#767776",
                "secondary": "#575d5a",
                "secondary-container": "#dee4e0",
                "inverse-primary": "#c9fdd8",
                "on-tertiary-fixed-variant": "#634e00",
                "on-error-container": "#570008",
                "on-background": "#2d2f2e",
                "surface-bright": "#f6f6f5",
                "on-primary-container": "#316044",
                "surface-variant": "#dbdddb",
                "tertiary-container": "#f5ce53",
                "tertiary": "#705900",
                "inverse-surface": "#0c0f0e",
                "on-surface": "#2d2f2e",
                "primary": "#366549",
                "on-secondary": "#eef4f0",
                "tertiary-fixed": "#f5ce53",
                "primary-container": "#c3f7d3",
                "surface-container-highest": "#dbdddb",
                "on-primary": "#cbffda",
                "tertiary-dim": "#624d00",
                "surface-container": "#e7e8e6",
                "error-dim": "#9f0519"
            },
            "borderRadius": {
                "DEFAULT": "0.125rem",
                "lg": "0.25rem",
                "xl": "0.5rem",
                "full": "0.75rem"
            },
            "fontFamily": {
                "headline": ["Epilogue"],
                "display": ["Epilogue"],
                "body": ["Manrope"],
                "label": ["Manrope"]
            }
        }
    }
}
</script>
<style>
    .material-symbols-outlined { font-variation-settings: 'FILL' 0, 'wght' 300, 'GRAD' 0, 'opsz' 24; }
    .hero-gradient { background: linear-gradient(135deg, #366549 0%, #2a593e 100%); }
</style>
<link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">"""

nav_block = """<!-- TopNavBar -->
<nav class="fixed top-0 w-full z-50 bg-[#f6f6f5]/80 backdrop-blur-xl shadow-[0px_20px_40px_rgba(45,29,46,0.06)]">
<div class="flex justify-between items-center w-full px-6 md:px-12 py-4 md:py-6 max-w-[1920px] mx-auto">
    <a class="text-xl md:text-2xl font-black tracking-[-0.02em] text-[#366549] uppercase font-['Epilogue']" href="index.html">The Elite 4</a>
    
    <!-- Desktop Nav Links (Kept exactly how it was!) -->
    <div class="hidden lg:flex gap-8 items-center">
        <a class="font-['Epilogue'] tracking-tighter font-bold uppercase text-sm text-[#575d5a] hover:text-[#366549] transition-colors hover:scale-[1.02]" href="index.html">Home</a>
        <a class="font-['Epilogue'] tracking-tighter font-bold uppercase text-sm text-[#575d5a] hover:text-[#366549] transition-colors hover:scale-[1.02]" href="about.html">About Us</a>
        <a class="font-['Epilogue'] tracking-tighter font-bold uppercase text-sm text-[#575d5a] hover:text-[#366549] transition-colors hover:scale-[1.02]" href="services.html">Services</a>
        <a class="font-['Epilogue'] tracking-tighter font-bold uppercase text-sm text-[#575d5a] hover:text-[#366549] transition-colors hover:scale-[1.02]" href="portfolio.html">Portfolio</a>
        <a class="font-['Epilogue'] tracking-tighter font-bold uppercase text-sm text-[#575d5a] hover:text-[#366549] transition-colors hover:scale-[1.02]" href="process.html">Process</a>
        <a class="font-['Epilogue'] tracking-tighter font-bold uppercase text-sm text-[#575d5a] hover:text-[#366549] transition-colors hover:scale-[1.02]" href="journal.html">Journal</a>
    </div>

    <!-- Right Side: CTA and 3 Horizontal Lines -->
    <div class="flex items-center gap-4">
        <!-- Kept the original button exactly as it was -->
        <a href="contact.html" class="hidden md:inline-block bg-[#366549] text-white px-6 py-3 rounded-md font-['Epilogue'] font-bold text-xs uppercase tracking-widest scale-95 hover:scale-100 active:scale-90 transition-transform shadow-lg shadow-[#366549]/20">
            Request Consultation
        </a>
        
        <!-- The 3 Horizontal Lines (Extra Help) visible everywhere -->
        <button id="mobile-menu-button" class="text-[#366549] p-2 hover:bg-[#366549]/10 rounded-full transition-colors flex items-center justify-center">
            <span class="material-symbols-outlined text-3xl">menu</span>
        </button>
    </div>
</div>

<!-- Mobile Nav Overlay -->
<div id="mobile-menu" class="fixed inset-0 bg-[#f6f6f5] z-[100] flex flex-col justify-center items-center gap-8 hidden opacity-0 transition-opacity duration-300">
    <button id="close-menu-button" class="absolute top-6 right-6 text-[#366549] p-2 hover:rotate-90 transition-transform">
        <span class="material-symbols-outlined text-4xl">close</span>
    </button>
    <a class="font-['Epilogue'] text-3xl font-bold uppercase tracking-widest text-[#575d5a] hover:text-[#366549] transition-colors" href="index.html">Home</a>
    <a class="font-['Epilogue'] text-3xl font-bold uppercase tracking-widest text-[#575d5a] hover:text-[#366549] transition-colors" href="about.html">About Us</a>
    <a class="font-['Epilogue'] text-3xl font-bold uppercase tracking-widest text-[#575d5a] hover:text-[#366549] transition-colors" href="services.html">Services</a>
    <a class="font-['Epilogue'] text-3xl font-bold uppercase tracking-widest text-[#575d5a] hover:text-[#366549] transition-colors" href="portfolio.html">Portfolio</a>
    <a class="font-['Epilogue'] text-3xl font-bold uppercase tracking-widest text-[#575d5a] hover:text-[#366549] transition-colors" href="process.html">Process</a>
    <a class="font-['Epilogue'] text-3xl font-bold uppercase tracking-widest text-[#575d5a] hover:text-[#366549] transition-colors" href="journal.html">Journal</a>
    <a href="contact.html" class="mt-8 bg-[#366549] text-white px-8 py-4 rounded-md font-['Epilogue'] font-bold text-sm uppercase tracking-widest shadow-lg text-center">
        Request Consultation
    </a>
</div>
</nav>"""

footer_block = """<!-- Footer -->
<footer class="w-full mt-auto bg-[#f0f1ef] flex flex-col items-center justify-center py-16 px-8 border-t border-[#acadac]/15">
<div class="max-w-7xl mx-auto w-full grid grid-cols-1 md:grid-cols-3 gap-12 mb-12">
    <div>
        <div class="text-xl font-black text-[#575d5a] mb-6 font-['Epilogue'] uppercase tracking-tight">The Elite 4</div>
        <p class="font-['Manrope'] text-sm leading-relaxed text-[#575d5a] max-w-xs">
            Minnesota's premier landscaping atelier. Symmetrically designed, built with grit, finished with grace.
        </p>
    </div>
    <div>
        <h4 class="font-['Epilogue'] text-xs font-black uppercase tracking-widest text-[#366549] mb-6">Service Areas</h4>
        <div class="grid grid-cols-2 gap-y-3">
            <a class="font-['Manrope'] text-sm text-[#575d5a] hover:text-[#366549] transition-colors" href="#">Minneapolis</a>
            <a class="font-['Manrope'] text-sm text-[#575d5a] hover:text-[#366549] transition-colors" href="#">Saint Paul</a>
            <a class="font-['Manrope'] text-sm text-[#575d5a] hover:text-[#366549] transition-colors" href="#">Edina</a>
            <a class="font-['Manrope'] text-sm text-[#575d5a] hover:text-[#366549] transition-colors" href="#">Wayzata</a>
            <a class="font-['Manrope'] text-sm text-[#575d5a] hover:text-[#366549] transition-colors" href="#">Minnetonka</a>
        </div>
    </div>
    <div>
        <h4 class="font-['Epilogue'] text-xs font-black uppercase tracking-widest text-[#366549] mb-6">Connect</h4>
        <div class="space-y-3 flex flex-col">
            <a class="font-['Manrope'] text-xs tracking-[0.15em] uppercase text-[#575d5a] hover:text-[#366549] transition-colors" href="contact.html">Contact Us</a>
            <a class="font-['Manrope'] text-xs tracking-[0.15em] uppercase text-[#575d5a] hover:text-[#366549] transition-colors" href="faq.html">FAQ</a>
            <a class="font-['Manrope'] text-xs tracking-[0.15em] uppercase text-[#575d5a] hover:text-[#366549] transition-colors" href="testimonials.html">Testimonials</a>
            <a class="font-['Manrope'] text-xs tracking-[0.15em] uppercase text-[#575d5a] hover:text-[#366549] transition-colors" href="#">Privacy Policy</a>
        </div>
    </div>
</div>
<div class="w-full text-center pt-8 border-t border-[#acadac]/10">
    <p class="font-['Manrope'] text-xs tracking-[0.15em] uppercase text-[#575d5a]">© 2026 The Elite 4. Architectural Landscaping Excellence.</p>
</div>
</footer>
<script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
<script>
    document.addEventListener('DOMContentLoaded', () => {
        AOS.init({duration: 800, once: true, offset: 50});
        const mobileMenuBtn = document.getElementById('mobile-menu-button');
        const closeMenuBtn = document.getElementById('close-menu-button');
        const mobileMenu = document.getElementById('mobile-menu');

        if(mobileMenuBtn && closeMenuBtn && mobileMenu) {
            mobileMenuBtn.addEventListener('click', () => {
                mobileMenu.classList.remove('hidden');
                setTimeout(() => mobileMenu.classList.remove('opacity-0'), 10);
                document.body.style.overflow = 'hidden';
            });
            closeMenuBtn.addEventListener('click', () => {
                mobileMenu.classList.add('opacity-0');
                setTimeout(() => mobileMenu.classList.add('hidden'), 300);
                document.body.style.overflow = '';
            });
            mobileMenu.querySelectorAll('a').forEach(link => {
                link.addEventListener('click', () => {
                    mobileMenu.classList.add('opacity-0');
                    setTimeout(() => mobileMenu.classList.add('hidden'), 300);
                    document.body.style.overflow = '';
                });
            });
        }
    });
</script>
</body>
</html>"""

def generate_page(filename, title, description, body_content):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>{title}</title>
<meta name="description" content="{description}">
<link href="https://fonts.googleapis.com/css2?family=Epilogue:wght@700;800;900&display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
{tailwind_config}
</head>
<body class="bg-[#f6f6f5] text-[#2d2f2e] font-['Manrope'] antialiased">
{nav_block}
<main class="w-full">
{body_content}
</main>
{footer_block}
"""
    with open(os.path.join("/Users/user/Documents/Elite 4", filename), "w") as f:
        f.write(html)


def build_hero(subtitle, title, description, image, cta1_text, cta1_link, cta2_text, cta2_link):
    return f"""
    <header class="relative min-h-screen flex flex-col md:flex-row pt-20">
        <div class="w-full md:w-1/2 flex flex-col justify-center px-8 md:px-20 py-20 bg-[#f6f6f5]" data-aos="fade-right">
            <div class="max-w-xl">
                <span class="font-['Manrope'] text-xs uppercase tracking-[0.2em] text-[#705900] font-bold mb-4 block">{subtitle}</span>
                <h1 class="font-['Epilogue'] text-5xl md:text-7xl font-extrabold text-[#2d2f2e] leading-[1.1] tracking-tighter mb-8">
                    {title}
                </h1>
                <p class="text-lg text-[#575d5a] leading-relaxed mb-12 max-w-lg">
                    {description}
                </p>
                <div class="flex flex-wrap gap-6">
                    <a href="{cta1_link}" class="inline-block bg-[#366549] text-white px-8 py-4 rounded-md font-['Epilogue'] font-bold text-sm uppercase tracking-widest hover:translate-y-[-2px] transition-transform shadow-lg shadow-[#366549]/20">{cta1_text}</a>
                    <a href="{cta2_link}" class="inline-block text-[#366549] border-b-2 border-[#acadac] hover:border-[#705900] px-2 py-4 font-['Epilogue'] font-bold text-sm uppercase tracking-widest transition-colors">{cta2_text}</a>
                </div>
            </div>
        </div>
        <div class="w-full md:w-1/2 relative min-h-[500px] overflow-hidden" data-aos="fade-left">
            <img src="{image}" alt="Landscape" loading="lazy" class="absolute inset-0 w-full h-full object-cover"/>
            <div class="absolute inset-0 bg-gradient-to-r from-[#f6f6f5]/20 to-transparent"></div>
        </div>
    </header>
    """

# 1. Index
generate_page("index.html", "The Elite 4 | Premium MN Landscape Design Strike-Force", "Minnesota's premier landscape design and hardscape construction strike-force.", 
    build_hero("Symmetry in Nature", "Premier Landscape Design Across <span class='text-[#366549] italic'>Minnesota.</span>", "Architecture for the outdoors. We transform Minnesota estates into luminous sanctuaries using precision-cut stone and curated botanical compositions.", "./hero-pathway.jpg", "View Portfolio", "portfolio.html", "Our Process", "process.html") + 
    """
    <section class="py-24 bg-[#f0f1ef]" data-aos="fade-up">
        <div class="max-w-7xl mx-auto px-8 grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            <div class="relative aspect-square">
                <img src="./landscape_team.png" alt="Team" loading="lazy" class="w-full h-full object-cover rounded-lg shadow-2xl"/>
                <div class="absolute -bottom-8 -right-8 bg-[#f6f6f5] p-8 shadow-xl max-w-xs border-l-4 border-[#705900]">
                    <p class="font-['Epilogue'] font-black text-4xl text-[#366549] mb-2">Weekend Only</p>
                    <p class="font-['Manrope'] text-[#575d5a] text-sm leading-relaxed">Exclusive availability for rapid-strike deployments. We build while you rest.</p>
                </div>
            </div>
            <div class="space-y-8">
                <h2 class="font-['Epilogue'] text-4xl font-extrabold tracking-tighter text-[#2d2f2e]">The "Elite 4" Boutique Strike-Force</h2>
                <p class="text-lg text-[#575d5a] leading-relaxed">We don't do mass-market landscaping. The Elite 4 is a specialized four-man crew of master craftsmen. We operate as a high-precision unit, focusing on one single masterpiece at a time.</p>
                <div class="p-8 bg-white rounded-xl shadow-sm border-l-2 border-[#366549]">
                    <h3 class="font-['Epilogue'] font-bold text-xl mb-3 text-[#366549]">Strategic Weekend Execution</h3>
                    <p class="text-[#575d5a] leading-relaxed">Designed for the high-profile homeowner. Our strike-force deploys on Friday evening and completes major hardscape transformations by Monday morning, minimizing disruption to your private sanctuary.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- 5 Pillars of Perfection: Bento Grid -->
    <section class="py-32 bg-[#f6f6f5] overflow-hidden">
        <div class="max-w-7xl mx-auto px-8">
            <div class="text-center mb-20" data-aos="fade-up">
                <h2 class="font-['Epilogue'] text-4xl md:text-5xl font-extrabold tracking-tighter mb-4 text-[#2d2f2e]">5 Pillars of Perfection</h2>
                <div class="w-24 h-1 bg-[#705900] mx-auto"></div>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-6 gap-6">
                <div class="md:col-span-3 bg-white p-10 flex flex-col justify-between group hover:bg-[#366549] transition-all duration-500 shadow-sm" data-aos="fade-up">
                    <span class="material-symbols-outlined text-4xl text-[#366549] group-hover:text-white mb-6">diamond</span>
                    <h3 class="font-['Epilogue'] text-2xl font-bold mb-4 group-hover:text-white">Quality</h3>
                    <p class="text-[#575d5a] group-hover:text-white/80 leading-relaxed">Zero compromises. We source Tier-1 granite and limestone, ensuring every joint is hair-line precise.</p>
                </div>
                <div class="md:col-span-3 bg-[#f0f1ef] p-10 flex flex-col justify-between hover:translate-y-[-4px] transition-transform shadow-sm" data-aos="fade-up" data-aos-delay="100">
                    <span class="material-symbols-outlined text-4xl text-[#575d5a] mb-6">shield_with_heart</span>
                    <h3 class="font-['Epilogue'] text-2xl font-bold mb-4 text-[#2d2f2e]">Safety</h3>
                    <p class="text-[#575d5a] leading-relaxed">A clean site is a safe site. Our rigorous protocols protect your estate, your family, and our strike-force.</p>
                </div>
                <div class="md:col-span-2 bg-white p-10 flex flex-col justify-between border-t-4 border-[#705900] shadow-sm" data-aos="fade-up" data-aos-delay="200">
                    <span class="material-symbols-outlined text-4xl text-[#705900] mb-6">handshake</span>
                    <h3 class="font-['Epilogue'] text-xl font-bold mb-4 text-[#2d2f2e]">Honest</h3>
                    <p class="text-[#575d5a] text-sm leading-relaxed">Transparent pricing and realistic timelines. If we say it will be done by Sunday sunset, it will be.</p>
                </div>
                <div class="md:col-span-2 bg-[#e1e3e1] p-10 flex flex-col justify-between shadow-sm" data-aos="fade-up" data-aos-delay="300">
                    <span class="material-symbols-outlined text-4xl text-[#575d5a] mb-6">groups</span>
                    <h3 class="font-['Epilogue'] text-xl font-bold mb-4 text-[#2d2f2e]">Teamwork</h3>
                    <p class="text-[#575d5a] text-sm leading-relaxed">The Elite 4 move in unison. A synchronized symphony of masonry and botanical artistry.</p>
                </div>
                <div class="md:col-span-2 bg-[#366549] p-10 flex flex-col justify-between shadow-lg" data-aos="fade-up" data-aos-delay="400">
                    <span class="material-symbols-outlined text-4xl text-white mb-6">workspace_premium</span>
                    <h3 class="font-['Epilogue'] text-xl font-bold mb-4 text-white">Attitude</h3>
                    <p class="text-white/80 text-sm leading-relaxed">Unrelenting grit combined with artistic grace. We embrace the labor because we revere the outcome.</p>
                </div>
            </div>
        </div>
    </section>
    """
)

# 2. About
generate_page("about.html", "About Us | The Elite 4 Founders", "Meet the Elite 4, Minnesota's premier luxury landscaping founders.", 
    build_hero("The Strike Force", "Four Craftsmen. One <span class='text-[#366549] italic'>Symphony.</span>", "The Elite 4 was founded by four of Minnesota's most experienced and highly sought-after landscape architecture professionals. We recognized a massive gap in the luxury landscaping market.", "./landscape_team.png", "View Process", "process.html", "Contact Us", "contact.html") + 
    """
    <section class="py-24 bg-[#f0f1ef]" data-aos="fade-up">
        <div class="max-w-4xl mx-auto text-center px-8">
            <h2 class="font-['Epilogue'] text-4xl md:text-5xl font-black mb-10 text-[#2d2f2e] tracking-tight">Precision, Integrity, and Grit</h2>
            <p class="text-[#575d5a] text-lg leading-loose font-medium mb-8">We are not a mass-market lawn care company. We are a specialized, four-man crew of master hardscape craftsmen. When you hire The Elite 4, you are hiring the owners of the company to physically build your luxury landscape. We operate as a high-precision military unit, focusing exclusively on one single masterpiece at a time.</p>
        </div>
    </section>
    """
)

# 3. Services
generate_page("services.html", "Services | Premium Hardscape Construction Minnesota", "We specialize in high-end hardscaping, retaining walls, and luxury patios.", 
    build_hero("Our Capabilities", "Symmetric Hardscape <span class='text-[#366549] italic'>Mastery.</span>", "We provide comprehensive, high-end landscape architecture and hardscape construction services. Whether you need a massive structural retaining wall engineered for safety, or a breathtaking luxury patio for entertaining.", "./modern_pool.png", "View Portfolio", "portfolio.html", "Consultation", "contact.html") + 
    """
    <section class="py-24 bg-[#f6f6f5] px-8">
        <div class="max-w-7xl mx-auto space-y-32">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-16 items-center">
                <div data-aos="fade-right" class="order-2 md:order-1">
                    <h2 class="font-['Epilogue'] text-4xl font-black mb-8 text-[#2d2f2e]">Luxury Patio & Outdoor Living Construction</h2>
                    <p class="text-[#575d5a] text-lg leading-loose mb-8">Expand your estate's livable square footage with our custom outdoor living spaces. We design and construct premium natural stone patios, modern geometric fire pits, and fully integrated outdoor kitchens.</p>
                    <a href="contact.html" class="inline-block bg-[#366549] text-white px-8 py-4 rounded-md font-['Epilogue'] font-black text-xs uppercase tracking-widest shadow-xl hover:translate-y-[-2px] transition-transform">Get a Quote</a>
                </div>
                <div data-aos="fade-left" class="order-1 md:order-2">
                    <img src="./luxury_patio.png" alt="Luxury Patio Construction" loading="lazy" class="w-full h-[500px] object-cover rounded-xl shadow-2xl">
                </div>
            </div>
        </div>
    </section>
    """
)

# 4. Portfolio
generate_page("portfolio.html", "Portfolio | Minnesota Luxury Landscape Gallery", "View our extensive portfolio of luxury Minnesota landscapes.", 
    build_hero("The Gallery", "Curated Outdoor <span class='text-[#366549] italic'>Sanctuaries.</span>", "Explore a curated gallery of our finest weekend hardscape transformations. From sprawling Minneapolis estates to private lakeside retreats in Wayzata.", "./luxury_patio.png", "Start Yours", "contact.html", "Our Process", "process.html") + 
    """
    <section class="py-24 bg-[#f0f1ef] px-8">
        <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8">
            <div class="group relative overflow-hidden rounded-xl shadow-lg" data-aos="fade-up">
                <img src="./retaining_wall.png" alt="Project" loading="lazy" class="w-full h-[500px] object-cover group-hover:scale-110 transition-transform duration-700">
                <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent flex flex-col justify-end p-10 opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                    <h3 class="font-['Epilogue'] text-white text-2xl font-bold">Limestone Retaining Wall</h3>
                </div>
            </div>
            <div class="group relative overflow-hidden rounded-xl shadow-lg" data-aos="fade-up" data-aos-delay="100">
                <img src="./modern_pool.png" alt="Project" loading="lazy" class="w-full h-[500px] object-cover group-hover:scale-110 transition-transform duration-700">
                <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent flex flex-col justify-end p-10 opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                    <h3 class="font-['Epilogue'] text-white text-2xl font-bold">Geometric Pool Scape</h3>
                </div>
            </div>
        </div>
    </section>
    """
)

# 5. Process
generate_page("process.html", "Our Process | The 48-Hour Hardscape Transformation", "Learn about our unique 48-hour luxury hardscape installation process.", 
    build_hero("The 48-Hour Strike", "We Build While <span class='text-[#366549] italic'>You Rest.</span>", "Traditional landscaping companies are notoriously slow. The Elite 4 has revolutionized the industry with our signature 48-Hour Hardscape Strike.", "./landscape_team.png", "Contact Us", "contact.html", "Read Journal", "journal.html") + 
    """
    <section class="py-24 bg-[#f6f6f5] text-center px-8">
        <div class="max-w-5xl mx-auto" data-aos="fade-up">
            <h2 class="font-['Epilogue'] text-4xl md:text-5xl font-black mb-10 text-[#2d2f2e] tracking-tight">The Anatomy of an Elite Deployment</h2>
            <div class="space-y-8 text-left mt-16">
                <div class="bg-white p-10 rounded-xl shadow-sm border-l-8 border-[#366549] flex flex-col md:flex-row gap-8 items-center" data-aos="fade-up">
                    <div class="text-6xl font-black text-[#705900]/20 font-['Epilogue'] min-w-[80px]">01</div>
                    <div>
                        <h3 class="font-['Epilogue'] text-2xl font-black mb-4 text-[#366549]">The Architectural Consultation</h3>
                        <p class="text-[#575d5a] leading-loose">We draft fully symmetrical, 3D luxury landscape designs ensuring exact aesthetic alignment.</p>
                    </div>
                </div>
                <div class="bg-white p-10 rounded-xl shadow-sm border-l-8 border-[#366549] flex flex-col md:flex-row gap-8 items-center" data-aos="fade-up" data-aos-delay="100">
                    <div class="text-6xl font-black text-[#705900]/20 font-['Epilogue'] min-w-[80px]">02</div>
                    <div>
                        <h3 class="font-['Epilogue'] text-2xl font-black mb-4 text-[#366549]">Friday 5 PM: Site Prep</h3>
                        <p class="text-[#575d5a] leading-loose">The Elite 4 arrives with heavy machinery. We immediately excavate the site.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
    """
)

# 6. Journal
generate_page("journal.html", "The Elite Journal | Landscape Design Insights", "Read our field reports and deep dives into luxury landscape architecture.", 
    build_hero("Field Reports", "Landscaping <span class='text-[#366549] italic'>Insights.</span>", "Stay informed with the latest developments in luxury landscape architecture. The Elite 4 shares our expertise on hardscape construction.", "./hero-pathway.jpg", "Subscribe", "contact.html", "View Portfolio", "portfolio.html") + 
    """
    <section class="py-24 bg-[#f0f1ef] px-8">
        <div class="max-w-4xl mx-auto grid grid-cols-1 gap-12">
            <div class="bg-white p-10 rounded-xl shadow-lg border-t-4 border-[#705900]" data-aos="fade-up">
                <span class="font-['Manrope'] text-xs uppercase tracking-widest text-[#366549] mb-4 block font-bold">Design Theory</span>
                <h3 class="font-['Epilogue'] text-3xl font-bold mb-4">The Importance of Symmetry in Luxury Hardscapes</h3>
                <p class="text-[#575d5a] mb-6">Why true luxury relies on geometric precision and mathematical balance...</p>
                <a href="contact.html" class="font-['Epilogue'] text-sm font-bold text-[#366549] uppercase tracking-widest">Consult With Us</a>
            </div>
        </div>
    </section>
    """
)

# 7. FAQ
generate_page("faq.html", "FAQ | Minnesota Luxury Landscaping Questions", "Answers to frequently asked questions about our premium landscaping services.", 
    build_hero("Common Questions", "Clarity & <span class='text-[#366549] italic'>Transparency.</span>", "Investing in luxury landscape architecture requires absolute clarity. We operate with complete transparency regarding our timelines.", "./retaining_wall.png", "Contact Us", "contact.html", "Our Services", "services.html") + 
    """
    <section class="py-24 bg-[#f6f6f5] px-8">
        <div class="max-w-4xl mx-auto space-y-8" data-aos="fade-up">
            <div class="bg-white p-8 rounded-xl shadow-sm border-l-4 border-[#366549]">
                <h3 class="font-['Epilogue'] text-xl font-bold mb-2">Do you only perform hardscape construction on weekends?</h3>
                <p class="text-[#575d5a]">Yes. Our signature 48-Hour Strike methodology is specifically designed for high-profile clients who require zero disruption during the work week.</p>
            </div>
        </div>
    </section>
    """
)

# 8. Testimonials
generate_page("testimonials.html", "Testimonials | Elite Landscaping Reviews MN", "Read reviews and testimonials from our luxury landscaping clients across Minnesota.", 
    build_hero("Client Reverence", "Estates <span class='text-[#366549] italic'>Transformed.</span>", "Our reputation is built on flawless execution and absolute client satisfaction.", "./luxury_patio.png", "View Portfolio", "portfolio.html", "Start Yours", "contact.html") + 
    """
    <section class="py-24 bg-[#f0f1ef] px-8">
        <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8" data-aos="fade-up">
            <div class="bg-white p-10 rounded-xl shadow-sm">
                <p class="text-[#575d5a] italic mb-6">"They arrived Friday evening with heavy machinery, and by Sunday morning our entire backyard was an architectural masterpiece. True professionals."</p>
                <p class="font-['Epilogue'] font-bold text-[#366549] uppercase tracking-widest text-xs">- The Anderson Estate</p>
            </div>
        </div>
    </section>
    """
)

# 9. Contact
generate_page("contact.html", "Contact | Hire The Elite 4 Landscapers", "Request a consultation for premium landscape design.", 
    """
    <header class="pt-40 pb-20 bg-[#f6f6f5]">
        <div class="max-w-6xl mx-auto px-8 grid grid-cols-1 md:grid-cols-2 gap-16 items-center">
            <div data-aos="fade-right">
                <span class="font-['Manrope'] text-xs uppercase tracking-[0.2em] text-[#705900] font-bold mb-4 block">Commission Our Strike-Force</span>
                <h1 class="font-['Epilogue'] text-5xl md:text-7xl font-extrabold text-[#2d2f2e] leading-[1.1] tracking-tighter mb-8">
                    Start Your <span class="text-[#366549] italic">Transformation.</span>
                </h1>
                <p class="text-lg text-[#575d5a] leading-relaxed mb-8">Fill out the brief below, and an Elite 4 architect will reach out within 24 hours.</p>
            </div>
            <div class="bg-white p-10 rounded-lg shadow-2xl border-t-4 border-[#366549]" data-aos="fade-left">
                <form action="#" method="POST" class="space-y-6">
                    <div>
                        <label class="block font-['Manrope'] text-xs uppercase tracking-widest text-[#575d5a] font-bold mb-2">Name</label>
                        <input type="text" class="w-full bg-[#f0f1ef] border border-[#acadac]/30 px-4 py-3 focus:outline-none focus:border-[#366549]">
                    </div>
                    <div>
                        <label class="block font-['Manrope'] text-xs uppercase tracking-widest text-[#575d5a] font-bold mb-2">Email</label>
                        <input type="email" class="w-full bg-[#f0f1ef] border border-[#acadac]/30 px-4 py-3 focus:outline-none focus:border-[#366549]">
                    </div>
                    <a href="index.html" class="block w-full text-center bg-[#366549] text-white px-8 py-4 font-['Epilogue'] font-bold uppercase tracking-widest shadow-lg shadow-[#366549]/20">Submit Inquiry</a>
                </form>
            </div>
        </div>
    </header>
    """
)

print("Exact original layout restored with desktop links AND hamburger menu.")
