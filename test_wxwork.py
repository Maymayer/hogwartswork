from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_selenium.test_hogwarts import TestHogwarts


class TestWxwork:

    def setup_method(self):
        options = webdriver.ChromeOptions()
        # 先启动一个带命令行参数--remote-debugging-port=9222的浏览器且登陆到企业微信即可使用以下方法
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.implicitly_wait(5)

    def wait(self, timeout, method):
        WebDriverWait(self.driver, timeout).until(method)

    def test_add_member(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1) '
                                                  '.index_service_cnt_item_title').click()
        print(self.driver.window_handles)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.save_screenshot("1.png")
        self.driver.find_element(By.ID, "username").send_keys("abc")
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("12345")
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys("15812341234")
        self.driver.find_element(By.CSS_SELECTOR, '[class="qui_btn ww_btn ww_btn_Blue js_btn_continue'
                                                  '.member_colRight_operationBar:nth-child(3) > .ww_btn_Blue"]').click()