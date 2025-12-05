import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    request.cls.driver = driver
    yield
    driver.quit()