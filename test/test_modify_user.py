# -*- coding: utf-8 -*-

from model.user import User


def test_modify_first_user(app):
    old_users = app.user.get_user_list()
    if app.user.count() == 0:
        app.user.create_user(User())
    user = User(lastname="new lastname", firstname="new firstname",
                address="new address", home="new home", mobile="new mobile",
                work="new work", phone2="secondary phone",
                email="new_email", email2="new_email_2", email3="new_email_3")
    user.id = old_users[0].id
    app.user.modify_first_user(user)
    assert len(old_users) == app.user.count()
    new_users = app.user.get_user_list()
    old_users[0] = user
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)


# def test_modify_first_user_mobile(app):
#     if app.user.count() == 0:
#         app.user.create_user(User())
#         user = User(mobile="mobile modified")
#         app.user.modify_first_user(user)
