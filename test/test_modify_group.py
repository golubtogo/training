# -*- coding: utf-8 -*-

from model.group import Group


def test_modify_group_name(app):
    app.group.modify_first_group(Group(group_name="new group name"))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(group_header="new header"))

