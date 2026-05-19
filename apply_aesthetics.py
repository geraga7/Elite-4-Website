import os
import glob
import re

base_dir = '/Users/user/Documents/Elite 4'
index_path = os.path.join(base_dir, 'index.html')

with open(index_path, 'r', encoding='utf-8') as f:
    index_html = f.read()

# Extract the <head> contents specifically the tailwind config and fonts and styles
# We want to replace everything from <script src="https://cdn.tailwindcss.com"></script>
# down to </style> before <!-- Schema Markup -->
start_marker = '<script src="https://cdn.tailwindcss.com"></script>'
end_marker = '</style>'

if start_marker in index_html and end_marker in index_html:
    start_idx = index_html.find(start_marker)
    # find the last </style> before the closing head
    end_idx = index_html.rfind(end_marker, 0, index_html.find('</head>')) + len(end_marker)
    
    new_head_content = index_html[start_idx:end_idx]

    for filename in glob.glob(os.path.join(base_dir, '*.html')):
        if os.path.basename(filename) == 'index.html':
            continue
            
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if start_marker in content and end_marker in content:
            s_idx = content.find(start_marker)
            e_idx = content.rfind(end_marker, 0, content.find('</head>')) + len(end_marker)
            
            content = content[:s_idx] + new_head_content + content[e_idx:]
            
            # Apply glassmorphism to the navbar
            content = re.sub(r'<nav class="bg-white/95 backdrop-blur-md[^"]*"', 
                             r'<nav class="glassmorphism py-4 px-6 md:px-12 flex justify-between items-center sticky top-0 z-50 transition-all duration-300"', content)
            content = re.sub(r'<nav class="glassmorphism[^"]*"', 
                             r'<nav class="glassmorphism py-4 px-6 md:px-12 flex justify-between items-center sticky top-0 z-50 transition-all duration-300"', content)

            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Applied aesthetic to {os.path.basename(filename)}")
