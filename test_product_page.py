import time
from pages.product_page import ProductPage


# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()                      # открываем страницу
#     page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.read_name_of_product()
    page.read_price_of_product()
    print ("\nYou are about to choose following item: " + page.item + " for price: " + page.price )
    page.add_to_basket()
    page.solve_quiz_and_get_code()

    page.product_should_be(page.item)
    page.price_should_be(page.price)



    time.sleep(5)


    # login_page = LoginPage(browser, browser.current_url)
    # login_page.should_be_login_form()
    # login_page.should_be_register_form()

