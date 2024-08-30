from selenium.webdriver.common.by import By


class OrderPageLocators:

    NAME_FIELD = By.XPATH, './/input[@placeholder="* Имя"]'
    LAST_FIELD = By.XPATH, './/input[@placeholder="* Фамилия"]'
    ADDRESS_FIELD = By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]'
    METRO_FIELD = By.CSS_SELECTOR, 'input[placeholder="* Станция метро"]'
    METRO_STATION = By.XPATH, '//div[text()="{}"]'
    PHONE_FIELD = By.CSS_SELECTOR, 'input[placeholder="* Телефон: на него позвонит курьер"]'
    NEXT_BUTTON = By.XPATH, './/button[text()="Далее"]'

    DATE_FIELD = By.CSS_SELECTOR, 'input[placeholder="* Когда привезти самокат"]'
    CHOOSE_DATE = By.CLASS_NAME, "react-datepicker__day--today"
    DURATION_FIELD = By.CLASS_NAME, "Dropdown-root"
    DURATION_RENT = By.XPATH, './/div[@class = "Dropdown-option" and text()="двое суток"]'

    SCOOTER_COLOR = By.XPATH, './/input[@id="{}"]/parent::label'
    GREY_COLOR = By.ID, "grey"
    ORDER_BUTTON = By.XPATH, './/*[contains(@class,"Order_Buttons")]//button[text()="Заказать"]'
    CONFIRM_BUTTON = By.XPATH, './/button[text()="Да"]'
    ORDER_COMPLETE = By.XPATH, './/*[contains(@class,"Order_ModalHeader")]'
