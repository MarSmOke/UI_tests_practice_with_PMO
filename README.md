Autotests for the Yandex.Scooter service:

- scooter order flow - test_make_order;
- list of “Important issues” - test_dropdown_list;
- redirects - test_redirect.

Fixtures are stored in conftest, locators are stored in the locators file, and test run results are stored in the allure_results folder. \
Requires installation of allure, selenium, pytest.\
The browser used is Mozilla Firefox.
