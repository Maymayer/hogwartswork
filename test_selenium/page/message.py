from time import sleep

from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage


class Message(BasePage):
    def send(self, app="", content="", group=""):
        self.find((By.LINK_TEXT, '选择需要发消息的应用')).click()
        self.find((By.CSS_SELECTOR, 'div[data-name="%s"]' % group)).click()
        self.find((By.LINK_TEXT, '确定')).click()

        self.find((By.LINK_TEXT, '选择发送范围')).click()
        sleep(3)
        self.find((By.CSS_SELECTOR, ".ww_searchInput_text")).send_keys(group)
        self.find((By.CSS_SELECTOR, '#searchResult li')).click()
        self.find((By.LINK_TEXT, '确定')).click()

        self.find((By.CSS_SELECTOR, "")).send_keys(content)
        self.find((By.LINK_TEXT, '发送')).click()

    def get_history(self):
        pass
