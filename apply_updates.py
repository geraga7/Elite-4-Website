import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Spacing hero banner & header
html = html.replace('<header class="bg-brand-light pt-20 pb-32 px-6 md:px-12 relative curved-bottom overflow-hidden">', 
                    '<header class="cinematic-bg pt-40 pb-32 px-6 md:px-12 relative curved-bottom overflow-hidden mt-8">')
html = html.replace('<nav class="bg-white py-4 px-6 md:px-12 flex justify-between items-center shadow-sm sticky top-0 z-50">',
                    '<nav class="bg-white/95 backdrop-blur-md py-4 px-6 md:px-12 flex justify-between items-center shadow-md sticky top-0 z-50">')

# 2. Add Schema Markup & SEO tags
schema = """
    <!-- Schema Markup -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "LandscapeProfessionals",
      "name": "The Elite 4",
      "image": "https://elite4landscaping.com/8k_luxury_garden.png",
      "@id": "",
      "url": "https://elite4landscaping.com",
      "telephone": "+16125550198",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "100 Luxury Lane",
        "addressLocality": "Minneapolis",
        "addressRegion": "MN",
        "postalCode": "55401",
        "addressCountry": "US"
      },
      "areaServed": ["Minneapolis", "Saint Paul", "Edina", "Wayzata", "Minnetonka", "River Falls, WI"],
      "priceRange": "$$$$"
    }
    </script>
"""
if "application/ld+json" not in html:
    html = html.replace('</head>', schema + '\n</head>')

# 3. Add cinematic styles & background animation
cinematic_styles = """
/* Cinematic & Animation Styles */
@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
.cinematic-bg {
    background: linear-gradient(-45deg, #e8f3ec, #ffffff, #d1e8d9, #f0fdf4);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
}
.cinematic-overlay {
    background: linear-gradient(to bottom, rgba(15, 74, 35, 0.2) 0%, rgba(0,0,0,0.6) 100%);
    mix-blend-mode: multiply;
}
.depth-of-field {
    filter: drop-shadow(0 25px 35px rgba(0,0,0,0.25));
}
.atmospheric-lighting {
    background: radial-gradient(circle at 50% 50%, rgba(255,255,255,0.15) 0%, rgba(0,0,0,0.5) 100%);
}
.float-cta {
    position: fixed;
    bottom: 30px;
    left: 30px;
    z-index: 150;
    animation: float 3s ease-in-out infinite;
}
@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0px); }
}
"""
html = html.replace('</style>', cinematic_styles + '\n</style>', 1)

# 4. Add new images & information to Gallery
new_gallery = """
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mt-6">
                <div class="relative group rounded-3xl overflow-hidden h-[400px] scroll-reveal shadow-2xl">
                    <img src="./firepit_lounge.png" alt="Firepit Lounge" class="w-full h-full object-cover group-hover:scale-110 transition duration-700"/>
                    <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent"></div>
                    <div class="absolute bottom-6 left-1/2 transform -translate-x-1/2 bg-white/95 backdrop-blur-sm py-3 px-8 rounded-full shadow-2xl whitespace-nowrap">
                        <span class="font-bold text-brand-dark">Firepit Lounges</span>
                    </div>
                </div>
                <div class="relative group rounded-3xl overflow-hidden h-[400px] scroll-reveal shadow-2xl">
                    <img src="./outdoor_kitchen.png" alt="Outdoor Kitchen" class="w-full h-full object-cover group-hover:scale-110 transition duration-700"/>
                    <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent"></div>
                    <div class="absolute bottom-6 left-1/2 transform -translate-x-1/2 bg-white/95 backdrop-blur-sm py-3 px-8 rounded-full shadow-2xl whitespace-nowrap">
                        <span class="font-bold text-brand-dark">Outdoor Kitchens</span>
                    </div>
                </div>
                <div class="relative group rounded-3xl overflow-hidden h-[400px] scroll-reveal shadow-2xl">
                    <img src="./garden_walkway.png" alt="Garden Walkway" class="w-full h-full object-cover group-hover:scale-110 transition duration-700"/>
                    <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent"></div>
                    <div class="absolute bottom-6 left-1/2 transform -translate-x-1/2 bg-white/95 backdrop-blur-sm py-3 px-8 rounded-full shadow-2xl whitespace-nowrap">
                        <span class="font-bold text-brand-dark">Garden Walkways</span>
                    </div>
                </div>
            </div>
"""
# Find the end of the first gallery grid and insert the new one
html = re.sub(r'(<span class="font-bold text-brand-dark">Luxury Patios</span>\s*</div>\s*</div>\s*</div>)', r'\1\n' + new_gallery, html)

# 5. Nav active state
html = html.replace('<a href="index.html" class="text-brand-primary">Home</a>', '<a href="index.html" class="text-white bg-brand-primary px-5 py-2.5 rounded-full shadow-lg font-bold hover:bg-green-600 transition">Home</a>')

# 6. Additional floating CTA
floating_cta = """
    <!-- Floating Left CTA -->
    <a href="contact.html" class="float-cta bg-brand-dark text-white px-6 py-4 rounded-full shadow-2xl flex items-center gap-3 hover:scale-105 transition-transform border-2 border-brand-primary">
        <i class="fas fa-calendar-check text-brand-primary text-xl"></i>
        <div class="flex flex-col">
            <span class="text-sm font-bold">Book 48h Strike</span>
            <span class="text-[10px] text-gray-300 uppercase tracking-wider">Available Weekends</span>
        </div>
    </a>
"""
if "<!-- Floating Left CTA -->" not in html:
    html = html.replace('</body>', floating_cta + '\n</body>')

# Write back
with open('index.html', 'w') as f:
    f.write(html)

print("Massive upgrade applied successfully!")
