"""
站点切换页面，依次进行筛选地点->点击地点->筛选站点->切换站点界面
"""
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.read_yaml import read_yaml
import os


class StationSwitchPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # 读取定位器
        data = read_yaml(os.path.join(os.path.dirname(__file__), '../data/home_page_data.yaml'))
        test_data = read_yaml(os.path.join(os.path.dirname(__file__), "../data/test_data.yaml"))
        self.location_input_locator = (By.XPATH, data.get('menu_stationSwitch_locationInput_locator'))
        self.default_locationName = test_data.get('locationName')
        self.choose_station_location = (By.XPATH, data.get('choose_station_location'))

    def input_location(self, locationName):
        input_box = self.wait.until(EC.visibility_of_element_located(self.location_input_locator))
        input_box.clear()
        input_box.send_keys(locationName)

    def choose_location(self):
        location_info =  self.wait.until(EC.visibility_of_element_located(self.choose_station_location))
        location_info.click()

    def switch_station(self, locationName=None, ):
        locationName = locationName or self.default_locationName
        self.input_location(locationName)
        time.sleep(2)
        self.choose_location()

