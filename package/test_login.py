import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.XPATH,"//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT,"Login").click()
    yield driver
    driver.quit()
    
    
# credentials = [ "mail,password,expected",
#     (2016sathishkumar.sk@gmail.com, Spectra@1902, success)
# ]

def test_Login_with_valid_credentials(driver):
    wait = WebDriverWait(driver,20)
    driver.find_element(By.ID,"input-email").send_keys("2016sathishkumar.sk@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("Spectra@1902")
    driver.find_element(By.CSS_SELECTOR,"input[type=submit]").click()
    edit_account = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Edit Account")))
    assert edit_account.is_displayed()
       
def test_Login_with_correct_username_invalid_password(driver):
    wait = WebDriverWait(driver,20)
    driver.find_element(By.ID,"input-email").send_keys("2016sathishkumar.sk@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("Reaper@1902")
    driver.find_element(By.CSS_SELECTOR,"input[type=submit]").click()
    error_alert = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'alert-danger') and contains(.,'Warning: No match')]")))
    assert error_alert.is_displayed()

def test_Login_with_incorrect_username_valid_password(driver):
    wait = WebDriverWait(driver,20)
    driver.find_element(By.ID,"input-email").send_keys("sathiskumark192@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("Spectra@1902")
    driver.find_element(By.CSS_SELECTOR,"input[type=submit]").click()
    error_alert = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'alert-danger') and contains(.,'Warning: No match')]")))
    assert error_alert.is_displayed()
    
def test_Login_with_incorrect_username_invalid_password(driver):
    wait = WebDriverWait(driver,20)
    driver.find_element(By.ID,"input-email").send_keys("sathiskumark192@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("Reaper@1902")
    driver.find_element(By.CSS_SELECTOR,"input[type=submit]").click()
    error_alert = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'alert-danger') and contains(.,'Warning: No match')]")))
    assert error_alert.is_displayed()