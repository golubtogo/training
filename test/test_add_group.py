# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create_group(Group(group_name="group name", group_header="1", group_footer="2"))




# def test_add_empty_group(app):
    # app.group.update_group(Group(group_name="", group_header="", group_footer=""))




