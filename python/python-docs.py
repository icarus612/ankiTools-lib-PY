import requests
from bs4 import BeautifulSoup as soup
from os import mkdir, getcwd, mkdir
import re

page =  soup(requests.get('https://docs.python.org/3/library/time.html').content, 'html.parser')
cards = []
for el in page.find_all('dl'):
	item = el.find('dt', {"class": "sig-object"})
	if item:
		raw_func = item.text.strip().replace('¶', '').replace(' → int', '').replace(' → float', '')