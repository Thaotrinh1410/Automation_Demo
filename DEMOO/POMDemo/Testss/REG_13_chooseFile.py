from lib2to3.pgen2 import driver
from xml.sax.xmlreader import Locator
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.color import Color
import re
import time
import unittest
import sys

sys.path.append("../")
from Pagess import RegisterPage
from Pagess import Locators

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
        firstname = register.enter_firstname("trinh")       
        register.enter_lastname("ng")
        useremail = register.enter_useremail("trinh@gmail.com")
        register.enter_gender()       
        phone = register.enter_phone("1234567892")
        checkbox = register.click_checkbox()
        path_file = "C:\\Users\\intern.nthithaotrinh\\Pictures\\snipping\\2.PNG"
        register.choose_path_file(path_file)
        register.enter_submit()
        time.sleep(10)
    
        if re.match(r"([a-zA-Z0-9\s_\\.\-\(\):])+(.PNG|.jpg|.png)$", path_file):
            print("Format Correct - Testcase Pass")    
        else:
            print("Incorrect")
        # color = driver.find_element(By.XPATH,"").value_of_css_property('color')       
        # print(color)
        # hex = Color.from_string(color).hex
        # print(hex)
        # color_pass = "#28a745"
        
        
        
              
                    
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        # print("Test Completed")
        
if __name__ == '__name__':
    unittest.main()
          