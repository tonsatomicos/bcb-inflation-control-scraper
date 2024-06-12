from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class WebDriverConfig:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--headless")
        self.driver = None

    def get_driver(self):
        if self.driver is None:
            self.driver = webdriver.Chrome(options=self.chrome_options)
        return self.driver

    def close_driver(self):
        if self.driver:
            self.driver.quit()
            self.driver = None
