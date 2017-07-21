import requests
import shutil

settings = 'https://www.google.com.mx/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png'

r = requests.get(settings, stream=True)
if r.status_code == 200:
    with open('image.png', 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)  