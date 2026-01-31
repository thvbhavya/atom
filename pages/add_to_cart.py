from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class addTocart:

    PRODUCTS_BTN = (By.CSS_SELECTOR, "a[href='/products']")
    VIEWPRODUCT = (By.CSS_SELECTOR, "a[href='/product_details/1']")
    ADDTOCARTBTN = (By.CSS_SELECTOR,"button[type='button']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.PRODUCTS_BTN)).click()

        self.wait.until(EC.element_to_be_clickable(self.VIEWPRODUCT)).click

        self.wait.until(EC.element_to_be_clickable(self.ADDTOCARTBTN)).click()
