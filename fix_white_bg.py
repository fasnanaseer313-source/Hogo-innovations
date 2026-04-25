"""
Removes white/near-white backgrounds from brand logo PNGs.
Saves cleaned versions with a _fixed suffix.
"""
from PIL import Image
import os

# Logos actively used in index.html / brands.html that have white backgrounds
TARGETS = {
    # file_in: file_out
    "assets/images/brands/essl_clean.png": "assets/images/brands/essl_fixed.png",
    "assets/images/brands/essl.png": "assets/images/brands/essl_fixed.png",
    "assets/images/brands/dahua_clean.png": "assets/images/brands/dahua_fixed.png",
    "assets/images/brands/dahua.png": "assets/images/brands/dahua_fixed.png",
    "assets/images/brands/ezviz_clean.png": "assets/images/brands/ezviz_fixed.png",
    "assets/images/brands/ezviz.png": "assets/images/brands/ezviz_fixed.png",
    "assets/images/brands/knx_new_logo_clean.png": "assets/images/brands/knx_fixed.png",
    "assets/images/brands/knx_new_logo.png": "assets/images/brands/knx_fixed.png",
    "assets/images/brands/samsung_new_logo_clean.png": "assets/images/brands/samsung_fixed.png",
    "assets/images/brands/samsung_new_logo.png": "assets/images/brands/samsung_fixed.png",
    "assets/images/brands/havells.png": "assets/images/brands/havells_fixed.png",
    "assets/images/brands/ozone_new_logo.png": "assets/images/brands/ozone_fixed.png",
    "assets/images/brands/prima_new_logo.png": "assets/images/brands/prima_fixed.png",
}

def remove_white_bg(src, dst, threshold=240, fuzz=30):
    img = Image.open(src).convert("RGBA")
    data = img.getdata()
    new_data = []
    for r, g, b, a in data:
        # if pixel is near-white, make it transparent
        if r >= threshold and g >= threshold and b >= threshold:
            # Smooth edge: fade based on how white it is
            whiteness = min(r, g, b)
            alpha = max(0, 255 - int((whiteness - (threshold - fuzz)) * 255 / fuzz))
            new_data.append((r, g, b, min(a, alpha)))
        else:
            new_data.append((r, g, b, a))
    img.putdata(new_data)
    img.save(dst, "PNG")
    print(f"  Saved: {dst}")

processed = set()
for src, dst in TARGETS.items():
    if dst in processed:
        continue
    # Use the best available source
    if os.path.exists(src):
        print(f"Processing {os.path.basename(src)} -> {os.path.basename(dst)}")
        try:
            remove_white_bg(src, dst)
            processed.add(dst)
        except Exception as e:
            print(f"  ERROR: {e}")
    else:
        print(f"  Skipping (not found): {src}")

print("\nDone!")
