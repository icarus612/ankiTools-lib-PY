import requests
import os
import json


path = 'audio-files'

try: 
  os.mkdir(path)
except:
  for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        os.remove(os.path.join(root, name))
    for name in dirs:
        os.rmdir(os.path.join(root, name))    
  os.rmdir(path)
  os.mkdir(path)

audio_json = {}
with open('audio-files.json') as audio_files:
  audio_json = json.loads(audio_files.read())

for name, src in audio_json.items(): 
  headers = {
    'authority': 'cdn.innovativelanguage.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'range': 'bytes=0-',
    'referer': src,
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'video',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
  }
  audio = requests.get(src, headers=headers)
  with open(os.path.join(path, name), 'wb') as audio_file:
    audio_file.write(audio.content)
