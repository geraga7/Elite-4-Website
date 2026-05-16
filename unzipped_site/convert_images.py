# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "Pillow",
# ]
# ///
from PIL import Image
import glob
import os

def convert_images():
    images = glob.glob('*.png') + glob.glob('*.jpg')
    for img_path in images:
        try:
            with Image.open(img_path) as img:
                # Convert to RGB if it's RGBA but saving as JPEG/WEBP without alpha
                # WEBP supports alpha, but let's optimize it
                base = os.path.splitext(img_path)[0]
                webp_path = f"{base}.webp"
                
                # Resize if it's too massive (like 8K) to a max width of 1920
                max_width = 1920
                if img.width > max_width:
                    ratio = max_width / float(img.width)
                    new_height = int(float(img.height) * float(ratio))
                    img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
                
                img.save(webp_path, "WEBP", quality=80, optimize=True)
                print(f"Converted and optimized {img_path} to {webp_path}")
        except Exception as e:
            print(f"Failed to convert {img_path}: {e}")

if __name__ == "__main__":
    convert_images()
