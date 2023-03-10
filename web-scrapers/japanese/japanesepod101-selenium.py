from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import json
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.japanesepod101.com/japanese-dictionary/')

try:
  driver.find_element(By.CLASS_NAME, 'lightBox-signup-header-close').click()
  driver.find_element(By.CSS_SELECTOR, 'label[for="dc-search-common"]').click()
except Exception as e: 
  print(e)

with open('particles.txt') as old_cards, open('output.txt', 'w') as new_cards, open('audio-files.json', 'w') as audio:
  audio_files = {}
  for card in old_cards.readlines(): 
    try:
      clist = [a.strip() for a in card.split('\t')]
      word = '-'.join(clist[1].split(' '))
      file_name = f'ic_jp_{word}.mp3'
      clist[4] = f'[sound:{file_name}]'

      search_bar = driver.find_element(By.ID, 'dc-search-input')
      search_bar.clear()
      search_bar.send_keys(word)

      driver.find_element(By.ID, 'dc-search-button').click()
      sleep(1)
      for element in driver.find_elements(By.CLASS_NAME, 'dc-result-row'):
        if element.find_element(By.CLASS_NAME, 'dc-vocab_romanization').get_attribute('innerHTML') == word:
          audio_files[file_name] = element.find_element(By.TAG_NAME, 'audio').find_element(By.TAG_NAME, 'source').get_attribute('src')
          new_cards.write(' | '.join(clist) + '\n')
          break
    
    except Exception as e:
      print(f'Error finding match for word: {word}')
      print(e)
  audio.write(json.dumps(audio_files))
