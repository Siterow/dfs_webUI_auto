import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.read_yaml import read_yaml


# 点击右上角人的头像来登出
class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # 读取右上角信息
        yaml_path = os.path.join(os.path.dirname(__file__), '../data/home_page_data.yaml')
        data = read_yaml(yaml_path)
        self.userMenu_locator = (By.XPATH, data.get("userMenu_locator"))  # 右上角用户头像
        self.logout_button_locator = (By.XPATH, data.get('logout_button_locator'))  # 退出登录按钮
        self.menu_business_locator = (By.XPATH, data.get('menu_business_locator'))  # 左侧菜单树
        self.menu_stationSwitch_locator = (By.XPATH, data.get('menu_stationSwitch_locator'))  # 选择菜单鼠后点功能

    def click_menu_tree(self):
        self.wait.until(EC.element_to_be_clickable(self.menu_business_locator)).click()

    def click_menu(self):
        self.wait.until(EC.element_to_be_clickable(self.menu_stationSwitch_locator)).click()

    # 点用户头像
    def click_avatar(self):
        avatar = self.wait.until(EC.element_to_be_clickable(self.userMenu_locator))
        avatar.click()

    def click_logout(self):
        logout = self.wait.until(EC.visibility_of_element_located(self.logout_button_locator))
        print("正在退出登录")
        logout.click()

    def change_menu(self):
        self.click_menu_tree()
        self.click_menu()

