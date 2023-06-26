from selenium.webdriver.common.by import By


class Order_Objects:

    addcart = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
    cart = (By.XPATH, "//a[@class='shopping_cart_link']")
    checkout = (By.XPATH, "//button[@id='checkout']")
    f_name = (By.XPATH, "//input[@id='first-name']")
    l_name = (By.XPATH, "//input[@id='last-name']")
    zip = (By.XPATH, "//input[@id='postal-code']")
    conti = (By.XPATH, "//input[@id='continue']")
    finish = (By.XPATH, "//button[@id='finish']")
    thank_you = (By.XPATH, "//h2[@class='complete-header']")
    "Thank you for your order!"

    def __init__(self, driver):
        self.driver = driver

    def Add_Cart(self):
        self.driver.find_element(*Order_Objects.addcart).click()

    def Cart(self):
        self.driver.find_element(*Order_Objects.cart).click()

    def Checkout(self):
        self.driver.find_element(*Order_Objects.checkout).click()

    def Data(self):
        self.driver.find_element(*Order_Objects.f_name).send_keys("kim")
        self.driver.find_element(*Order_Objects.l_name).send_keys("jong")
        self.driver.find_element(*Order_Objects.zip).send_keys("411011")

    def Continue(self):
        self.driver.find_element(*Order_Objects.conti).click()

    def Finish(self):
        self.driver.find_element(*Order_Objects.finish).click()

    def Status(self):
        t = self.driver.find_element(*Order_Objects.thank_you).text
        return t
