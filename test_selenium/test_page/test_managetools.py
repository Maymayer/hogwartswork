from test_selenium.page.managetools import ManageTools


class TestManageTools:
    def setup(self):
        self.managetools = ManageTools(reuse=True)

    def test_material_add_picture(self):
        self.managetools.material_add_pictrue("test_selenium/abu1.jpg")
        assert "success" in self.managetools.get_result()
