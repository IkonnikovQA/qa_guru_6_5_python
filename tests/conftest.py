import pytest
from selene import browser
from selenium import webdriver
import os


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = os.getenv('selene_base_url', 'https://demoqa.com')
    browser.config.window_width = os.getenv('selene_window_width', 1920)
    browser.config.window_height = os.getenv('selene_window_height', 1080)
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless')
    browser.config.driver_options = driver_options

    yield

    browser.quit()