import links
import pytest
from pages.header_page import HeaderPage
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestHeaderPage:

    def test_scooter_logo(self, driver):

        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        header_page = HeaderPage(driver)

        main_page.click_cookie_button()
        main_page.click_order_button_in_header()
        order_page.find_name_field()
        header_page.click_on_scooter_logo()
        result_url = header_page.get_current_url()

        assert result_url == links.main_page

    def test_yandex_logo(self, driver):

        main_page = MainPage(driver)
        header_page = HeaderPage(driver)

        main_page.click_cookie_button()
        header_page.click_on_yandex_logo()
        header_page.switch_pages()
        result_url = header_page.get_current_url()

        assert result_url == links.dzen_page
