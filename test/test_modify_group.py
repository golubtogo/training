# -*- coding: utf-8 -*-

from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create_group(Group(group_name=""))
    app.group.modify_first_group(Group(group_name="modify name"))


def test_clean_group_name(app):
    if app.group.count() == 0:
        app.group.create_group(Group(group_name="test name"))
    app.group.modify_first_group(Group(group_name=""))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create_group(Group(group_header=""))
    app.group.modify_first_group(Group(group_header="modify header"))


def test_clean_group_header(app):
    if app.group.count() == 0:
        app.group.create_group(Group(group_header="modify header"))
    app.group.modify_first_group(Group(group_header=""))
