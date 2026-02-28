from selenium.webdriver.common.by import By
from page_objects.base_page import basepage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class currency_dropdown(basepage):
    _currency_dropdown = (By.XPATH,"//span[text()='Currency']")
    _currency_euro = (By.XPATH,"//button[@name='EUR']")
    _currency_pound = (By.XPATH,"//button[@name='GBP']")
    _currency_dollar = (By.XPATH,"//button[@name='USD']")
    _dropdown_menu = (By.CSS_SELECTOR, ".dropdown.open")
    
    def select_currency(self, currency:str):
        self._open_dropdown()
        
        currency = currency.upper()
        if currency == 'EUR':
            self.click(self._currency_euro)
        
        elif currency == 'GBP':
            self.click(self._currency_pound)
        
        elif currency == 'USD':
            self.click(self._currency_dollar)
        
        else:
            raise ValueError (f"Unsupported currency value:{currency}")
        
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(self._dropdown_menu)
        )
        
    def _open_dropdown(self):
        self.click(self._currency_dropdown)