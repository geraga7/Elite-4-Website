import os
import glob
import re

def optimize_website():
    html_files = glob.glob('/Users/user/Documents/Elite 4/*.html')
    
    # 1. Update HTML files to defer heavy scripts and use webp
    for f in html_files:
        with open(f, 'r') as file:
            content = file.read()
            
        # Defer AOS
        content = content.replace('<script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>', '<script defer src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>')
        
        # Defer Three.js and Vanta
        content = content.replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r134/three.min.js"></script>', '<script defer src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r134/three.min.js"></script>')
        content = content.replace('<script src="https://cdn.jsdelivr.net/npm/vanta@latest/dist/vanta.waves.min.js"></script>', '<script defer src="https://cdn.jsdelivr.net/npm/vanta@latest/dist/vanta.waves.min.js"></script>')
        
        # Change DOMContentLoaded to window load for Vanta and AOS
        # Since we deferred the scripts, they might not be ready at DOMContentLoaded.
        content = content.replace("document.addEventListener('DOMContentLoaded', () => {", "window.addEventListener('load', () => {")
        
        # Update image extensions to .webp
        content = content.replace('.png"', '.webp"')
        content = content.replace('.jpg"', '.webp"')
        
        # Add preconnect to speed up CDN fetching
        if '<link rel="preconnect" href="https://fonts.googleapis.com">' not in content:
            content = content.replace('<head>', '<head>\n<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link rel="preconnect" href="https://cdnjs.cloudflare.com">\n<link rel="preconnect" href="https://cdn.tailwindcss.com">')
            
        with open(f, 'w') as file:
            file.write(content)

    print("HTML optimization (deferring scripts, preconnecting CDNs, swapping to WebP) completed.")

if __name__ == "__main__":
    optimize_website()
