from selenium.webdriver.common.by import By
from page_objects.base_page import basepage

class currency_dropdown(basepage):
    _currency_dropdown = (By.XPATH,"//span[text()='Currency']")
    _currency_euro = (By.XPATH,"//button[@name='EUR']")
    _currency_pound = (By.XPATH,"//button[@name='GBP']")
    _currency_dollar = (By.XPATH,"//button[@name='USD']")
    
    def select_currency(self, currency:str):
        self._open_dropdown()
        
        currency = currency.upper()
        if currency == 'EUR':
            self._click(self._currency_euro)
        
        elif currency == 'GBP':
            self._click(self._currency_pound)
        
        elif currency == 'USD':
            self._click(self._currency_dollar)
        
        else:
            raise ValueError (f"Unsupported currency value:{currency}")
        
    def _open_dropdown(self):
        self._click(self._currency_dropdown)