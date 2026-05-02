import datetime
import pytest
import os
import sys
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from Utility import config_reader

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#print("SYS PATH:", sys.path)
class InvalidWebDriverException(Exception):
    pass

@pytest.fixture()
def browser(request):
    browser = config_reader.read_configuration("app", "browser").strip().lower()

    print("Launching browser:", browser)

    if browser == "chrome":
        options = ChromeOptions()

        if os.getenv("CI"):
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")
        

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),options=options)

    elif browser == "firefox":
        options = FirefoxOptions()

        if os.getenv("CI"):
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")

        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )

    elif browser == "edge":
        options = EdgeOptions()

        if os.getenv("CI"):
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()),
            options=options
        )

    else:
        raise InvalidWebDriverException(f"Invalid WebDriver provided: {browser}")
    driver.maximize_window()
    app_url = config_reader.read_configuration("app","url")
    # print(f"App URL: '{app_url}'") --> to debug what url it pick up
    driver.get(app_url)
    WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState")=="complete")
    if request.cls:
        request.cls.driver=driver
    yield driver
    driver.quit()

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