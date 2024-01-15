from pages.main_page import MainPageScooter
import pytest
import allure
import locators


class TestDropdownList:
    @allure.title('Get answers for selected questions')
    @allure.description("Click each question and get the answer")
    @pytest.mark.parametrize('question, answer, expected_text',
         [[locators.question_0, locators.answer_0, locators.texts[0]],
         [locators.question_1, locators.answer_1, locators.texts[1]],
         [locators.question_2, locators.answer_2, locators.texts[2]],
         [locators.question_3, locators.answer_3, locators.texts[3]],
         [locators.question_4, locators.answer_4, locators.texts[4]],
         [locators.question_5, locators.answer_5, locators.texts[5]],
         [locators.question_6, locators.answer_6, locators.texts[6]],
         [locators.question_7, locators.answer_7, locators.texts[7]]]
                             )
    def test_answer_the_question(self, setup_driver, question, answer, expected_text):
        main_page = MainPageScooter(setup_driver)
        main_page.go_base_page()
        main_page.click_cookie()
        main_page.scroll_to_element(question)
        main_page.click_element(question)
        main_page.wait_for_element(answer)
        assert main_page.get_element(answer).text == expected_text
