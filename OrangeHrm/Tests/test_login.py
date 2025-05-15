from Pages.loginPage import LoginPage
from Utilities import read_config
import pytest

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_login(self):
        username = read_config.get_configData("login cred","username") 
        password = read_config.get_configData("login cred","password")
        login_page = LoginPage(self.driver)

        login_page.set_logindetails(username,password)