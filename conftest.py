import os
import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_chrome_driver():
    options = Options()

    # Headless mode for Docker/CI — reads HEADLESS env var
    if os.getenv("HEADLESS", "false").lower() == "true":
        options.add_argument("--headless=new")

    # Required in Docker — without these Chrome WILL crash
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--remote-debugging-port=9222")

    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)


@pytest.fixture(scope="class")
def setup(request):
    driver = get_chrome_driver()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield driver
    driver.quit()


# Screenshot on failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver") or getattr(item.cls, "driver", None) if item.cls else None
        if driver:
            os.makedirs("reports/screenshots", exist_ok=True)
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            driver.save_screenshot(f"reports/screenshots/{item.name}_{ts}.png")
