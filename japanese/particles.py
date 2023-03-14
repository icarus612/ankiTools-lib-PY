from helpers.jpod101_crawlers import search, download_audio

def split(f, s='\t'):
  return [[i.strip() for i in x.split(s)] for x in f.readlines()]

prefix = 'ic_jp_'
suffix = '.mp3'

with open('./imported-decks/particles-new.txt') as p_new, open('./imported-decks/particles-old.txt') as p_old, open('./particles-final.txt', 'w') as p_final:
  new = split(p_new, '|')  
  old = split(p_old)
  final = []
  audio_dict = search([x[1] for x in new])
  update_audio = dict()

  for card in new:
    if card[1] in audio_dict.keys():
      card.extend([f'[sound:{prefix}{card[1]}{suffix}]', '', ''])
      update_audio[prefix + card[1] + suffix] = audio_dict[card[1]]
      final.append(card)

  p_final.writelines([' | '.join(x) + '\n' for x in final])
  download_audio(update_audio)
