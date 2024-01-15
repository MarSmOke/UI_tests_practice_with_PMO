Автотесты для сервиса Яндекс.Самокат:

- проверка флоу заказа самоката - test_make_order;
- проверка списка "Важных вопросов" - test_dropdown_list;
- проверка редиректов - test_redirect.

Фикстуры хранятся в conftest, локаторы - в файле locators, результаты прогона тестов - в папке allure_results. \
Необходима установка allure, selenium, pytest.\
Используемый браузер - Mozilla Firefox.