from pages.base_page import BasePage
from pages.order_page import OrderPage
from pages.about_rent_page import AboutRentPage
from locators.about_rent_locators import AboutRentLocators
from selenium.webdriver.support import expected_conditions


class TestAltOrderingAScooter:
    def test_alt_ordering_a_scooter(self, driver):
        BasePage.scroll_by_bottom_page_order_button(driver)
        BasePage.click_bottom_page_order_button(driver)
        OrderPage.input_alt_name(driver)
        OrderPage.input_alt_surname(driver)
        OrderPage.input_alt_address(driver)
        OrderPage.select_alt_metro(driver)
        OrderPage.input_alt_phone_number(driver)
        OrderPage.click_next_button(driver)
        AboutRentPage.input_alt_date(driver)
        AboutRentPage.click_about_rent_title(driver)
        AboutRentPage.open_rent_time(driver)
        AboutRentPage.choose_rent_time_three_days(driver)
        AboutRentPage.click_order_button(driver)
        AboutRentPage.click_accept_button(driver)
        assert expected_conditions.visibility_of_element_located(AboutRentLocators.PLACED_ORDER)