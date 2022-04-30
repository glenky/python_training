from model.group import Group


def test_modify_first_group(app):
    app.group.modify_first_group(Group(name="modified_name111", header="modified_header111", footer="modified_footer111"))


def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="6666"))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="8888"))




