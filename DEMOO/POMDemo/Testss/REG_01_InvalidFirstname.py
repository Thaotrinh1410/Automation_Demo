from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.color import Color
import time
import unittest
import sys
sys.path.append("../")
from Pagess import RegisterPage

#No input firstname field

class RegisterTest(unittest.TestCase):
       
    def setUp(self):
        self.driver = webdriver.Chrome("D:\Selenium_AutoTest\chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/automation-practice-form")
    
        
    def test_case1(self):
        
        driver = self.driver
        # driver.get("https://demoqa.com/automation-practice-form")        
        register = RegisterPage(driver)
        firstname = register.enter_firstname("")       
        register.enter_lastname("ng")
        register.enter_gender()
        register.enter_phone("0123456789")
        register.enter_submit()
        time.sleep(10)
    
        # title_form = "Thanks for submitting the form"
        color = driver.find_element(By.ID,"firstName").value_of_css_property('border-color')
        print(color)
        hex = Color.from_string(color).hex
        print(hex)
        
        color_fail = "#dc3545"
        
        if(hex == color_fail):
            print(hex+ " Testcase Pass")
        else:
            print("Testcase Fail")

        
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        # print("Test Completed")
        
if __name__ == '__name__':
    unittest.main()
          