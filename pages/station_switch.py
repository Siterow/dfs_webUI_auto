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
        self.location_input_locator = (By.XPATH, data.get('search_station_location'))
        self.station_input_locator = (By.XPATH, data.get('search_station_name'))
        self.button_search = (By.XPATH, data.get('button_search'))
        self.choose_station_locator = (By.XPATH, data.get('choose_station'))
        self.button_switch_station = (By.XPATH, data.get('button_switch_station'))
        self.welding_hx_single = (By.XPATH, data.get('welding_hx_single'))
        self.welding_hx_single_check = (By.XPATH, data.get('welding_hx_single_check'))
        # 读取基础数据，地点名称与站点名称
        test_data = read_yaml(os.path.join(os.path.dirname(__file__), "../data/test_data.yaml"))
        self.default_locationName = test_data.get('locationName')
        self.default_stationName = test_data.get('stationName')

    def choose_location(self, locationName):
        input_box = self.wait.until(EC.visibility_of_element_located(self.location_input_locator))
        input_box.clear()
        input_box.send_keys(locationName)
        time.sleep(1)
        # 使用动态定位器来匹配搜索的地点名称
        dynamic_location_locator = (By.XPATH, f'//span[contains(text(), "{locationName}")]')
        print(f"正在查找站点: {locationName}")
        print(f"使用的定位器: {dynamic_location_locator}")
        station_info = self.wait.until(EC.visibility_of_element_located(dynamic_location_locator))
        station_info.click()

    def choose_station(self, stationName):
        input_box = self.wait.until(EC.visibility_of_element_located(self.station_input_locator))
        input_box.clear()
        input_box.send_keys(stationName)
        search_click_info = self.wait.until(EC.visibility_of_element_located(self.button_search))
        search_click_info.click()
        time.sleep(2)  # 增加等待时间
        # 使用动态定位器来匹配搜索的站点名称
        dynamic_station_locator = (By.XPATH, f'//span[contains(text(), "{stationName}")]')
        print(f"正在查找站点: {stationName}")
        print(f"使用的定位器: {dynamic_station_locator}")
        station_info = self.wait.until(EC.visibility_of_element_located(dynamic_station_locator))
        station_info.click()
        self.wait.until(EC.visibility_of_element_located(self.welding_hx_single)).click()
        self.wait.until(EC.visibility_of_element_located(self.welding_hx_single_check)).click()

    def click_switch_button(self):
        button = self.wait.until(EC.visibility_of_element_located(self.button_switch_station))
        button.click()

    def switch_station(self, locationName=None, stationName=None):
        locationName = locationName or self.default_locationName
        stationName = stationName or self.default_stationName
        self.choose_location(locationName)
        self.choose_station(stationName)
        # self.click_switch_button()

