import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()


@pytest.fixture
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    login_page.login()  # 用 yaml 的账号密码
    return driver
