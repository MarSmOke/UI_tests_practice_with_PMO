import allure
from pages.base_page import BasePage
import locators


class MainPageScooter(BasePage):

    @allure.step('Click cookie')
    def click_cookie(self):
        self.click_element(locators.cookie_button)

    @allure.step('Click Yandex logo')
    def click_yandex_logo(self):
        self.click_element(locators.yandex_logo)

    @allure.step('Click Scooter logo')
    def click_scooter_logo(self):
        self.click_element(locators.scooter_logo)
