from configparser import ConfigParser

def get_configData(category , key):
    config = ConfigParser()
    config.read("./configuration/config.ini")
    return config.get(category , key)