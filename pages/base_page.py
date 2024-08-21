from locators.base_page_locators import BasePageLocators
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def scroll_by_about_the_important(driver):
        element = driver.find_element(By.XPATH, BasePageLocators.ABOUT_THE_IMPORTANT)
        driver.execute_script("arguments[0].scrollIntoView();", element)

    @staticmethod
    def click_top_page_order_button(driver):
        driver.find_element(By.XPATH, BasePageLocators.TOP_PAGE_ORDER_BUTTON).click()

    @staticmethod
    def scroll_by_bottom_page_order_button(driver):
        element = driver.find_element(By.XPATH, BasePageLocators.BOTTOM_PAGE_ORDER_BUTTON)
        driver.execute_script("arguments[0].scrollIntoView();", element)

    @staticmethod
    def click_bottom_page_order_button(driver):
        driver.find_element(By.XPATH, BasePageLocators.BOTTOM_PAGE_ORDER_BUTTON).click()

    @staticmethod
    def click_logo_yandex(driver):
        driver.find_element(By.XPATH, BasePageLocators.LOGO_YANDEX).click()

    @staticmethod
    def click_logo_scooter(driver):
        driver.find_element(By.XPATH, BasePageLocators.LOGO_SCOOTER).click()
    