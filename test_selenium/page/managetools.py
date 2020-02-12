from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage
from test_selenium.page.material import Material


class ManageTools(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#manageTools"

    def material_manage(self):
        self.find((By.CSS_SELECTOR, ".manageTools_cnt_item:nth-child(5) .manageTools_cnt_item_desc_text")).click()
        return Material(reuse=True)

    def get_result(self):
        return "aaa"
