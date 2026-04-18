from PIL import Image

def remove_all_white(image_path, output_path, tolerance=230):
    img = Image.open(image_path)
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        # Check if pixel is close to white
        # If r, g, b are all above the tolerance, make it completely transparent
        if item[0] >= tolerance and item[1] >= tolerance and item[2] >= tolerance:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(output_path, "PNG")
    print(f"Saved {output_path}")

try:
    remove_all_white("assets/images/hogo_main_logo.png", "assets/images/hogo_main_logo_transparent.png")
except Exception as e:
    print(f"Error: {e}")
