from pages.login_page import LoginPage
from pages.add_to_cart import addTocart

def test_add_to_cart(driver):

    login_page = LoginPage(driver)
    cart_page = addTocart(driver)

    login_page.open()
    login_page.login("jane.doe@gmail.com", "Jane.doe")

    cart_page.add_to_cart()
