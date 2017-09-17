from wheel.signatures import assertTrue

import pytest
from faker import Faker

from page_objects.login_page import LoginPage
from utils.pytest_fixtures.web_driver import driver


__author__ = 'anton.skomarovskyi@gmail.com'


class TestLogin:

    def test_user_is_authorized_if_credentials_are_valid(self, driver):
        user_login = 'test_task@test.com'
        user_password = 'qwerty'

        login_page = LoginPage(driver).open()

        sut = login_page.login_as(user_login, user_password)

        assertTrue(sut.is_it_home_page)

    def test_user_is_not_authorized_if_credentials_are_not_valid(self, driver):
        fake = Faker()
        user_login = fake.pystr()
        user_password = fake.pystr()

        login_page = LoginPage(driver).open()

        sut = login_page.login_as_expecting_error(user_login, user_password)

        assertTrue(sut.is_it_login_page)

    def test_password_is_required_filed(self, driver):
        fake = Faker()
        user_login = fake.pystr()

        login_page = LoginPage(driver).open()
        login_page.type_username(user_login)

        sut = login_page.submit_login_expecting_failure()

        assertTrue(sut.is_it_login_page)
        assertTrue(sut.is_password_message_error_appeared)

    def test_email_is_required_filed(self, driver):
        fake = Faker()
        user_password = fake.pystr()

        login_page = LoginPage(driver).open()
        login_page.type_password(user_password)

        sut = login_page.submit_login_expecting_failure()

        assertTrue(sut.is_it_login_page)
        assertTrue(sut.is_email_message_error_appeared)

    def test_email_and_password_are_required_fileds(self, driver):
        login_page = LoginPage(driver).open()

        sut = login_page.submit_login_expecting_failure()

        assertTrue(sut.is_it_login_page)
        assertTrue(sut.is_email_message_error_appeared)
        assertTrue(sut.is_password_message_error_appeared)
