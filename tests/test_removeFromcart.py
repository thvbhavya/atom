from pages.login_page import LoginPage
from pages.add_to_cart import addTocart
from test_addTocart import test_add_to_cart

def remove_from_Cart(test_valid_login):

    login_page =LoginPage(test_valid_login)
    cart_page=addTocart(test_valid_login)

    login_page.open()
    cart_page.remove_from_cart()