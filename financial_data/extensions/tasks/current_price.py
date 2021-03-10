from selenium import webdriver
from scraperfy.intraday_scraper import current_price as cp
from . import celery

PATH = "C:/Program Files (x86)/chromedriver.exe"

@celery.task(name='current_price_task')
def get_current_price_task():

    op = webdriver.ChromeOptions()
    op.add_argument('headless')

    driver = webdriver.Chrome(PATH, options=op)

    current_price = cp.CurrentPrice(driver, 'IBOV')
    return current_price.print_asset_data()

@celery.task(name='smoke_task')
def smoke_task():
    print("Running smoke test...")
