# -*- coding: utf-8 -*-
# 1.13th lesson - code refactoring, FF
import pytest
from model.group import Group

testdata = [
    Group(name="second", header="second1", footer="second2"),
    Group(name="", header="", footer="")
]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    group = Group(name="second", header="second1", footer="second2")
    app.group.create(group)
    assert len(old_groups)+1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)






