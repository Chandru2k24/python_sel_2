from configparser import ConfigParser
def get_config(category, key):
    config = ConfigParser()
    config.read("C:\\python_sel_2\\tests\\config.ini")
    return config.get(category, key)