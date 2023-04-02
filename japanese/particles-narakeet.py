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

			
audio_path = 'audio/particles/narakeet'
working_proxy = ''
def get_proxy_list():
  options = webdriver.ChromeOptions()
  options.add_argument("start-maximized")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_experimental_option('useAutomationExtension', False)
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
  driver.get("https://sslproxies.org/")
  proxies = [[td.get_attribute('innerHTML') for td in tr.find_elements(By.TAG_NAME, 'td')] for tr in driver.find_element(By.TAG_NAME, 'table').find_elements(By.TAG_NAME, 'tr')][1:]
  driver.quit()
  return [':'.join(proxy[:2]) for proxy in proxies]

def scrape_audio(proxy, val='wa'):
	try:
		options = webdriver.ChromeOptions()
		options.add_argument(f'--proxy-server={proxy}')
		driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
		driver.get(f'https://www.narakeet.com/languages/japanese-text-to-speech/')
	except Exception as e:
		print(e)
		return False

	for idx in range(8):
		sleep(2)
		try:
			format_select = Select(driver.find_element(By.ID, 'cfgAudioFormat'))
			format_select.select_by_value('mp3')
			voice_select = Select(driver.find_element(By.ID, 'cfgVideoVoice'))
			voice_select.select_by_value('yuriko')
			driver.find_element(By.CSS_SELECTOR, 'textarea.textarea').clear()
			driver.find_element(By.CSS_SELECTOR, 'textarea.textarea').send_keys(val.split('/')[0])
			driver.find_element(By.NAME, 'generateaudio').click()
			break
		except Exception as e:
			if idx == 7:
				print('Page load timeout.')
				driver.close()
				return False
			
	for idx in range(8):
		try:
			sleep(8)
			status = driver.find_element(By.CSS_SELECTOR, '[data-show-stage]').get_attribute('stage').lower().strip()
			print(status)
			if status == 'finished':					
				url = driver.find_element(By.CSS_SELECTOR, '[data-prop-link="result"]').get_attribute('href')
				driver.close()
				return url
			elif status == 'error':
				print('Audio creation error.')
				driver.close()
				return False
		except:
			if idx == 7:
				print('Audio creation timeout.')
				driver.close()
				return False

	# Just in case something somehow doesn't catch
	driver.close()
	return False

try: 
	os.mkdir(audio_path)
except:
	pass

for p in get_proxy_list():
	print(f'Attempting to use proxy: {p}')
	if scrape_audio(p):
		print(f'Success! Setting proxy ip to {p}')
		working_proxy = p
		break
	print('Moving on to next attempt.')

with open('./created-decks/jlptsensei-particles-current.json', 'r') as jlpt_json:
	raw_json = json.loads(jlpt_json.read())

for deck_name, deck in raw_json.items():
	with open(f'./jlptsensei-particles-{deck_name}.txt', 'w') as deck_file:
		for card in deck:
			file_name = f"ic_nrkt_{card[0].replace('...', '-').replace(' ', '').replace('/', '-')}.mp3"
			audio_url = scrape_audio(working_proxy, card[1])
			if audio_url: 
				audio = requests.get(audio_url)
				card.append(f'[sound:{file_name}]')
				with open(os.path.join(audio_path, file_name), 'wb') as audio_file:
					audio_file.write(audio.content)


			deck_file.write(' | '.join(card) + '\n')

