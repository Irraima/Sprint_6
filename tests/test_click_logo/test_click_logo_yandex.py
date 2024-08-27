from pages.base_page import BasePage
from pages.order_page import OrderPage
from data import URL
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestClickLogoYandex:

    def test_click_logo_yandex(self, driver):
        BasePage.click_top_page_order_button(driver)
        OrderPage.click_logo_yandex(driver)
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(URL.URL_YANDEX))
        assert driver.current_url == URL.URL_YANDEX
