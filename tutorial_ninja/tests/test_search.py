import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        wait = WebDriverWait(self.driver, 20)
        self.driver.find_element(By.XPATH,"//input[@name='search']").send_keys("macbook")
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
        displayed_product = wait.until(EC.visibility_of_element_located((By.LINK_TEXT,"MacBook Pro")))
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