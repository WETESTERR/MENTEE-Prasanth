from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import config



class Driver:

    def get_driver(self, browser_name):
        if browser_name == "chrome":
            driver = webdriver.Chrome(ChromeDriverManager().install())
        elif browser_name == "firefox":
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        return driver

    def launch_url(self, url, driver):
        driver.get(url)
        driver.maximize_window()


    def quit_driver(self,driver):
        driver.quit()


