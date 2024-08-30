from selenium.webdriver.common.by import By


class MainPageLocators:

    QUESTION = By.ID, 'accordion__heading-{}'
    ANSWER = By.ID, 'accordion__panel-{}'
    COOKIE_BUTTON = By.ID, 'rcc-confirm-button'
    ORDER_BUTTON_HEADER = [By.XPATH, './/div[contains(@class,"Header_Nav")]//button[text()="Заказать"]']
    ORDER_BUTTON_IN_PAGE = [By.XPATH, './/div[contains(@class,"Home_FinishButton")]//button[text()="Заказать"]']



