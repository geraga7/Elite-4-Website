import os
import glob
import re

def fix_mobile_menu():
    files = glob.glob('/Users/user/Documents/Elite 4/*.html')
    
    for f in files:
        with open(f, 'r') as file:
            content = file.read()
            
        # Replace the broken mobile menu overlay with a fixed, scrollable, solid background one
        
        # We need to find the entire div id="mobile-menu"
        # It starts with: <div id="mobile-menu" class="fixed inset-0 bg-[#f6f6f5] z-[100] flex flex-col justify-center items-center gap-8 hidden opacity-0 transition-opacity duration-300">
        # And ends with the </div> before </nav>
        
        pattern = re.compile(r'<div id="mobile-menu".*?</div>\s*</nav>', re.DOTALL)
        
        new_menu = """<div id="mobile-menu" class="fixed inset-0 bg-[#2d2f2e] z-[100] flex flex-col items-center pt-24 pb-12 overflow-y-auto hidden opacity-0 transition-opacity duration-300">
    <button id="close-menu-button" class="absolute top-6 right-6 text-[#c3f7d3] p-2 hover:rotate-90 transition-transform">
        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="block">
            <line x1="18" y1="6" x2="6" y2="18"></line>
            <line x1="6" y1="6" x2="18" y2="18"></line>
        </svg>
    </button>
    <div class="flex flex-col items-center gap-10 w-full min-h-max my-auto">
        <a class="font-['Epilogue'] text-3xl md:text-5xl font-black uppercase tracking-widest text-white hover:text-[#c3f7d3] transition-colors" href="index.html">Home</a>
        <a class="font-['Epilogue'] text-3xl md:text-5xl font-black uppercase tracking-widest text-white hover:text-[#c3f7d3] transition-colors" href="about.html">About Us</a>
        <a class="font-['Epilogue'] text-3xl md:text-5xl font-black uppercase tracking-widest text-white hover:text-[#c3f7d3] transition-colors" href="services.html">Services</a>
        <a class="font-['Epilogue'] text-3xl md:text-5xl font-black uppercase tracking-widest text-white hover:text-[#c3f7d3] transition-colors" href="portfolio.html">Portfolio</a>
        <a class="font-['Epilogue'] text-3xl md:text-5xl font-black uppercase tracking-widest text-white hover:text-[#c3f7d3] transition-colors" href="process.html">Process</a>
        <a class="font-['Epilogue'] text-3xl md:text-5xl font-black uppercase tracking-widest text-white hover:text-[#c3f7d3] transition-colors" href="journal.html">Journal</a>
        <a href="contact.html" class="mt-6 bg-[#c3f7d3] text-[#1e4d33] px-10 py-5 rounded-md font-['Epilogue'] font-black text-sm uppercase tracking-widest shadow-lg text-center hover:scale-105 transition-transform">
            Request Consultation
        </a>
    </div>
</div>
</nav>"""
        
        new_content = pattern.sub(new_menu, content)
        
        with open(f, 'w') as file:
            file.write(new_content)

    print("Mobile menu overlay fixed successfully.")

if __name__ == "__main__":
    fix_mobile_menu()
