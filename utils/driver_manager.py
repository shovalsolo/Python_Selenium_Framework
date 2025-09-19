from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from config.config import Config
from selenium.webdriver.chrome.service import Service
import os


class DriverManager:
    @staticmethod
    def get_driver():
        driver = None
        browser = Config.BROWSER.lower()
        
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            if Config.HEADLESS:
                options.add_argument("--headless=new")
            # service = Service(executable_path='/Users/macsho/Programming/Python/Python_Selenium_Framework/showcase_framework/chromedriver')
            driver = webdriver.Chrome(options=options)
            # service = ChromeService(executable_path="chromedriver")
            # driver = webdriver.Chrome(service=service, options=options)
            
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            if Config.HEADLESS:
                options.add_argument("--headless")
            service = FirefoxService(executable_path="geckodriver")
            driver = webdriver.Firefox(service=service, options=options)
            
        elif browser == "edge":
            options = webdriver.EdgeOptions()
            if Config.HEADLESS:
                options.add_argument("--headless")
            service = EdgeService(executable_path="msedgedriver")
            driver = webdriver.Edge(service=service, options=options)
            
        else:
            raise ValueError(f"Unsupported browser: {browser}")
            
        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        driver.maximize_window()
        return driver