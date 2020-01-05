from selenium.webdriver.common.by import By


class Contract:
    # add_memeber_button = (By.CSS, "xx")
    def add_member(self, data):
        # self.driver.find_element("添加成员").click
        # sendkeys
        # click save
        return self

    def add_member_error(self, data):
        return AddMemberPage()

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