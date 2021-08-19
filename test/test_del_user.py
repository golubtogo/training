# -*- coding: utf-8 -*-
from model.user import User


def test_delete_first_user(app):
    if app.user.count() == 0:
        app.user.create_user(User(firstname="test firstname"))
    app.user.delete_first_user()
