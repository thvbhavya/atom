from pages.login_page import LoginPage
from config.config import *

def test_valid_login(setup):
    driver=setup
    login_page=LoginPage(driver)

    login_page.open(BASE_URL)
    login_page.login(VALID_USERNAME,VALID_PASSWORD)
    assert "inventory" in driver.current_url
    
def test_invalid_login(setup):
    driver=setup
    login_page= LoginPage(driver)

    login_page.open(BASE_URL)
    login_page.login(INVALID_USERNAME,INVALID_PASSWORD)

    error_msg=login_page.get_error_message()
    assert "Epic sadface: Username and password do not match any user in this service" in error_msg