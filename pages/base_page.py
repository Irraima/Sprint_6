from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @staticmethod
    def get_text_from_element(element):
        return element.text

    def set_text_to_form(self, locator, text):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).send_keys(text)

    def scroll_to_bottom_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_and_click_with_wait(self, locator):
        self.driver.execute_script('arguments[0].scrollIntoView();', self.driver.find_element(*locator))
        self.click_on_element(locator)

    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

    def switch_pages(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains('https://dzen.ru/'))
