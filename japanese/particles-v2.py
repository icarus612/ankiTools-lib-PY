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

audio_path = 'particles-v2-audio'

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
			
			driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
			params = {
				"latitude": 34.0207305,
				"longitude": -118.6919153,
				"accuracy": 100
			}

			driver.execute_cdp_cmd("Page.setGeolocationOverride", params)
			driver.get(f'https://www.narakeet.com/languages/japanese-text-to-speech/')

			format_select = Select(driver.find_element(By.ID, 'cfgAudioFormat'))
			format_select.select_by_value('mp3')

			voice_select = Select(driver.find_element(By.ID, 'cfgVideoVoice'))
			voice_select.select_by_value('yuriko')

			driver.find_element(By.CLASS_NAME, 'textarea').clear()
			driver.find_element(By.CLASS_NAME, 'textarea').send_keys(card[1].split('/')[0])
			
			driver.find_element(By.NAME, 'generateaudio').click()

			for _ in range(8):
				sleep(5)
				if driver.find_element(By.CSS_SELECTOR, '[data-show-stage]').get_attribute('stage').lower().strip() == 'finished':
					card.append(f'[sound:{file_name}]')
					audio = requests.get(driver.find_element(By.CSS_SELECTOR, '[data-prop-link="result"]').get_attribute('href'))
					with open(os.path.join(audio_path, file_name), 'wb') as audio_file:
						audio_file.write(audio.content)
					break

			deck_file.write(' | '.join(card) + '\n')
