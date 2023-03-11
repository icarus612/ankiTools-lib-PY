from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import json
import sys
from time import sleep

def search(word_list, key_prefix="ic_jp_", key_suffix='.mp3'):
  def check_val(val):
    return val if val else ""

  audio_json = {}
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
  driver.get('https://www.japanesepod101.com/japanese-dictionary/')

  try:
    driver.find_element(By.CLASS_NAME, 'lightBox-signup-header-close').click()
    driver.find_element(By.CSS_SELECTOR, 'label[for="dc-search-common"]').click()
  except Exception as e: 
    print(e)

  for raw_word in word_list: 
    prefix = check_val(key_prefix)
    suffix = check_val(key_suffix)
    word = ''.join(raw_word.split(' '))
    file_path = prefix + word + suffix

    try:
      search_bar = driver.find_element(By.ID, 'dc-search-input')
      search_bar.clear()
      search_bar.send_keys(word)

      driver.find_element(By.ID, 'dc-search-button').click()
      sleep(1)
      for element in driver.find_elements(By.CLASS_NAME, 'dc-result-row'):
        if element.find_element(By.CLASS_NAME, 'dc-vocab_romanization').get_attribute('innerHTML') == word:
          audio_json[file_path] = element.find_element(By.TAG_NAME, 'audio').find_element(By.TAG_NAME, 'source').get_attribute('src')
    
    except Exception as e:
      print(f'Error finding match for word: {raw_word}')

    return audio_json
