import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from page_objects.home_page import home_page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from unittest import result

@pytest.mark.usefixtures("browser")
class TestCurrency:
    def test_euro_crrency(self):
        currency_name = "EUR"
        home = home_page(self.driver)
        result = home.check_currency(currency_name)
        allure.attach(self.driver.get_screenshot_as_png(),name="Euro",attachment_type=allure.attachment_type.PNG)
        assert result.is_product_displayed("EURO")
        
        