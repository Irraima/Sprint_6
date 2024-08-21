from pages.base_page import BasePage
from locators import base_page_locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestTextParILiveOutsideTheMRR:

    def test_text_par_i_live_outside_the_mrr(self, driver):
        BasePage.scroll_by_about_the_important(driver)
        driver.find_element(By.XPATH, base_page_locators.BasePageLocators.I_LIVE_OUTSIDE_THE_MRR).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, base_page_locators.BasePageLocators.I_LIVE_OUTSIDE_THE_MRR_OPEN)))
        assert driver.find_element(By.XPATH, base_page_locators.BasePageLocators.I_LIVE_OUTSIDE_THE_MRR_OPEN).text ==  base_page_locators.BasePageLocators.I_LIVE_OUTSIDE_THE_MRR_TEXT
