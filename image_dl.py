import requests, shutil, os
from pathlib import Path

def save_image(link,folder=''):
    # Check if a folder was passed, creates it if not exists
    if folder != '':
        if not os.path.exists(folder):
            os.makedirs(folder)
    # Gets the filename
    filename = link.split('/')[-1:][0]
    filename = folder+filename
    
    try:
        # Check if file already exists based on filename
        # then download and save image
        if not Path(filename).is_file():
            try:
                r = requests.get(link, stream=True)
                if r.status_code == 200:
                    with open(filename, 'wb') as f:
                        r.raw.decode_content = True
                        shutil.copyfileobj(r.raw, f)
                    print('Saved '+filename)
            # This is in case the url can't be resolved
            except socket.gaierror:
                print('Error downloading '+filename)
                pass
        else:
            print('File already exists')
            pass
    except OSError as e:
        print('Weird filename, skipping')
        pass
