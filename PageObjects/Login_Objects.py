from selenium.webdriver.common.by import By


class Login_Onjects:
    username = (By.XPATH, "//input[@id='user-name']")
    password = (By.XPATH, "//input[@id='password']")
    logon = (By.XPATH,"//input[@id='login-button']")

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, Email):
        self.driver.find_element(*Login_Onjects.username).send_keys(Email)

    def enter_password(self, Password):
        self.driver.find_element(*Login_Onjects.password).send_keys(Password)

    def click_login(self):
        self.driver.find_element(*Login_Onjects.logon).click()

    def Status(self):
        pass
