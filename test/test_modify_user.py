# -*- coding: utf-8 -*-

from model.user import User
from random import randrange


def test_modify_some_user(app):
    if app.user.count() == 0:
        app.user.create_user(User(lastname="test lastname mod", firstname="test firstname mod"))
    old_users = app.user.get_user_list()
    index = randrange(len(old_users))
    user = User(lastname="new lastname", firstname="new firstname")
    user.id = old_users[index].id
    app.user.modify_user_by_index(index, user)
    new_users = app.user.get_user_list()
    assert len(old_users) == app.user.count()
    old_users[index] = user
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)


# def test_modify_first_user_mobile(app):
#     if app.user.count() == 0:
#         app.user.create_user(User())
#         user = User(mobile="mobile modified")
#         app.user.modify_first_user(user)
