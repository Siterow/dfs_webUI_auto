"""
站点切换页面，依次进行筛选地点->点击地点->筛选站点->切换站点界面
"""
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.read_yaml import read_yaml
import os


class WeldingHxSingle:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # 读取定位器
        data = read_yaml(os.path.join(os.path.dirname(__file__), '../data/home_page_data.yaml'))
        self.update_toorCode = (By.XPATH, data.get('update_toorCode'))
        self.update_boxCode = (By.XPATH, data.get('update_boxCode'))
        # 暗门定位器
        self.open_simulation = (By.XPATH, data.get('open-simulation'))
        self.hidden_gate_input = (By.XPATH, data.get('hidden_gate_input'))
        self.dialog_mask = (By.XPATH, data.get('dialog_mask'))

    def reset_toorCode(self):
        self.wait.until(EC.visibility_of_element_located(self.update_toorCode)).click()
        time.sleep(3)
        self.wait.until(EC.visibility_of_element_located(self.update_boxCode)).click()

    def open_hidden_gate(self, width_px: int = 100, height_px: int = 100):
        """
        通过修改元素宽高，打开暗门元素并点击。
        """
        gate = self.wait.until(EC.presence_of_element_located(self.open_simulation))
        # 设置宽高，必要时确保可见性和可点击性
        self.driver.execute_script(
            "arguments[0].style.width=arguments[1];"
            "arguments[0].style.height=arguments[2];"
            "arguments[0].style.display='block';"
            "arguments[0].style.visibility='visible';"
            "arguments[0].style.opacity='1';",
            gate,
            f"{width_px}px",
            f"{height_px}px",
        )
        # 使用 JS 点击避免遮挡/拦截
        self.driver.execute_script("arguments[0].click();", gate)

    def open_hidden_gate_and_submit(self, content: str, width_px: int = 100, height_px: int = 100):
        """
        打开暗门 → 输入内容 → 点击弹窗外部（遮罩）关闭。
        如果遮罩不存在，降级为发送 ESC 关闭。
        """
        self.open_hidden_gate(width_px=width_px, height_px=height_px)
        # 查找并选择可见且可交互的输入框
        time.sleep(3)
        print("正在点击暗门")
        input_box = self.wait.until(EC.visibility_of_element_located(self.hidden_gate_input))
        input_box.send_keys(content)
        input_box.send_keys(Keys.ENTER)

        # self.driver.execute_script(
        #     """
        #     function setElInputByLabel(labelText, value) {
        #       let label = Array.from(document.querySelectorAll('label.el-form-item__label'))
        #                        .find(l => l.textContent.trim() === labelText);
        #       if (!label) return false;
        #       let input = label.nextElementSibling?.querySelector('input');
        #       if (!input) return false;
        #       input.value = value;
        #       input.dispatchEvent(new Event('input', { bubbles: true }));
        #       input.dispatchEvent(new Event('change', { bubbles: true }));
        #       return true;
        #     }
        #     function generateRandomDigits(length) {
        #       return Array.from({length}, () => Math.floor(Math.random() * 10)).join('');
        #     }
        #     let randomValue = 'TEST-DJM-' + generateRandomDigits(9);
        #     setElInputByLabel('扫码', randomValue);
        #     """
        # )


    # def welding_hx_manufacture(self, content = None):
    #     # self.reset_toorCode()
    #     # time.sleep(3)
    #     lotCode = content or 'content'
    #     self.open_hidden_gate_and_submit(lotCode,100,100)





