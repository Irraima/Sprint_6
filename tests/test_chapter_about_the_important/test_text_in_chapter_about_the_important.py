from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest


class TestTextInChapterAboutTheImportant:

    @pytest.mark.parametrize(
        'question,opens,answer',
        [
            [BasePageLocators.WHAT_IS_THE_PRICE, BasePageLocators.WHAT_IS_THE_PRICE_OPEN, BasePageLocators.WHAT_IS_THE_PRICE_TEXT],
            [BasePageLocators.I_WANT_SEVERAL_AT_ONCE, BasePageLocators.I_WANT_SEVERAL_AT_ONCE_OPEN, BasePageLocators.I_WANT_SEVERAL_AT_ONCE_TEXT],
            [BasePageLocators.HOW_TIME_IS_CALCULATED, BasePageLocators.HOW_TIME_IS_CALCULATED_OPEN, BasePageLocators.HOW_TIME_IS_CALCULATED_TEXT],
            [BasePageLocators.POSSIBLE_TO_ORDER_FOR_TODAY, BasePageLocators.POSSIBLE_TO_ORDER_FOR_TODAY_OPEN, BasePageLocators.POSSIBLE_TO_ORDER_FOR_TODAY_TEXT],
            [BasePageLocators.POSSIBLE_TO_EXTEND_THE_ORDER, BasePageLocators.POSSIBLE_TO_EXTEND_THE_ORDER_OPEN, BasePageLocators.POSSIBLE_TO_EXTEND_THE_ORDER_TEXT],
            [BasePageLocators.DO_YOU_BRING_A_CHARGER, BasePageLocators.DO_YOU_BRING_A_CHARGER_OPEN, BasePageLocators.DO_YOU_BRING_A_CHARGER_TEXT],
            [BasePageLocators.IS_IT_POSSIBLE_TO_CANCEL_AN_ORDER, BasePageLocators.IS_IT_POSSIBLE_TO_CANCEL_AN_ORDER_OPEN, BasePageLocators.IS_IT_POSSIBLE_TO_CANCEL_AN_ORDER_TEXT],
            [BasePageLocators.I_LIVE_OUTSIDE_THE_MRR, BasePageLocators.I_LIVE_OUTSIDE_THE_MRR_OPEN, BasePageLocators.I_LIVE_OUTSIDE_THE_MRR_TEXT]
        ]
    )
    def test_negative_input(self, question, opens, answer, driver):
        BasePage.scroll_by_about_the_important(driver)
        driver.find_element(By.XPATH, question).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, opens)))
        assert driver.find_element(By.XPATH, opens).text == answer
