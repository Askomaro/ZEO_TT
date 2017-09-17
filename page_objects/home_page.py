from selenium.webdriver.chrome.webdriver import WebDriver

from page_objects.base_page import BasePage


__author__ = 'anton.skomarovskyi@gmail.com'


class HomePage(BasePage):

    # XPATH locators
    __USER_MENU = '//div[@class="user-menu"]'

    def __init__(self, driver):
        """
        :type driver: WebDriver
        """
        super(HomePage, self).__init__(driver)

        self.__driver = driver

    @property
    def is_it_home_page(self):

        return self._check_web_element_existing(self.__USER_MENU)
