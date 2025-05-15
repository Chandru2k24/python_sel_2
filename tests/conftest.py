import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tests import read_config


# @pytest.fixture(scope="class",params=["chrome","firefox","edge"])
@pytest.fixture()
def setup_and_teardown(request):
    browser=read_config.get_config("basic info", "browser")
    driver=None
    if browser.__eq__("chrome"):
        driver=webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver=webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver=webdriver.Edge()
    # options = Options()
    # options.add_argument(
    #     "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    # )
    # options.add_argument("--disable-blink-features=AutomationControlled")
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_experimental_option("useAutomationExtension", False)
    # if request.param=="chrome":
    #   driver=webdriver.Chrome()
    # elif request.param=="firefox":
    #   driver=webdriver.Firefox()
    # elif request.param=="edge":
    #    driver=webdriver.Edge()
    url=read_config.get_config("basic info", "url")
    driver.get(url)
    driver.maximize_window()
    request.cls.driver=driver
    yield driver
    driver.quit()
    # Teardown explicitly registered
    # def quit_driver():
    #     try:
    #         driver.quit()
    #     except Exception as e:
    #         print(f"Error while quitting driver: {e}")

    # request.addfinalizer(quit_driver)