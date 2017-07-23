import requests
import shutil

def save_image(link):
    filename = link.split('/')[1:]
    r = requests.get(link, stream=True)
    if r.status_code == 200:
        with open(filename, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)  
