# -*- coding: utf-8 -*-
# 1.13th lesson - code refactoring, FF
import pytest
#from data.add_group import testdata
#from data.groups import constant as testdata
from model.group import Group


# def test_add_group(app, data_groups):
def test_add_group(app, json_groups):
    #group = data_groups
    group = json_groups
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups)+1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
#def test_add_group(app, group):
#    old_groups = app.group.get_group_list()
#    app.group.create(group)
#    assert len(old_groups)+1 == app.group.count()
#    new_groups = app.group.get_group_list()
#    old_groups.append(group)
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)







