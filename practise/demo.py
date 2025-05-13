import selenium
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("https://www.google.co.in/")
time.sleep(3)
driver.quit()