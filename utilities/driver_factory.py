from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import config
caps = DesiredCapabilities.FIREFOX
caps["Marionette"] = True
caps["binary"] = "Applications/Firefox.app/Contents/MacOS/firefox-bin"
#driver = webdriver.Chrome("/Users/prasanth/workspace/MENTEE-Prasanth/drivers/chromedriver")
#driver = webdriver.Firefox(capabilities=caps,executable_path="/Users/prasanth/workspace/MENTEE-Prasanth/drivers/geckodriver")
#driver.get("http://automationpractice.com/index.php")
#driver.maximize_window()
#title = driver.title
#print(title)
#assert "My Store" in title


class Driver:

    def get_driver(self, browser_name):
        if browser_name == "chrome":
            driver = webdriver.Chrome("/Users/prasanth/workspace/MENTEE-Prasanth/drivers/chromedriver")
        elif browser_name == "firefox":
            driver = webdriver.Firefox(capabilities=caps,
                                   executable_path="/Users/prasanth/workspace/MENTEE-Prasanth/drivers/geckodriver")
        return driver

    def launch_url(self, url, driver):
        driver.get(url)
        driver.maximize_window()


    def quit_driver(self,driver):
        driver.quit()


