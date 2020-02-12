from test_selenium.page.main_page import Main


class TestMain:
    def setup(self):
        self.main = Main(reuse=True)

    def test_add_member(self):
        self.main.add_member().add_member("xxx")
        self.main.import_users().get_message()
        assert "aaa" in self.main.import_users().get_message()

    def test_import_user(self):
        self.main.import_users("test_selenium/abu1.jpg")
        assert "success" in self.main.get_message()

    def test_send_message(self):
        message = self.main.send_message()
        message.send(app="", content="content", group="")
        assert "content" in message.get_message()
