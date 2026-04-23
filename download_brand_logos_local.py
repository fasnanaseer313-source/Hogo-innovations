import os
import requests

brands = {
    "hikvision": "hikvision.com",
    "dahua": "dahuasecurity.com",
    "ezviz": "ezvizlife.com",
    "essl": "esslsecurity.com",
    "wipro": "wipro.com",
    "yale": "yalehome.com",
    "godrej": "godrej.com",
    "dlink": "dlink.com",
    "netgear": "netgear.com",
    "tplink": "tp-link.com",
    "cisco": "cisco.com",
    "tuya": "tuya.com",
    "faac": "faacgroup.com",
    "bft": "bft-automation.com",
    "nice": "niceforyou.com",
    "knx": "knx.org",
    "panasonic": "panasonic.com",
    "samsung": "samsung.com",
    "schneider": "se.com",
    "legrand": "legrand.com",
    "havells": "havells.com",
    "philips": "philips.com",
    "ozon": "ozon.ru",
    "prima": "prima.com",
    "key": "keyautomation.it",
    "beninca": "beninca.com"
}

output_dir = "assets/images/brands/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print(f"Downloading {len(brands)} logos...")

for name, domain in brands.items():
    url = f"https://logo.clearbit.com/{domain}?size=256"
    filepath = os.path.join(output_dir, f"{name}.png")
    
    try:
        print(f"Downloading {name} from {url}...")
        response = requests.get(url, stream=True, timeout=10)
        if response.status_code == 200:
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"  Successfully saved to {filepath}")
        else:
            print(f"  Failed to download {name}: Status {response.status_code}")
    except Exception as e:
        print(f"  Error downloading {name}: {e}")

print("Download complete.")
