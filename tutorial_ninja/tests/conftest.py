import datetime
import pytest
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from Utility import config_reader

class InvalidWebDriverException(Exception):
    pass

@pytest.fixture()
def browser(request):
    browser = config_reader.read_configuration("app","browser").strip().lower()
    if browser == ("chrome"):
        driver = webdriver.Chrome()
    elif browser == ("firefox"):
        driver = webdriver.Firefox()
    elif browser == ("edge"): 
        driver = webdriver.Edge()
    else:
        raise InvalidWebDriverException(f"Invalid WebDriver provided: {browser}")
    driver.maximize_window()
    app_url = config_reader.read_configuration("app","url")
    # print(f"App URL: '{app_url}'") --> to debug what url it pick up
    driver.get(app_url)
    request.cls.driver=driver
    yield driver
    driver.quit()
    
@pytest.fixture()
def login_page(browser):
    driver=browser
    driver.find_element(By.XPATH,"//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT,"Login").click()
    return driver

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        if hasattr(item, "cls") and item.cls:
            driver = getattr(item.cls, "driver", None)
            if driver:
                os.makedirs("screenshots", exist_ok=True)
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                name = report.nodeid.replace("::", "_").replace("/", "_").replace("\\", "_")
                driver.save_screenshot(f"screenshots/{name}_{timestamp}.png")