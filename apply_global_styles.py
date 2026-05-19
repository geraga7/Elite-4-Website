import os
import glob
import re

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

files = glob.glob('*.html')

for filepath in files:
    filename = os.path.basename(filepath)
    with open(filepath, 'r') as f:
        html = f.read()

    # Add schema
    if "application/ld+json" not in html:
        html = html.replace('</head>', schema + '\n</head>')

    # Add cinematic styles (only if not already there)
    if "/* Cinematic & Animation Styles */" not in html:
        html = html.replace('</style>', cinematic_styles + '\n</style>', 1)
        
    # Update Navbar wrapper
    html = html.replace('<nav class="bg-white py-4 px-6 md:px-12 flex justify-between items-center shadow-sm sticky top-0 z-50">',
                        '<nav class="bg-white/95 backdrop-blur-md py-4 px-6 md:px-12 flex justify-between items-center shadow-md sticky top-0 z-50">')

    # Update active nav item
    nav_links = {
        'index.html': 'Home',
        'about.html': 'About Us',
        'services.html': 'Services',
        'portfolio.html': 'Portfolio',
        'process.html': 'Process',
        'journal.html': 'Journal'
    }
    
    # Reset all links to default first to avoid double replacing
    for href, text in nav_links.items():
        # find the active one and turn it back to normal (in case script runs multiple times)
        active_pattern = f'<a href="{href}" class="text-white bg-brand-primary px-5 py-2.5 rounded-full shadow-lg font-bold hover:bg-green-600 transition">{text}</a>'
        normal_pattern = f'<a href="{href}" class="hover:text-brand-primary transition">{text}</a>'
        html = html.replace(active_pattern, normal_pattern)
        
        # also handle the index.html case which had a different class initially
        html = html.replace(f'<a href="{href}" class="text-brand-primary">{text}</a>', normal_pattern)

    # Now set the active one
    if filename in nav_links:
        href = filename
        text = nav_links[filename]
        normal_pattern = f'<a href="{href}" class="hover:text-brand-primary transition">{text}</a>'
        active_pattern = f'<a href="{href}" class="text-white bg-brand-primary px-5 py-2.5 rounded-full shadow-lg font-bold hover:bg-green-600 transition">{text}</a>'
        html = html.replace(normal_pattern, active_pattern)

    # Update inner headers
    if filename != 'index.html':
        # Replace normal inner page header classes with cinematic-bg
        # Look for headers like: <header class="bg-brand-light pt-32 pb-24 px-6 md:px-12 text-center curved-bottom">
        html = re.sub(r'<header class="bg-brand-light pt-\d+ pb-\d+', r'<header class="cinematic-bg pt-40 pb-24 mt-8', html)

    # Add floating CTA
    if "<!-- Floating Left CTA -->" not in html:
        html = html.replace('</body>', floating_cta + '\n</body>')

    with open(filepath, 'w') as f:
        f.write(html)

print("Applied global styles and active nav states to all HTML files.")
