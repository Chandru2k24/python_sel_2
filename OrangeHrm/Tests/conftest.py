import pytest
from Utilities import read_config
from selenium import webdriver
@pytest.fixture()
def setup_and_teardown(request):
    browser = read_config.get_configData("basic info","browser")
    driver = None
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        print("The browser is invalid ")
    
    driver.maximize_window()
    driver.implicitly_wait(10)
    url = read_config.get_configData("basic info","url")
    driver.get(url)
    request.cls.driver = driver

    yield
    driver.quit()