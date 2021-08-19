# -*- coding: utf-8 -*-

from model.user import User


def test_modify_first_user(app):
    app.user.modify_first_user(User(
              lastname="new lastname", firstname="new firstname",
              address="new address", home="new home", mobile="new mobile",
              work="new work", phone2="secondary phone",
              email="new_email", email2="new_email_2", email3="new_email_3"))
