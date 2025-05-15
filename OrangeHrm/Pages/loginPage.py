from selenium.webdriver.common.by import By
from Pages.BasePage import Action
class LoginPage:

    def __init__(self,driver):
        self.driver = driver
        self.username = (By.NAME,"username")
        self.password = (By.NAME,"password")
        self.loginBtn = (By.XPATH,"//button[text()=' Login ']")
        
    def set_logindetails(self,uname,password):
        user_input=self.driver.find_element(*self.username)
        pass_input=self.driver.find_element(*self.password)
        login_btn=self.driver.find_element(*self.loginBtn)

        Action.sendKeys(user_input,uname)
        Action.sendKeys(pass_input,password)
        Action.click(login_btn)

     


