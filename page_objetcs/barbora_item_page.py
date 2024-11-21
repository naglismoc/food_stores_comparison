from selenium.webdriver.common.by import By

class BarboraItemPage():

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/div/div[3]/div/dl[2]/dd[3]").text

    def get_size(self):
        return self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/div/div[3]/div/dl[2]/dd[2]").text