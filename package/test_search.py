from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture()
def setup_and_teardown():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    yield driver
    driver.quit()
    

def test_search_a_valid_element(setup_and_teardown):
    driver.find_element(By.XPATH,"//input[@name='search']").send_keys("macbook")
    driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
    assert driver.find_element(By.LINK_TEXT,"MacBook Pro").is_displayed()
    # driver.save_screenshot("MacBook.png")
    
    
def test_search_a_invalid_element(setup_and_teardown):
    driver.find_element(By.XPATH,"//input[@name='search']").send_keys("acer")
    driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
    expected_text = "There is no product that matches the search criteria."
    actual_text =driver.find_element(By.XPATH,"//div[@id='content']//p[text()='There is no product that matches the search criteria.']").text
    assert actual_text == expected_text
    # driver.save_screenshot("invalid.png")
    
def test_search_with_no_context(setup_and_teardown):
    # driver.find_element(By.XPATH,"//input[@name='search']").send_keys("acer")
    driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
    expected_text = "There is no product that matches the search criteria."
    actual_text =driver.find_element(By.XPATH,"//div[@id='content']//p[text()='There is no product that matches the search criteria.']").text
    assert actual_text == expected_text