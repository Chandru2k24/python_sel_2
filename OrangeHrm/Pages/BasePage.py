class Action:

    @staticmethod
    def click(ele):
        ele.click()

    @staticmethod
    def sendKeys(ele,text):
        ele.send_keys(text)

    @staticmethod
    def get_text(ele):
        return ele.text