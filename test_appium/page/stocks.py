from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.base_page import BasePage


class Stocks(BasePage):
    _name_locator = (MobileBy.ID, "name")

    def search(self, key: str):
        # todo:
        self.find(MobileBy.ID, "action_search").click()
        self.find(MobileBy.ID, "search_input_text").send_keys(key)
        # element = (MobileBy.ID, "name")
        self.find(self._name_locator).click()
        return self

    def add_select_return(self):
        element = self.find_by_text("加自选")
        element.click()
        self.find(MobileBy.ID, "action_close").click()
        return self

    def get_stocks(self):
        return self.find(MobileBy.ID, "portfolio_stockName").text
