from selenium.webdriver.chrome.webdriver import WebDriver

import utils.webdriver_extensions as wd_ext

__author__ = 'anton.skomarovskyi@gmail.com'

class HomePage:

    # XPATH locators
    __USER_MENU = '//div[@class="user-menu"]'

    def __init__(self, driver):
        """
        :type driver: WebDriver
        """
        self.__driver = driver

    @property
    def is_it_home_page(self):

        return wd_ext.check_exists_by_xpath(self.__driver, self.__USER_MENU)
