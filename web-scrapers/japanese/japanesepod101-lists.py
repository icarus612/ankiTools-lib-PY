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
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(f'https://www.japanesepod101.com/japanese-word-lists/?coreX={end_point}')

try:
  driver.find_element(By.CLASS_NAME, 'lightBox-signup-header-close').click()
except Exception as e: 
  print(e)

with open('output.txt', 'w') as core_words, open('audio-files.json', 'w') as audio_file:
	audio_urls = {}
	while True:
		try: 
			for element in driver.find_elements(By.CLASS_NAME, 'wlv-item'):
				higarana = element.find_element(By.CLASS_NAME, 'wlv-item__word').get_attribute('innerHTML')
				romaji = element.find_element(By.CLASS_NAME, 'js-wlv-word-field-romaji').get_attribute('innerHTML')
				english = element.find_element(By.CLASS_NAME, 'wlv-item__english').get_attribute('innerHTML')
				word = '-'.join(english.split(' '))
				file_name = f'ic_jp_{word}.mp3'
				sound = f'[sound:{file_name}]'

				audio_urls[file_name] = element.find_element(By.TAG_NAME, 'audio').get_attribute('src')
				core_words.write(' | '.join([higarana, romaji, english , sound]) + '\n')

			driver.find_element(By.CLASS_NAME, 'r101-pagination--b').find_element(By.CSS_SELECTOR, 'a[rel="next"]').click()
			sleep(1)
		except Exception as e:
			print('End of list.')
			break 

	audio_file.write(json.dumps(audio_urls))

print('Exit status: 0')