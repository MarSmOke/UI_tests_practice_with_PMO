import allure
from pages.base_page import BasePage
import locators
import random


class OrderPageScooter(BasePage):

    @allure.step('Click the first order button')
    def click_order_button_first(self):
        self.click_element(locators.order_button_header)

    @allure.step('Click the second order button')
    def click_order_button_second(self):
        self.click_element(locators.order_button_finish)

    @allure.step('Click the next button')
    def click_next_button(self):
        self.click_element(locators.next_button)

    @allure.step('Click the confirm button')
    def click_confirm_button(self):
        self.click_element(locators.confirm_button)

    @allure.step('Set name')
    def set_name(self, name):
        self.set_value(locators.name_field, name)

    @allure.step('Set surname')
    def set_surname(self, surname):
        self.set_value(locators.surname_field, surname)

    @allure.step('Set address')
    def set_address(self, address):
        self.set_value(locators.address_field, address)

    @allure.step('Set station')
    def set_station(self):
        self.click_element(locators.station_field)
        path, locator = locators.station
        locator = locator.format(num=random.randint(1, 224))
        self.click_element((path, locator))

    @allure.step('Set phone')
    def set_phone(self, phone):
        self.set_value(locators.phone_field, phone)

    @allure.step('Set date')
    def set_date(self, date):
        self.set_value(locators.date_field, date)

    @allure.step('Set time terms')
    def set_time(self):
        self.wait_for_element(locators.time_field)
        self.click_element(locators.time_field)
        self.click_element(locators.days)

    @allure.step('Set scooter color')
    def set_color(self):
        self.click_element(locators.time_field)

    @allure.step('Set comment')
    def add_comment(self, comment):
        self.set_value(locators.comment_field, comment)

    @allure.step('Fill order form for whom')
    def fill_form_for_whom(self, name, surname, address, phone):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_station()
        self.set_phone(phone)

    @allure.step('Fill order form about rent')
    def fill_form_about_rent(self, date, comment):
        self.set_date(date)
        self.set_time()
        self.set_color()
        self.add_comment(comment)
