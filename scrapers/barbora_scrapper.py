from selenium.webdriver.common.by import By

from models.barbora_item import BarboraItem


class BarboraScrapper():
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url


    def collectData(self):
        self.acceptCookies()
        self.ageConsent()
        self.getUrls()
        self.collectEach()

    def getUrls(self):
        for i in range(1, 10):
            self.driver.get(f"{self.url}?page={i}")
            ul = self.driver.find_element(By.XPATH, '//*[@id="category-page-results-placeholder"]/div/ul')
            lis = ul.find_elements(By.TAG_NAME, 'li')
            print(len(lis))
            if len(lis) == 0:
                break
            for a in lis:
                href = a.find_element(By.TAG_NAME, 'a').get_attribute('href')
                self.hrefs.append(href)

    def collectEach(self):
        for link in self.hrefs:
            self.driver.get(link)
            item = BarboraItem(self.driver)
            item.fill()
            item.save()

    def acceptCookies(driver):
        driver.get("https://barbora.lt")
        driver.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinDeclineAll').click()

    def ageConsent(self):
        self.driver.get(self.url)
        is_20 = len(self.driver.find_elements(By.ID, 'fti-modal-option-1')) != 0
        if is_20:
            self.driver.find_element(By.ID, "fti-modal-option-1").click()