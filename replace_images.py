import glob
import re
import shutil
import os
import random

# Source images
source_dir = "/Users/user/.gemini/antigravity/brain/62a06723-d7c6-4cff-9918-c026c2692d89/"
images = {
    "landscape_team_working_1777344702612.png": "landscape_team.png",
    "luxury_patio_night_1777344663632.png": "luxury_patio.png",
    "modern_pool_landscape_1777344676610.png": "modern_pool.png",
    "stone_retaining_wall_1777344690831.png": "retaining_wall.png"
}

# Copy files
for src, dst in images.items():
    src_path = os.path.join(source_dir, src)
    dst_path = os.path.join("/Users/user/Documents/Elite 4", dst)
    shutil.copy2(src_path, dst_path)

# Add existing hero
final_images = list(images.values()) + ["hero-pathway.jpg"]

# Replace in HTML
html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()
    
    # Find all placeholder URLs
    pattern = r'https://lh3.googleusercontent.com/aida-public/[a-zA-Z0-9_-]+'
    
    def replacer(match):
        return "./" + random.choice(final_images)
        
    new_content = re.sub(pattern, replacer, content)
    
    with open(file, 'w') as f:
        f.write(new_content)

print("Images replaced successfully.")
