# -*- coding: utf-8 -*-

from model.user import User
import os


def test_add_new_user(app):
    old_users = app.user.get_user_list()
    user = User(firstname="firstname", middlename="middlename", lastname="lastname", nickname="nickname",
                photo=os.getcwd() + "\\images\\test_image.png", title="title",
                company="company", address="address\n+380111111111",
                home="+123456", mobile="+1234567", work="+12345678", fax="fax",
                email="email-1+@gmail.com", email2="email-2+@gmail.com", email3="email-3+@gmail.com", homepage="homepage",
                byear="2000", bmonth="January", bday="1", ayear="2015", amonth="February", aday="1",
                address2="secondary address", phone2="+123456789", notes="hello", new_group="")
    app.user.create_user(user)
    assert len(old_users) + 1 == app.user.count()
    new_users = app.user.get_user_list()
    old_users.append(user)
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)

