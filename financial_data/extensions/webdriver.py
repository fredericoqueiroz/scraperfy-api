from selenium import webdriver

PATH = "C:/Program Files (x86)/chromedriver.exe"

def init_chrome_driver(path=PATH):

    op = webdriver.ChromeOptions()
    op.add_argument('headless')

    driver = webdriver.Chrome(PATH, options=op)

    return driver
