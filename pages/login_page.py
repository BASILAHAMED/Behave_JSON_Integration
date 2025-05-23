from locators.web_locators import LoginLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def login(self, username, password):
        self.driver.find_element(*LoginLocators.username).clear()
        self.driver.find_element(*LoginLocators.username).send_keys(username)
        self.driver.find_element(*LoginLocators.password).clear()
        self.driver.find_element(*LoginLocators.password).send_keys(password)
        self.driver.find_element(*LoginLocators.login_button).click()

    def login_successful(self):
        try:
            self.wait.until(EC.presence_of_element_located(LoginLocators.inventory))
            return True
        except:
            return False
