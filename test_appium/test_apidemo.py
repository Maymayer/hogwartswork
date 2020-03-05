# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestXueqiu:
    def setup(self):
        caps = {"platformName": "android",
                "deviceName": "hogwarts",
                "appPackage": "io.appium.andriod.apis",
                "appActivity": ".ApiDemos",
                # "noReset": True,
                # "dontStopAppOnReset": True,
                # "unicodeKeyboard": True,
                # "resetKeyboard": True
                "skipServerInstallation": True
                }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(30)

        # WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located())

    def test_toase(self):
        scroll_to_element = (
            MobileBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable('
            'new UiSelector().scrollable(true).instance(0))'
            '.scrollIntoView('
            'new UiSelector().text("Views").instance(0));')
        self.driver.find_element(*scroll_to_element).click()

        scroll_to_element = (
            MobileBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable('
            'new UiSelector().scrollable(true).instance(0))'
            '.scrollIntoView('
            'new UiSelector().text("Popup Menu").instance(0));')
        self.driver.find_element(*scroll_to_element).click()
        # self.driver.find_element(By.XPATH, "//*[@text='MAKE A POPUP!']").click()
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Make a Popup!").click()
        self.driver.find_element(By.XPATH, "//*[@text='Search']").click()
        toast = self.driver.find_element(By.XPATH, "//*[@class='android.widget.Toast']").text
        assert "Search" in toast
        assert "Clicked" in toast

    def test_scroll(self):
        size = self.driver.get_window_size()
        for i in range(10):
            TouchAction(self.driver) \
                .long_press(x=size['width'] * 0.5, y=size['height'] * 0.8) \
                .move_to(x=size['width'] * 0.5, y=size['height'] * 0.2) \
                .release() \
                .perform()

    def test_device(self):
        self.driver.background_app(5)
        self.driver.lock(5)
        self.driver.unlock()

    def teardown(self):
        # sleep(20)
        pass
        # self.driver.quit()
