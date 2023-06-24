import time

from PageObjects.Login_Objects import Login_Onjects
from Utilities.Logger import LogGenerator
from Utilities.Read_Excel_File import Read_Excel_File


class Test_login:
    log = LogGenerator.getLog()
    # Wr = Read_Excel_File.write_excel()

    def test_Login_By_Data_Driver_Case(self, setup):
        # self.log.info("Login By Data Driver Case is Started")
        self.driver = setup
        # self.log.info("Invoking Browser And Opening URL")
        L = Login_Onjects(self.driver)
        for r in range(2, 5):
            L.enter_username(Read_Excel_File.read_excel(r, 2))
            L.enter_password(Read_Excel_File.read_excel(r, 3))
            L.click_login()
            time.sleep(3)
