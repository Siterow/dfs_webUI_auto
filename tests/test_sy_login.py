from pages.login_page import LoginPage
import time


def test_login(driver):
    page = LoginPage(driver)
    page.login()  # 使用yaml里的账号密码
    time.sleep(2)
    assert "退出登录" in driver.page_source
