from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_message(self, message):
        text_in_message = self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE).text
        assert message in text_in_message, message + "is not in the real message: " + text_in_message

    def should_not_be_checkout_button(self):
        assert self.is_not_element_present(*BasketPageLocators.CHECKOUT_BUTTON), \
           "Checkout button is presented, but should not be"
