import pytest
from selenium import webdriver

import links


@pytest.fixture(scope='function')
def driver():

    firefox_options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=firefox_options)
    driver.maximize_window()
    driver.get(links.main_page)
    yield driver
    driver.quit()
