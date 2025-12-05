# pages/practice_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PracticePage(BasePage):


    CHECKBOX = (By.ID, 'checkBoxOption1')
    RADIO_OPTION = (By.CSS_SELECTOR, "input[value='radio2']")
    DROPDOWN = (By.ID, 'dropdown-class-example')
    SUGGESTION = (By.ID, 'autocomplete')
    SUGGESTION_LIST = (By.CLASS_NAME, 'ui-menu-item')
    ALERT_BTN = (By.ID, 'alertbtn')
    CONFIRM_BTN = (By.ID, 'confirmbtn')


def go_to(self):
    self.open('/')


def click_checkbox(self):
    self.click(self.CHECKBOX)


def is_checkbox_selected(self):
    return self.driver.find_element(*self.CHECKBOX).is_selected()


def click_radio(self):
    self.click(self.RADIO_OPTION)

def select_dropdown(self, visible_text):
    from selenium.webdriver.support.ui import Select
    select = Select(self.find(self.DROPDOWN))
    select.select_by_visible_text(visible_text)

def type_suggestion(self, text):
    self.type(self.SUGGESTION, text)

def get_suggestions(self):
    return [el.text for el in self.driver.find_elements(*self.SUGGESTION_LIST) if el.text]

def click_alert(self):
    self.click(self.ALERT_BTN)

def click_confirm(self):
    self.click(self.CONFIRM_BTN)
