from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

# @pytest.fixture()
# def setup_and_teardown():
#     global self.driver
#     self.driver = webdriver.Chrome()
#     self.driver.maximize_window()
#     self.driver.get("https://tutorialsninja.com/demo/")
#     yield self.driver
#     self.driver.quit()
   
@pytest.mark.usefixtures("browser") 
class TestSearch:
    def test_search_a_valid_element(self):
        self.driver.find_element(By.XPATH,"//input[@name='search']").send_keys("macbook")
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
        assert self.driver.find_element(By.LINK_TEXT,"MacBook Pro").is_displayed()
        # self.driver.save_screenshot("MacBook.png")
        
        
    def test_search_a_invalid_element(self):
        self.driver.find_element(By.XPATH,"//input[@name='search']").send_keys("acer")
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
        expected_text = "There is no product that matches the search criteria."
        actual_text =self.driver.find_element(By.XPATH,"//div[@id='content']//p[text()='There is no product that matches the search criteria.']").text
        assert actual_text == expected_text
        # self.driver.save_screenshot("invalid.png")
        
    def test_search_with_no_context(self):
        # self.driver.find_element(By.XPATH,"//input[@name='search']").send_keys("acer")
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
        expected_text = "There is no product that matches the search criteria."
        actual_text =self.driver.find_element(By.XPATH,"//div[@id='content']//p[text()='There is no product that matches the search criteria.']").text
        assert actual_text == expected_text