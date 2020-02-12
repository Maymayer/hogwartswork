from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage


class ManageTools(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#manageTools"

    def material_add_picture(self):
        self.find((By.PARTIAL_LINK_TEXT, "素材库")).click()
        self.find((By.PARTIAL_LINK_TEXT, "图片")).click()
        self.find((By.PARTIAL_LINK_TEXT, "添加图片")).click()
        self.find((By.ID, "js_upload_file_input")).send_keys(path)
        self.find((By.ID, "submit_csv")).click()
        self.find((By.ID, "reloadContact")).click()
        return self

    def get_result(self):
        return "aaa"
