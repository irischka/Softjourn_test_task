import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            ec.presence_of_element_located(locator)
        )

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            ec.presence_of_all_elements_located(locator)
        )

    def navigate_to_page(self):
        """ Use for command line"""
        # self.driver.get(os.environ["automation_test_url"])

        """ Use for Run in IDE """
        self.driver.get("https://www.google.com.ua/?hl=ua")
