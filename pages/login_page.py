import pytest
import time
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in (self.browser.current_url), 'there is no login word in current url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'no any login form on the page'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'no any register form on the page'

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = 'qpWO0mRaI'
        input1 = self.browser.find_element(*LoginPageLocators.EMAIL_ADRESS_INPUT)
        input1.send_keys(email)
        input2 = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        input2.send_keys(password)
        input3 = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_INPUT)
        input3.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()
