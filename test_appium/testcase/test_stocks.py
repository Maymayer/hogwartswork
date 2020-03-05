from test_appium.page.app import App


class TestStocks:
    def setup(self):
        self.main = App().start().main()

    def test_stocks(self):
        assert "京东" in self.main.goto_stocks().search("jd").add_select_return().get_stocks()
