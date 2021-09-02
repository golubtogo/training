# -*- coding: utf-8 -*-
from model.user import User


def test_delete_first_user(app):
    if app.user.count() == 0:
        app.user.create_user(User(firstname="test firstname"))
    old_users = app.user.get_user_list()
    app.user.delete_first_user()
    assert len(old_users) - 1 == app.user.count()
    new_users = app.user.get_user_list()
    old_users[0:1] = []
    assert old_users == new_users

