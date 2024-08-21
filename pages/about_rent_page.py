from data import Data
from pages.base_page import BasePage
from locators.about_rent_locators import AboutRentLocators
from selenium.webdriver.common.by import By


class AboutRentPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @staticmethod
    def input_date(driver):
        driver.find_element(By.XPATH, AboutRentLocators.DATE).send_keys(Data.DATE)

    @staticmethod
    def input_alt_date(driver):
        driver.find_element(By.XPATH, AboutRentLocators.DATE).send_keys(Data.ALT_DATE)

    @staticmethod
    def open_rent_time(driver):
        driver.find_element(By.XPATH, AboutRentLocators.RENT_TIME).click()

    @staticmethod
    def choose_rent_time_three_days(driver):
        driver.find_element(By.XPATH, AboutRentLocators.CHOOSE_RENT_TIME_THREE_DAYS).click()

    @staticmethod
    def choose_rent_time_two_days(driver):
        driver.find_element(By.XPATH, AboutRentLocators.CHOOSE_RENT_TIME_TWO_DAYS).click()

    @staticmethod
    def click_order_button(driver):
        driver.find_element(By.XPATH, AboutRentLocators.ORDER_BUTTON).click()

    @staticmethod
    def click_accept_button(driver):
        driver.find_element(By.XPATH, AboutRentLocators.ACCEPT_BUTTON).click()

    @staticmethod
    def click_about_rent_title(driver):
        driver.find_element(By.XPATH, AboutRentLocators.ABOUT_RENT_TITLE).click()
