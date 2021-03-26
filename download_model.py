import gdown

url = 'https://drive.google.com/uc?id=1-Acc1gp5ZAQ80mooPpEiisKUL5cBq5tB'
output = 'blenderbot_italian.zip'

gdown.cached_download(url, output, postprocess=gdown.extractall)