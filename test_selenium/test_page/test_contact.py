from test_selenium.page.contact import Contact


class TestContact:
    def test_add_member(self):
        contact = Contact()
        contact.add_member("xxx")

    def test_edit_member(self):
        contact = Contact()
        contact.edit_users("xxx")
