from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class addTocart:

    PRODUCTS_BTN = (By.CSS_SELECTOR, "a[href='/products']")
    VIEWPRODUCT = (By.CSS_SELECTOR, "a[href='/product_details/1']")
    ADDTOCARTBTN = (By.CSS_SELECTOR,"button[type='button']")
    CONTINUESHOP=(By.CSS_SELECTOR,".btn.btn-success.close-modal.btn-block")
    CARTBTN=(By.CSS_SELECTOR,"body > header:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1)")
    PROD_REMOVEBTN=(By.CSS_SELECTOR,".cart_quantity_delete")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.PRODUCTS_BTN)).click()

        self.wait.until(EC.element_to_be_clickable(self.VIEWPRODUCT)).click

        self.wait.until(EC.element_to_be_clickable(self.ADDTOCARTBTN)).click()

    def remove_from_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTINUESHOP)).click()
        self.wait.until(EC.element_to_be_clickable(self.CARTBTN)).click()
        self.wait.until(EC.element_to_be_clickable(self.PROD_REMOVEBTN)).click()
        


