import pytest
from selenium.webdriver.common.by import By
import read_config
import time

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_valid_login(self):
        self.driver.find_element(By.ID,"login2").click()
        username = read_config.get_config("login credentials","uname")
        password = read_config.get_config("login credentials","pass")
        self.driver.find_element(By.ID,"loginusername").send_keys(username)
        self.driver.find_element(By.ID,"loginpassword").send_keys(password)
        self.driver.find_element(By.XPATH,"//button[text()='Log in']").click()
        time.sleep(5)
        assert self.driver.find_element(By.ID,"logout2").is_displayed()