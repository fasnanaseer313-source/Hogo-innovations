
import os
from PIL import Image

def remove_white_background(image_path, output_path, tolerance=240):
    if not os.path.exists(image_path):
        print(f"Skipping {image_path}, file not found.")
        return
    
    img = Image.open(image_path)
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        # Check if pixel is close to white (R, G, B > tolerance)
        if item[0] >= tolerance and item[1] >= tolerance and item[2] >= tolerance:
            # Make it transparent
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(output_path, "PNG")
    print(f"Processed: {output_path}")

logos_to_clean = [
    "dahua.png",
    "ezviz.png",
    "essl.png",
    "yale.png",
    "tuya.png",
    "faac.png",
    "bft.png",
    "nice.png",
    "knx_new_logo.png",
    "samsung_new_logo.png",
    "schneider.png",
    "beninca.png",
    "came.png"
]

base_path = "assets/images/brands/"

for logo in logos_to_clean:
    input_file = os.path.join(base_path, logo)
    # Output to a cleaned filename
    output_file = os.path.join(base_path, logo.replace(".png", "_clean.png"))
    remove_white_background(input_file, output_file)
