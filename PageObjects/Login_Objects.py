import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from Utilities.Read_Excel_File import Read_Excel_File


class Login_Onjects:
    username = (By.XPATH, "//input[@id='user-name']")
    password = (By.XPATH, "//input[@id='password']")
    logon = (By.XPATH, "//input[@id='login-button']")
    Products = (By.XPATH, "//span[@class='title']")
    Menu = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    Logout = (By.XPATH, "//a[@id='logout_sidebar_link']")

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, Email):
        self.driver.find_element(*Login_Onjects.username).send_keys(Email)

    def enter_password(self, Password):
        self.driver.find_element(*Login_Onjects.password).send_keys(Password)

    def click_login(self):
        self.driver.find_element(*Login_Onjects.logon).click()

    def Status(self, r):
        try:
            pr = self.driver.find_element(*Login_Onjects.Products).text
            if pr == "Products":
                self.driver.get_screenshot_as_file(f"C:\\Users\\Tejas\\Swag Labs\\Screenshots\\Login\\Login_By_Data_Driver_Case_is_Pass_Test_{r-1}.png")
                self.driver.find_element(*Login_Onjects.Menu).click()
                time.sleep(1)
                self.driver.find_element(*Login_Onjects.Logout).click()
                Read_Excel_File.write_excel(r, 5, "Pass")
                time.sleep(1)
        except NoSuchElementException:
            self.driver.get_screenshot_as_file(f"C:\\Users\\Tejas\\Swag Labs\\Screenshots\\Login\\Login_By_Data_Driver_Case_is_Fail_Test_{r-1}.png")
            Read_Excel_File.write_excel(r, 5, "Fail")
            self.driver.refresh()

    @staticmethod
    def Excel_Test_Result(r):
        if Read_Excel_File.read_excel(r, 4) == Read_Excel_File.read_excel(r, 5):
            Read_Excel_File.write_excel(r, 6, "Pass")
        else:
            Read_Excel_File.write_excel(r, 6, "Fail")
