from lib2to3.pgen2 import driver
from selenium.webdriver.common.by import By
from .Locators import Locators

class SearchFunction(object):
    def __init__(self, driver):
        self.driver = driver
             
    def enter_text(self, search):
        
        self.driver.find_element(By.XPATH,(Locators.search_w3)).clear()
        self.driver.find_element(By.XPATH,(Locators.search_w3)).send_keys(search)
        
        
    def click_search(self): 
        self.driver.find_element(By.XPATH,(Locators.button_search )).click()
        