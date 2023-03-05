from modules.jp101.get_audio import get_audio 

with open('audio-files.json') as audio_files:
  audio_json = json.loads(audio_files.read())
  get_audio(audio_json)

