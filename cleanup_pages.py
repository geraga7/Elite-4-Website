import os
import glob
import re

base_dir = '/Users/user/Documents/Elite 4'

for filename in glob.glob(os.path.join(base_dir, '*.html')):
    if os.path.basename(filename) == 'index.html':
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    # Remove 8K Showcase
    content = re.sub(r'<!-- 8K Super High Resolution Architectural Showcase -->.*?</section>', '', content, flags=re.DOTALL)
    
    # Remove Interactive Estimator
    content = re.sub(r'<!-- Interactive Project Investment & Timeline Estimator -->.*?</section>', '', content, flags=re.DOTALL)
    
    # Remove Before/After Visualizer
    content = re.sub(r'<!-- Interactive Before/After Visualizer -->.*?</section>', '', content, flags=re.DOTALL)
    
    # Remove Interactive Estimator JS
    content = re.sub(r'<!-- Interactive Estimator & Slider JS -->.*?</script>', '', content, flags=re.DOTALL)
    
    # Remove any extra blank lines left over
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
    
    if content != original_content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Cleaned up {os.path.basename(filename)}")
