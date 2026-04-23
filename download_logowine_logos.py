import os
import requests

brands = {
    "samsung": "Samsung/Samsung-Logo.wine.svg",
    "hikvision": "Hikvision/Hikvision-Logo.wine.svg",
    "dahua": "Dahua_Technology/Dahua_Technology-Logo.wine.svg",
    "ezviz": "EZVIZ/EZVIZ-Logo.wine.svg",
    "tplink": "TP-Link/TP-Link-Logo.wine.svg",
    "dlink": "D-Link/D-Link-Logo.wine.svg",
    "cisco": "Cisco/Cisco-Logo.wine.svg",
    "panasonic": "Panasonic/Panasonic-Logo.wine.svg",
    "philips": "Philips/Philips-Logo.wine.svg",
    "wipro": "Wipro/Wipro-Logo.wine.svg"
}

output_dir = "assets/images/brands/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

for name, path in brands.items():
    url = f"https://www.logo.wine/a/logo/{path}"
    filepath = os.path.join(output_dir, f"{name}.svg")
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
