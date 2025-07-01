import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.read_yaml import read_yaml


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # 读取右上角信息
        yaml_path = os.path.join(os.path.dirname(__file__), '../data/home_page_data.yaml')
        data = read_yaml(yaml_path)
        self.userMenu_locator = (By.XPATH, data.get("userMenu_locator"))
        self.logout_button_locator = (By.XPATH, data.get('logout_button_locator'))

    def click_avatar(self):
        avatar = self.wait.until(EC.element_to_be_clickable(self.userMenu_locator))
        avatar.click()

    def click_logout(self):
        logout = self.wait.until(EC.visibility_of_element_located(self.logout_button_locator))
        print("正在退出登录")
        logout.click()

