import configparser

def get_config(section, key):
    config = configparser.ConfigParser()
    config.read("./config.ini")  
    return config.get(section, key)

from configparser import ConfigParser

def get_config(category , key):
    config = ConfigParser()
    config.read("./config.ini")
    return config.get(category , key)