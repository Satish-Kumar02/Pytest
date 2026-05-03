from selenium.webdriver.common.by import By
from page_objects.base_page import basepage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class navbar(basepage):
    _navbar= (By.XPATH,"//nav[@id='menu']")
    _navbar_menu= (By.CSS_SELECTOR, "ul.nav.navbar-nav > li")
    # def get_navbar(self):
    #     self.type(self._navbar)
    
    def is_displayed(self):
        return self.is_visible(self._navbar)

    def get_menu(self):
        menu_items = self.find_elements(*self._navbar_menu)
        print("Debug elements->", menu_items)
        return [el.text.strip()for el in menu_items]