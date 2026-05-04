from PIL import Image, ImageDraw
import os

def clean_image(src, dst):
    img = Image.open(src).convert("RGB")
    draw = ImageDraw.Draw(img)
    
    # Coordinates for the "ON" box area (rough estimate based on 1600x900)
    # The box is in the right half, top area.
    # Let's try to fill a patch that matches the ceiling color.
    # Ceiling color is roughly (240, 230, 215)
    ceiling_color = (244, 238, 225) 
    
    # Patch 1: The "ON" box area
    # Based on the screenshot, it's about 2/3 to the right, and near the top.
    # X: 950 to 1150, Y: 50 to 200
    draw.rectangle([950, 60, 1150, 180], fill=ceiling_color)
    
    # Patch 2: Any other artifacts? The "unwanted blue" was from transparency.
    # By saving as JPG/RGB, we avoid transparency issues.
    
    img.save(dst, "JPEG", quality=95)
    print(f"Saved: {dst}")

src = "assets/images/smart_glass_new.jpg"
dst = "assets/images/smart_glass_cleaned.jpg"

if os.path.exists(src):
    clean_image(src, dst)
else:
    print(f"File not found: {src}")
