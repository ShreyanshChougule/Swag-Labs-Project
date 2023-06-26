import time

from PageObjects.Login_Objects import Login_Onjects
from PageObjects.Products_List_Objects import Products_List_Objects
from Utilities.Logger import LogGenerator
from Utilities.Read_Excel_File import Read_Excel_File


class Test_Verify_Products_List:
    log = LogGenerator.getLog("All_Products")

    def test_verify_product_list(self, setup):
        self.log.info("Verify Products List Test is Started")
        self.driver = setup
        self.log.info("Invoking Browser And Opening URL")
        L = Login_Onjects(self.driver)
        P = Products_List_Objects(self.driver)

        L.click_login()
        L.enter_username(Read_Excel_File.read_excel(2, 2))
        L.enter_password(Read_Excel_File.read_excel(2, 3))
        L.click_login()
        self.log.info("Entering Login Credential and Click on Login Button")
        time.sleep(2)

        N = P.get_Product_list_no()
        self.log.info(f"Total Products in Page are: {N}")
        for i in [P.Backpack(), P.Bike_Light(), P.Bolt_T_Shirt(), P.Fleece_Jacket(), P.Onesie(), P.All_The_Things()]:
            self.log.info(f"Screenshot of the page is Captured {i}")
        self.driver.close()
        self.log.info("Verify Products List Test is Completed")