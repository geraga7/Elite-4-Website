import os
import glob
import re

def enhance_hamburger():
    files = glob.glob('/Users/user/Documents/Elite 4/*.html')
    
    for f in files:
        with open(f, 'r') as file:
            content = file.read()
            
        # The button currently looks like:
        # <button id="mobile-menu-button" class="lg:hidden text-[#366549] p-2 hover:bg-[#366549]/10 rounded-full transition-colors flex items-center justify-center">
        #     <svg ...>
        # </button>
        
        # We will add a "MENU" text span inside the button, before the SVG.
        
        # First, let's update the button class to look more like a pill rather than a circle,
        # and ensure gap-2 is there so the text and icon have space.
        
        old_btn_class = 'class="lg:hidden text-[#366549] p-2 hover:bg-[#366549]/10 rounded-full transition-colors flex items-center justify-center"'
        new_btn_class = 'class="lg:hidden text-[#366549] px-4 py-2 hover:bg-[#366549]/10 rounded-full transition-colors flex items-center justify-center gap-2 border border-[#366549]/20 shadow-sm"'
        
        content = content.replace(old_btn_class, new_btn_class)
        
        # Now add the MENU text right before the SVG
        old_svg = '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="block">'
        new_svg_with_text = '<span class="font-[\'Epilogue\'] text-xs font-bold uppercase tracking-[0.2em] pt-[2px]">Menu</span>\n            ' + old_svg
        
        content = content.replace(old_svg, new_svg_with_text)
        
        with open(f, 'w') as file:
            file.write(content)

    print("Added MENU text to the hamburger button.")

if __name__ == "__main__":
    enhance_hamburger()
