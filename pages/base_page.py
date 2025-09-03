from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver_manager import DriverManager


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        
    def open(self, url):
        self.driver.get(url)
        
    def find_element(self, *locator):
        return self.driver.find_element(*locator)
        
    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)
        
    def wait_for_element(self, *locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        
    def wait_for_element_clickable(self, *locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        
    def get_title(self):
        return self.driver.title
    
    def wait_for_element_to_disappear(self, *locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )