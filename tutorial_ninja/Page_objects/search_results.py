from selenium.webdriver.common.by import By
from page_objects.base_page import basepage

class search_results(basepage):
    
    _no_results = (By.XPATH,"//p[text()= 'There is no product that matches the search criteria.']")

    def is_product_displayed(self, product_name: str):
        locator = (
            By.XPATH,
            f"//a[contains(translate(text(),"
            f"'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),"
            f"'{product_name.lower()}')]"
        )
        return self.is_element_displayed(locator)
    
    def is_no_product_displayed(self)-> bool:
        return self.is_element_displayed(self._no_results)
