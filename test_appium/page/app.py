from datetime import datetime

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.page.base_page import BasePage
from test_appium.page.main import Main


class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = ".view.WelcomeActivityAlias"

    def start(self):
        if self._driver is None:
            caps = {"platformName": "android",
                    "deviceName": "hogwarts",
                    "appPackage": self._package,
                    "appActivity": self._activity,
                    "noReset": True,
                    # "dontStopAppOnReset": True,
                    # "unicodeKeyboard": True,
                    # "resetKeyboard": True
                    # "skipServerInstallation": True,
                    # "chromedriverExecutableDir": "/Users/seveniruby/projects/chromedriver/all",
                    # "chromedriverExecutable": "/Users/seveniruby/projects/chromedriver/all/chromedriver_2.20"
                    # "avd" = "webviewtest"
                    }

            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self._driver.implicitly_wait(10)
        else:
            print(self.driver)
            # todo: kill app start app
            self._driver.start_activity(self._package, self._activity)

        # WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located())

        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self) -> Main:
        # todo:wait into main
        """
        def wait_load(driver):
            print(datetime.datetime.now())
            source = self._driver.page_source
            if "我的" in source:
                return True
            if "同意" in source:
                return True
            return False
        WebDriverWait(self._driver, 30).until(wait_load)
        """
        return Main(self._driver)
