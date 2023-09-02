import requests
from bs4 import BeautifulSoup as soup

cards = []
req = soup(requests.get('https://numpy.org/doc/stable/reference/arrays.ndarray.html').content, 'html.parser')

urls = [i.find('a')["href"] for i in req.find_all(class_='toctree-l3')]


for url in urls:
	try:
		print(f"Retrieving definition for {url.partition('.')[2][:-5]}")
		full = soup(requests.get(f"https://numpy.org/doc/stable/reference/{url}").content, 'html.parser')
		item = full.find('dl', class_="py")
		full_m = item.find('dt', class_='sig-object')
		front = f"ndarray.{full_m.find('span', {'sig-name'}).text}"
		if 'method' in [i.text for i in full.find_all('p')]:
			front += f"(<i>{''.join([i.text for i in full_m.find_all({'class': 'sig-param'})])}</i>)"
		back = item.find('dd').find('p').text.replace('\n', '')
		cards.append([front, back])
	except Exception as e:
		print(e)
with open(f'numpy_arrays.txt', 'w') as file:
	file.writelines([f'{" | ".join(i)} \n' for i in cards])