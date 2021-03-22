import gdown

url = 'https://drive.google.com/uc?id=1Hih1QAZSM-W07UVSmhFfZhEWYcDNzjfJ'
output = 'blenderbot_italian.zip'

gdown.cached_download(url, output, postprocess=gdown.extractall)