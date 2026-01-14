from base_page import basepage
from components import search_bar

class home_page(basepage):
    def __init__(self,driver):
        self.driver = driver
        self.search_bar = search_bar(driver)
        
    def search_product(self,product_name: str):
        self.search_bar.search_for(product_name)