import pytest
import allure
from selenium import webdriver
from page_objects.home_page import home_page
from components.navbar import navbar
from selenium.webdriver.support import expected_conditions as EC
from unittest import result

#@pytest.mark.navbar
def test_navbar_visible(browser):
    home = home_page(browser)
    assert home.navbar.is_displayed()

@pytest.mark.navbar    
def test_menu(browser):
    lists= ['Desktops', 'Laptops & Notebooks', 'Components', 'Tablets', 'Software', 'Phones & PDAs', 'Cameras', 'MP3 Players']
    home = home_page(browser)
    menus = home.navbar.get_menu()
    assert lists == menus