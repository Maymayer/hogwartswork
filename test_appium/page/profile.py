from selenium.webdriver.common.by import By

from test_appium.page.base_page import BasePage


class Profile(BasePage):
    def login_by_password(self, phone, password):
        self.find(By.XPATH, "//*[@text='账号密码登录']").click()
        self.find(By.ID, "login_account").send_keys("15810005017")
        self.find(By.ID, "login_password").send_keys("123456")
        self.find(By.ID, "button_next").click()
        self.find(By.ID, "md_content").click()
        self.find(By.ID, "md_").click()