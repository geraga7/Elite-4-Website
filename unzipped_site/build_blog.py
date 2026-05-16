import os
import glob
import re

base_dir = '/Users/user/Documents/Elite 4'

# 1. Grab header and footer from index.html to wrap our posts
with open(os.path.join(base_dir, 'index.html'), 'r', encoding='utf-8') as f:
    idx_content = f.read()

head_match = re.search(r'(<!DOCTYPE html>.*?</nav>)', idx_content, re.DOTALL)
footer_match = re.search(r'(<footer.*</html>)', idx_content, re.DOTALL)
chatbot_match = re.search(r'(<!-- AI Concierge Widget -->.*?</script>)', idx_content, re.DOTALL)
mobile_menu_match = re.search(r'(<div id="mobile-menu".*?</div>)', idx_content, re.DOTALL)

header_html = head_match.group(1) if head_match else ""
if mobile_menu_match and '<div id="mobile-menu"' not in header_html:
    header_html += "\n" + mobile_menu_match.group(1)
footer_html = footer_match.group(1) if footer_match else ""

# 2. Define post contents
post_symmetry_main = """
<main class="w-full pt-32 pb-20 px-6 max-w-4xl mx-auto">
    <div class="mb-10 text-center">
        <span class="font-sans text-xs uppercase tracking-widest text-brand-primary mb-4 block font-bold">Design Theory</span>
        <h1 class="font-heading text-4xl md:text-6xl font-bold mb-6 text-brand-dark">The Importance of Symmetry in Luxury Hardscapes</h1>
        <p class="text-brand-gray text-sm">By Gerald • Oct 12, 2026</p>
    </div>
    <div class="w-full h-[400px] rounded-3xl overflow-hidden mb-12 shadow-2xl">
        <img src="./luxury_patio.webp" alt="Luxury Patio Symmetry" class="w-full h-full object-cover">
    </div>
    <div class="prose prose-lg max-w-none text-brand-gray space-y-6">
        <p>In the realm of elite landscaping, beauty is not random. It is mathematically calculated. True luxury relies on geometric precision and an unwavering commitment to balance.</p>
        <p>When our Strike Force arrives on site, the very first thing we analyze is the visual weight of your property. We don't just lay stone; we create an architectural extension of your home. By utilizing high-end Tier-1 materials and ensuring perfectly symmetrical cuts, we guarantee a flawless execution that immediately elevates your property's prestige.</p>
        <p>A symmetrical patio isn't just visually stunning; it implies order, permanence, and clinical perfection. That is the Elite 4 standard.</p>
    </div>
    <div class="mt-16 text-center border-t border-gray-100 pt-12">
        <a href="contact.html" class="inline-block bg-brand-primary text-white px-8 py-4 rounded-full font-bold hover:bg-green-600 transition shadow-lg">Start Your Symmetrical Masterpiece</a>
    </div>
</main>
"""

post_retaining_main = """
<main class="w-full pt-32 pb-20 px-6 max-w-4xl mx-auto">
    <div class="mb-10 text-center">
        <span class="font-sans text-xs uppercase tracking-widest text-brand-primary mb-4 block font-bold">Engineering</span>
        <h1 class="font-heading text-4xl md:text-6xl font-bold mb-6 text-brand-dark">The Anatomy of a Tier-1 Retaining Wall</h1>
        <p class="text-brand-gray text-sm">By Cole • Sep 28, 2026</p>
    </div>
    <div class="w-full h-[400px] rounded-3xl overflow-hidden mb-12 shadow-2xl">
        <img src="./retaining_wall.webp" alt="Retaining Wall" class="w-full h-full object-cover">
    </div>
    <div class="prose prose-lg max-w-none text-brand-gray space-y-6">
        <p>A retaining wall is the unsung hero of landscape architecture. While it serves a critical structural purpose—holding back tons of earth—it must also act as a striking visual feature.</p>
        <p>We refuse to build standard block walls. We utilize imported limestone, massive boulder formations, and precisely engineered drainage systems to ensure your wall lasts for generations. During our 48+ hour strikes, we employ heavy excavation to dig deep footings, ensuring zero movement even during harsh Minnesota winters.</p>
        <p>Never compromise on engineering. A failing wall is a liability; an Elite 4 wall is a fortress of beauty.</p>
    </div>
    <div class="mt-16 text-center border-t border-gray-100 pt-12">
        <a href="contact.html" class="inline-block bg-brand-primary text-white px-8 py-4 rounded-full font-bold hover:bg-green-600 transition shadow-lg">Secure Your Property</a>
    </div>
</main>
"""

with open(os.path.join(base_dir, 'post-symmetry.html'), 'w', encoding='utf-8') as f:
    f.write(header_html + "\n" + post_symmetry_main + "\n" + footer_html)

with open(os.path.join(base_dir, 'post-retaining-walls.html'), 'w', encoding='utf-8') as f:
    f.write(header_html + "\n" + post_retaining_main + "\n" + footer_html)

# 3. Update journal.html content to list both posts
journal_main = """
<main class="w-full">
    <header class="relative min-h-screen flex flex-col md:flex-row pt-20">
        <div class="w-full md:w-1/2 flex flex-col justify-center px-8 md:px-20 py-20 bg-brand-light">
            <div class="max-w-xl">
                <span class="font-sans text-xs uppercase tracking-[0.2em] text-brand-primary font-bold mb-4 block">Field Reports</span>
                <h1 class="font-heading text-5xl md:text-7xl font-extrabold text-brand-dark leading-[1.1] tracking-tighter mb-8">
                    Landscaping <span class='text-brand-primary italic'>Insights.</span>
                </h1>
                <p class="text-lg text-brand-gray leading-relaxed mb-12 max-w-lg">
                    Stay informed with the latest developments in luxury landscape architecture. The Elite 4 shares our expertise on hardscape construction.
                </p>
                <div class="flex flex-wrap gap-6">
                    <a href="contact.html" class="inline-block bg-brand-primary text-white px-8 py-4 rounded-md font-heading font-bold text-sm uppercase tracking-widest hover:translate-y-[-2px] transition-transform shadow-lg shadow-[#366549]/20">Subscribe</a>
                </div>
            </div>
        </div>
        <div class="w-full md:w-1/2 relative min-h-[500px] overflow-hidden">
            <img src="./hero-pathway.webp" alt="Landscape" loading="lazy" class="absolute inset-0 w-full h-full object-cover"/>
            <div class="absolute inset-0 bg-gradient-to-r from-[#f6f6f5]/20 to-transparent"></div>
        </div>
    </header>
    
    <section class="py-24 bg-brand-light px-8">
        <div class="max-w-5xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12">
            <!-- Post 1 -->
            <div class="bg-white/80 p-10 rounded-xl shadow-lg border-t-4 border-[#705900] hover:-translate-y-2 transition-transform duration-300">
                <div class="h-48 rounded-lg overflow-hidden mb-6"><img src="./luxury_patio.webp" class="w-full h-full object-cover"/></div>
                <span class="font-sans text-xs uppercase tracking-widest text-brand-primary mb-4 block font-bold">Design Theory</span>
                <h3 class="font-heading text-3xl font-bold mb-4 text-brand-dark">The Importance of Symmetry in Luxury Hardscapes</h3>
                <p class="text-brand-gray mb-6">Why true luxury relies on geometric precision and mathematical balance...</p>
                <a href="post-symmetry.html" class="font-heading text-sm font-bold text-brand-primary uppercase tracking-widest hover:text-brand-dark">Read Full Post &rarr;</a>
            </div>
            
            <!-- Post 2 -->
            <div class="bg-white/80 p-10 rounded-xl shadow-lg border-t-4 border-[#705900] hover:-translate-y-2 transition-transform duration-300">
                <div class="h-48 rounded-lg overflow-hidden mb-6"><img src="./retaining_wall.webp" class="w-full h-full object-cover"/></div>
                <span class="font-sans text-xs uppercase tracking-widest text-brand-primary mb-4 block font-bold">Engineering</span>
                <h3 class="font-heading text-3xl font-bold mb-4 text-brand-dark">The Anatomy of a Tier-1 Retaining Wall</h3>
                <p class="text-brand-gray mb-6">We utilize imported limestone and massive boulder formations to ensure your wall lasts for generations...</p>
                <a href="post-retaining-walls.html" class="font-heading text-sm font-bold text-brand-primary uppercase tracking-widest hover:text-brand-dark">Read Full Post &rarr;</a>
            </div>
        </div>
    </section>
</main>
"""

with open(os.path.join(base_dir, 'journal.html'), 'w', encoding='utf-8') as f:
    f.write(header_html + "\n" + journal_main + "\n" + footer_html)

# 4. Update the footer links across all files
for filename in glob.glob(os.path.join(base_dir, '*.html')):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We will replace the Popular Posts block specifically if it exists.
    # The footers have things like:
    # <h5 class="text-sm font-bold group-hover:text-brand-primary transition leading-tight">Symmetry</h5> or The Importance of Symmetry
    # We just need to make sure the links are right. 
    # Let's replace href="journal.html" where it's wrapping the luxury_patio image with post-symmetry.html
    
    content = re.sub(r'<a href="journal\.html" class="flex gap-4 group">(\s*<img src="\./luxury_patio\.webp")', r'<a href="post-symmetry.html" class="flex gap-4 group">\1', content)
    content = re.sub(r'<a href="journal\.html" class="flex gap-4 group">(\s*<img src="\./retaining_wall\.webp")', r'<a href="post-retaining-walls.html" class="flex gap-4 group">\1', content)

    # Ensure mobile menu works on ALL pages by ensuring the button toggles #mobile-menu.
    # The javascript is already at the bottom of the HTML files from apply_new_design.py.

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Blog pages generated and links updated.")
