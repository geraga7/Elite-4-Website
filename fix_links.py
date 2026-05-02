import glob

for file in glob.glob('*.html'):
    with open(file, 'r') as f:
        content = f.read()
    
    content = content.replace('href="#">Home</a>', 'href="index.html">Home</a>')
    content = content.replace('href="#">About Us</a>', 'href="about.html">About Us</a>')
    content = content.replace('href="#">Services</a>', 'href="services.html">Services</a>')
    content = content.replace('href="#">Portfolio</a>', 'href="portfolio.html">Portfolio</a>')
    content = content.replace('href="#">Process</a>', 'href="process.html">Process</a>')
    content = content.replace('href="#">Journal</a>', 'href="journal.html">Journal</a>')
    
    with open(file, 'w') as f:
        f.write(content)
