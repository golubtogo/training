# -*- coding: utf-8 -*-
from model.user import User
import random


def test_delete_some_user(app, db, check_ui):
    if len(db.get_user_list()) == 0:
        app.user.create_user(User(firstname="firstname test delete", lastname="lastname test delete"))
    old_users = db.get_user_list()
    user = random.choice(old_users)
    app.user.delete_user_by_id(user.id)
    new_users = db.get_user_list()
    assert len(old_users) - 1 == len(new_users)
    old_users.remove(user)
    assert old_users == new_users
    # if check_ui:
    #     assert new_users == app.user.get_user_list()


