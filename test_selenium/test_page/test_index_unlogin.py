from selenium import webdriver
from selenium.webdriver.common.by import By

from test_selenium.page.index_unlogin import IndexUnLogin


class TestIndexUnlogin:
    def setup(self):
        self.index = IndexUnLogin()

    def test_register(self):
        self.index.goto_register().register("aaaabbbb")

    def test_login(self):
        register_page = self.index.goto_login().goto_registry().register("测吧")
        print(register_page.get_error_message)
        assert "请选择" in "|".join(register_page.get_error_message())

    def teardown(self):
        self.index.close()
