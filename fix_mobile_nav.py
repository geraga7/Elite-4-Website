import os
import glob
import re

new_nav = """<!-- TopNavBar -->
<nav class="fixed top-0 w-full z-50 bg-[#f6f6f5]/80 backdrop-blur-xl shadow-[0px_20px_40px_rgba(45,29,46,0.06)]">
<div class="flex justify-between items-center w-full px-6 md:px-12 py-4 md:py-6 max-w-[1920px] mx-auto">
    <a class="text-xl md:text-2xl font-black tracking-[-0.02em] text-[#366549] uppercase font-['Epilogue']" href="index.html">The Elite 4</a>
    
    <!-- Desktop Nav Links -->
    <div class="hidden md:flex gap-8 items-center">
        <a class="font-['Epilogue'] tracking-tighter font-bold uppercase text-sm text-[#575d5a] hover:text-[#366549] transition-colors hover:scale-[1.02]" href="index.html">Home</a>
        <a class="font-['Epilogue'] tracking-tighter font-bold uppercase text-sm text-[#575d5a] hover:text-[#366549] transition-colors hover:scale-[1.02]" href="about.html">About Us</a>
        <a class="font-['Epilogue'] tracking-tighter font-bold uppercase text-sm text-[#575d5a] hover:text-[#366549] transition-colors hover:scale-[1.02]" href="services.html">Services</a>
        <a class="font-['Epilogue'] tracking-tighter font-bold uppercase text-sm text-[#575d5a] hover:text-[#366549] transition-colors hover:scale-[1.02]" href="portfolio.html">Portfolio</a>
        <a class="font-['Epilogue'] tracking-tighter font-bold uppercase text-sm text-[#575d5a] hover:text-[#366549] transition-colors hover:scale-[1.02]" href="process.html">Process</a>
        <a class="font-['Epilogue'] tracking-tighter font-bold uppercase text-sm text-[#575d5a] hover:text-[#366549] transition-colors hover:scale-[1.02]" href="journal.html">Journal</a>
    </div>

    <!-- Desktop CTA -->
    <a href="contact.html" class="hidden md:inline-block bg-primary text-on-primary px-6 py-3 rounded-md font-['Epilogue'] font-bold text-xs uppercase tracking-widest scale-95 hover:scale-100 active:scale-90 transition-transform shadow-lg shadow-primary/20">
        Request Consultation
    </a>

    <!-- Mobile Menu Button -->
    <button id="mobile-menu-button" class="md:hidden text-primary p-2">
        <span class="material-symbols-outlined text-3xl">menu</span>
    </button>
</div>

<!-- Mobile Nav Overlay -->
<div id="mobile-menu" class="fixed inset-0 bg-surface z-40 flex flex-col justify-center items-center gap-8 hidden opacity-0 transition-opacity duration-300">
    <button id="close-menu-button" class="absolute top-6 right-6 text-primary p-2 hover:scale-110 transition-transform">
        <span class="material-symbols-outlined text-4xl">close</span>
    </button>
    <a class="font-['Epilogue'] text-2xl font-bold uppercase tracking-widest text-[#575d5a] hover:text-primary transition-colors" href="index.html">Home</a>
    <a class="font-['Epilogue'] text-2xl font-bold uppercase tracking-widest text-[#575d5a] hover:text-primary transition-colors" href="about.html">About Us</a>
    <a class="font-['Epilogue'] text-2xl font-bold uppercase tracking-widest text-[#575d5a] hover:text-primary transition-colors" href="services.html">Services</a>
    <a class="font-['Epilogue'] text-2xl font-bold uppercase tracking-widest text-[#575d5a] hover:text-primary transition-colors" href="portfolio.html">Portfolio</a>
    <a class="font-['Epilogue'] text-2xl font-bold uppercase tracking-widest text-[#575d5a] hover:text-primary transition-colors" href="process.html">Process</a>
    <a class="font-['Epilogue'] text-2xl font-bold uppercase tracking-widest text-[#575d5a] hover:text-primary transition-colors" href="journal.html">Journal</a>
    
    <a href="contact.html" class="mt-8 bg-primary text-on-primary px-8 py-4 rounded-md font-['Epilogue'] font-bold text-sm uppercase tracking-widest shadow-lg hover:scale-105 active:scale-95 transition-transform text-center">
        Request Consultation
    </a>
</div>
</nav>"""

mobile_script = """
<script>
    document.addEventListener('DOMContentLoaded', () => {
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
</body>"""

def fix_html_files():
    files = glob.glob('*.html')
    
    # 1. Regex to replace the entire <nav> block
    # We will search for <!-- TopNavBar --> ... </nav>
    nav_pattern = re.compile(r'<!-- TopNavBar -->\s*<nav.*?</nav>', re.DOTALL)
    
    # 2. Map of button texts to hrefs
    replacements = {
        r"View Portfolio": "portfolio.html",
        r"Our Process": "process.html",
        r"Join the Strike-Force": "contact.html",
        r"Read Field Report": "journal.html",
        r"Subscribe": "contact.html", # For the journal CTA
        r"Submit Inquiry": "contact.html" # For forms, though submit buttons should remain buttons if they submit. Let's exclude Submit Inquiry or let it be a button.
    }

    for f in files:
        with open(f, 'r') as file:
            content = file.read()
            
        # Replace nav
        content = nav_pattern.sub(new_nav, content)
        
        # Add mobile script before </body>
        if "<script>" not in content[-500:]:  # Check if we already added it
            content = content.replace("</body>", mobile_script)
            
        # Convert standalone buttons to anchors
        # Pattern looks for <button class="..."> \s* TEXT \s* </button>
        for btn_text, link in replacements.items():
            if btn_text == "Submit Inquiry": continue # Keep submit as button
            
            # Using regex to find buttons matching the text
            # We want to replace <button ...> TEXT </button> with <a href="..." class="inline-block text-center ..."> TEXT </a>
            pattern_str = r'(<button\s+[^>]*class="([^"]*)".*?>)\s*(' + btn_text + r')\s*(</button>)'
            
            def btn_replacer(match):
                classes = match.group(2)
                text = match.group(3)
                # ensure inline-block is there for <a>
                if "inline-block" not in classes and "block" not in classes and "flex" not in classes:
                    classes = "inline-block text-center " + classes
                else:
                    classes = "text-center " + classes
                
                # reconstruct as <a>
                return f'<a href="{link}" class="{classes}">{text}</a>'
            
            content = re.sub(pattern_str, btn_replacer, content, flags=re.DOTALL)
            
            # What about buttons that don't have a class attribute? (very rare here)
            # What about buttons where the text is mixed with spans or icons?
            # Example: Join the Strike-Force or Our Process
            # If the text is directly inside the button, it matches.

        # Another case: the footer has "Join the Strike-Force"
        
        # Another case: <div class="flex items-center gap-2 ..."> Read Field Report <span ...></span></div> in Journal
        # Journal has a div instead of a button. We can replace that div with an anchor.
        if "Read Field Report" in content:
            # We can just change the surrounding container manually or do a simple replace
            content = content.replace('<div class="flex items-center gap-2 text-tertiary font-bold font-label uppercase tracking-widest text-sm">', '<a href="journal.html" class="flex items-center gap-2 text-tertiary font-bold font-label uppercase tracking-widest text-sm hover:translate-x-2 transition-transform cursor-pointer">')
            content = content.replace('arrow_forward</span>\n</div>', 'arrow_forward</span>\n</a>')

        # Contact form action on contact.html
        if f == "contact.html":
            content = content.replace('<form class="space-y-6">', '<form action="#" method="POST" class="space-y-6">')

        with open(f, 'w') as file:
            file.write(content)
            
    print("All files updated successfully.")

if __name__ == "__main__":
    fix_html_files()
