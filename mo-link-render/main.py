from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # chạy không mở cửa sổ
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)
driver.get("https://example.com")  # thay link của bạn
time.sleep(5)
driver.quit()
