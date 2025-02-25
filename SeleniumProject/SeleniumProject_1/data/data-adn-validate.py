import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

import os
os.environ['WDM_LOCAL'] = '1'

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.wikipedia.org/")

url = driver.current_url
print(f"Web saytning url manzili: {url}")
assert url == "https://www.wikipedia.org/", "url manzili topilmadi"

current_title = driver.title
print(f"title: {current_title}")
assert current_title == "Wikipedia", "incorrect title"

html_code = driver.page_source  # html kodelar
print(html_code)

time.sleep(3)