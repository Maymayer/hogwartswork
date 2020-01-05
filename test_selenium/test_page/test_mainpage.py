from test_selenium.page.main_page import Main


class TestMain:
    def test_add_member(self):
        main = Main()
        main.add_member().add_member("xxx")
        main.import_users().get_message()
        assert "aaa" in main.import_users().get_message()