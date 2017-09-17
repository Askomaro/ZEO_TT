from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


__author__ = 'anton.skomarovskyi@gmail.com'


class BasePage:

    def __init__(self, driver):
        """
        :type driver: WebDriver
        """
        self.__driver = driver

    def _find_element(self, selector, by=By.XPATH):
        web_el = self.__driver.find_element(by, selector)

        return web_el

    def _check_web_element_existing(self, selector, by=By.XPATH):
        """

        :rtype : bool
        :type selector: str
        :type by: By
        """
        try:
            self.__driver.find_element(by, selector)
        except NoSuchElementException:
            return False
        return True
