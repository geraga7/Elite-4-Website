import glob
import re

def inject_aos_and_seo():
    files = glob.glob('*.html')
    
    aos_css = '<link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">\n</head>'
    aos_js = '<script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>\n<script>AOS.init({duration: 800, once: true, offset: 100});</script>\n</body>'
    
    for f in files:
        with open(f, 'r') as file:
            content = file.read()
            
        # 1. Add AOS CSS
        if 'aos.css' not in content:
            content = content.replace('</head>', aos_css)
            
        # 2. Add AOS JS
        if 'aos.js' not in content:
            # Insert before the last </body>
            content = content.replace('</body>', aos_js)
            
        # 3. Add data-aos="fade-up" to main sections and grids
        # Let's find <section class="..."> and add data-aos="fade-up"
        # We will use regex to add it if not exists
        def add_aos_section(match):
            tag = match.group(0)
            if 'data-aos=' not in tag:
                return tag.replace('<section ', '<section data-aos="fade-up" ')
            return tag
            
        content = re.sub(r'<section [^>]+>', add_aos_section, content)

        # Same for major divs like bento grids or cards
        # We can look for divs with 'group', 'bg-surface-container-', 'rounded' etc.
        def add_aos_div(match):
            tag = match.group(0)
            if 'data-aos=' not in tag:
                return tag.replace('<div ', '<div data-aos="fade-up" ')
            return tag
            
        content = re.sub(r'<div[^>]+class="[^"]*(bg-surface-container-[^\s"]+|shadow-[^\s"]+)[^"]*"[^>]*>', add_aos_div, content)

        # 4. Add loading="lazy" to all images (except absolute inset-0 images in headers which are LCP)
        # Actually it's easier to just ensure good alt text and lazy loading on all images.
        def add_lazy_loading(match):
            img_tag = match.group(0)
            if 'loading="lazy"' not in img_tag and 'hero' not in img_tag.lower():
                return img_tag.replace('<img ', '<img loading="lazy" ')
            return img_tag
            
        content = re.sub(r'<img [^>]+>', add_lazy_loading, content)
        
        with open(f, 'w') as file:
            file.write(content)
            
    print("Injected AOS animations, lazy loading, and interactive elements across all pages.")

if __name__ == "__main__":
    inject_aos_and_seo()
