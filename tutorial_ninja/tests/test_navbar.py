import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from page_objects.home_page import home_page
from selenium.webdriver.support import expected_conditions as EC
from unittest import result

@pytest.mark.navbar
def test_navbar_visible(browser):
    home = home_page(browser)
    assert home.navbar.is_displayed()