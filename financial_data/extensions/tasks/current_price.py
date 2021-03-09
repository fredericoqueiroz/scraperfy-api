from selenium import webdriver
from scraperfy.intraday_scraper import current_price as cp
from . import celery

PATH = "C:/Program Files (x86)/chromedriver.exe"

def get_current_price_task(asset):

    op = webdriver.ChromeOptions()
    op.add_argument('headless')

    driver = webdriver.Chrome(PATH, options=op)

    return cp.CurrentPrice(driver, asset)
