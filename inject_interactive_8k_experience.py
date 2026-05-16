import os
import glob
import shutil
import re

base_dir = '/Users/user/Documents/Elite 4'
artifacts_dir = '/Users/user/.gemini/antigravity/brain/0e41f3ad-b990-4986-a1de-8bd1b3fd1f1b'

# 1. Copy 8K Images
image_mappings = {
    '8k_luxury_garden': '8k_luxury_garden.png',
    '8k_modern_patio': '8k_modern_patio.png',
    '8k_water_feature': '8k_water_feature.png'
}

for prefix, dest_name in image_mappings.items():
    matches = glob.glob(os.path.join(artifacts_dir, f"{prefix}*.png"))
    if matches:
        src = matches[0]
        dest = os.path.join(base_dir, dest_name)
        shutil.copy(src, dest)
        print(f"Copied {src} to {dest}")

# 2. Interactive Estimator & Before/After Widgets HTML & JS
estimator_html = """
    <!-- Interactive Project Investment & Timeline Estimator -->
    <section class="py-20 px-6 max-w-7xl mx-auto my-12 bg-gradient-to-br from-brand-light/60 via-white to-brand-light/30 rounded-[40px] border border-brand-primary/20 shadow-2xl relative overflow-hidden">
        <div class="absolute top-0 right-0 w-96 h-96 bg-brand-primary/10 rounded-full blur-3xl -mr-20 -mt-20 pointer-events-none"></div>
        <div class="absolute bottom-0 left-0 w-96 h-96 bg-brand-dark/10 rounded-full blur-3xl -ml-20 -mb-20 pointer-events-none"></div>
        
        <div class="relative z-10 max-w-4xl mx-auto text-center mb-12">
            <div class="inline-flex items-center gap-2 bg-brand-primary/10 border border-brand-primary/30 px-4 py-2 rounded-full text-brand-primary font-bold text-xs uppercase tracking-widest mb-4 shadow-sm">
                <i class="fas fa-calculator animate-pulse"></i> Interactive Investment Estimator
            </div>
            <h2 class="font-heading text-4xl md:text-5xl font-black text-brand-dark tracking-tight mb-4">
                Calculate Your 48+ Hour Masterwork
            </h2>
            <p class="text-brand-gray text-base md:text-lg max-w-2xl mx-auto leading-relaxed">
                Select your desired architectural hardscape parameters below to instantly generate a transparent baseline investment tier and execution timeline.
            </p>
        </div>

        <div class="relative z-10 grid grid-cols-1 md:grid-cols-3 gap-8 max-w-5xl mx-auto items-center bg-white p-8 md:p-12 rounded-3xl shadow-xl border border-gray-100">
            <!-- Parameter 1: Project Type -->
            <div class="space-y-3 text-left">
                <label class="font-heading font-bold text-brand-dark text-sm block uppercase tracking-wider flex items-center gap-2">
                    <i class="fas fa-layer-group text-brand-primary"></i> 1. Project Type
                </label>
                <select id="est-type" class="w-full bg-brand-light/50 border border-gray-200 rounded-2xl px-5 py-4 font-semibold text-brand-dark focus:outline-none focus:border-brand-primary transition shadow-sm text-sm cursor-pointer">
                    <option value="patio">Luxury Hardscape Patio & Fire Pit</option>
                    <option value="wall">Limestone Structural Retaining Wall</option>
                    <option value="pool">Luminous Geometric Pool Scape</option>
                    <option value="full">Ultimate Symmetrical Estate Overhaul</option>
                </select>
            </div>

            <!-- Parameter 2: Estate Size -->
            <div class="space-y-3 text-left">
                <label class="font-heading font-bold text-brand-dark text-sm block uppercase tracking-wider flex items-center gap-2">
                    <i class="fas fa-ruler-combined text-brand-primary"></i> 2. Estate Scale
                </label>
                <select id="est-size" class="w-full bg-brand-light/50 border border-gray-200 rounded-2xl px-5 py-4 font-semibold text-brand-dark focus:outline-none focus:border-brand-primary transition shadow-sm text-sm cursor-pointer">
                    <option value="standard">Standard Sanctuary (~500 - 1,000 sq ft)</option>
                    <option value="premium">Premium Manor (~1,000 - 2,500 sq ft)</option>
                    <option value="compound">Prestige Compound (2,500+ sq ft)</option>
                </select>
            </div>

            <!-- Calculation Output -->
            <div class="bg-brand-dark text-white p-6 md:p-8 rounded-2xl shadow-2xl flex flex-col justify-center items-center text-center relative overflow-hidden border-b-4 border-brand-primary">
                <div class="absolute inset-0 bg-brand-primary/10 blob-shape pointer-events-none opacity-50"></div>
                <div class="relative z-10 w-full">
                    <span class="text-xs text-brand-primary font-bold uppercase tracking-widest block mb-1">Estimated Investment</span>
                    <div id="est-price" class="text-3xl md:text-4xl font-heading font-black tracking-tight text-white mb-2">$25,000 - $45,000</div>
                    <div class="w-full h-px bg-white/20 my-3"></div>
                    <span class="text-xs text-gray-300 font-medium block flex items-center justify-center gap-1.5 mb-4">
                        <i class="fas fa-clock text-brand-primary"></i> <span id="est-time">48+ Hours (Fri Eve - Sun Sunset)</span>
                    </span>
                    <a href="contact.html" class="block w-full bg-brand-primary hover:bg-green-600 text-white font-bold py-3 px-6 rounded-full text-xs uppercase tracking-wider transition shadow-lg text-center">
                        Lock In This Rate →
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- Interactive Before/After Visualizer -->
    <section class="py-20 px-6 max-w-7xl mx-auto my-12 bg-white rounded-[40px] border border-gray-100 shadow-2xl overflow-hidden relative">
        <div class="relative z-10 max-w-4xl mx-auto text-center mb-12">
            <div class="inline-flex items-center gap-2 bg-brand-primary/10 border border-brand-primary/30 px-4 py-2 rounded-full text-brand-primary font-bold text-xs uppercase tracking-widest mb-4 shadow-sm">
                <i class="fas fa-sliders-h animate-pulse"></i> Interactive Transformation
            </div>
            <h2 class="font-heading text-4xl md:text-5xl font-black text-brand-dark tracking-tight mb-4">
                Drag To Experience The Strike
            </h2>
            <p class="text-brand-gray text-base md:text-lg max-w-2xl mx-auto leading-relaxed">
                Witness the uncompromising precision of our 48+ hour deployments. Drag the slider to reveal the clinical minimalist luxury upgrade.
            </p>
        </div>

        <div class="max-w-5xl mx-auto relative rounded-3xl overflow-hidden shadow-2xl border-8 border-white bg-gray-100 select-none group" id="ba-container">
            <!-- 8K Badge -->
            <span class="absolute top-6 left-6 bg-black/80 text-white border border-white/20 px-4 py-2 rounded-full text-xs font-bold tracking-widest backdrop-blur-md z-30 shadow-lg flex items-center gap-2">
                <i class="fas fa-camera text-brand-primary"></i> 8K ULTRA HD RESOLUTION
            </span>
            
            <!-- After Image (Underneath) -->
            <img src="./8k_water_feature.png" alt="After Masterpiece" class="w-full h-[500px] md:h-[600px] object-cover pointer-events-none"/>
            <span class="absolute bottom-6 right-6 bg-brand-primary text-white px-5 py-2 rounded-full text-xs font-bold uppercase tracking-widest z-20 shadow-lg">
                After (Elite 4 Masterwork)
            </span>

            <!-- Before Image (On Top, Clipped) -->
            <div class="absolute inset-0 w-1/2 overflow-hidden z-10 border-r-4 border-brand-primary shadow-2xl" id="ba-before">
                <img src="./hero-pathway.webp" alt="Before" class="w-full h-[500px] md:h-[600px] object-cover pointer-events-none max-w-none" style="width: 1000px;" id="ba-before-img"/>
                <span class="absolute bottom-6 left-6 bg-brand-dark text-white px-5 py-2 rounded-full text-xs font-bold uppercase tracking-widest shadow-lg">
                    Before (Standard Yard)
                </span>
            </div>

            <!-- Slider Handle -->
            <div class="absolute top-0 bottom-0 left-1/2 w-1 bg-brand-primary z-20 cursor-ew-resize flex items-center justify-center shadow-2xl" id="ba-handle">
                <div class="w-12 h-12 bg-brand-primary border-4 border-white rounded-full shadow-2xl flex items-center justify-center text-white text-lg hover:scale-110 transition-transform">
                    <i class="fas fa-arrows-alt-h"></i>
                </div>
            </div>
        </div>
    </section>
"""

interactive_js = """
    <!-- Interactive Estimator & Slider JS -->
    <script>
    window.addEventListener('load', () => {
        // Estimator Logic
        const estType = document.getElementById('est-type');
        const estSize = document.getElementById('est-size');
        const estPrice = document.getElementById('est-price');
        const estTime = document.getElementById('est-time');

        const pricing = {
            patio: { standard: "$25,000 - $40,000", premium: "$40,000 - $70,000", compound: "$70,000 - $120,000+" },
            wall: { standard: "$18,000 - $35,000", premium: "$35,000 - $60,000", compound: "$60,000 - $95,000+" },
            pool: { standard: "$65,000 - $95,000", premium: "$95,000 - $150,000", compound: "$150,000 - $250,000+" },
            full: { standard: "$90,000 - $140,000", premium: "$140,000 - $220,000", compound: "$220,000 - $400,000+" }
        };

        const timelines = {
            standard: "48+ Hours (Fri Eve - Sun Sunset)",
            premium: "48+ Hours (Rollover to 2nd Weekend)",
            compound: "48+ Hours (Dedicated 2-3 Weekends)"
        };

        function updateEstimator() {
            if(estType && estSize && estPrice && estTime) {
                const t = estType.value;
                const s = estSize.value;
                estPrice.textContent = pricing[t][s];
                estTime.textContent = timelines[s];
            }
        }

        if(estType && estSize) {
            estType.addEventListener('change', updateEstimator);
            estSize.addEventListener('change', updateEstimator);
        }

        // Before/After Slider Logic
        const baContainer = document.getElementById('ba-container');
        const baBefore = document.getElementById('ba-before');
        const baHandle = document.getElementById('ba-handle');
        const baBeforeImg = document.getElementById('ba-before-img');

        if(baContainer && baBefore && baHandle && baBeforeImg) {
            function adjustWidth() {
                baBeforeImg.style.width = baContainer.offsetWidth + 'px';
            }
            adjustWidth();
            window.addEventListener('resize', adjustWidth);

            let isDragging = false;

            function onMove(e) {
                if(!isDragging) return;
                const rect = baContainer.getBoundingClientRect();
                let x = (e.clientX || e.touches[0].clientX) - rect.left;
                x = Math.max(0, Math.min(x, rect.width));
                const pct = (x / rect.width) * 100;
                baBefore.style.width = pct + '%';
                baHandle.style.left = pct + '%';
            }

            baHandle.addEventListener('mousedown', () => isDragging = true);
            baContainer.addEventListener('mouseup', () => isDragging = false);
            baContainer.addEventListener('mouseleave', () => isDragging = false);
            baContainer.addEventListener('mousemove', onMove);

            baHandle.addEventListener('touchstart', () => isDragging = true);
            baContainer.addEventListener('touchend', () => isDragging = false);
            baContainer.addEventListener('touchmove', onMove);
        }
    });
    </script>
"""

# Quick Ask Buttons for AI Widget
quick_ask_html = """
            <!-- Quick Ask Prompts -->
            <div class="px-5 py-3 bg-brand-light/40 border-t border-b border-gray-100 flex flex-wrap gap-2 max-h-28 overflow-y-auto">
                <span class="text-[10px] font-bold text-brand-dark uppercase tracking-wider w-full block mb-1"><i class="fas fa-bolt text-brand-primary mr-1"></i> Interactive Quick Prompts:</span>
                <button class="ai-quick-btn bg-white hover:bg-brand-primary hover:text-white text-brand-dark border border-gray-200 text-xs px-3 py-1.5 rounded-full transition shadow-sm font-medium flex items-center gap-1.5">
                    ⚡ 48+ Hour Availability
                </button>
                <button class="ai-quick-btn bg-white hover:bg-brand-primary hover:text-white text-brand-dark border border-gray-200 text-xs px-3 py-1.5 rounded-full transition shadow-sm font-medium flex items-center gap-1.5">
                    💎 Tier-1 Materials
                </button>
                <button class="ai-quick-btn bg-white hover:bg-brand-primary hover:text-white text-brand-dark border border-gray-200 text-xs px-3 py-1.5 rounded-full transition shadow-sm font-medium flex items-center gap-1.5">
                    💰 Investment Tiers
                </button>
                <button class="ai-quick-btn bg-white hover:bg-brand-primary hover:text-white text-brand-dark border border-gray-200 text-xs px-3 py-1.5 rounded-full transition shadow-sm font-medium flex items-center gap-1.5">
                    📅 Meet The Founders
                </button>
            </div>
"""

quick_ask_js = """
        // Quick Ask Button Click Handlers
        const quickBtns = document.querySelectorAll('.ai-quick-btn');
        quickBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                if(aiInput) {
                    aiInput.value = btn.textContent.trim().replace('⚡ ', '').replace('💎 ', '').replace('💰 ', '').replace('📅 ', '');
                    handleSend();
                }
            });
        });
"""

# Button Mappings with Rich Information & Subtitles
button_replacements = [
    # Start Yours
    (r'>Start Yours</a', r'>\n<span class="block text-base font-bold">Start Your 48+ Hour Masterwork <i class="fas fa-arrow-right ml-2"></i></span><span class="block text-[10px] font-normal uppercase tracking-wider opacity-90 mt-0.5">Book a free consultation with our founders</span>\n</a'),
    # View Portfolio
    (r'>\s*View Portfolio\s*<i class="fas fa-arrow-right"></i>\s*</a', r'>\n<span class="block text-base font-bold text-brand-dark group-hover:text-brand-primary transition">Explore Our Past Projects <i class="fas fa-arrow-right ml-2"></i></span><span class="block text-[10px] font-normal uppercase tracking-wider text-brand-gray mt-0.5">See precision stone & pool gallery</span>\n</a'),
    # Our Story
    (r'>Our Story</a', r'>\n<span class="block text-base font-bold">Meet The Elite 4 Founders <i class="fas fa-arrow-right ml-2"></i></span><span class="block text-[10px] font-normal uppercase tracking-wider opacity-90 mt-0.5">Learn about our weekend strike force</span>\n</a'),
    # Read More
    (r'>Read More</a', r'>\n<span class="block text-sm font-bold">Explore Capability Details <i class="fas fa-arrow-right ml-1"></i></span><span class="block text-[9px] font-normal uppercase tracking-wider opacity-90 mt-0.5">View materials & structural specs</span>\n</a'),
    # See All Projects
    (r'>See All Projects</a', r'>\n<span class="block text-base font-bold">View Complete 8K Gallery <i class="fas fa-arrow-right ml-2"></i></span><span class="block text-[10px] font-normal uppercase tracking-wider opacity-90 mt-0.5">Explore our luxury Minnesota portfolio</span>\n</a'),
    # More About Us
    (r'>More About Us</a', r'>\n<span class="block text-base font-bold">Discover Our Weekend Standard <i class="fas fa-arrow-right ml-2"></i></span><span class="block text-[10px] font-normal uppercase tracking-wider opacity-90 mt-0.5">Learn why our grass is always greener</span>\n</a'),
    # Submit Request
    (r'>Submit Request</button', r'>\n<span class="block text-base font-bold">Secure Your Consultation Slot <i class="fas fa-arrow-right ml-2"></i></span><span class="block text-[10px] font-normal uppercase tracking-wider opacity-90 mt-0.5">Direct communication with Gerald, Cole, Dom & Gerardo</span>\n</button'),
    # Request Consultation (Mobile Menu)
    (r'>Request Consultation</a', r'>\n<span class="block text-base font-bold">Request Consultation <i class="fas fa-arrow-right ml-2"></i></span><span class="block text-[10px] font-normal uppercase tracking-wider opacity-90 mt-0.5">Guaranteed 48+ Hour Turnaround</span>\n</a'),
]

# 8K Image Showcase Injection for all pages
image_8k_showcase_html = """
    <!-- 8K Super High Resolution Architectural Showcase -->
    <section class="py-20 px-6 max-w-7xl mx-auto my-12 bg-white rounded-[40px] border border-gray-100 shadow-2xl overflow-hidden relative">
        <div class="relative z-10 max-w-4xl mx-auto text-center mb-16">
            <div class="inline-flex items-center gap-2 bg-brand-primary/10 border border-brand-primary/30 px-4 py-2 rounded-full text-brand-primary font-bold text-xs uppercase tracking-widest mb-4 shadow-sm">
                <i class="fas fa-camera-retro animate-pulse"></i> 8K Ultra-High Resolution Gallery
            </div>
            <h2 class="font-heading text-4xl md:text-5xl font-black text-brand-dark tracking-tight mb-4">
                Uncompromising Architectural Precision
            </h2>
            <p class="text-brand-gray text-base md:text-lg max-w-2xl mx-auto leading-relaxed">
                Explore our flagship Minnesota estate deployments captured in magnificent 8K super high resolution. Every cut, contour, and botanical composition is engineered for absolute visual dominance.
            </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-7xl mx-auto items-center">
            <!-- 8K Card 1 -->
            <div class="bg-brand-light/30 rounded-3xl overflow-hidden shadow-xl border border-gray-100 group flex flex-col h-full">
                <div class="h-80 overflow-hidden relative">
                    <span class="absolute top-4 left-4 bg-black/80 text-white border border-white/20 px-3 py-1 rounded-full text-[10px] font-bold tracking-widest backdrop-blur-md z-20 shadow-md flex items-center gap-1.5">
                        <i class="fas fa-gem text-brand-primary"></i> 8K ULTRA HD
                    </span>
                    <img src="./8k_luxury_garden.png" alt="8K Luxury Garden" class="w-full h-full object-cover group-hover:scale-110 transition duration-700"/>
                </div>
                <div class="p-8 flex flex-col flex-grow justify-between bg-white">
                    <div>
                        <h3 class="font-heading font-black text-xl text-brand-dark mb-3">Sunset Estate Garden</h3>
                        <p class="text-brand-gray text-sm mb-6 leading-relaxed">Symmetrical botanical compositions framed by precision limestone retaining walls and warm recessed architectural lighting.</p>
                    </div>
                    <a href="portfolio.html" class="inline-block bg-brand-light hover:bg-brand-primary hover:text-white text-brand-primary font-bold py-3 px-6 rounded-full text-xs uppercase tracking-wider transition text-center shadow-sm">
                        Inspect 8K Masterwork →
                    </a>
                </div>
            </div>

            <!-- 8K Card 2 -->
            <div class="bg-brand-light/30 rounded-3xl overflow-hidden shadow-xl border border-gray-100 group flex flex-col h-full md:-translate-y-4 border-b-4 border-brand-primary">
                <div class="h-80 overflow-hidden relative">
                    <span class="absolute top-4 left-4 bg-black/80 text-white border border-white/20 px-3 py-1 rounded-full text-[10px] font-bold tracking-widest backdrop-blur-md z-20 shadow-md flex items-center gap-1.5">
                        <i class="fas fa-gem text-brand-primary"></i> 8K ULTRA HD
                    </span>
                    <img src="./8k_modern_patio.png" alt="8K Modern Patio" class="w-full h-full object-cover group-hover:scale-110 transition duration-700"/>
                </div>
                <div class="p-8 flex flex-col flex-grow justify-between bg-white">
                    <div>
                        <h3 class="font-heading font-black text-xl text-brand-dark mb-3">Premium Living Patio</h3>
                        <p class="text-brand-gray text-sm mb-6 leading-relaxed">Fully integrated modern outdoor kitchen, sleek geometric fire pit, and flawless stone masonry completed in a single weekend.</p>
                    </div>
                    <a href="portfolio.html" class="inline-block bg-brand-primary hover:bg-green-600 text-white font-bold py-3 px-6 rounded-full text-xs uppercase tracking-wider transition text-center shadow-lg">
                        Inspect 8K Masterwork →
                    </a>
                </div>
            </div>

            <!-- 8K Card 3 -->
            <div class="bg-brand-light/30 rounded-3xl overflow-hidden shadow-xl border border-gray-100 group flex flex-col h-full">
                <div class="h-80 overflow-hidden relative">
                    <span class="absolute top-4 left-4 bg-black/80 text-white border border-white/20 px-3 py-1 rounded-full text-[10px] font-bold tracking-widest backdrop-blur-md z-20 shadow-md flex items-center gap-1.5">
                        <i class="fas fa-gem text-brand-primary"></i> 8K ULTRA HD
                    </span>
                    <img src="./8k_water_feature.png" alt="8K Water Feature" class="w-full h-full object-cover group-hover:scale-110 transition duration-700"/>
                </div>
                <div class="p-8 flex flex-col flex-grow justify-between bg-white">
                    <div>
                        <h3 class="font-heading font-black text-xl text-brand-dark mb-3">Luminous Infinity Pool</h3>
                        <p class="text-brand-gray text-sm mb-6 leading-relaxed">Glowing geometric infinity pool scape overlooking tranquil waters, engineered with clinical minimalist luxury landscaping.</p>
                    </div>
                    <a href="portfolio.html" class="inline-block bg-brand-light hover:bg-brand-primary hover:text-white text-brand-primary font-bold py-3 px-6 rounded-full text-xs uppercase tracking-wider transition text-center shadow-sm">
                        Inspect 8K Masterwork →
                    </a>
                </div>
            </div>
        </div>
    </section>
"""

# Process all HTML files
for filename in glob.glob(os.path.join(base_dir, '*.html')):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Apply button replacements
    for old_pat, new_sub in button_replacements:
        content = re.sub(old_pat, new_sub, content)

    # 2. Inject Interactive Estimator & Before/After Widgets before Footer if not present
    if 'Interactive Project Investment' not in content:
        content = content.replace('<!-- Footer -->', estimator_html + '\n    <!-- Footer -->')

    # 3. Inject 8K Showcase before Estimator/Footer if not present
    if '8K Super High Resolution Architectural Showcase' not in content:
        if '<!-- Interactive Project Investment' in content:
            content = content.replace('<!-- Interactive Project Investment', image_8k_showcase_html + '\n    <!-- Interactive Project Investment')
        else:
            content = content.replace('<!-- Footer -->', image_8k_showcase_html + '\n    <!-- Footer -->')

    # 4. Inject Interactive JS and Quick Ask JS
    if '// Estimator Logic' not in content:
        content = content.replace('<!-- AI Concierge Widget -->', interactive_js + '\n    <!-- AI Concierge Widget -->')

    if '<!-- Quick Ask Prompts -->' not in content:
        content = content.replace('<div id="ai-messages"', quick_ask_html + '\n            <div id="ai-messages"')
        content = content.replace('if(aiSendBtn && aiInput) {', quick_ask_js + '\n        if(aiSendBtn && aiInput) {')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully upgraded {filename} with interactive 8K experience and rich button info.")

print("\nAll website pages have been successfully transformed into an elite interactive 8K experience!")
