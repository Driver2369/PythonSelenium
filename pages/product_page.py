from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import ProductPageLocators

class ProductPage(BasePage):
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
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_CONFIRMATION), "Register password confirmation field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), "Register button is not presented"


    def add_to_basket(self):
        basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        basket_btn.click()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), "Add to basket button is not presented"

    # def read_name_of_product_in_notification(self):
    #     name_notification = self.browser.find_element(*ProductPageLocators.NOTIFICATION_NAME).text
    #     return name_notification

    def read_name_of_product(self):
        self.item = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        return self.item

    def read_price_of_product(self):
        self.price = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT).text
        return self.price

    def product_should_be(self, item):
        item_notification = self.browser.find_element(*ProductPageLocators.NOTIFICATION_NAME).text
        assert item == item_notification, item + " is not equal to " + item_notification

    def price_should_be(self, price):
        price_notification = self.browser.find_element(*ProductPageLocators.NOTIFICATION_PRICE).text
        assert price == price_notification, price + " is not equal to " + price_notification
