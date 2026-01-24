from selenium.webdriver.common.by import By
from pages.base_page import BasePage #importing BasePage to inherit its methods

class LoginPage(BasePage):  #subclassing BasePage to inherit its methods
    USERNAME=(By.ID,"user-name")
    PASSWORD=(By.ID,"password")
    LOGIN_BTN=(By.ID,"login-button")
    ERROR_MSG=(By.XPATH,"//div[@class='error-message-container error']")

    def open(self,url):
        self.driver.get(url)

    def login(self,username,password):
        self.wait_for_element(self.USERNAME).send_keys(username)
        self.wait_for_element(self.PASSWORD).send_keys(password)
        self.wait_for_element(self.LOGIN_BTN).click()

    def get_error_message(self):
        return self.wait_for_element(self.ERROR_MSG).text