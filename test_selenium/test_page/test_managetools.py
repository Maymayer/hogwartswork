from test_selenium.page.managetools import ManageTools


class TestManageTools:
    def setup(self):
        self.managetools = ManageTools(reuse=True)

    def test_material_image_upload(self):
        self.managetools.material_manage().image_upload("E:\\pythonwork\\hogwartswork\\test_selenium\\abu1.jpg")
        # assert "success" in self.managetools.get_result()
