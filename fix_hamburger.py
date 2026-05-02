import os
import glob
import re

def fix_hamburger_display():
    files = glob.glob('/Users/user/Documents/Elite 4/*.html')
    
    for f in files:
        with open(f, 'r') as file:
            content = file.read()
            
        # Add lg:hidden to the mobile-menu-button so it only shows on mobile/tablet
        # The current class string starts with: class="text-[#366549] p-2
        
        # Replace the exact opening button tag
        old_btn = '<button id="mobile-menu-button" class="text-[#366549] p-2 hover:bg-[#366549]/10 rounded-full transition-colors flex items-center justify-center">'
        new_btn = '<button id="mobile-menu-button" class="lg:hidden text-[#366549] p-2 hover:bg-[#366549]/10 rounded-full transition-colors flex items-center justify-center">'
        
        content = content.replace(old_btn, new_btn)
        
        with open(f, 'w') as file:
            file.write(content)

    print("Mobile menu button (3 lines) hidden on desktop screens successfully.")

if __name__ == "__main__":
    fix_hamburger_display()
