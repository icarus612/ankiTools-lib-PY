from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from sys import argv
import json
from time import sleep

end_point = argv[1] if len(argv) > 1 else '100'
audio_urls = {}
cards_lst = []
page = 1

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(f'https://www.japanesepod101.com/japanese-word-lists/?coreX={end_point}')

try:
  driver.find_element(By.CLASS_NAME, 'lightBox-signup-header-close').click()
except Exception as e: 
  print(e)

try:
	driver.find_element(By.CLASS_NAME, 'js-show-sign-in-form').click()
	sleep(1)
	email = input("Enter Login Email: ")
	password = input("Enter Login Password: ")
	driver.find_element(By.CLASS_NAME, 'js-sign-in--a__email-input').send_keys(email)
	driver.find_element(By.CLASS_NAME, 'js-sign-in--a__password-input').send_keys(password)
	driver.find_element(By.CLASS_NAME, 'js-ln-sign-in-button').click()
	sleep(1)
except Exception as e: 
  print(e)

while True:
	print(f'Getting elements for page {page}')
	page += 1

	for element in driver.find_elements(By.CLASS_NAME, 'wlv-item'):
		try: 
			higarana = element.find_element(By.CLASS_NAME, 'js-wlv-word-field-kana').find_element(By.CLASS_NAME, 'wlv-item__word').get_attribute('innerHTML')
			romaji = element.find_element(By.CLASS_NAME, 'js-wlv-word-field-romaji').get_attribute('innerHTML')
			english = element.find_element(By.CLASS_NAME, 'wlv-item__english').get_attribute('innerHTML')
			file_name = f'ic_jp_{romaji}.mp3'
			sound = f'[sound:{file_name}]'
			audio_urls[file_name] = element.find_element(By.TAG_NAME, 'audio').get_attribute('src')
			cards_lst.append(' | '.join([higarana, romaji, english , "", sound]) + '\n')
		except:
			print('Element missing content')

	try: 
		driver.find_element(By.CLASS_NAME, 'r101-pagination--b').find_element(By.CSS_SELECTOR, 'a[rel="next"]').click()
		sleep(1)
	except:
		print(f'End of list at page {page}')
		break 

with open('output.txt', 'w') as core_words, open('audio-files.json', 'w') as audio_file:
	core_words.writelines(cards_lst)
	audio_file.write(json.dumps(audio_urls))

print('Exit status: 0')