import locators
from pages.main_page import MainPageScooter
import allure


class TestRedirect:
    @allure.title('Redirect to the Dzen page')
    @allure.description("Click Yandex logo and go to the Dzen page")
    def test_yandex_redirect(self, setup_driver):
        main_page = MainPageScooter(setup_driver)
        main_page.go_base_page()
        main_page.click_yandex_logo()
        main_page.wait_for_new_window()
        main_page.switch_to_window()
        main_page.wait_for_element(locators.dzen_logo)
        assert main_page.get_page() == 'https://dzen.ru/?yredirect=true'

    @allure.title('Redirect to the Scooter page')
    @allure.description("Click Scooter logo and go to the same page")
    def test_scooter_redirect(self, setup_driver):
        main_page = MainPageScooter(setup_driver)
        main_page.go_base_page()
        main_page.wait_for_element(locators.scooter_logo)
        main_page.click_scooter_logo()
        assert main_page.get_page() == 'https://qa-scooter.praktikum-services.ru/'
