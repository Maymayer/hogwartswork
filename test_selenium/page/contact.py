from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage


class Contact(BasePage):
    _add_member_button = (By.CSS_SELECTOR, "xx")
    _name_locator = (By.NAME, 'username')
    _acctid_locator = (By.NAME, 'acctid')
    _gender_locator = (By.CSS_SELECTOR, '.ww_radio[value="2"]')
    _mobile_locator = (By.NAME, 'mobile')

    def add_member(self, data):
        # self.driver.find_element("添加成员").click
        # sendkeys
        # click save
        # name_locator = (By.NAME, 'username')
        # acctid_locator = (By.NAME, 'acctid')
        # gender_locator = (By.CSS_SELECTOR, '.ww_radio[value="2"]')
        # mobile_locator = (By.NAME, 'mobile')
        self.find(self._name_locator).send_keys("aaaa")
        self.find(self._acctid_locator).send_keys("aaaa")
        self.find(self._gender_locator).click()
        self.find((By.CSS_SELECTOR, ".ww_telInput_zipCode_input")).click()
        self.find((By.CSS_SELECTOR, 'li[data-value="853"]')).click()
        self.find(self._mobile_locator).send_keys("15810005017")

    def add_member_error(self, data):
        pass
        # return AddMemberPage()

    def search(self, data):
        pass

    def import_users(self, data):
        pass

    def export_users(self, data):
        pass

    def set_department(self, data):
        pass

    def delete_users(self):
        pass

    def invite_users(self):
        pass

    def edit_users(self, data):
        self.find((By.CSS_SELECTOR,
                                 ".member_colRight_memberTable_tr_Inactive > "
                                 ".member_colRight_memberTable_td:nth-child(2)")).click()
        self.find((By.LINK_TEXT, "编辑")).click()
        self.find(self._name_locator).send_keys("aaaa")
        self.find(self._acctid_locator).send_keys("aaaa")
        self.find(self._gender_locator).click()
        self.find((By.CSS_SELECTOR, ".ww_telInput_zipCode_input")).click()
        self.find((By.CSS_SELECTOR, 'li[data-value="853"]')).click()
        self.find(self._mobile_locator).send_keys("15810005017")
        self.find((By.CSS_SELECTOR, ".member_colRight_operationBar:nth-child(3) > .ww_btn_Blue")).click()

