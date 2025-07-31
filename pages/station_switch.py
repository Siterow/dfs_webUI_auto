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
        self.location_input_locator = (By.XPATH, data.get('search_station_location'))
        self.station_input_locator = (By.XPATH, data.get('search_station_name'))
        self.button_search = (By.XPATH, data.get('button_search'))
        self.choose_station_locator = (By.XPATH, data.get('choose_station'))
        self.button_switch_station = (By.XPATH, data.get('button_switch_station'))

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
        
        # # 尝试查找所有包含站点名称的元素
        # try:
        #     all_stations = self.driver.find_elements(By.XPATH, f'//*[contains(text(), "{stationName}")]')
        #     print(f"找到 {len(all_stations)} 个包含 '{stationName}' 的元素:")
        #     for i, elem in enumerate(all_stations):
        #         print(f"  元素 {i+1}: {elem.text}")
        # except Exception as e:
        #     print(f"查找元素时出错: {e}")
        #
        station_info = self.wait.until(EC.visibility_of_element_located(dynamic_station_locator))
        station_info.click()

    def click_switch_button(self):
        button = self.wait.until(EC.visibility_of_element_located(self.button_switch_station))
        button.click()

    def switch_station(self, locationName=None, stationName=None):
        locationName = locationName or self.default_locationName
        stationName = stationName or self.default_stationName
        self.choose_location(locationName)
        self.choose_station(stationName)
        self.click_switch_button()

