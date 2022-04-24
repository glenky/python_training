# -*- coding: utf-8 -*-
# 1.13th lesson - code refactoring, FF
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

from application import Application
from group import Group


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Application()
    
    def test_add_group(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="second", header="second1", footer="second2"))
        self.app.logout()

    def test_add_empty_group(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="", header="", footer=""))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()

if __name__ == "__main__":
    unittest.main()
