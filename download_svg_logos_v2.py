import os
import requests

brands = {
    "hikvision": "hikvision-1",
    "dahua": "dahua-technology",
    "ezviz": "ezviz",
    "essl": "essl",
    "wipro": "wipro-1",
    "yale": "yale-2",
    "godrej": "godrej",
    "dlink": "d-link-1",
    "netgear": "netgear-1",
    "tplink": "tp-link-logo",
    "cisco": "cisco-2",
    "tuya": "tuya",
    "faac": "faac",
    "bft": "bft-1",
    "nice": "nice-2",
    "knx": "knx-1",
    "panasonic": "panasonic-1",
    "samsung": "samsung-1",
    "schneider": "schneider-electric",
    "legrand": "legrand",
    "havells": "havells",
    "philips": "philips-1"
}

output_dir = "assets/images/brands/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

for name, slug in brands.items():
    url = f"https://cdn.worldvectorlogo.com/logos/{slug}.svg"
    filepath = os.path.join(output_dir, f"{name}.svg")
    
    if os.path.exists(filepath):
        print(f"Skipping {name}, already exists.")
        continue

    print(f"Downloading {name} from {url}...")
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            with open(filepath, 'wb') as f:
                f.write(response.content)
            print(f"  Successfully saved to {filepath}")
        else:
            print(f"  Failed for {name}: Status {response.status_code}")
    except Exception as e:
        print(f"  Error downloading {name}: {e}")

print("Done.")
