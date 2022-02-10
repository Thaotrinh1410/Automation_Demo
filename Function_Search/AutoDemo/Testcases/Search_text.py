
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import sys
sys.path.append("../")
from PageElement import SearchFunction


class SearchText(unittest.TestCase):
       
    def setUp(self):
        self.driver = webdriver.Chrome("D:\Selenium_AutoTest\chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://www.w3schools.com/")
    
        
    def test_case(self):
        
        driver = self.driver      
        register = SearchFunction(driver)
        register.enter_text("java")       
        # register.click_search()
        time.sleep(10)
        
        arr = driver.find_elements(By.XPATH,"//div[@id='listofsearchresults']/a[contains(@class,'search_item')]")
        print(arr[0].text)
        
        
        
        
        

        
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        # print("Test Completed")
        
if __name__ == '__name__':
    unittest.main()