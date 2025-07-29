from conftest import logged_in_driver
from pages.home_page import HomePage
import time


def test_logout(logged_in_driver):
    logout = HomePage(logged_in_driver)
    logout.click_avatar()
    time.sleep(2)
    logout.click_logout()
    assert "退出" in logged_in_driver.page_source
