import os
import glob
import re

base_dir = '/Users/user/Documents/Elite 4'

# 1. Complete SEO Metadata per page
seo_mappings = {
    'index.html': {
        'title': 'The Elite 4 | Luxury Landscape Design & Master Hardscaping Minnesota',
        'desc': 'Experience Minnesota\'s premier weekend-only landscaping strike force. The Elite 4 specializes in luxury limestone retaining walls, geometric pools, and hardscapes deployed in 48+ hours.',
        'keywords': 'luxury landscaping Minnesota, limestone retaining walls Minneapolis, 48 hour hardscape deployment, geometric pool builders MN, premium outdoor living, The Elite 4 landscaping'
    },
    'about.html': {
        'title': 'Meet The Elite 4 | Founders & Weekend Strike Force Landscaping MN',
        'desc': 'Get to know Gerald, Cole, Dom, and Gerardo—the four master craftsmen behind The Elite 4. Discover our weekend-only deployment model and clinical minimalist landscaping standards.',
        'keywords': 'The Elite 4 founders, Gerald Cole Dom Gerardo, weekend landscaping strike force, Minnesota landscape architects, luxury garden designers MN'
    },
    'services.html': {
        'title': 'Luxury Landscaping Services | Retaining Walls, Pools & Hardscapes MN',
        'desc': 'Explore The Elite 4\'s uncompromising architectural hardscaping services. From natural limestone retaining walls to luminous geometric pools and outdoor kitchens, deployed in 48+ hours.',
        'keywords': 'limestone retaining wall construction, geometric pool installation MN, luxury patio builders Minneapolis, outdoor kitchen masonry, high-end hardscaping services'
    },
    'portfolio.html': {
        'title': '8K Landscape Design Portfolio | The Elite 4 Masterworks Minnesota',
        'desc': 'Immerse yourself in The Elite 4\'s flagship Minnesota estate deployments captured in magnificent 8K resolution. Explore luxury patios, water features, and symmetrical gardens.',
        'keywords': '8K landscaping portfolio, luxury garden gallery Minnesota, retaining wall pictures MN, geometric pool showcase, clinical minimalist landscape design'
    },
    'process.html': {
        'title': 'The 48+ Hour Strike Force Process | The Elite 4 Landscaping MN',
        'desc': 'Learn how The Elite 4 transforms premium Minnesota properties in a single weekend. Explore our 48+ hour deployment process from precision site prep to the final handover.',
        'keywords': '48 hour landscaping process, weekend yard transformation, landscape deployment timeline, efficient hardscaping MN, The Elite 4 process'
    },
    'journal.html': {
        'title': 'The Elite 4 Journal | Luxury Landscaping Insights & Architecture MN',
        'desc': 'Read the latest insights on clinical minimalist landscape design, limestone structural engineering, and botanical symmetry from the founders of The Elite 4.',
        'keywords': 'landscaping blog Minnesota, luxury hardscape insights, retaining wall engineering guide, botanical symmetry tips, outdoor living articles'
    },
    'faq.html': {
        'title': 'Frequently Asked Questions | The Elite 4 Luxury Landscaping MN',
        'desc': 'Have questions about our 48+ hour weekend strike force, investment tiers, or Tier-1 materials? Find complete, transparent answers from The Elite 4.',
        'keywords': 'landscaping FAQ Minnesota, hardscape investment questions, weekend landscaping cost, The Elite 4 warranty, landscape design consultation'
    },
    'testimonials.html': {
        'title': 'Client Testimonials & Reviews | The Elite 4 Landscaping Minnesota',
        'desc': 'Read verified reviews from luxury estate owners across Minnesota. Discover why clients trust The Elite 4\'s weekend strike force for their multi-million dollar properties.',
        'keywords': 'The Elite 4 reviews, luxury landscaping testimonials MN, Minnesota landscape contractor ratings, client success stories hardscaping'
    },
    'contact.html': {
        'title': 'Secure Your Weekend Slot | Contact The Elite 4 Landscaping MN',
        'desc': 'Direct communication with Gerald, Cole, Dom, and Gerardo. Request a consultation today to secure your 48+ hour weekend deployment slot.',
        'keywords': 'contact The Elite 4, book landscaping consultation MN, schedule hardscape estimate Minneapolis, weekend landscaping contractor contact'
    },
    'post-retaining-walls.html': {
        'title': 'The Art of Limestone Retaining Walls | The Elite 4 Journal MN',
        'desc': 'Explore the structural engineering and clinical minimalist beauty of natural limestone retaining walls in Minnesota. An authoritative guide by The Elite 4.',
        'keywords': 'limestone retaining walls guide, structural hardscaping MN, natural stone wall construction, retaining wall drainage, Minneapolis masonry'
    },
    'post-symmetry.html': {
        'title': 'Symmetry in Botanical Compositions | The Elite 4 Journal MN',
        'desc': 'Discover how The Elite 4 utilizes geometric precision and architectural lines to create flawless botanical compositions for luxury Minnesota estates.',
        'keywords': 'botanical symmetry landscaping, geometric garden design MN, architectural planting guide, luxury estate landscaping Minnesota'
    }
}

# 2. CTA Button Replacements
cta_replacements = [
    # Book a Consultation
    (r'>Book a Consultation</a', r'>\n<span class="block text-base font-bold">Secure Your Consultation Slot <i class="fas fa-arrow-right ml-2"></i></span><span class="block text-[10px] font-normal uppercase tracking-wider opacity-90 mt-0.5">Guaranteed 48+ Hour Turnaround</span>\n</a'),
    # Request Consultation (where not already updated)
    (r'>Request Consultation</a', r'>\n<span class="block text-base font-bold">Request Consultation <i class="fas fa-arrow-right ml-2"></i></span><span class="block text-[10px] font-normal uppercase tracking-wider opacity-90 mt-0.5">Guaranteed 48+ Hour Turnaround</span>\n</a'),
    # Start Your Symmetrical Masterpiece
    (r'>Start Your Symmetrical Masterpiece</a', r'>\n<span class="block text-base font-bold">Start Your Symmetrical Masterpiece <i class="fas fa-arrow-right ml-2"></i></span><span class="block text-[10px] font-normal uppercase tracking-wider opacity-90 mt-0.5">Custom botanical engineering & layout</span>\n</a'),
    # Secure Your Property
    (r'>Secure Your Property</a', r'>\n<span class="block text-base font-bold">Secure Your Property <i class="fas fa-arrow-right ml-2"></i></span><span class="block text-[10px] font-normal uppercase tracking-wider opacity-90 mt-0.5">Grade stabilization & limestone walls</span>\n</a'),
    # Subscribe (in journal/blog)
    (r'>Subscribe</a', r'>\n<span class="block text-base font-bold">Subscribe To Journal <i class="fas fa-arrow-right ml-2"></i></span><span class="block text-[10px] font-normal uppercase tracking-wider opacity-90 mt-0.5">Receive private architectural briefings</span>\n</a'),
    # Contact Us (as CTA button)
    (r'class="([^"]*bg-brand-primary[^"]*)">Contact Us</a', r'class="\1">\n<span class="block text-base font-bold">Contact The Founders <i class="fas fa-arrow-right ml-2"></i></span><span class="block text-[10px] font-normal uppercase tracking-wider opacity-90 mt-0.5">Direct line to Gerald, Cole, Dom & Gerardo</span>\n</a'),
    # Submit Inquiry (in contact form)
    (r'>Submit Inquiry</a', r'>\n<span class="block text-base font-bold">Transmit Inquiry To Strike Force <i class="fas fa-arrow-right ml-2"></i></span><span class="block text-[10px] font-normal uppercase tracking-wider opacity-90 mt-0.5">Average response time: under 2 hours</span>\n</a'),
    # Read Journal
    (r'>Read Journal</a', r'>\n<span class="block text-base font-bold">Read Elite Journal <i class="fas fa-arrow-right ml-2"></i></span><span class="block text-[10px] font-normal uppercase tracking-wider opacity-90 mt-0.5">Explore field reports & deep dives</span>\n</a'),
    # Explore Services / Our Services (as CTA button)
    (r'class="([^"]*bg-brand-primary[^"]*)">(Explore Services|Our Services)</a', r'class="\1">\n<span class="block text-base font-bold">Explore Master Capabilities <i class="fas fa-arrow-right ml-2"></i></span><span class="block text-[10px] font-normal uppercase tracking-wider opacity-90 mt-0.5">View limestone, pool & patio specifications</span>\n</a'),
    # Get Started
    (r'>Get Started</a', r'>\n<span class="block text-base font-bold">Initiate Your Deployment <i class="fas fa-arrow-right ml-2"></i></span><span class="block text-[10px] font-normal uppercase tracking-wider opacity-90 mt-0.5">Lock in your weekend strike schedule</span>\n</a'),
    # Back to Journal
    (r'>Back to Journal</a', r'>\n<span class="block text-base font-bold"><i class="fas fa-arrow-left mr-2"></i> Return To Journal</span><span class="block text-[10px] font-normal uppercase tracking-wider opacity-90 mt-0.5">Explore more architectural insights</span>\n</a'),
    # Read Article
    (r'>Read Article</a', r'>\n<span class="block text-base font-bold">Read Full Architectural Briefing <i class="fas fa-arrow-right ml-2"></i></span><span class="block text-[10px] font-normal uppercase tracking-wider opacity-90 mt-0.5">Estimated reading time: 4 minutes</span>\n</a'),
    # Lock In This Rate
    (r'>\s*Lock In This Rate →\s*</a', r'>\n<span class="block text-base font-bold">Lock In This Rate <i class="fas fa-arrow-right ml-2"></i></span><span class="block text-[10px] font-normal uppercase tracking-wider opacity-90 mt-0.5">Secure weekend slot with $500 refundable deposit</span>\n</a')
]

for filepath in glob.glob(os.path.join(base_dir, '*.html')):
    filename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Apply SEO Metadata Overhaul
    if filename in seo_mappings:
        seo = seo_mappings[filename]
        # Build comprehensive SEO block
        seo_block = f"""<title>{seo['title']}</title>
    <meta name="description" content="{seo['desc']}"/>
    <meta name="keywords" content="{seo['keywords']}"/>
    <meta name="author" content="The Elite 4"/>
    <meta name="robots" content="index, follow"/>
    <meta property="og:title" content="{seo['title']}"/>
    <meta property="og:description" content="{seo['desc']}"/>
    <meta property="og:type" content="website"/>
    <meta property="og:url" content="https://elite4landscaping.com/{filename}"/>
    <meta property="og:image" content="https://elite4landscaping.com/8k_luxury_garden.png"/>
    <meta name="twitter:card" content="summary_large_image"/>
    <meta name="twitter:title" content="{seo['title']}"/>
    <meta name="twitter:description" content="{seo['desc']}"/>
    <link rel="canonical" href="https://elite4landscaping.com/{filename}"/>"""

        # Replace existing title and any existing meta description/keywords
        # First remove any existing meta description/keywords/canonical to avoid duplicates
        content = re.sub(r'<meta[^>]*name="description"[^>]*>\s*', '', content)
        content = re.sub(r'<meta[^>]*name="keywords"[^>]*>\s*', '', content)
        content = re.sub(r'<meta[^>]*name="author"[^>]*>\s*', '', content)
        content = re.sub(r'<meta[^>]*name="robots"[^>]*>\s*', '', content)
        content = re.sub(r'<meta[^>]*property="og:[^>]*>\s*', '', content)
        content = re.sub(r'<meta[^>]*name="twitter:[^>]*>\s*', '', content)
        content = re.sub(r'<link[^>]*rel="canonical"[^>]*>\s*', '', content)

        # Replace title tag with the full seo block
        content = re.sub(r'<title>[^<]*</title>', seo_block, content)

    # 2. Apply CTA Button Replacements
    for old_pat, new_sub in cta_replacements:
        content = re.sub(old_pat, new_sub, content)

    # 3. Unique Subtitles for 8K Showcase Cards
    # Card 1
    content = content.replace(
        '<h3 class="font-heading font-black text-xl text-brand-dark mb-3">Sunset Estate Garden</h3>\n                        <p class="text-brand-gray text-sm mb-6 leading-relaxed">Symmetrical botanical compositions framed by precision limestone retaining walls and warm recessed architectural lighting.</p>\n                    </div>\n                    <a href="portfolio.html" class="inline-block bg-brand-light hover:bg-brand-primary hover:text-white text-brand-primary font-bold py-3 px-6 rounded-full text-xs uppercase tracking-wider transition text-center shadow-sm">\n                        Inspect 8K Masterwork →\n                    </a>',
        '<h3 class="font-heading font-black text-xl text-brand-dark mb-3">Sunset Estate Garden</h3>\n                        <p class="text-brand-gray text-sm mb-6 leading-relaxed">Symmetrical botanical compositions framed by precision limestone retaining walls and warm recessed architectural lighting.</p>\n                    </div>\n                    <a href="portfolio.html" class="inline-block bg-brand-light hover:bg-brand-primary hover:text-white text-brand-primary font-bold py-3 px-6 rounded-full text-xs uppercase tracking-wider transition text-center shadow-sm">\n                        <span class="block text-xs font-bold uppercase tracking-wider">Inspect 8K Masterwork <i class="fas fa-arrow-right ml-1"></i></span><span class="block text-[9px] font-normal uppercase tracking-wider opacity-80 mt-0.5">Explore limestone retaining wall specs</span>\n                    </a>'
    )
    # Card 2
    content = content.replace(
        '<h3 class="font-heading font-black text-xl text-brand-dark mb-3">Premium Living Patio</h3>\n                        <p class="text-brand-gray text-sm mb-6 leading-relaxed">Fully integrated modern outdoor kitchen, sleek geometric fire pit, and flawless stone masonry completed in a single weekend.</p>\n                    </div>\n                    <a href="portfolio.html" class="inline-block bg-brand-primary hover:bg-green-600 text-white font-bold py-3 px-6 rounded-full text-xs uppercase tracking-wider transition text-center shadow-lg">\n                        Inspect 8K Masterwork →\n                    </a>',
        '<h3 class="font-heading font-black text-xl text-brand-dark mb-3">Premium Living Patio</h3>\n                        <p class="text-brand-gray text-sm mb-6 leading-relaxed">Fully integrated modern outdoor kitchen, sleek geometric fire pit, and flawless stone masonry completed in a single weekend.</p>\n                    </div>\n                    <a href="portfolio.html" class="inline-block bg-brand-primary hover:bg-green-600 text-white font-bold py-3 px-6 rounded-full text-xs uppercase tracking-wider transition text-center shadow-lg">\n                        <span class="block text-xs font-bold uppercase tracking-wider">Inspect 8K Masterwork <i class="fas fa-arrow-right ml-1"></i></span><span class="block text-[9px] font-normal uppercase tracking-wider opacity-80 mt-0.5">View outdoor kitchen masonry details</span>\n                    </a>'
    )
    # Card 3
    content = content.replace(
        '<h3 class="font-heading font-black text-xl text-brand-dark mb-3">Luminous Infinity Pool</h3>\n                        <p class="text-brand-gray text-sm mb-6 leading-relaxed">Glowing geometric infinity pool scape overlooking tranquil waters, engineered with clinical minimalist luxury landscaping.</p>\n                    </div>\n                    <a href="portfolio.html" class="inline-block bg-brand-light hover:bg-brand-primary hover:text-white text-brand-primary font-bold py-3 px-6 rounded-full text-xs uppercase tracking-wider transition text-center shadow-sm">\n                        Inspect 8K Masterwork →\n                    </a>',
        '<h3 class="font-heading font-black text-xl text-brand-dark mb-3">Luminous Infinity Pool</h3>\n                        <p class="text-brand-gray text-sm mb-6 leading-relaxed">Glowing geometric infinity pool scape overlooking tranquil waters, engineered with clinical minimalist luxury landscaping.</p>\n                    </div>\n                    <a href="portfolio.html" class="inline-block bg-brand-light hover:bg-brand-primary hover:text-white text-brand-primary font-bold py-3 px-6 rounded-full text-xs uppercase tracking-wider transition text-center shadow-sm">\n                        <span class="block text-xs font-bold uppercase tracking-wider">Inspect 8K Masterwork <i class="fas fa-arrow-right ml-1"></i></span><span class="block text-[9px] font-normal uppercase tracking-wider opacity-80 mt-0.5">Examine geometric pool engineering</span>\n                    </a>'
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully optimized SEO & CTAs for {filename}")

print("\nAll website pages have been fully SEO optimized and all CTAs enriched with unique information!")
