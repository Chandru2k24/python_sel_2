import selenium
from selenium import webdriver
import time
def test_Open():
    driver=webdriver.Chrome()
    driver.get("https://www.google.co.in/")
    time.sleep(3)
    driver.quit()