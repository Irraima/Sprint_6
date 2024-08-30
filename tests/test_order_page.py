import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators
from testdata import OrderData


class TestOrderPage:

    @pytest.mark.parametrize('name, last_name, address, metro, scooter_color, phone', [*OrderData.user])
    def test_create_order_by_header_button(self, driver, name, last_name, address, metro, scooter_color, phone):

        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.click_cookie_button()
        main_page.click_order_button_in_header()
        order_page.fill_user_data_form(name, last_name, address, metro, phone)
        order_page.set_order_details_and_confirm(scooter_color)
        result = order_page.get_text_from_popup()

        assert 'Заказ оформлен' in result

    @pytest.mark.parametrize('name, last_name, address, metro, scooter_color, phone', [*OrderData.user])
    def test_create_order_by_page_button(self,  driver, name, last_name, address, metro, scooter_color, phone):

        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.click_cookie_button()
        main_page.click_order_button_in_page()
        order_page.fill_user_data_form(name, last_name, address, metro, phone)
        order_page.set_order_details_and_confirm(scooter_color)
        result = order_page.get_text_from_popup()

        assert 'Заказ оформлен' in result
