import urllib.request
import os

logos = {
    "raviz_orig": "https://theraviz.com/wp-content/themes/raviz/assets/images/logo-black.png",
    "kseb_orig": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/KSEB_Logo_2022.svg/800px-KSEB_Logo_2022.svg.png",
    "nesto_orig": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Nesto_Logo_2019.png/800px-Nesto_Logo_2019.png",
    "speakeazy_orig": "https://www.speakeazyacademy.com/assets/images/logo.png",
    "mrpl_orig": "https://upload.wikimedia.org/wikipedia/en/thumb/e/ef/Mangalore_Refinery_and_Petrochemicals_Logo.svg/800px-Mangalore_Refinery_and_Petrochemicals_Logo.svg.png",
    "hp_orig": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/HP_logo_2012.svg/800px-HP_logo_2012.svg.png",
    "paratha_orig": "https://parathako.com/wp-content/uploads/2021/08/paratha-logo-1.png",
    "shadowfax_orig": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Shadowfax_Logo.png/800px-Shadowfax_Logo.png",
    "kmct_orig": "https://www.kmct.edu.in/assets/images/logo.png",
    "nakshathra_orig": "https://nakshathra.store/pub/media/logo/stores/1/logo.png",
    "sbi_orig": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/SBI-logo.svg/800px-SBI-logo.svg.png"
}

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
