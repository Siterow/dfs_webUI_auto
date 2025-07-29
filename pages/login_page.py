import os
from selenium.webdriver.common.by import By
from utils.read_yaml import read_yaml


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        # 读取登录信息
        data = read_yaml(os.path.join(os.path.dirname(__file__), "../data/login_data.yaml"))
        test_data = read_yaml(os.path.join(os.path.dirname(__file__), "../data/test_data.yaml"))
        self.default_username = test_data.get("username")
        self.default_password = test_data.get("password")
        self.url = test_data.get("loginUrl")
        self.username_locator = (By.XPATH, data.get("username_locator"))
        self.password_locator = (By.XPATH, data.get("password_locator"))
        self.login_button_locator = (By.XPATH, data.get("login_button_locator"))

    def open(self):
        self.driver.get(self.url)

    def input_username(self, username):
        self.driver.find_element(*self.username_locator).send_keys(username)

    def input_password(self, password):
        self.driver.find_element(*self.password_locator).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button_locator).click()

    def login(self, username=None, password=None):
        self.open()
        username = username or self.default_username
        password = password or self.default_password
        self.input_username(username)
        self.input_password(password)
        self.click_login()

