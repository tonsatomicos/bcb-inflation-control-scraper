import pandas as pd
from io import StringIO
from .interface_data_extractor import InterfaceDataExtractor
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class DataExtractor(InterfaceDataExtractor):
    def __init__(self, webdriver_config):
        self.webdriver_config = webdriver_config

    def extract_data(self, url_extract, table_xpath) -> pd.DataFrame:
        browser = self.webdriver_config.get_driver()
        if browser:
            try:
                browser.get(url_extract)

                sleep(30)

                wait = WebDriverWait(browser, 50)
                wait.until(
                    lambda browser: browser.execute_script("return document.readyState")
                    == "complete"
                )

                xpath = wait.until(
                    EC.presence_of_element_located((By.XPATH, table_xpath))
                )
                table_html = xpath.get_attribute("outerHTML")

                df = pd.read_html(StringIO(table_html))[0]
                return df

            except Exception as e:
                raise ValueError(f"Erro na extração dos dados: {e}")

            finally:
                if browser:
                    browser.quit()