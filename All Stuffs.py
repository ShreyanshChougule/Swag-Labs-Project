from selenium import  webdriver
from selenium.webdriver.common.by import By

dr = webdriver.Edge()

dr.find_element(By.XPATH, "").send_keys()