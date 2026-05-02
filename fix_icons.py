import os
import glob
import re

hamburger_svg = '''
<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="block">
    <line x1="3" y1="12" x2="21" y2="12"></line>
    <line x1="3" y1="6" x2="21" y2="6"></line>
    <line x1="3" y1="18" x2="21" y2="18"></line>
</svg>
'''

close_svg = '''
<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="block">
    <line x1="18" y1="6" x2="6" y2="18"></line>
    <line x1="6" y1="6" x2="18" y2="18"></line>
</svg>
'''

def fix_icons():
    files = glob.glob('/Users/user/Documents/Elite 4/*.html')
    
    # We want to replace <span class="material-symbols-outlined text-3xl">menu</span>
    # and <span class="material-symbols-outlined text-4xl">close</span>
    # with the SVGs.
    
    menu_pattern = re.compile(r'<span[^>]*material-symbols-outlined[^>]*>menu</span>', re.IGNORECASE)
    close_pattern = re.compile(r'<span[^>]*material-symbols-outlined[^>]*>close</span>', re.IGNORECASE)
    
    for f in files:
        with open(f, 'r') as file:
            content = file.read()
            
        content = menu_pattern.sub(hamburger_svg, content)
        content = close_pattern.sub(close_svg, content)
        
        with open(f, 'w') as file:
            file.write(content)

    print("Icons replaced with pure SVGs successfully.")

if __name__ == "__main__":
    fix_icons()
