from pages.login_page import LoginPage


def test_valid_login(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("jane.doe@gmail.com", "Jane.doe")


