import pytest
from selenium import webdriver


@pytest.fixture
def setup_driver():
    driver = webdriver.Firefox()
    driver.fullscreen_window()
    yield driver
    driver.quit()
