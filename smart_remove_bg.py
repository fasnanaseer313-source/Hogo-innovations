from PIL import Image, ImageDraw

def process_logo(input_path, output_path):
    # Open image
    img = Image.open(input_path).convert("RGBA")
    
    # We will do a flood fill on a dummy mode "L" or "RGB" and then apply as mask?
    # Or just flood fill with a unique color, then replace that color with transparent.
    
    width, height = img.size
    
    # Create a wrapper image with a 1px border so all edges are connected
    wrapper = Image.new("RGBA", (width + 2, height + 2), (255, 255, 255, 255))
    wrapper.paste(img, (1, 1))
    
    # Magic color that is definitely not in the logo
    magic_color = (255, 0, 255, 255) # Magenta
    
    # Flood fill from (0,0) with magic color for any pixel close to white
    # Pillow's floodfill uses an exact match. If background is not perfectly pure white, we need a custom BFS.
    
    pixels = wrapper.load()
    
    # BFS to replace near-white background
    queue = [(0, 0)]
    visited = set()
    visited.add((0, 0))
    tolerance = 230 # High tolerance for white
    
    while queue:
        x, y = queue.pop(0)
        
        r, g, b, a = pixels[x, y]
        # Check if near white
        if r >= tolerance and g >= tolerance and b >= tolerance and a > 0:
            pixels[x, y] = (0, 0, 0, 0) # Make transparent
            
            # Add neighbors
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < width + 2 and 0 <= ny < height + 2:
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
    
    # Crop back to original size
    final_img = wrapper.crop((1, 1, width + 1, height + 1))
    final_img.save(output_path, "PNG")
    print(f"Saved {output_path}")

if __name__ == "__main__":
    try:
        process_logo("assets/images/hogo_main_logo.png", "assets/images/hogo_main_logo_transparent.png")
    except Exception as e:
        print(f"Error: {e}")
