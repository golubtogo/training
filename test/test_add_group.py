# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.update_group(Group(group_name="group name", group_header="1", group_footer="2"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.update_group(Group(group_name="", group_header="", group_footer=""))
    app.session.logout()



