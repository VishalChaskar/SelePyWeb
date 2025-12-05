from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    # Locators

    header_text = (By.XPATH, "//h1[normalize-space()='Practice Page']")

    # Actions

    def get_title(self):
        return self.driver.title

    def wait_for_page_load(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete")

    def is_header_displayed(self):
        header = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.header_text))
        return header.is_displayed()
