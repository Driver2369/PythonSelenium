from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".page_inner .btn.btn-default:first-child")

class BasketPageLocators():
    BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "#content_inner .col-sm-4:first-child")

class LoginPageLocators():
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.NAME, "login_submit")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_CONFIRMATION = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, "#add_to_basket_form [type=\"submit\"]")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, "#content_inner h1")
    NOTIFICATION_NAME = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) strong")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, ".price_color")
    NOTIFICATION_PRICE = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) .alertinner")
