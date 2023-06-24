import configparser

data = configparser.RawConfigParser()
data.read("C:\\Users\\Tejas\\Swag Labs\\Configuration\\Config.ini")


class Read_Confi_File:

    @staticmethod
    def get_URL():
        UL = data.get("Login_Page", "URL")
        return UL

    @staticmethod
    def get_Excel_Path():
        Path = data.get("Login_Page", "Excel_Path")
        return Path