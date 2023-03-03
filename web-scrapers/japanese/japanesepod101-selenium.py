from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.japanesepod101.com/japanese-dictionary/")

try:
  driver.find_element(By.CLASS_NAME, "lightBox-signup-header-close").click()
  driver.find_element(By.CSS_SELECTOR, "label[for='dc-search-common']").click()
  driver.find_element(By.ID, "dc-search-input").send_keys("wa")
  driver.find_element(By.ID, "dc-search-button").click()

except Exception as e: 
  print(e)




sleep(1000)