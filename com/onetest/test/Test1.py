# import org.testng.annotations.Test
from selenium import webdriver
from com.onetest.drivers.SelfHealingDriver import SelfHealingDriver
from selenium.webdriver.common.by import By

from com.onetest.utils import PropertyManager


class Test1:
    @staticmethod
    def logo_test():
        base_driver = webdriver.Firefox()
        driver = SelfHealingDriver(base_driver)
        base_driver.get(PropertyManager.get_property_value('app.url'))
        driver.find_element((By.XPATH,"//*[@name='usrname']"),"username input of login form")
        driver.quit()

Test1.logo_test()