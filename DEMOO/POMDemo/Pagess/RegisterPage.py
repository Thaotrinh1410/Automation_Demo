from lib2to3.pgen2 import driver
from selenium.webdriver.common.by import By
from .Locators import Locators

class RegisterPage(object):
    def __init__(self, driver):
        self.driver = driver
             
    def enter_firstname(self, firstname):
        
        self.driver.find_element(By.XPATH,(Locators.firstname)).clear()
        self.driver.find_element(By.XPATH,(Locators.firstname)).send_keys(firstname)
        
    def enter_lastname(self, lastname):
        self.driver.find_element(By.XPATH,(Locators.lastname)).clear()
        self.driver.find_element(By.XPATH,(Locators.lastname)).send_keys(lastname)
        
    def enter_useremail(self, username):
        self.driver.find_element(By.XPATH,(Locators.useremail)).clear()
        self.driver.find_element(By.XPATH,(Locators.useremail)).send_keys(username)
        
    def enter_gender(self):
        self.driver.find_element(By.XPATH,(Locators.gender)).click()
        
    def enter_phone(self, phone):
        self.driver.find_element(By.ID,(Locators.phone_id)).clear()
        self.driver.find_element(By.ID,(Locators.phone_id)).send_keys(phone)
        
    def click_checkbox(self):
        self.driver.find_element(By.XPATH,(Locators.check_box)).click()
        
    def choose_path_file(self, file):
        self.driver.find_element(By.XPATH,(Locators.choose_file)).send_keys(file)
        
    def enter_submit(self):
        
        self.driver.execute_script("window.scrollTo(0, 400)")
        self.driver.find_element(By.XPATH,(Locators.submit)).click()
        
    def close_element(self):
        self.driver.find_element(By.ID,(Locators.close_element)).click()
        
    def close_form(self):
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.driver.find_element(By.ID,(Locators.close_form)).click()
        
    def find_title(self):
        self.driver.find_element(By.XPATH,(Locators.title_submit_success)).text
        
