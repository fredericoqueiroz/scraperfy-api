from selenium import webdriver
from selenium.webdriver.firefox.options import Options

CHROME_PATH = "C:/Program Files (x86)/chromedriver.exe"
FIREFOX_PATH = "C:/Program Files (x86)/geckodriver.exe"

def init_chrome_driver(path=CHROME_PATH):

    op = webdriver.ChromeOptions()
    op.add_argument('headless')

    driver = webdriver.Chrome(path, options=op)

    return driver

def init_firefox_driver(path=FIREFOX_PATH):

    op = Options()
    op.add_argument('--headless')

    driver = webdriver.Firefox(executable_path=path, options=op)

    return driver
