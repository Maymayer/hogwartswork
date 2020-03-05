import logging

import yaml
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    logging.basicConfig(level=logging.INFO)
    _driver: WebDriver
    _black_list = [
        (MobileBy.ID, 'tv_agree'),
        (By.XPATH, '//*[@text="确定"'),
        (MobileBy.ID, 'image_cancle'),
        (By.XPATH, '//*[@text="下次再说"')
    ]
    _error_max = 10
    _error_count = 0

    _params = {}

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    # todo: 当有广告、评价等各种弹框出现时，要进行异常流程处理，通过装饰器让函数自动处理异常
    def find(self, locator, value: str = None):
        logging.info(locator)
        logging.info(value)
        try:
            # 寻找控件
            if isinstance(locator, tuple):
                return self._driver.find_element(*locator)
            else:
                return self._driver.find_element(locator, value)
            # 成功，清空异常计数
            self._error_count = 0

            # element = self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(locator, value)
        except Exception as e:
            # 次数太多直接报错
            if self._error_count > self._error_max:
                raise e
            else:
                # 记录异常次数
                self._error_count += 1
            for element in self._black_list:
                # logging.info(element)
                elements = self.find(element)
                if len(elements) > 0:
                    elements[0].click()
                    return self.find(locator, value)

    # todo:通过装饰器让函数自动处理异常
    def find_and_get_text(self, locator, value: str = None):
        logging.info(locator)
        logging.info(value)
        try:
            # 寻找控件
            if isinstance(locator, tuple):
                return self._driver.find_element(*locator)
            else:
                return self._driver.find_element(locator, value)
            # 成功，清空异常计数
            self._error_count = 0

            # element = self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(locator, value)
        except Exception as e:
            # 次数太多直接报错
            if self._error_count > self._error_max:
                raise e
            else:
                # 记录异常次数
                self._error_count += 1
            for element in self._black_list:
                # logging.info(element)
                elements = self.find(element)
                if len(elements) > 0:
                    elements[0].click()
                    return self.find(locator, value)

    def get_toast(self):
        return self.find(By.Xpath, "//*[@class='android.widget.Toast]").text

    def text(self, key):
        return By.XPATH, "//*[@text='%s']" % key

    def find_by_text(self, key):
        return self.find(self.text(key))

    def steps(self, path):
        with open(path) as f:
            steps: list[dict] = yaml.safe_load(f)
            element: WebElement = None
            for step in steps:
                logging.info(step)
                if "by" in step.keys():
                    element = self.find(step["by"], step["locator"])
                if "action" in step.keys():
                    action = step["action"]
                    if action == "find":
                        pass
                    elif action == "click":
                        element.click()
                    elif action == "text":
                        element.text
                    elif action == "attribute":
                        element.get_attribute(step["value"])
                    elif action in ["send", "input"]:
                        content: str = step["value"]
                        for key in self._params.keys():
                            content = content.replace("{%s}" % key, self._params[key])
                        element.send_keys(content)
