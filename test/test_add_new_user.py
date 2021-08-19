# -*- coding: utf-8 -*-

from model.user import User
import os


def test_add_new_user(app):
    app.user.create_user(User(firstname="firstname", middlename="middlename", lastname="lastname", nickname="nickname",
                              photo=os.getcwd() + "\\images\\test_image.png", title="title",
                              company="company", address="address\n+380111111111",
                              home="home", mobile="mobile", work="work", fax="fax",
                              email="e-mail", email2="e-mail2", email3="e-mail3", homepage="homepage",
                              byear="2000", bmonth="January", bday="1", ayear="2015", amonth="February", aday="1",
                              address2="secondary address", phone2="secondary home", notes="hello", new_group=""))
