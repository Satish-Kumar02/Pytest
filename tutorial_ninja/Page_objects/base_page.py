from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class basepage:
    def __init__(self,driver,timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(driver,timeout)
        
    def click(self,locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        
    def type(self,locator,text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
        
    def get_text(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text
    
    def is_visible(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
    
    def is_element_displayed(self, locator):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(locator)
            ).is_displayed()
        except:
            return False