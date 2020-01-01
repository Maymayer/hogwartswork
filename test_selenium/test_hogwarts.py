import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestHogwarts:
    def setup_method(self):
        """
        # 多浏览器方法
        browser = os.getenv("browser", "").lower()
        if browser == "edge":
            self.driver = webdriver.Edge()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Chrome()
        """
        # options = webdriver.ChromeOptions()
        """
        搞定chrome被windows defender修改打开设置方法：打开注册表 regedit， 直接找下面路径并删除
        HKEY_CURRENT_USER\\Software\\Google\\Chrome\\TriggeredReset
        # 禁止 Chrome 收到自动测试软件控制显示
        # options.add_argument("disable-infobars")
        先启动一个带命令行参数--remote-debugging-port=9222的浏览器即可使用以下方法
        # options.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=options)
        """
        self.driver = webdriver.Chrome()
        self.driver.get("https://testerhome.com")
        self.driver.implicitly_wait(5)

    def wait(self, timeout, method):
        WebDriverWait(self.driver, timeout).until(method)

    def test_hogwarts(self):
        self.driver.find_element(By.LINK_TEXT, '社团').click()
        # sleep(1)
        # todo: 显式等待
        element = (By.PARTIAL_LINK_TEXT, '霍格沃兹测试学院')
        self.driver.set_window_size(1222, 823)
        self.driver.save_screenshot("1.png")
        self.wait(10, expected_conditions.element_to_be_clickable(element))
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element))
        self.driver.find_element(*element).click()
        # self.driver.find_element(By.CSS_SELECTOR, '[data-name="霍格沃兹测试学院"]').click()
        # done：隐式等待
        # self.driver.find_element(By.CSS_SELECTOR, '.topic:nth-child(1) .title a').click()

    def test_testerhome(self):
        self.driver.find_element(By.LINK_TEXT, "MTSC2020 中国互联网测试开发大会议题征集").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn > .caret").click()
        self.driver.find_element(By.LINK_TEXT, "征集议题范围").click()

    def test_testerhome_2(self):
        element1 = (By.PARTIAL_LINK_TEXT, 'MTSC2020 中国互联网测试开发大会议题征集')
        self.wait(10, expected_conditions.element_to_be_clickable(element1))
        self.driver.find_element(*element1).click()
        element2 = (By.CSS_SELECTOR, '[class="btn btn-default"]')
        self.wait(10, expected_conditions.element_to_be_clickable(element2))
        self.driver.find_element(*element2).click()
        # self.driver.find_element(By.LINK_TEXT, "征集议题范围").click()
        element3 = (By.CSS_SELECTOR, '.toc-item-link:nth-child(4)')
        self.wait(10, expected_conditions.element_to_be_clickable(element3))
        self.driver.find_element(*element3).click()

    # 老师示例窗口等方法
    def test_mtsc2020(self):
        self.driver.get("https://testerhome.com/topics/21805")
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "第六届中国互联网测试开发大会").click()
        print(self.driver.window_handles)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.save_screenshot("1.png")
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "演讲申请").click()

    def test_js(self):
        for code in [
            "return document.title",
            "return document.querySelector('.active').className",
            "return JSON.stringify(performance.timing)"
        ]:
            result = self.driver.execute_script(code)
            print(result)

    def teardown_method(self):
        sleep(5)
        self.driver.quit()
