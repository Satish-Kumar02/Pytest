import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from Page_objects.home_page import home_page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("browser") 
class TestSearch:
    def test_search_a_valid_element(self):
        home = home_page(self.driver)
        displayed_product = home.search_product("macbook")
        allure.attach(self.driver.get_screenshot_as_png(),name="macbook",attachment_type=allure.attachment_type.PNG)
        assert displayed_product.is_displayed()
        # self.driver.save_screenshot("MacBook.png")
        
        
    def test_search_a_invalid_element(self):
        wait = WebDriverWait(self.driver,10)
        self.driver.find_element(By.XPATH,"//input[@name='search']").send_keys("acer")
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
        expected_text = "There is no product that matches the search criteria."
        message_element =wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@id='content']//p[text()='There is no product that matches the search criteria.']")))
        actual_text = message_element.text
        allure.attach(self.driver.get_screenshot_as_png(),name="no product",attachment_type=allure.attachment_type.PNG)
        assert "no product" in actual_text
        # self.driver.save_screenshot("invalid.png")
        
    def test_search_with_no_context(self):
        wait = WebDriverWait(self.driver,10)
        # self.driver.find_element(By.XPATH,"//input[@name='search']").send_keys("acer")
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
        expected_text = "There is no product that matches the search criteria."
        message_element =wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@id='content']//p[text()='There is no product that matches the search criteria.']")))
        actual_text = message_element.text
        allure.attach(self.driver.get_screenshot_as_png(),name="no product",attachment_type=allure.attachment_type.PNG)
        assert "no product" in actual_text