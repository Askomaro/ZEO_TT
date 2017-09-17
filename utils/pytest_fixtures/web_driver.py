import pytest
from selenium import webdriver

__author__ = 'anton.skomarovskyi@gmail.com'


@pytest.yield_fixture(scope='function')
def driver():
    _driver = webdriver.Chrome()
    yield _driver

    print('Close WebDriver.')
    _driver.quit()
