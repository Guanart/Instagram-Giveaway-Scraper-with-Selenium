from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options

# Driver
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 5)
# Options
options = Options()    
options.headless = False                    
options.add_argument('--start-minimized')   
options.add_argument('--disable-extensions')