from selenium.webdriver.common.by import By
from page_objects.base_page import basepage

class search_results(basepage):

    def is_product_displayed(self, product_name: str):
        locator = (
            By.XPATH,
            f"//a[contains(translate(text(),"
            f"'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),"
            f"'{product_name.lower()}')]"
        )
        return self.is_element_displayed(locator)
