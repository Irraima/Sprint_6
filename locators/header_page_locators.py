from selenium.webdriver.common.by import By


class HeaderPageLocators:

    SCOOTER_LOGO = By.XPATH, './/a[contains(@class, "Header_LogoScooter")]'
    YANDEX_LOGO = By.XPATH, './/a[contains(@class, "Header_LogoYandex")]'
