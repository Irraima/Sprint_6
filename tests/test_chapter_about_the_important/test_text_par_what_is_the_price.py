from pages.base_page import BasePage
from locators import base_page_locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestTextParWhatIsThePrice:

    def test_text_par_what_is_the_price(self, driver):
        BasePage.scroll_by_about_the_important(driver)
        driver.find_element(By.XPATH, base_page_locators.BasePageLocators.WHAT_IS_THE_PRICE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, base_page_locators.BasePageLocators.WHAT_IS_THE_PRICE_OPEN)))
        assert driver.find_element(By.XPATH, base_page_locators.BasePageLocators.WHAT_IS_THE_PRICE_OPEN).text == base_page_locators.BasePageLocators.WHAT_IS_THE_PRICE_TEXT
