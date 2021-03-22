import gdown

url = 'https://drive.google.com/uc?id=1Z4aWbKAEulcg-ykGrd-ugnx1IUDajepn'
output = 'blenderbot_italian.zip'

gdown.cached_download(url, output, postprocess=gdown.extractall)