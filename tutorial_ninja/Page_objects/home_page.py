from page_objects.search_results import search_results
from page_objects import base_page
from components.search_bar import search_bar
from selenium.webdriver.common.by import By

class home_page(base_page.basepage):
    def __init__(self,driver):
        super().__init__(driver)
        self.search_bar = search_bar(driver)
        
    def search_product(self,product_name: str):
        self.search_bar.search_for(product_name)
        return search_results(self.driver)
        # print(search_bar, type(search_bar))