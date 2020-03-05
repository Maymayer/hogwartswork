from test_appium.page.app import App
from test_appium.page.base_page import BasePage


class TestSteps:
    def test_steps(self):
        base = BasePage()
        base.steps("E:\\pythonwork\\hogwartswork\\test_appium\\page\\steps.yaml")

    def test_search(self):
        App().start().main().goto_search_page().search("jd")
