import os
import glob
import re

def fix_text_visibility():
    files = glob.glob('/Users/user/Documents/Elite 4/*.html')
    
    for f in files:
        with open(f, 'r') as file:
            content = file.read()
            
        # 1. Fix the MENU button contrast
        # We need to find the <button id="mobile-menu-button"...
        # Old: class="lg:hidden text-[#366549] px-4 py-2 hover:bg-[#366549]/10 rounded-full transition-colors flex items-center justify-center gap-2 border border-[#366549]/20 shadow-sm"
        # We will make it bg-[#366549] text-white so it pops out completely!
        
        old_btn_class = 'class="lg:hidden text-[#366549] px-4 py-2 hover:bg-[#366549]/10 rounded-full transition-colors flex items-center justify-center gap-2 border border-[#366549]/20 shadow-sm"'
        new_btn_class = 'class="lg:hidden bg-[#366549] text-white px-4 py-2 hover:bg-[#2a593e] rounded-full transition-colors flex items-center justify-center gap-2 shadow-lg border border-[#c3f7d3]/20"'
        content = content.replace(old_btn_class, new_btn_class)
        
        # 2. Fix the mobile menu overlay scrolling
        # Old inner div: <div class="flex flex-col items-center gap-10 w-full min-h-max my-auto">
        # Replace with: <div class="flex flex-col items-center gap-10 w-full mt-10">
        
        old_inner_div = '<div class="flex flex-col items-center gap-10 w-full min-h-max my-auto">'
        new_inner_div = '<div class="flex flex-col items-center gap-10 w-full mt-10 pb-20">'
        content = content.replace(old_inner_div, new_inner_div)
        
        # Also let's make sure the close button is fully visible (white text)
        content = content.replace('id="close-menu-button" class="absolute top-6 right-6 text-[#c3f7d3]', 'id="close-menu-button" class="absolute top-6 right-6 text-white bg-[#366549] rounded-full shadow-lg')
        
        with open(f, 'w') as file:
            file.write(content)

    print("Fixed MENU text contrast and mobile menu scroll issues.")

if __name__ == "__main__":
    fix_text_visibility()
