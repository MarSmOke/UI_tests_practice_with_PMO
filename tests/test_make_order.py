import locators
from pages.order_page import OrderPageScooter
import pytest
from datetime import datetime
import allure


class TestMakeOrder:

    order_data_1 = ['Марина', 'Смирнова', 'ул. Восточная, 11в', '+7991402789', 'Пожалуйста, позвоните за час']
    order_data_2 = ['Татьяна', 'Нестерова', 'ул. Декабристов, 1', '+79221377337', '']

    @allure.title("Make an order")
    @allure.description("Positive scenario of making order with two different buttons and customer data")
    @pytest.mark.parametrize('order_data, order_button', [[order_data_1, locators.order_button_header], [order_data_2, locators.order_button_finish]])
    def test_fill_the_from(self, setup_driver, order_data, order_button):
        order_page = OrderPageScooter(setup_driver)
        order_page.go_base_page()
        order_page.scroll_to_element(order_button)
        order_page.wait_for_element(order_button)
        order_page.click_element(order_button)
        order_page.fill_form_for_whom(f"{order_data[0]}", f"{order_data[1]}",
                                      f"{order_data[2]}", f"{order_data[3]}")
        order_page.click_next_button()
        order_page.fill_form_about_rent(f"{datetime.now().date()}", f"{order_data[4]}")
        order_page.click_next_button()
        order_page.click_confirm_button()
        assert order_page.wait_for_element(locators.cancel_button)

