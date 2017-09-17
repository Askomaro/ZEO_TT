from selenium.webdriver.chrome.webdriver import WebDriver

from page_objects.home_page import HomePage
import utils.webdriver_extensions as wd_ext


__author__ = 'anton.skomarovskyi@gmail.com'


class LoginPage:
    __LOGIN_PAGE_URL = 'https://accountstage.mackeeper.com/'

    # XPATH locators
    __USERNAME = '//input[@id="email"]'
    __PASSWORD = '//input[@id="password"]'
    __LOGIN = '//form[@action=""]/input[@type="submit"]'
    __LOGIN_WITH_FB = '//input[@id="submit" and @value="Log In with Facebook"]'
    __USER_MENU = '//div[@class="user-menu"]'
    __EMAIL_ERROR_MESSAGE = '//input[@id="email"]/following-sibling::span[@class="form__error"]'
    __PASSWORD_ERROR_MESSAGE = '//input[@id="password"]/following-sibling::span[@class="form__error"]'

    def __init__(self, driver):
        """
        :type driver: WebDriver
        """
        self.__driver = driver

    def open(self):
        self.__driver.get(self.__LOGIN_PAGE_URL)

        return self

    def type_username(self, username):
        """
        :rtype self: LoginPage
        """
        self.__driver.find_element_by_xpath(self.__USERNAME).send_keys(username)

        return self

    def type_password(self, password):
        """
        :rtype self: LoginPage
        """
        self.__driver.find_element_by_xpath(self.__PASSWORD).send_keys(password)

        return self

    def submit_login(self):
        """
        :rtype self: HomePage
        Return a new page object representing the destination.
        """
        self.__driver.find_element_by_xpath(self.__LOGIN).click()

        return HomePage(self.__driver)

    def submit_login_expecting_failure(self):
        """
        :rtype self: LoginPage
        Return a new page object representing the destination. Should the user ever be
        navigated to the home page after submiting a login with credentials
        expected to fail login, the script will fail when it attempts to instantiate
        the LoginPage PageObject.
        """
        self.__driver.find_element_by_xpath(self.__LOGIN).click()

        return LoginPage(self.__driver)

    def login_as(self, username, password):
        """
        :rtype self: HomePage
        Conceptually, the login page offers the user the service of being able to "log into"
        the application using a user name and password.
        """
        self.type_username(username)
        self.type_password(password)

        return self.submit_login()

    def login_as_expecting_error(self, username, password):
        """
        :rtype self: LoginPage
        """
        self.type_username(username)
        self.type_password(password)

        return self.submit_login_expecting_failure()

    @property
    def is_it_login_page(self):

        return not wd_ext.check_exists_by_xpath(self.__driver, self.__USER_MENU)

    @property
    def is_email_message_error_appeared(self):
        web_el = self.__driver.find_element_by_xpath(self.__EMAIL_ERROR_MESSAGE)
        error_message = web_el.text

        return error_message != ""

    @property
    def is_password_message_error_appeared(self):
        web_el = self.__driver.find_element_by_xpath(self.__PASSWORD_ERROR_MESSAGE)
        error_message = web_el.text

        return error_message != ""
