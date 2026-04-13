from page_objects.search_results import search_results
from page_objects import base_page
from components.search_bar import search_bar
from components.currency_dropdown import currency_dropdown
from selenium.webdriver.common.by import By
from page_objects.log_in import login_page

class home_page(base_page.basepage):
    def __init__(self,driver):
        super().__init__(driver)
        self.search_bar = search_bar(driver)
        self.currency_dropdown = currency_dropdown(driver)
        
    _product_prices = (By.CSS_SELECTOR, ".price")
    _my_account = (By.XPATH, "//a[@title='My Account']")
    _login_link = (By.LINK_TEXT, "Login")

    def is_currency_symbol_displayed(self, symbol: str) -> bool:
        prices = self.driver.find_elements(*self._product_prices)
        return any(symbol in price.text for price in prices)
        
    def search_product(self,product_name: str):
        self.search_bar.search_for(product_name)
        return search_results(self.driver)
        # print(search_bar, type(search_bar))
        
    def check_currency(self,currency_name: str):
        self.currency_dropdown.select_currency(currency_name)
        return self

    def go_to_login_page(self):
        self.click(self._my_account)
        self.click(self._login_link)
        return login_page(self.driver)