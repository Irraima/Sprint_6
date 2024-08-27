from data import Login
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.by import By


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @staticmethod
    def click_logo_yandex(driver):
        driver.find_element(By.XPATH, OrderPageLocators.LOGO_YANDEX).click()

    @staticmethod
    def click_logo_scooter(driver):
        driver.find_element(By.XPATH, OrderPageLocators.LOGO_SCOOTER).click()

    @staticmethod
    def input_name(driver):
        driver.find_element(By.XPATH, OrderPageLocators.INPUT_NAME).send_keys(Login.NAME)

    @staticmethod
    def input_alt_name(driver):
        driver.find_element(By.XPATH, OrderPageLocators.INPUT_NAME).send_keys(Login.ALT_NAME)

    @staticmethod
    def input_surname(driver):
        driver.find_element(By.XPATH, OrderPageLocators.INPUT_SURNAME).send_keys(Login.SURNAME)

    @staticmethod
    def input_alt_surname(driver):
        driver.find_element(By.XPATH, OrderPageLocators.INPUT_SURNAME).send_keys(Login.ALT_SURNAME)

    @staticmethod
    def input_address(driver):
        driver.find_element(By.XPATH, OrderPageLocators.INPUT_ADDRESS).send_keys(Login.ADDRESS)

    @staticmethod
    def input_alt_address(driver):
        driver.find_element(By.XPATH, OrderPageLocators.INPUT_ADDRESS).send_keys(Login.ALT_ADDRESS)

    @staticmethod
    def open_select_metro_station(driver):
        driver.find_element(By.XPATH, OrderPageLocators.OPEN_SELECT_METRO_STATION).click()

    @staticmethod
    def select_metro(driver):
        driver.find_element(By.XPATH, OrderPageLocators.OPEN_SELECT_METRO_STATION).click()
        driver.find_element(By.XPATH, f"//button[starts-with(@class, 'Order_SelectOption')]/div[text()='Бульвар Рокоссовского']").click()

    @staticmethod
    def select_alt_metro(driver):
        driver.find_element(By.XPATH, OrderPageLocators.OPEN_SELECT_METRO_STATION).click()
        driver.find_element(By.XPATH, f"//button[starts-with(@class, 'Order_SelectOption')]/div[text()='Комсомольская']").click()

    @staticmethod
    def input_phone_number(driver):
        driver.find_element(By.XPATH, OrderPageLocators.INPUT_PHONE_NUMBER).send_keys(Login.PHONE_NUMBER)

    @staticmethod
    def input_alt_phone_number(driver):
        driver.find_element(By.XPATH, OrderPageLocators.INPUT_PHONE_NUMBER).send_keys(Login.ALT_PHONE_NUMBER)

    @staticmethod
    def click_next_button(driver):
        driver.find_element(By.XPATH, OrderPageLocators.NEXT_BUTTON).click()

    @staticmethod
    def click_title(driver):
        driver.find_element(By.XPATH, OrderPageLocators.TITLE_ORDER_PAGE).click()
