import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.wikipedia.org/")

time.sleep(3)

driver.find_elements("id", "js-link-box-en")[0].click()

print(driver.find_elements("id", "js-link-box-en"))

time.sleep(3)

