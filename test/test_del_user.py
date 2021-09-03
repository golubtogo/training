# -*- coding: utf-8 -*-
from model.user import User
from random import randrange


def test_delete_some_user(app):
    if app.user.count() == 0:
        app.user.create_user(User(firstname="firstname test delete", lastname="lastname test delete"))
    old_users = app.user.get_user_list()
    index = randrange(len(old_users))
    app.user.delete_user_by_index(index)
    new_users = app.user.get_user_list()
    assert len(old_users) - 1 == app.user.count()
    old_users[index:index+1] = []
    assert old_users == new_users

