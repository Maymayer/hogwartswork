from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ""
    _driver = None

    def __init__(self, driver: WebDriver = None, reuse=False):
        if driver is None:
            if reuse:
                options = webdriver.ChromeOptions()
                # options.add_argument("disable-infobars")
                # 先启动一个带命令行参数 - -remote - debugging - port = 9222
                # 的浏览器即可使用以下方法
                options.debugger_address = "127.0.0.1:9222"
                self._driver = webdriver.Chrome(options=options)
            else:
                # index页面需要用这个，因为index是一个新页面
                self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(3)
        else:
            # Login和register等页面需要用，因为他们是从上一个页面跳转的
            self._driver = driver
        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self, locator):
        return self._driver.find_element(*locator)

    def close(self):
        sleep(20)
        self._driver.quit()
