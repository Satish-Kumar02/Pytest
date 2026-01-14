from selenium import webdriver
from selenium.webdriver.common.by import By
from Page_objects import base_page

class search_bar(base_page):
    _search_input = (By.XPATH,"//input[@name='search']")
    _search_button = (By.XPATH,"//button[@class='btn btn-default btn-lg']")
    
    def search_for(self, text :str):
        self.type(self._search_input, text)
        self.click(self._search_button) 