# -*- coding: utf-8 -*-

from model.group import Group


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.update_group(Group(group_name="new_name"))
    app.session.logout()
