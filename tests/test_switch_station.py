from conftest import logged_in_driver
from pages.home_page import HomePage
from pages.station_switch import StationSwitchPage
import time


def test_switch_station(logged_in_driver):
    try:
        home = HomePage(logged_in_driver)
        home.change_menu()
        time.sleep(1)
        station_switch = StationSwitchPage(logged_in_driver)
        station_switch.switch_station()
        time.sleep(2)
        # 示例断言，实际可根据切换后页面内容调整
        assert "确认切换" in logged_in_driver.page_source
    except Exception as e:
        print(f"测试失败: {e}")
        # 打印当前页面源码以便调试
        print("当前页面源码:")
        print(logged_in_driver.page_source[:1000])  # 只打印前1000个字符
        raise



