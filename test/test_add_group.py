# -*- coding: utf-8 -*-
# 1.13th lesson - code refactoring, FF
from model.group import Group

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="second", header="second1", footer="second2"))
    app.session.logout()

#def test_add_empty_group(app):
#    app.session.login(username="admin", password="secret")
#    app.group.create(Group(name="", header="", footer=""))
#    app.session.logout()


