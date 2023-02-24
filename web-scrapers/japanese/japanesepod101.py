import requests
from bs4 import BeautifulSoup as soup
from os import mkdir, getcwd, mkdir
import re

url = 'https://www.japanesepod101.com/learningcenter/reference/dictionary_post'
data = {
  'post': 'dictionary_reference',
  'match_type': 'exact',
  'search_query': 'wa',
  'common': 'true'
}

headers = {
  "accept": "*/*",
  "accept-language": "en-US,en;q=0.9",
  "cache-control": "no-cache",
  "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
  "pragma": "no-cache",
  "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
  "sec-ch-ua-mobile": "?0",
  "sec-ch-ua-platform": "\"Linux\"",
  "sec-fetch-dest": "empty",
  "sec-fetch-mode": "cors",
  "sec-fetch-site": "same-origin",
  "x-requested-with": "XMLHttpRequest",
  "Referer": "https://www.japanesepod101.com/japanese-dictionary/",
  "Referrer-Policy": "strict-origin-when-cross-origin"
}

cookies = {
"PHPSESSID": "606757d1dgnek6eij418dvgh71",
"guid": "a0541665d7689c1b9eb190a74df9994951990137",
"clickpath": "https%3A%2F%2Fwww.youtube.com%2F%7C%2Flearn-with-pdf%3Fsrc%3Dyoutube_mastocomp_200_must_know_words_yt_desc_%28pdf_lp%29%26utm_medium%3Dyt_desc%26utm_content%3Dyt_desc_%28pdf_lp%29%26utm_campaign%3Dmastocomp_200_must_know_words%26utm_term%3D%28not-set%29%26utm_source%3Dyoutube%26utm_source%3Dyoutube%7Cyoutube_mastocomp_200_must_know_words_yt_desc_%28pdf_lp%29%7Cyoutube_core_words_episode_10_yt_desc_%28pdf_lp%29%7Cyoutube_core_words_episode_1_yt_desc_%28pdf_lp%29",
"guidmember": "4116586",
"_amember_ru": "ellishogan95@gmail.com",
"_amember_rp": "8a869fd42a982a7e40a02971ad73e506"
}
page = soup(requests.post(url=url, data=data, headers=headers, cookies=cookies).content, 'html.parser')

print(page)
#cards = []
#for el in page.find("table", {"class": "table-bordered"}).find_all('tr'):
#	td = el.find_all('td')
#	if len(td) <= 1: 
#		continue
#	cards.append(''.join(f'<b>Os method</b> used to {td[1].find("p").text.lower()} | {td[1].find("a").text}'))
#	with open(f'{getcwd()}/output.txt', 'w') as file:
#		file.writelines([f'{i} \n' for i in cards])
