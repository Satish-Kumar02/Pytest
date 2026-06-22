import pytest
from page_objects.home_page import home_page

class Test_product:
    #@pytest.mark.product
    def test_add_product_to_cart(self, browser):
        home = home_page(browser)
        results = home.search_product('Apple Cinema 30"')
        product = results.select_product('Apple Cinema 30"')
        #product.select_radio_option("7")
        product.select_checkbox()
        product.enter_text("test")
        product.select_dropdown("Green")
        product.text_area("testing")
        product.upload_file(r"C:\Users\Sathish Kumar\Desktop\Git\Pytest\tutorial_ninja\file")
        product.set_quantity(2)
        product.add_to_cart()
        assert "Radio required!" in product.get_validation_message()
        
    # def test_add_Macbook(self, browser):
    #     home = home_page(browser)
    #     product = home.add_mac()
    #     product.