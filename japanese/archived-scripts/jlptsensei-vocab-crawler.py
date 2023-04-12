import requests
import json
from bs4 import BeautifulSoup as soup

def clean_txt(txt):
  return txt.strip().replace('~', '...').replace('〜', '...').replace('～', '...').replace('+', '...').replace('・', ' / ').replace('」', ' ').replace('「',  '')

def find_td(el, val, r=True):
  return el.find('td', f'jl-td-{val}', recursive=r)

files = ['n1', 'n2', 'n3', 'n4', 'n5']
new_deck = {}
for n_key in files:
  elements = {
    'verbs': [],
    'nouns': [],
    'adjectives': [],
  }
  for e_key, element in elements.items():
    for idx in range(10):
      try:
        page = soup(requests.get(f'https://jlptsensei.com/jlpt-{n_key}-{e_key}-vocabulary-list/{idx}').content, 'html.parser')
        for particle in page.find_all('tr', {'class': 'jl-row'}):
          hiragana = find_td(particle, 'vr').find('p').text
          romaji = find_td(particle, 'vr').text.replace(hiragana, '') 
          info = find_td(particle, 'vm').text
          audio_name = f'ic-nrkt-{"".join(romaji.split(" "))}'
          sound = f'[sound:{audio_name}]'
          card = [hiragana, romaji, info]
          if '【' in card[1]:
            card[1] = card[1].split('【')[1].replace('】', '')
          element.append(card)
      except Exception as e:
        print(e)
  new_deck[n_key] = elements
  print(elements)
#for key, val in files.items():
#  with open(f'jlptsensei-particles-{key}.txt', 'w') as p_file:
#    for card in val:
#      p_file.write(card + '\n')

with open(f'jlptsensei-vocab.json', 'w') as p_file:
  p_file.write(json.dumps(new_deck))
