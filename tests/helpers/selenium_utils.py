import os
import os.path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

TIMEOUT = 30


class SeleniumUtils:
    driver = None
    wait = None
    headless = None

    def __init__(self, headless=True):
        print('Init selenium utils.', flush=True)
        self.setup_driver()
        self.headless = headless

    def __del__(self):
        if self.driver is not None:
            self.driver.close()
            del self.driver

    def setup_driver(self):
        options = webdriver.ChromeOptions()
        if self.headless:
            options.add_argument("--headless")
        options.add_argument("--incognito")
        options.add_argument("--start-maximized")  # open Browser in maximized mode
        options.add_argument("--disable-infobars")  # disabling infobars
        options.add_argument("--disable-extensions")  # disabling extensions
        options.add_argument("--disable-gpu")  # applicable to Windows OS only
        options.add_argument("--no-sandbox")  # Bypass OS security model
        options.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--ignore-certificate-errors")
        downloads_path = os.path.abspath('downloads')
        prefs = {
            'profile.default_content_settings.popups': 0,
            'download.default_directory': downloads_path,
            'safebrowsing.enable': False,
            'download.prompt_for_download': False,
            'excludeSwitches': ['disable-popup-blocking'],
            'profile.default_content_setting_values.automatic_downloads': 1
        }
        options.add_experimental_option("prefs", prefs)
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, int(TIMEOUT))

    @staticmethod
    def print_element_info(element):
        print('html:', element.get_attribute('innerHTML'))
        return True

    def get_element_by_id(self, identifier):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(
                (
                    By.ID,
                    identifier
                )
            )
        )
