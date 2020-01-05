from time import sleep

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver=None):
        if driver is None:
            # index页面需要用这个，因为index是一个新页面
            self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(3)

            self._driver.get(self._base_url)
        else:
            # Login和register等页面需要用，因为他们是从上一个页面跳转的
            self._driver = driver

    def close(self):
        sleep(20)
        self._driver.quit()
