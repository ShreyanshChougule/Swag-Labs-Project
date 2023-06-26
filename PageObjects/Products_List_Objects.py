import time

from selenium.webdriver.common.by import By


class Products_List_Objects:
    all_list = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div")
    backpack = (By.XPATH, "//div[normalize-space()='Sauce Labs Backpack']")
    bike_light = (By.XPATH, "//div[normalize-space()='Sauce Labs Bike Light']")
    bolt_T_shirt = (By.XPATH, "//div[normalize-space()='Sauce Labs Bolt T-Shirt']")
    fleece_jacket = (By.XPATH, "//div[normalize-space()='Sauce Labs Fleece Jacket']")
    onesie = (By.XPATH, "//div[normalize-space()='Sauce Labs Onesie']")
    all_the_things = (By.XPATH, "//div[normalize-space()='Test.allTheThings() T-Shirt (Red)']")
    # --------------------------------------------------
    A1 = (By.XPATH, "//div[@class='inventory_details_name large_size']")
    A2 = (By.XPATH, "//div[@class='inventory_details_price']")

    def __init__(self, driver):
        self.driver = driver

    def get_Product_list_no(self):
        All = len(self.driver.find_elements(*Products_List_Objects.all_list))
        return All

    def Backpack(self):
        self.driver.find_element(*Products_List_Objects.backpack).click()
        if self.driver.find_element(*Products_List_Objects.A1).text == "Sauce Labs Backpack" and self.driver.find_element(*Products_List_Objects.A2).text == "$29.99":
            self.driver.get_screenshot_as_file("C:\\Users\\Tejas\\Swag Labs\\Screenshots\\All_Products\\Backpack.png")
            self.driver.back()
            time.sleep(2)
            return "Successfull"

    def Bike_Light(self):
        self.driver.find_element(*Products_List_Objects.bike_light).click()
        if self.driver.find_element(*Products_List_Objects.A1).text == "Sauce Labs Bike Light" and self.driver.find_element(*Products_List_Objects.A2).text == "$9.99":
            self.driver.get_screenshot_as_file("C:\\Users\\Tejas\\Swag Labs\\Screenshots\\All_Products\\Bike_Light.png")
            self.driver.back()
            time.sleep(2)
            return "Successfull"

    def Bolt_T_Shirt(self):
        self.driver.find_element(*Products_List_Objects.bolt_T_shirt).click()
        if self.driver.find_element(*Products_List_Objects.A1).text == "Sauce Labs Bolt T-Shirt" and self.driver.find_element(*Products_List_Objects.A2).text == "$15.99":
            self.driver.get_screenshot_as_file("C:\\Users\\Tejas\\Swag Labs\\Screenshots\\All_Products\\Bolt_T_Shirt.png")
            self.driver.back()
            time.sleep(2)
            return "Successfull"

    def Fleece_Jacket(self):
        self.driver.find_element(*Products_List_Objects.fleece_jacket).click()
        if self.driver.find_element(*Products_List_Objects.A1).text == "Sauce Labs Fleece Jacket" and self.driver.find_element(*Products_List_Objects.A2).text == "$49.99":
            self.driver.get_screenshot_as_file("C:\\Users\\Tejas\\Swag Labs\\Screenshots\\All_Products\\Fleece_Jacket.png")
            self.driver.back()
            time.sleep(2)
            return "Successfull"

    def Onesie(self):
        self.driver.find_element(*Products_List_Objects.onesie).click()
        if self.driver.find_element(*Products_List_Objects.A1).text == "Sauce Labs Onesie" and self.driver.find_element(*Products_List_Objects.A2).text == "$7.99":
            self.driver.get_screenshot_as_file("C:\\Users\\Tejas\\Swag Labs\\Screenshots\\All_Products\\Onesie.png")
            self.driver.back()
            time.sleep(2)
            return "Successfull"

    def All_The_Things(self):
        self.driver.find_element(*Products_List_Objects.all_the_things).click()
        if self.driver.find_element(*Products_List_Objects.A1).text == "Test.allTheThings() T-Shirt (Red)" and self.driver.find_element(*Products_List_Objects.A2).text == "$15.99":
            self.driver.get_screenshot_as_file("C:\\Users\\Tejas\\Swag Labs\\Screenshots\\All_Products\\All_The_Things_T_Shirt.png")
            self.driver.back()
            time.sleep(2)
            return "Successfull"
