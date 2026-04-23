import urllib.request
import os

logos = {
    "hikvision": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Hikvision_logo.svg/1024px-Hikvision_logo.svg.png",
    "dahua": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Dahua_Technology_logo.svg/1024px-Dahua_Technology_logo.svg.png",
    "ezviz": "https://www.ezviz.com/assets/images/logo.png", # Might need better one
    "essl": "https://www.esslsecurity.com/assets/images/logo.png", # Might need better one
    "wipro": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Wipro_Logo.svg/1024px-Wipro_Logo.svg.png",
    "yale": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Yale_Logo.svg/1024px-Yale_Logo.svg.png",
    "godrej": "https://upload.wikimedia.org/wikipedia/en/thumb/1/1b/Godrej_Logo.svg/1024px-Godrej_Logo.svg.png",
    "dlink": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/D-Link_logo.svg/1024px-D-Link_logo.svg.png",
    "netgear": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Netgear_logo.svg/1024px-Netgear_logo.svg.png",
    "tplink": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/TP-Link_Logo.svg/1024px-TP-Link_Logo.svg.png",
    "cisco": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Cisco_logo_blue_2016.svg/1024px-Cisco_logo_blue_2016.svg.png",
    "tuya": "https://images.tuyacdn.com/fe-static/home/tuya_logo.png",
    "faac": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/FAAC_logo.svg/1024px-FAAC_logo.svg.png",
    "bft": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/BFT_logo.svg/1024px-BFT_logo.svg.png",
    "nice": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Nice_logo.svg/1024px-Nice_logo.svg.png",
    "panasonic": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Panasonic_logo.svg/1024px-Panasonic_logo.svg.png",
    "samsung": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Samsung_Logo.svg/1024px-Samsung_Logo.svg.png",
    "schneider": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Schneider_Electric_2007.svg/1024px-Schneider_Electric_2007.svg.png",
    "legrand": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Legrand_logo.svg/1024px-Legrand_logo.svg.png",
    "havells": "https://upload.wikimedia.org/wikipedia/en/thumb/e/ef/Havells_Logo.svg/1024px-Havells_Logo.svg.png",
    "philips": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Philips_logo.svg/1024px-Philips_logo.svg.png",
    "knx": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/KNX_logo.svg/1024px-KNX_logo.svg.png"
}

# Fallback/Additional brands that might be harder to find direct URLs for
# Prima, Ozon, KEY, Beninca
# I will use clearbit for these or try to find them

dir_path = "assets/images/brands/"
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

for name, url in logos.items():
    print(f"Downloading {name}...")
    try:
        urllib.request.urlretrieve(url, os.path.join(dir_path, f"{name}.png"))
        print(f"Success: {name}")
    except Exception as e:
        print(f"Failed {name}: {e}")
