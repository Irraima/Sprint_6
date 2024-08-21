from pages.base_page import BasePage
from pages.order_page import OrderPage
from pages.about_rent_page import AboutRentPage
from locators.about_rent_locators import AboutRentLocators
from selenium.webdriver.support import expected_conditions


class TestOrderingAScooter:
    def test_ordering_a_scooter(self, driver):
        BasePage.click_top_page_order_button(driver)
        OrderPage.input_name(driver)
        OrderPage.input_surname(driver)
        OrderPage.input_address(driver)
        OrderPage.select_metro(driver)
        OrderPage.input_phone_number(driver)
        OrderPage.click_next_button(driver)
        AboutRentPage.input_date(driver)
        AboutRentPage.click_about_rent_title(driver)
        AboutRentPage.open_rent_time(driver)
        AboutRentPage.choose_rent_time_two_days(driver)
        AboutRentPage.click_order_button(driver)
        AboutRentPage.click_accept_button(driver)
        assert expected_conditions.visibility_of_element_located(AboutRentLocators.PLACED_ORDER)
