import time

from PageObjects.Login_Objects import Login_Onjects
from PageObjects.Order_Objects import Order_Objects
from Utilities.Logger import LogGenerator
from Utilities.Read_Excel_File import Read_Excel_File


class Test_Order:
    log = LogGenerator.getLog("Order")

    def test_order(self, setup):
        self.log.info("Placing an Order Test is Started")
        self.driver = setup
        self.log.info("Invoking Browser And Opening URL")
        L = Login_Onjects(self.driver)
        L.click_login()
        L.enter_username(Read_Excel_File.read_excel(2, 2))
        L.enter_password(Read_Excel_File.read_excel(2, 3))
        L.click_login()
        self.log.info("Entering Login Credential and Click on Login Button")
        time.sleep(2)

        O = Order_Objects(self.driver)
        O.Add_Cart()
        self.log.info("Product or Itam Added to Cart")
        O.Cart()
        O.Checkout()
        self.log.info("Product Vefication is Done and Click On Checkout")
        O.Data()
        self.log.info("Entering Valid Credential")
        O.Continue()
        self.log.info("Click On Continue")
        time.sleep(2)
        O.Finish()
        if O.Status() == "Thank you for your order!":
            self.log.info("Thank you for your order")
            self.driver.get_screenshot_as_file("C:\\Users\\Tejas\\Swag Labs\\Screenshots\\Order\\Order_Placed.png")
        self.driver.close()
        self.log.info("Placing an Order Test is Completed")