import requests
import json 
res = requests.get('paste your link here')
response = json.loads(res.text)