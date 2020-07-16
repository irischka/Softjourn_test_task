import json
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# CONFIG_PATH = 'tests\config.json'  # Use for command line
# # CONFIG_PATH = r'..\tests\config.json'  # Use for Run in IDE
# DEFAULT_WAIT_TIME = 10
# SUPPORTED_BROWSERS = ['chrome', 'firefox']


@pytest.fixture(scope="function")
def browser():
    chrome_options = Options()
    chrome_options.headless = False  # or True
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()  # or driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()


# or

#
# @pytest.fixture
# def config():
#     with open(CONFIG_PATH) as config_file:
#         data = json.load(config_file)
#         return data
#
#
# @pytest.fixture
# def config_browser(config):
#     """ Validate and return the browser choice from the config data """
#     if 'browser' not in config:
#         raise Exception('The config file does not contain "browser"')
#     elif config['browser'] not in SUPPORTED_BROWSERS:
#         raise Exception(f'"{config["browser"]}" is not a supported browser')
#     return config['browser']
#
#
# @pytest.fixture
# def config_wait_time(config):
#     """ Validate and return the wait time from the config data """
#     return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME
#
#
# @pytest.fixture(scope='function')
# def browser(config_browser, config_wait_time):
#     """ Initialize WebDriver """
#     if config_browser == 'chrome':
#         driver = webdriver.Chrome()
#     elif config_browser == 'firefox':
#         driver = webdriver.Firefox()
#     else:
#         raise Exception(f'"{config_browser}" is not a supported browser')
#     """ Wait implicitly for elements to be ready before attempting interactions """
#     driver.maximize_window()
#     driver.implicitly_wait(config_wait_time)
#     """ Return the driver object at the end of setup """
#     yield driver
#     """ For cleanup, quit the driver """
#     driver.quit()
