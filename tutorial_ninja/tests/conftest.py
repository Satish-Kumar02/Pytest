import datetime
import pytest
import os
# import shutil
# import allure
import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from tutorial_ninja.Utility import config_reader
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from selenium.webdriver.edge.options import Options as EdgeOptions

class InvalidWebDriverException(Exception):
    pass

# @pytest.fixture(params=["Chrome","Firefox","edge"])
@pytest.fixture()
def browser(request):
    browser = config_reader.read_configuration("app","browser").lower()
    if browser.__eq__("Chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"): 
        driver = webdriver.Edge()
    else:
        raise InvalidWebDriverException(f"Invalid WebDriver provided: {browser}")
    # if request.param == "Chrome":
    #     options = ChromeOptions()
    #     options.add_argument("--headless")
    #     options.add_argument("--window-size=1920,1080")
    #     driver = webdriver.Chrome(options=options)
    # elif request.param == "Firefox":
    #     options = FirefoxOptions()
    #     options.add_argument("-headless")   # <-- THIS is the key
    #     options.add_argument("--width=1920")
    #     options.add_argument("--height=1080")
    #     driver = webdriver.Firefox(options=options)
    # else:
    #     options = EdgeOptions()
    #     options.add_argument("--headless")
    #     options.add_argument("--window-size=1920,1080")
    #     driver = webdriver.Edge(options=options)
    # driver = webdriver.Chrome()
    driver.maximize_window()
    app_url = config_reader.read_configuration("app","url")
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

# Allure_Results_Dir ="Reports"

# @pytest.hookimpl(tryfirst=True)
# def pytest_sessionstart(session):
#     if os.path.exists(Allure_Results_Dir):
#         shutil.rmtree(Allure_Results_Dir)
#         os.mkdir(Allure_Results_Dir, exist_ok=True)