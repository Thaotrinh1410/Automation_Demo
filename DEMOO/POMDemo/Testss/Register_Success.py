from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time
import unittest
import sys
sys.path.append("../")
from Pagess import RegisterPage

#Register Successful
class RegisterTest(unittest.TestCase):
       
    def setUp(self):
        self.driver = webdriver.Chrome("D:\Selenium_AutoTest\chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/automation-practice-form")
    
    def test_register(self):
    
        driver = self.driver
        # driver.get("https://demoqa.com/automation-practice-form")       
        register = RegisterPage(driver)
        register.enter_firstname("trinh")
        register.enter_lastname("ng")
        register.enter_gender()
        register.enter_phone("0123456789")
        register.enter_submit()
        time.sleep(5)
        register.close_element()
        time.sleep(2)
        register.close_form()
        # driver.refresh()
        
        
    # def test_case1(self):
        
    #     driver = self.driver
    #     # driver.get("https://demoqa.com/automation-practice-form")        
    #     register = RegisterPage(driver)
    #     register.enter_firstname("")       
    #     register.enter_lastname("ng")
    #     register.enter_gender()
    #     register.enter_phone("0123456789")
    #     register.enter_submit()
    #     time.sleep(10)
    
        
        
        find_title =driver.find_element(By.XPATH,"//*[@id='example-modal-sizes-title-lg']")
        find_title = find_title.text
        title_form = "Thanks for submitting the form"       
        if (find_title == title_form):
            print("Submit Success - Testcase Pass")           
        else:
            print("Testcase Fail")
              
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        # print("Test Completed")
        
if __name__ == '__name__':
    unittest.main()
          







