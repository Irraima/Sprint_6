from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def go_to(self, link):
        self.driver.get(link)

    def click_to_question(self, locator, num):
        method, locator = locator
        locator = locator.format(num)
        self.find_element_with_wait((method, locator))
        self.click_on_element((method, locator))

    def get_answer(self, locator, num):
        method, locator = locator
        locator = locator.format(num)
        element = self.find_element_with_wait((method, locator))
        return self.get_text_from_element(element)

    def click_cookie_button(self, locator=MainPageLocators.COOKIE_BUTTON):
        self.find_element_with_wait(locator)
        self.click_on_element(locator)

    def click_order_button_in_header(self):
        self.find_element_with_wait(MainPageLocators.ORDER_BUTTON_HEADER).click()

    def click_order_button_in_page(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_IN_PAGE)
        self.click_on_element(MainPageLocators.ORDER_BUTTON_IN_PAGE)
