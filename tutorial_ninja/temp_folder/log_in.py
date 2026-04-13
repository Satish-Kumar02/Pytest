from selenium.webdriver.common.by import By
from page_objects.base_page import basepage

class login_page(basepage):
    _email=(By.ID,"input-email")
    _password = (By.ID, "input-password")
    _login_button = (By.CSS_SELECTOR,"input[type=submit]")
    _error_alert = (By.XPATH,"//div[contains(@class,'alert-danger')]")
    _edit_account = (By.LINK_TEXT, "Edit Account")

    def login(self, email: str, password: str):
        self.type(self._email, email)
        self.type(self._password, password)
        self.click(self._login_button)
        return self

    def is_login_successful(self):
        return self.is_visible(self._edit_account)

    def get_error_message(self):
        return self.get_text(self._error_alert)