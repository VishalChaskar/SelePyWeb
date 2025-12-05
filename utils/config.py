# utils/config.py
import os


class Config:


    BASE_URL = os.getenv('BASE_URL', 'https://rahulshettyacademy.com/AutomationPractice/')
    BROWSER = os.getenv('BROWSER', 'chrome')  # 'chrome' or 'firefox'
    HEADLESS = os.getenv('HEADLESS', 'false').lower() in ('1', 'true', 'yes')
    IMPLICIT_WAIT = int(os.getenv('IMPLICIT_WAIT', '10'))
    PAGE_LOAD_TIMEOUT = int(os.getenv('PAGE_LOAD_TIMEOUT', '30'))

config = Config()
