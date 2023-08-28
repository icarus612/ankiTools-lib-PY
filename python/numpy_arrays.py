import requests
from bs4 import BeautifulSoup as soup

cards = []
req = soup(requests.get('https://numpy.org/doc/stable/reference/arrays.ndarray.html').content, 'html.parser')

urls = [i.href for i in req.find_all()]


for url in urls:
	item = soup(requests.get(url).content, 'html.parser')
	front = item.find()
	back = item.find()
	card.append([front, back])
	
with open(f'numpy_arrays.txt', 'w') as file:
	file.writelines([f'{" | ".join(i)} \n' for i in cards])