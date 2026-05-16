import os
import glob
import re

def fix_menu_position():
    files = glob.glob('/Users/user/Documents/Elite 4/*.html')
    
    for f in files:
        with open(f, 'r') as file:
            content = file.read()
            
        # We need to find the mobile-menu div and move it OUTSIDE the nav.
        # Currently it looks like:
        # <div id="mobile-menu" ...> ... </div>
        # </nav>
        
        # We will extract the mobile-menu div, remove it from inside <nav>, and append it after </nav>
        
        pattern = re.compile(r'(<div id="mobile-menu".*?</div>)\s*</nav>', re.DOTALL)
        
        match = pattern.search(content)
        if match:
            menu_html = match.group(1)
            # Remove it from inside nav
            content = pattern.sub('</nav>\n' + menu_html, content)
            
            with open(f, 'w') as file:
                file.write(content)

    print("Moved mobile-menu outside of nav to fix the backdrop-filter fixed positioning bug.")

if __name__ == "__main__":
    fix_menu_position()
