import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser():
    chrome_options = Options()
    chrome_options.headless = False  # or True
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()  # or driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()
