import os
import glob
import re

vanta_scripts = """
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r134/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/vanta@latest/dist/vanta.waves.min.js"></script>
"""

vanta_init = """
<!-- Vanta Water Background -->
<div id="vanta-bg" class="fixed inset-0 z-[-1] pointer-events-none"></div>
<script>
document.addEventListener('DOMContentLoaded', () => {
    if (typeof VANTA !== 'undefined') {
        VANTA.WAVES({
            el: "#vanta-bg",
            mouseControls: true,
            touchControls: true,
            gyroControls: false,
            minHeight: 200.00,
            minWidth: 200.00,
            scale: 1.00,
            scaleMobile: 1.00,
            color: 0x2a593e,
            shininess: 25.00,
            waveHeight: 12.00,
            waveSpeed: 0.40,
            zoom: 0.85
        });
    }
});
</script>
"""

def add_water_background():
    files = glob.glob('/Users/user/Documents/Elite 4/*.html')
    
    for f in files:
        with open(f, 'r') as file:
            content = file.read()
            
        # Add scripts to head
        if "vanta.waves.min.js" not in content:
            content = content.replace("</head>", vanta_scripts + "</head>")
            
        # Add vanta init before </body>
        if "id=\"vanta-bg\"" not in content:
            content = content.replace("</body>", vanta_init + "\n</body>")
            
        # Make backgrounds translucent so the water is visible
        content = content.replace('bg-[#f6f6f5]', 'bg-[#f6f6f5]/70 backdrop-blur-md')
        content = content.replace('bg-[#f0f1ef]', 'bg-[#f0f1ef]/70 backdrop-blur-md')
        content = content.replace('bg-white', 'bg-white/80 backdrop-blur-md')
        
        # Don't mess up the mobile menu overlay which is a dark bg
        content = content.replace('bg-[#2d2f2e]/70 backdrop-blur-md', 'bg-[#2d2f2e]') # Just in case
        
        with open(f, 'w') as file:
            file.write(content)

    print("Water background added successfully.")

if __name__ == "__main__":
    add_water_background()
