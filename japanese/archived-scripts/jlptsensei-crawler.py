import requests
import json
from bs4 import BeautifulSoup as soup

files = {
  'n1': [],
  'n2': [],
  'n3': [],
  'n4': [],
  'n5': [],
}
for i in range(1, 2):
  page = soup(requests.get(f'https://jlptsensei.com/complete-japanese-particles-list/page/{i}/').content, 'html.parser')
  for particle in page.find_all('tr', {'class': 'jl-row'}):
    card = [particle.find('td', f'jl-td-{i}').text.strip().replace('~', '...').replace('〜', '...').replace('～', '...').replace('+', '...').replace('・', ' / ').replace('」', ' ').replace('「',  '') for i in ['gr', 'gj', 'gm', 'nl']]
    if '【' in card[1]:
      card[1] = card[1].split('【')[1].replace('】', '')
    files[card[3].lower()].append(' | '.join(card[:3]))

#for key, val in files.items():
#  with open(f'jlptsensei-particles-{key}.txt', 'w') as p_file:
#    for card in val:
#      p_file.write(card + '\n')

with open(f'jlptsensei-particles.json', 'w') as p_file:
  p_file.write(json.dumps(files))
