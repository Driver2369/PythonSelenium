import pytest
import time
from pages.product_page import ProductPage
from pages.base_page import BasePage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage



@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                               marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

#@pytest.mark.xfail(reason="fixing this bug right now") - just to not forget how to put reason
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.read_name_of_product()
    page.read_price_of_product()
    print("\nYou are about to choose following item: " + page.item + " for price: " + page.price)
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    #asserts
    page.product_should_be(page.item)
    page.price_should_be(page.price)


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.read_name_of_product()
    page.read_price_of_product()
    print("\nYou are about to choose following item: " + page.item + " for price: " + page.price)
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    # asserts
    page.should_not_be_success_message()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # open registration page
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_register_form()
        # register a new user
        email = "TestUser" + str(time.time()) + "@fakemail.org"
        password = "12344565124@4"
        page.register_new_user(email, password)
        # check that notification is shown
        page.should_be_success_registration_message()
        page.should_be_in_registration_success_message("Thanks for registering!")
        # check that user is logged in
        page.should_be_authorized_user()
        yield
        # teardown just skip at the moment
        pass



    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_basket_button()
        # asserts
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_basket_button()
        page.read_name_of_product()
        page.read_price_of_product()
        print("\nYou are about to choose following item: " + page.item + " for price: " + page.price)
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        # asserts
        page.product_should_be(page.item)
        page.price_should_be(page.price)


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.read_name_of_product()
    page.read_price_of_product()
    print("\nYou are about to choose following item: " + page.item + " for price: " + page.price)
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    # asserts
    page.should_dissappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    # asserts
    page.should_be_login_form()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    # asserts
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_checkout_button()
    basket_page.should_be_message("Your basket is empty.")





