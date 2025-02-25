import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = "normal"
chrome_options.page_load_strategy = "eager"
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--window-size=700,700")
chrome_options.add_argument("--disable-cache")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


start_time = time.time()

driver.get("https://www.wikipedia.org/")

end_time = time.time()

result = start_time - end_time

print(result)

