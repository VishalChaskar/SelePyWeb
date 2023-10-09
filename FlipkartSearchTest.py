import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
driver = webdriver.Chrome(chrome_options)
driver.maximize_window()
driver.get("https://www.flipkart.com")
driver.save_screenshot('Screenshots/test1.png')
time.sleep(3)

title = "Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!"

assert title == driver.title

driver.save_screenshot('Screenshots/test.png')

