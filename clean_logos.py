from PIL import Image
import os

def remove_checkerboard(image_path, output_path):
    if not os.path.exists(image_path):
        print(f"File not found: {image_path}")
        return
        
    img = Image.open(image_path)
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        r, g, b, a = item
        # Checkerboard usually consists of white (#ffffff) and light grey (#cccccc or #eeeeee)
        # We target pixels where r, g, b are all very high or all close to each other in the grey range
        
        # White or very light grey
        if r > 210 and g > 210 and b > 210:
            newData.append((255, 255, 255, 0))
        # Mid-grey checkerboard (often around 180-210)
        elif abs(r - g) < 5 and abs(g - b) < 5 and r > 180:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(output_path, "PNG")
    print(f"Processed {output_path}")

brands_dir = "assets/images/brands/"
files = [f for f in os.listdir(brands_dir) if f.endswith(".png")]

for f in files:
    input_p = os.path.join(brands_dir, f)
    # Give it a new name or overwrite? Let's give it a clean name.
    output_p = os.path.join(brands_dir, f.replace(".png", "_clean.png"))
    remove_checkerboard(input_p, output_p)
