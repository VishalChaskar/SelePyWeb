# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver


    def open(self, url):
        self.driver.get(url)


    def find(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))


    def click(self, locator, timeout=10):
        el = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        el.click()


    def type(self, locator, text, timeout=10):
        el = self.find(locator, timeout)
        el.clear()
        el.send_keys(text)


    def is_visible(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False


def get_text(self, locator, timeout=5):
    return self.find(locator, timeout).text