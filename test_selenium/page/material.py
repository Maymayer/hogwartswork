from time import sleep

from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage


class Material(BasePage):
    def image_upload(self, path):
        self.find((By.LINK_TEXT, "图片")).click()
        self.find((By.LINK_TEXT, "添加图片")).click()
        self.find((By.ID, "js_upload_input")).send_keys(path)
        sleep(5)
        self.find((By.LINK_TEXT, "完成")).click()
        return self
