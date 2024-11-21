from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from models.barbora_item import BarboraItem
from scrapers.barbora_scrapper import BarboraScrapper


def initGathering():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 10)
    return driver, wait

def executeDataGathering():
    driver, wait = initGathering()
    barbora = BarboraScrapper(driver, 'https://barbora.lt/bakaleja/kruopos/grikiai')
    barbora.collectData()
    # rimi
    # iki




executeDataGathering()