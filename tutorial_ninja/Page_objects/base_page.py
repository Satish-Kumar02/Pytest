from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class basepage:
    def __init__(self,driver,timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(driver,timeout)
        
    