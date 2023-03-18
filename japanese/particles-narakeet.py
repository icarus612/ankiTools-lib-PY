from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import requests
import json
import os
from time import sleep

def get_proxy_list():
  options = webdriver.ChromeOptions()
  options.add_argument("start-maximized")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_experimental_option('useAutomationExtension', False)
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
  driver.get("https://sslproxies.org/")
  proxies = [[td.get_attribute('innerHTML') for td in tr.find_elements(By.TAG_NAME, 'td')] for tr in driver.find_element(By.TAG_NAME, 'table').find_elements(By.TAG_NAME, 'tr')][1:]
  driver.quit()
  return [':'.join(proxy[:2]) for proxy in proxies if proxy[4] == 'elite proxy']

#proxies = get_proxy_list()
audio_path = 'audio/particles/narakeet'
proxy_idx = 0

try: 
	os.mkdir(audio_path)
except:
	pass

with open('./created-decks/jlptsensei-particles.json', 'r') as jlpt_json:
	raw_json = json.loads(jlpt_json.read())

for deck_name, deck in raw_json.items():
	with open(f'./jlptsensei-particles-{deck_name}.txt', 'w') as deck_file:
		for card in deck:
			file_name = f"ic_nrkt_{card[0].replace('...', '-').replace(' ', '').replace('/', '-')}.mp3"
			#proxy = proxies[proxy_idx % len(proxies)]
			#print(f'Proxy selected: {proxy}')
			#options = webdriver.ChromeOptions()
			#options.add_argument(f'--proxy-server={proxy}')
			driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
			driver.get(f'https://www.narakeet.com/languages/japanese-text-to-speech/')
			for _ in range(8):
				sleep(1)
				try:
					format_select = Select(driver.find_element(By.ID, 'cfgAudioFormat'))
					format_select.select_by_value('mp3')
					voice_select = Select(driver.find_element(By.ID, 'cfgVideoVoice'))
					voice_select.select_by_value('yuriko')
					driver.find_element(By.CLASS_NAME, 'textarea').clear()
					driver.find_element(By.CLASS_NAME, 'textarea').send_keys(card[1].split('/')[0])
					driver.find_element(By.NAME, 'generateaudio').click()
				except:
					sleep(5)

			for _ in range(8):
				status = driver.find_elements(By.CSS_SELECTOR, '.dialog.wide:not(.hidden)')
				print(*[stat.find_element(By.TAG_NAME, 'h1').get_attribute('innerHTML') for stat in status])
				
				if status == 'finished':
					card.append(f'[sound:{file_name}]')
					audio = requests.get(driver.find_element(By.CSS_SELECTOR, '[data-prop-link="result"]').get_attribute('href'))
					with open(os.path.join(audio_path, file_name), 'wb') as audio_file:
						audio_file.write(audio.content)
					break

			driver.quit()
			deck_file.write(' | '.join(card) + '\n')

