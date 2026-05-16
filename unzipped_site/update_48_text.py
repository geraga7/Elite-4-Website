import os
import glob

base_dir = '/Users/user/Documents/Elite 4'

replacements = [
    ("Our 48-Hour Guarantee", "Our 48+ Hour Masterwork"),
    ("See how we complete the work in 48 hours", "See how we complete the work in 48 hours or more"),
    ("We try to strike everything in 48 hours, but if we need more time, we come back a different weekend or most likely the following weekend.", "We complete jobs in 48 hours or more, returning the following weekend if necessary to ensure absolute perfection."),
    ("48-Hour Strike", "48+ Hour Strike"),
    ("48-Hour", "48+ Hour"),
    ("48HR", "48+ HR"),
    ("Strike everything in 48 hours (or the following weekend)", "Complete jobs in 48 hours or more"),
]

for filename in glob.glob(os.path.join(base_dir, '*.html')):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements:
        content = content.replace(old, new)
        
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")
