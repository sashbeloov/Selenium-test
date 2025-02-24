import time  # Vaqtni kutish uchun time kutubxonasini import qilamiz
from selenium import webdriver  # Seleniumning webdriver modulini import qilamiz
from webdriver_manager.chrome import ChromeDriverManager  # ChromeDriverManager kutubxonasini import qilamiz
from selenium.webdriver.chrome.service import Service  # Seleniumning Service klassini import qilamiz

service = Service(executable_path=ChromeDriverManager().install())  # ChromeDriver'ni o'rnatib, yo'lini olish
driver = webdriver.Chrome(service=service)  # Chrome brauzerini ishga tushurish va `driver` ob'ektini yaratish
driver.get("https://github.com/")  # Github saytiga o'tish

time.sleep(5)  # 5 soniya kutish (saytni to'liq yuklash uchun vaqt berish)

driver.back()  # Avvalgi sahifaga o'tish (bu holda https://www.google.com/ kabi bo'lishi mumkin)

time.sleep(10)  # 10 soniya kutish (brauzer navigatsiyasidan keyin kutish)

driver.forward()  # Oldingi sahifaga qaytish (yani, `back()` yordamida ketgan sahifaga)

time.sleep(3)  # 3 soniya kutish

driver.refresh()  # Saytni yangilash (refresh qilish)

time.sleep(3)  # 3 soniya kutish
