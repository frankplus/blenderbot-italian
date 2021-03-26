import gdown

url = 'https://drive.google.com/uc?id=1wpkBI0cCeCVB0isaF-VaABeyI7-DFIMc'
output = 'blenderbot_italian.zip'

gdown.cached_download(url, output, postprocess=gdown.extractall)