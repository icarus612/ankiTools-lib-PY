import requests
import os
import json
import sys

json_path = input('Input audio files json path or url: ') if len(sys.argv) < 2 else sys.argv[1]
audio_path = input('Input path to save audio files: ') if len(sys.argv) < 3 else sys.argv[2]
wipe_old_audio = bool(input('Wipe old audio files from current audio directory? ') if len(sys.argv) < 4 else sys.argv[2])

try: 
  os.mkdir(audio_path)
except:
  if wipe_old_audio: 
    for root, dirs, files in os.walk(audio_path, topdown=False):
      for name in files:
          os.remove(os.path.join(root, name))
      for name in dirs:
          os.rmdir(os.path.join(root, name))    
    os.rmdir(audio_path)
    os.mkdir(audio_path)

audio_json = {}
with open(json_path if json_path.endswith('.json') else f'{json_path}.json') as audio_files:
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
