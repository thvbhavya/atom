from selenium.webdriver.common.by import By

class addTocart:

    PRODUCTS_BTN = (By.CSS_SELECTOR, "a[href='/products']")
    VIEWPRODUCT = (By.CSS_SELECTOR, "a[href='/product_details/1']")
    ADDTOCARTBTN = (By.CSS_SELECTOR, "button[type='button']")

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        self.driver.find_element(*self.PRODUCTS_BTN).click()
        self.driver.find_element(*self.VIEWPRODUCT).click()
        self.driver.find_element(*self.ADDTOCARTBTN).click()
