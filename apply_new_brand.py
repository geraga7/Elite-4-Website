import glob
import re

new_cinematic_bg = """
.cinematic-bg {
    background: radial-gradient(at 0% 0%, rgba(18,166,56,0.15) 0px, transparent 50%),
                radial-gradient(at 100% 0%, rgba(15,74,35,0.1) 0px, transparent 50%),
                radial-gradient(at 100% 100%, rgba(18,166,56,0.15) 0px, transparent 50%),
                radial-gradient(at 0% 100%, rgba(255,255,255,1) 0px, transparent 50%),
                #f8fbf9;
    background-size: 200% 200%;
    animation: gradientBG 15s ease infinite;
}
"""

logo_html = """
        <a href="index.html" class="flex items-center gap-3">
            <img src="./logo.jpg" alt="4 Elite Landscapers Logo" class="h-12 w-12 md:h-14 md:w-14 rounded-full border-2 border-brand-primary shadow-md hover:scale-105 transition-transform object-cover"/>
            <span class="font-heading font-black text-xl md:text-2xl text-brand-dark uppercase tracking-tight">4 Elite Landscapers</span>
        </a>
"""

footer_logo_html = """
                <a href="index.html" class="flex items-center gap-3 mb-6">
                    <img src="./logo.jpg" alt="4 Elite Landscapers Logo" class="h-10 w-10 rounded-full border border-brand-primary shadow-sm object-cover"/>
                    <span class="font-heading font-black text-xl uppercase tracking-tight text-white">4 Elite Landscapers</span>
                </a>
"""

files = glob.glob('*.html')

for filepath in files:
    with open(filepath, 'r') as f:
        html = f.read()

    # 1. Replace the CSS for cinematic-bg
    html = re.sub(r'\.cinematic-bg\s*\{[^}]+\}', new_cinematic_bg.strip(), html)

    # 2. Replace the main text "The Elite 4" -> "4 Elite Landscapers"
    # Be careful not to replace it in URLs or attributes if possible, but mostly it's safe in text
    html = html.replace('The Elite 4', '4 Elite Landscapers')
    html = html.replace('the elite 4', '4 elite landscapers')
    html = html.replace('THE ELITE 4', '4 ELITE LANDSCAPERS')

    # 3. Replace Navbar Logo
    # Usually looks like:
    # <a href="index.html" class="flex items-center gap-2">
    #     <i class="fas fa-leaf text-brand-primary text-3xl"></i>
    #     <span class="font-heading font-black text-2xl text-brand-dark uppercase tracking-tight">4 Elite Landscapers</span>
    # </a>
    nav_logo_pattern = r'<a href="index\.html" class="flex items-center gap-2">\s*<i class="fas fa-leaf[^>]+></i>\s*<span class="font-heading[^>]+>4 Elite Landscapers</span>\s*</a>'
    html = re.sub(nav_logo_pattern, logo_html.strip(), html, count=1)

    # 4. Replace Footer Logo
    # Looks like:
    # <a href="index.html" class="flex items-center gap-2 mb-6">
    #     <i class="fas fa-leaf text-brand-primary text-3xl"></i>
    #     <span class="font-heading font-black text-2xl uppercase tracking-tight">4 Elite Landscapers</span>
    # </a>
    footer_logo_pattern = r'<a href="index\.html" class="flex items-center gap-2 mb-6">\s*<i class="fas fa-leaf[^>]+></i>\s*<span class="font-heading[^>]+>4 Elite Landscapers</span>\s*</a>'
    html = re.sub(footer_logo_pattern, footer_logo_html.strip(), html)

    with open(filepath, 'w') as f:
        f.write(html)

print("Applied new brand, logo, and modern background effect to all HTML files.")
