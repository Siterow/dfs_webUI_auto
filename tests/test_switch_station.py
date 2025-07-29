from conftest import logged_in_driver
from pages.home_page import HomePage
from pages.station_switch import StationSwitchPage
import time


def test_switch_station(logged_in_driver):
    home = HomePage(logged_in_driver)
    home.click_menu_tree()
    home.click_menu()
    station_switch = StationSwitchPage(logged_in_driver)
    station_switch.switch_station()
    time.sleep(2)
    # 示例断言，实际可根据切换后页面内容调整
    assert "站点切换" in logged_in_driver.page_source



