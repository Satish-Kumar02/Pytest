from selenium import webdriver
from selenium.webdriver.common.by import By

def test_search_a_element():
    driver = webdriver.Chrome()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.XPATH,"//input[@name='search']").send_keys("macbook")
    driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
    assert driver.find_element(By.LINK_TEXT,"MacBook Pro").is_displayed()
    # driver.save_screenshot("MacBook.png")
    driver.quit()