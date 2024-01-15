from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, setup_driver):
        self.driver = setup_driver
        self.base_url = 'https://qa-scooter.praktikum-services.ru/'

    def go_base_page(self):
        return self.driver.get(self.base_url)

    def get_element(self, locator):
        return self.driver.find_element(*locator)

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))

    def click_element(self, locator):
        return self.driver.find_element(*locator).click()

    def set_value(self, locator, value):
        return self.driver.find_element(*locator).send_keys(value)

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_page(self):
        return self.driver.current_url

    def wait_for_new_window(self):
        return WebDriverWait(self.driver, 5).until(expected_conditions.number_of_windows_to_be(2))

    def switch_to_window(self):
        return self.driver.switch_to.window(self.driver.window_handles[-1])
