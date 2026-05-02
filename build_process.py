import os

base_dir = '/Users/user/Documents/Elite 4'
process_path = os.path.join(base_dir, 'process.html')
index_path = os.path.join(base_dir, 'index.html')

# 1. Update index.html process text
with open(index_path, 'r', encoding='utf-8') as f:
    idx_content = f.read()

idx_content = idx_content.replace(
    "Friday 5 PM arrival with heavy machinery for excavation.",
    "Saturday 7:30 AM arrival with heavy machinery for precise excavation."
)
idx_content = idx_content.replace(
    "Massive Saturday deployment building the structural foundation.",
    "Relentless structural deployment operating from morning until dark."
)
idx_content = idx_content.replace(
    "Sunday completion. Absolute perfection delivered before sunset.",
    "Sunday completion or rollover to following weekend for perfection."
)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(idx_content)

# 2. Build the new Process.html
# We will extract the header and footer from the updated index.html
import re
head_match = re.search(r'(<!DOCTYPE html>.*?</nav>)', idx_content, re.DOTALL)
footer_match = re.search(r'(<footer.*</html>)', idx_content, re.DOTALL)
chatbot_match = re.search(r'(<!-- AI Concierge Widget -->.*?</script>)', idx_content, re.DOTALL)

header_html = head_match.group(1) if head_match else ""
footer_html = footer_match.group(1) if footer_match else ""

# Ensure mobile menu works in header
if '<div id="mobile-menu"' not in header_html:
    mobile_menu_match = re.search(r'(<div id="mobile-menu".*?</div>)', idx_content, re.DOTALL)
    if mobile_menu_match:
        header_html += "\n" + mobile_menu_match.group(1)

MAIN_CONTENT = """
    <!-- Process Hero -->
    <header class="bg-brand-light pt-20 pb-32 px-6 md:px-12 relative curved-bottom overflow-hidden">
        <div class="max-w-4xl mx-auto text-center relative z-10">
            <div class="flex items-center justify-center gap-2 text-brand-primary font-bold mb-4 uppercase tracking-widest text-sm">
                <i class="fas fa-hammer"></i>
                <span>The Anatomy of a Strike</span>
            </div>
            <h1 class="font-heading text-5xl md:text-7xl font-extrabold text-brand-dark leading-[1.1] mb-6">
                Our 48-Hour Guarantee
            </h1>
            <p class="text-brand-gray text-lg mb-8 leading-relaxed max-w-2xl mx-auto">
                We don't do drawn-out construction zones. We operate exclusively on weekends, starting at 7:30 AM. We execute with military precision to deliver perfection without disrupting your work week.
            </p>
            <a href="contact.html" class="inline-block bg-brand-primary text-white px-8 py-4 rounded-full font-bold hover:bg-green-600 transition shadow-lg shadow-green-500/30">Book a Consultation</a>
        </div>
        <svg class="absolute bottom-0 left-0 w-full" viewBox="0 0 1440 100" xmlns="http://www.w3.org/2000/svg"><path fill="#ffffff" d="M0,50 C320,150 420,-50 1440,50 L1440,100 L0,100 Z"></path></svg>
    </header>

    <!-- Step 1 -->
    <section class="py-20 px-6 max-w-7xl mx-auto relative">
        <div class="flex flex-col md:flex-row gap-16 items-center">
            <div class="w-full md:w-1/2 relative">
                <div class="absolute -inset-4 bg-brand-light blob-shape z-0"></div>
                <div class="relative z-10 blob-shape overflow-hidden border-8 border-white shadow-xl h-[400px]">
                    <img src="./image_consultation.png" alt="Consultation" class="w-full h-full object-cover"/>
                </div>
            </div>
            <div class="w-full md:w-1/2 space-y-6">
                <span class="text-brand-primary font-bold tracking-widest text-sm uppercase block">Step 01</span>
                <h2 class="font-heading text-4xl md:text-5xl font-bold text-brand-dark leading-tight">
                    The Consultation & Masterplan
                </h2>
                <p class="text-brand-gray leading-relaxed text-lg">
                    Before we ever break ground, we sit down with you to architect a masterplan. We discuss your vision, analyze your property's topography, and select the highest-grade Tier-1 materials. Every cut, every stone, and every plant is planned with absolute precision to ensure a flawless execution.
                </p>
            </div>
        </div>
    </section>

    <!-- Step 2 -->
    <section class="py-20 px-6 max-w-7xl mx-auto relative">
        <div class="flex flex-col md:flex-row-reverse gap-16 items-center">
            <div class="w-full md:w-1/2 relative">
                <div class="absolute -inset-4 bg-brand-light blob-shape-2 z-0"></div>
                <div class="relative z-10 blob-shape-2 overflow-hidden border-8 border-white shadow-xl h-[400px]">
                    <img src="./image_site_prep.png" alt="Site Prep" class="w-full h-full object-cover"/>
                </div>
            </div>
            <div class="w-full md:w-1/2 space-y-6">
                <span class="text-brand-primary font-bold tracking-widest text-sm uppercase block">Step 02</span>
                <h2 class="font-heading text-4xl md:text-5xl font-bold text-brand-dark leading-tight">
                    Saturday 7:30 AM: Site Prep
                </h2>
                <p class="text-brand-gray leading-relaxed text-lg">
                    We arrive early Saturday morning at exactly 7:30 AM with heavy machinery. We don't waste time. Our first priority is precise excavation and site preparation. We protect your existing landscape and property while rapidly clearing the canvas for your new architectural feature.
                </p>
            </div>
        </div>
    </section>

    <!-- Step 3 -->
    <section class="py-20 px-6 max-w-7xl mx-auto relative">
        <div class="flex flex-col md:flex-row gap-16 items-center">
            <div class="w-full md:w-1/2 relative">
                <div class="absolute -inset-4 bg-brand-light blob-shape z-0"></div>
                <div class="relative z-10 blob-shape overflow-hidden border-8 border-white shadow-xl h-[400px]">
                    <img src="./image_the_strike.png" alt="The Strike" class="w-full h-full object-cover"/>
                </div>
            </div>
            <div class="w-full md:w-1/2 space-y-6">
                <span class="text-brand-primary font-bold tracking-widest text-sm uppercase block">Step 03</span>
                <h2 class="font-heading text-4xl md:text-5xl font-bold text-brand-dark leading-tight">
                    The Weekend Strike
                </h2>
                <p class="text-brand-gray leading-relaxed text-lg">
                    This is where the magic happens. All four founders work in perfect unison. It is a relentless, synchronized deployment operating from morning until dark. We lay the structural foundation and begin the precision stone cuts. Because we only work weekends, we can focus 100% of our energy on your estate.
                </p>
            </div>
        </div>
    </section>

    <!-- Step 4 -->
    <section class="py-20 px-6 max-w-7xl mx-auto relative mb-20">
        <div class="flex flex-col md:flex-row-reverse gap-16 items-center">
            <div class="w-full md:w-1/2 relative">
                <div class="absolute -inset-4 bg-brand-light blob-shape-2 z-0"></div>
                <div class="relative z-10 blob-shape-2 overflow-hidden border-8 border-white shadow-xl h-[400px]">
                    <img src="./image_the_handover.png" alt="The Handover" class="w-full h-full object-cover"/>
                </div>
            </div>
            <div class="w-full md:w-1/2 space-y-6">
                <span class="text-brand-primary font-bold tracking-widest text-sm uppercase block">Step 04</span>
                <h2 class="font-heading text-4xl md:text-5xl font-bold text-brand-dark leading-tight">
                    Sunday Sunset: The Handover
                </h2>
                <p class="text-brand-gray leading-relaxed text-lg">
                    Our goal is to hand over a pristine, completely finished landscape by Sunday sunset. You go to work on Monday, and your yard is transformed. However, we never sacrifice quality for speed. If a complex masterwork requires more time, we will clean the site and return the following weekend to achieve absolute perfection.
                </p>
            </div>
        </div>
    </section>

    <!-- CTA -->
    <section class="bg-brand-dark mx-6 md:mx-auto max-w-7xl rounded-[40px] overflow-hidden relative shadow-2xl mb-24 text-center p-16">
        <div class="relative z-10 text-white">
            <h2 class="font-heading text-4xl font-bold mb-6">Ready to schedule your Strike?</h2>
            <p class="text-gray-300 mb-8 max-w-xl mx-auto">Skip the months-long construction zones. Get a premium hardscape built by the owners, completed over the weekend.</p>
            <a href="contact.html" class="inline-block bg-brand-primary text-white px-8 py-4 rounded-full font-bold hover:bg-green-600 transition shadow-lg">Request Consultation</a>
        </div>
    </section>
"""

new_process_html = f"{header_html}\n{MAIN_CONTENT}\n{footer_html}"

with open(process_path, 'w', encoding='utf-8') as f:
    f.write(new_process_html)

print("Updated index.html and wrote process.html")
