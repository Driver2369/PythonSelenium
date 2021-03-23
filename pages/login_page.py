from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import LoginPageLocators
class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        self.url = self.browser.current_url
        assert "login" in self.url, "Substring login is not present in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Login email field is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login password field is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), "Register email field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD), "Register password field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_CONFIRMATION), \
            "Register password confirmation field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), "Register button is not presented"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRMATION).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

    def should_be_success_registration_message(self):
        assert self.is_element_present(*LoginPageLocators.SUCCESS_REGISTRATION_MESSAGE), \
            "Registration was probably unsuccessful"

    def should_be_in_registration_success_message(self, message):
        text_in_message = self.browser.find_element(*LoginPageLocators.SUCCESS_REGISTRATION_MESSAGE).text
        assert message in text_in_message, message + "is not in the real message: " + text_in_message
