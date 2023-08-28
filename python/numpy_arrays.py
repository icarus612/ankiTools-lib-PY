import requests
from bs4 import BeautifulSoup as soup

req = soup(requests.get('https://numpy.org/doc/stable/reference/arrays.ndarray.html').content, 'html.parser')