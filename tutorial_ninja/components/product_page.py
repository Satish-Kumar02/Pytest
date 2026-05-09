from page_objects.base_page import basepage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class product_page(basepage):

    _add_to_cart = (By.ID, "button-cart")
    _quantity = (By.ID, "input-quantity")
    _checkbox = (By.XPATH,"//input[@name='option[223][]' and @value='10']")
    _date_input = (By.ID, "input-option219")
    _time_input = (By.ID, "input-option221")
    _datetime_input = (By.ID, "input-option220")
    _validation_message = (By.CSS_SELECTOR,".text-danger")

    def select_radio_option(self, value):
        locator = (By.XPATH,f"//*[@id='input-option218']//input[@value='{value}']")
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        #self.driver.execute_script("arguments[0].click();",element)

    def select_checkbox(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self._checkbox))
        self.driver.execute_script("arguments[0].click();",element)

    def enter_text(self, text):
        self.type((By.ID, "input-option208"),text)

    def text_area(self, text):
        locator = (By.ID, "input-option209")
        self.clear(locator)
        self.type(locator, text)

    def select_dropdown(self, visible_text):
        dropdown_locator = (By.ID, "input-option217")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(dropdown_locator))
        try:
            self.select_by_visible_text(dropdown_locator, visible_text)
        except:
            
            dropdown = Select(self.driver.find_element(*dropdown_locator))
            for option in dropdown.options:
                if visible_text.lower() in option.text.lower():
                    option.click()
                    return
            dropdown.select_by_value(visible_text.lower())

    def upload_file(self, path):
        locators = [
            (By.XPATH, "//input[@type='file']"),
            (By.XPATH, "//input[contains(@name, 'upload')]"),
            (By.CSS_SELECTOR, "input[type='file']"),
        ]
        
        for locator in locators:
            try:
                element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(locator))
                # Scroll to element to make sure it's visible
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                # Send the file path
                element.send_keys(path)
                return True
            except:
                continue
        
        # If no file input found, it's optional - just skip it
        return False

    def set_quantity(self, quantity):
        self.clear(self._quantity)
        self.type(self._quantity,str(quantity))

    def add_to_cart(self):
        self.click(self._add_to_cart)

    def set_date(self, date_value):
        self.type(self._date_input, date_value)

    def set_time(self, time_value):
        self.type(self._time_input, time_value)

    def set_datetime(self, datetime_value):
        self.type(self._datetime_input, datetime_value)
    
    def get_validation_message(self):
        try:
            # Wait for the validation message to appear
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self._validation_message))
            return self.get_text(self._validation_message)
        except:
            # Try alternative selectors if the primary one fails
            alt_locators = [
                (By.XPATH, "//div[@class='alert alert-danger']"),
                (By.CSS_SELECTOR, ".alert-danger"),
                (By.XPATH, "//div[contains(@class, 'text-danger')]")
            ]
            for locator in alt_locators:
                try:
                    element = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located(locator))
                    return element.text
                except:
                    continue
            return ""