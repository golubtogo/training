# -*- coding: utf-8 -*-

from model.group import GroupModify


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(GroupModify(modified_name="modified_name"))
    app.session.logout()
