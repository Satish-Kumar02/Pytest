import pytest
import allure
from page_objects.home_page import home_page


@pytest.mark.usefixtures("browser")
class TestCurrency:
    def test_euro_crrency(self):
        home = home_page(self.driver)
        home.check_currency("EUR")
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="Euro",
            attachment_type=allure.attachment_type.PNG)

        assert home.is_currency_symbol_displayed("€")
        
    def test_pound_currency(self):
        home = home_page(self.driver)
        home.check_currency("GBP")
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="£Pound Sterling",
                      attachment_type=allure.attachment_type.PNG)
        assert home.is_currency_symbol_displayed("£") 
        
    def test_dollar_currency(self):
        home = home_page(self.driver)
        home.check_currency("USD")
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="$US Dollar",
                      attachment_type=allure.attachment_type.PNG)
        assert home.is_currency_symbol_displayed("$")