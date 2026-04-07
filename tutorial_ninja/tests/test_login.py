import allure
from page_objects.home_page import home_page

# @pytest.fixture(autouse=True)
# def self.driver():
#     self.driver = webdriver.Chrome()
#     self.driver.maximize_window()
#     self.driver.get("https://tutorialsninja.com/demo/")
    
#     yield self.driver
#     self.driver.quit()
    
    
# credentials = [ "mail,password,expected",
#     (2016sathishkumar.sk@gmail.com, Spectra@1902, success)
# ]
@allure.severity(allure.severity_level.BLOCKER)
class TestLogin:
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_Login_with_valid_credentials(self, browser):
        home = home_page(browser)
        login = home.go_to_login_page()
        login.login("2016sathishkumar.sk@gmail.com","Spectra@1902")
        assert login.is_login_successful()
     
    @allure.severity(allure.severity_level.CRITICAL)   
    def test_Login_with_correct_username_invalid_password(self,browser):
        home = home_page(browser)
        login = home.go_to_login_page()
        login.login("2016sathishkumar.sk@gmail.com","Reaper@1902")
        assert "Warning" in login.get_error_message()

    @allure.severity(allure.severity_level.NORMAL)
    def test_Login_with_incorrect_username_valid_password(self,browser):
        home = home_page(browser)
        login = home.go_to_login_page()
        login.login("sathiskumark192@gmail.com","Spectra@1902")
        assert "Warning" in login.get_error_message()
        
    @allure.severity(allure.severity_level.MINOR)
    def test_Login_with_incorrect_username_invalid_password(self, browser):
        home = home_page(browser)
        login = home.go_to_login_page()
        login.login("sathiskumark192@gmail.com","Reaper@1902")
        assert "Warning" in login.get_error_message()