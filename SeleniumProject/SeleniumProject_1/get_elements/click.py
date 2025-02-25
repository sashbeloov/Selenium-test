import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.wikipedia.org/")

time.sleep(3)

login_button = driver.find_element("xpath", "//*[@id='searchInput']")
login_button.click()

search_field = driver.find_element("xpath", "//*[@id='searchInput']")
search_field.send_keys("city")
time.sleep(3)

search_field.clear()

search_field.send_keys("tashkent")
time.sleep(3)