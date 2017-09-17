from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver

__author__ = 'anton.skomarovskyi@gmail.com'


def check_exists_by_xpath(driver, xpath):
    """

    :rtype : bool
    :type driver: WebDriver
    :type xpath: str
    """
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True
