from audio_search import search

import json

input_file = ""
output_file = ""

with open('particles.txt') as old_cards, open('output.txt', 'w') as new_cards, open('audio-files.json', 'w') as audio:
  audio_files = {}
  for card in old_cards.readlines():   
    clist = [a.strip() for a in card.split('\t')]
    word = '-'.join(clist[1].split(' '))
    file_name = f'ic_jp_{word}.mp3'
    clist[4] = f'[sound:{file_name}]'
    new_cards.write(' | '.join(clist) + '\n')
    break


  audio.write(json.dumps(audio_files))
