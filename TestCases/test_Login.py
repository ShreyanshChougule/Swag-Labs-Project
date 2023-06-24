import time

from PageObjects.Login_Objects import Login_Onjects
from Utilities.Logger import LogGenerator
from Utilities.Read_Excel_File import Read_Excel_File


class Test_login:
    log = LogGenerator.getLog()

    def test_Login_By_Data_Driven_Case(self, setup):
        self.log.info("Login By Data Driven Test is Started")
        self.driver = setup
        self.log.info("Invoking Browser And Opening URL")
        L = Login_Onjects(self.driver)
        for r in range(2, 6):
            L.enter_username(Read_Excel_File.read_excel(r, 2))
            self.log.info(f"Entering Username: {Read_Excel_File.read_excel(r, 2)}")
            L.enter_password(Read_Excel_File.read_excel(r, 3))
            self.log.info(f"Entering Password: {Read_Excel_File.read_excel(r, 3)}")
            L.click_login()
            self.log.info("Clicking on Login Button")
            time.sleep(3)
            L.Status(r)
            self.log.info("Status of the page is Captured")
            L.Excel_Test_Result(r)
            self.log.info("Test Result is Written on Excel")
        self.driver.close()
        self.log.info("Test Login By Data Driven is Completed")
