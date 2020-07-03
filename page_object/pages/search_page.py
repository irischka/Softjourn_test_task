from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from page_object.pages.base_page import BasePage


class SearchPage(BasePage):
    """ Locators """

    SEARCH_FIELD = (By.XPATH, "//input[@name='q']")
    RESULT_TEXT = (By.CSS_SELECTOR, "span.st")
    BOLT_TEXT = (By.CSS_SELECTOR, "span.st em")

    """ Warning Messages/texts """

    SELENIUM_TEXT = "Selenium"

    """ The methods return locators  """

    @property
    def search_field(self):
        return self.find_element(self.SEARCH_FIELD)

    def search_field_delete_text(self):
        self.search_field.send_keys(Keys.CONTROL, "a", Keys.DELETE)
        return self

    def search_field_submit(self):
        self.search_field.send_keys(Keys.ENTER)
        return self

    def search_field_click(self):
        self.search_field.click()
        return self

    def set_search_field(self, text):
        self.search_field_click()
        self.search_field_delete_text()
        self.search_field.send_keys(text)
        return self
