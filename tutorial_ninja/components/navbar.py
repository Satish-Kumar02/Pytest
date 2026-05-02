from selenium.webdriver.common.by import By
from page_objects.base_page import basepage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class navbar(basepage):
    _navbar= (By.XPATH,"//nav[@id='menu']")
    # def get_navbar(self):
    #     self.type(self._navbar)
    
    def is_displayed(self):
        return self.is_visible(self._navbar)