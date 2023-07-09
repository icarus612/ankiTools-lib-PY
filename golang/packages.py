import requests
from bs4 import BeautifulSoup as soup
from sys import argv 

lib = argv[1] if len(argv) > 1 else 'fmt'
#should_remove_start = len(argv) <= 2  or argv[2].lower() not in ['0', 'false', 'f', 'n', 'no']
page =  soup(requests.get(f'https://pkg.go.dev/{lib}@go1.20.5').content, 'html.parser')
cards = []

for el in [i.find('span') for i in page.find_all('h4') if 'func' in i.text]:
  name = el.find("a").text.strip()
  func = f'{lib}.{name}()'
  info_start = f'<b>{lib.capitalize()} function</b> used to'
  p_el = el.find_next('p')
  info_end = p_el.text[len(name) + 1:].replace('\n', '').split(' ') if p_el else ['']
  if len(info_end[0]) > 0 and info_end[0][-1] == 's': 
    info_end[0] = info_end[0][:-1]
  with_options = el.find_next('div').find('pre').text
  info = info_start + ' ' + ' '.join(info_end)
  cards.append([func, info, '', with_options])

with open(f'{lib}.txt', 'w') as file:
  file.writelines([f'{" | ".join(i)} \n' for i in cards])	