import os
import glob
import re

base_dir = '/Users/user/Documents/Elite 4'

mobile_menu_overlay = """
    <!-- Mobile Menu Overlay -->
    <div id="mobile-menu" class="fixed inset-0 bg-white z-[100] flex flex-col pt-24 pb-12 px-8 overflow-y-auto hidden opacity-0 transition-opacity duration-300">
        <button id="close-menu-btn" class="absolute top-6 right-6 text-brand-dark text-3xl hover:text-brand-primary transition-colors">
            <i class="fas fa-times"></i>
        </button>
        <div class="flex flex-col gap-8 w-full mt-10">
            <a class="font-heading text-3xl font-black uppercase text-brand-dark hover:text-brand-primary transition-colors" href="index.html">Home</a>
            <a class="font-heading text-3xl font-black uppercase text-brand-dark hover:text-brand-primary transition-colors" href="about.html">About Us</a>
            <a class="font-heading text-3xl font-black uppercase text-brand-dark hover:text-brand-primary transition-colors" href="services.html">Services</a>
            <a class="font-heading text-3xl font-black uppercase text-brand-dark hover:text-brand-primary transition-colors" href="portfolio.html">Portfolio</a>
            <a class="font-heading text-3xl font-black uppercase text-brand-dark hover:text-brand-primary transition-colors" href="process.html">Process</a>
            <a class="font-heading text-3xl font-black uppercase text-brand-dark hover:text-brand-primary transition-colors" href="journal.html">Journal</a>
            <a href="contact.html" class="mt-6 bg-brand-primary text-white px-8 py-4 rounded-full font-bold text-center shadow-lg">Request Consultation</a>
        </div>
    </div>
"""

mobile_js = """
    <!-- Custom JS -->
    <script>
        // Mobile Menu
        const mobileBtn = document.getElementById('mobile-menu-btn');
        const closeBtn = document.getElementById('close-menu-btn');
        const mobileMenu = document.getElementById('mobile-menu');
        
        if (mobileBtn && closeBtn && mobileMenu) {
            mobileBtn.addEventListener('click', () => {
                mobileMenu.classList.remove('hidden');
                setTimeout(() => mobileMenu.classList.remove('opacity-0'), 10);
                document.body.style.overflow = 'hidden';
            });
            closeBtn.addEventListener('click', () => {
                mobileMenu.classList.add('opacity-0');
                setTimeout(() => mobileMenu.classList.add('hidden'), 300);
                document.body.style.overflow = '';
            });
        }
    </script>
"""

for filename in glob.glob(os.path.join(base_dir, '*.html')):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add id="mobile-menu-btn" to the hamburger button if it doesn't have it
    content = re.sub(r'<button class="lg:hidden text-brand-dark text-2xl">', r'<button id="mobile-menu-btn" class="lg:hidden text-brand-dark text-2xl">', content)
    
    # 2. Insert Mobile Menu Overlay right after </nav> if not exists
    if 'id="mobile-menu"' not in content:
        content = content.replace('</nav>', '</nav>\n' + mobile_menu_overlay)
        
    # 3. Insert Custom JS before <!-- AI Concierge Widget --> if not exists
    if '// Mobile Menu' not in content:
        content = content.replace('<!-- AI Concierge Widget -->', mobile_js + '\n    <!-- AI Concierge Widget -->')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed mobile menu interaction on all pages.")
