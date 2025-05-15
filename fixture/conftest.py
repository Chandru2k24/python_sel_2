import pytest
from selenium import webdriver
import read_config

@pytest.fixture()
def setup_and_teardown(request):
    browser = read_config.get_config("basic info", "browser")
    driver = None
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("the browser not not valid")
    driver.maximize_window()
    driver.implicitly_wait(5)
    url= read_config.get_config("basic info","url")

    driver.get(url)
    request.cls.driver=driver
    yield
    driver.quit()

    import pytest
from selenium import webdriver
import read_config

@pytest.fixture()
def setup_and_teardown(request):
    browser = read_config.get_config("basic", "browser")
    driver = None
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("the browser not not valid")
    driver.maximize_window()
    driver.implicitly_wait(10)
    url = read_config.get_config("basic","url")
    driver.get(url)

    request.cls.driver = driver

    yield
    driver.quit()