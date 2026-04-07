import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from tutorial_ninja.page_objects.home_page import home_page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from unittest import result

@pytest.mark.usefixtures("browser") 
class TestSearch:
    def test_search_a_valid_element(self):
        product_name = "macbook"
        home = home_page(self.driver)
        results = home.search_product("macbook")
        allure.attach(self.driver.get_screenshot_as_png(),name="macbook",attachment_type=allure.attachment_type.PNG)
        assert results.is_product_displayed("macbook")
        # self.driver.save_screenshot("MacBook.png")
             
    def test_search_a_invalid_element(self):
        product_name = "acer"
        home = home_page(self.driver)
        results = home.search_product("acer")
        allure.attach(self.driver.get_screenshot_as_png(),name="acer",attachment_type=allure.attachment_type.PNG)
        assert results.is_no_product_displayed()
        
    def test_search_with_no_context(self):
        product_name = ""
        home = home_page(self.driver)
        results = home.search_product("acer")
        allure.attach(self.driver.get_screenshot_as_png(),name="",attachment_type=allure.attachment_type.PNG)
        assert results.is_product_displayed("")