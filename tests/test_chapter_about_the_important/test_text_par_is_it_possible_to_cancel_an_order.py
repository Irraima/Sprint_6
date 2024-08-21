from pages.base_page import BasePage
from locators import base_page_locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestTextParIsItPossibleToCancelAnOrder:

    def test_text_par_is_it_possible_to_cancel_an_order(self, driver):
        BasePage.scroll_by_about_the_important(driver)
        driver.find_element(By.XPATH, base_page_locators.BasePageLocators.IS_IT_POSSIBLE_TO_CANCEL_AN_ORDER).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, base_page_locators.BasePageLocators.IS_IT_POSSIBLE_TO_CANCEL_AN_ORDER_OPEN)))
        assert driver.find_element(By.XPATH, base_page_locators.BasePageLocators.IS_IT_POSSIBLE_TO_CANCEL_AN_ORDER_OPEN).text == base_page_locators.BasePageLocators.IS_IT_POSSIBLE_TO_CANCEL_AN_ORDER_TEXT
