from data import URL
from pages.base_page import BasePage
from pages.order_page import OrderPage


class TestClickLogoScooter:

    def test_click_logo_scooter(self, driver):
        BasePage.click_top_page_order_button(driver)
        OrderPage.click_logo_scooter(driver)
        assert driver.current_url == URL.URL
