import requests
from bs4 import BeautifulSoup as soup
from os import mkdir, getcwd, mkdir
import re

url = 'https://www.japanesepod101.com/japanese-word-lists/?coreX=100'


page = soup(requests.get(url=url).content, 'html.parser')

print(page)
cards = []
for el in page.find("table", {"class": "table-bordered"}).find_all('tr'):
	td = el.find_all('td')
	if len(td) <= 1: 
		continue
	cards.append(''.join(f'<b>Os method</b> used to {td[1].find("p").text.lower()} | {td[1].find("a").text}'))
	with open(f'{getcwd()}/output.txt', 'w') as file:
		file.writelines([f'{i} \n' for i in cards])