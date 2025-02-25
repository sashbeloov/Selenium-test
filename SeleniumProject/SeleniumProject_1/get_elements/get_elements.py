import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

import os
os.environ['WDM_LOCAL'] = '1'

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.wiktionary.org/")
time.sleep(3)

driver.find_element("id", "hiddenLanguageInput").click()

time.sleep(3)