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

with open('./created-decks/jlptsensei-particles.json', 'r') as jlpt_json:
  print(json.loads(jlpt_json.read()))
