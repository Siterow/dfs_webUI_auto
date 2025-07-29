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

    def input_location(self, locationName='1地点车间1'):
        input_box = self.wait.until(EC.visibility_of_element_located(self.location_input_locator))
        input_box.clear()
        input_box.send_keys(locationName)

    def switch_station(self, locationName=None, ):
        locationName = locationName or self.default_locationName
        self.input_location(locationName)
