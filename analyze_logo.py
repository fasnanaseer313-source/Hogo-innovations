from PIL import Image

def analyze_white_components(image_path):
    img = Image.open(image_path).convert("RGBA")
    width, height = img.size
    pixels = img.load()
    
    visited = set()
    tolerance = 230
    
    components = []
    
    for y in range(height):
        for x in range(width):
            if (x, y) not in visited:
                r, g, b, a = pixels[x, y]
                if r >= tolerance and g >= tolerance and b >= tolerance and a > 0:
                    # found a new white component
                    queue = [(x, y)]
                    visited.add((x, y))
                    size = 0
                    min_x, max_x = x, x
                    min_y, max_y = y, y
                    
                    while queue:
                        cx, cy = queue.pop(0)
                        size += 1
                        min_x = min(min_x, cx)
                        max_x = max(max_x, cx)
                        min_y = min(min_y, cy)
                        max_y = max(max_y, cy)
                        
                        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                            nx, ny = cx + dx, cy + dy
                            if 0 <= nx < width and 0 <= ny < height:
                                if (nx, ny) not in visited:
                                    nr, ng, nb, na = pixels[nx, ny]
                                    if nr >= tolerance and ng >= tolerance and nb >= tolerance and na > 0:
                                        visited.add((nx, ny))
                                        queue.append((nx, ny))
                    components.append({'size': size, 'bbox': (min_x, min_y, max_x, max_y), 'start': (x, y)})

    components.sort(key=lambda c: c['size'], reverse=True)
    for i, c in enumerate(components[:10]):
        print(f"Component {i}: Size={c['size']}, BBox={c['bbox']}, Start={c['start']}")

if __name__ == "__main__":
    analyze_white_components("assets/images/hogo_main_logo.png")
