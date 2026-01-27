from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AddToCartPage(BasePage):  #subclassing BasePage to inherit its methods
    ADD_TO_CART_BTN=(By.ID,"add-to-cart-sauce-labs-backpack")
    CART_ICON=(By.CSS_SELECTOR,"shopping_cart_link")
    CART_PAGE=(By.CSS_SELECTOR,"title")
    
    def add_item_to_cart(self):
        self.wait_for_element(self.ADD_TO_CART_BTN).click()

    def go_to_cart(self):
        self.wait_for_element(self.CART_ICON).click()

    def validate_cart_page(self):
        return self.wait_for_element(self.CART_PAGE).text