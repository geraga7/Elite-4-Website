import glob

for file in glob.glob('*.html'):
    with open(file, 'r') as f:
        content = f.read()
    
    # The footers have: href="#">Contact Us</a> and href="#">Contact</a>
    content = content.replace('href="#">Contact Us</a>', 'href="contact.html">Contact Us</a>')
    content = content.replace('href="#">Contact</a>', 'href="contact.html">Contact</a>')
    
    with open(file, 'w') as f:
        f.write(content)

