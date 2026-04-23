import os
import subprocess

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

for name, slug in brands.items():
    url = f"https://cdn.worldvectorlogo.com/logos/{slug}.svg"
    filepath = os.path.join(output_dir, f"{name}.svg")
    print(f"Downloading {name}...")
    cmd = f'powershell -Command "Invoke-WebRequest -Uri \'{url}\' -OutFile \'{filepath}\'"'
    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"  Saved to {filepath}")
    except:
        print(f"  Failed for {name}")

print("Done.")
