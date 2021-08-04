# -*- coding: utf-8 -*-

import pytest
from user import User
from application import Application
import os


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_user(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.add_user(User(firstname="firstname", middlename="middlename", lastname="lastname", nickname="nickname",
                      photo=os.getcwd() + "\\images\\test_image.png", title="title",
                      company="company", address="address\n+380111111111",
                      home="home", mobile="mobile", work="work", fax="fax",
                      email="e-mail", email_2="e-mail2", email_3="e-mail3", homepage="homepage",
                      byear="2000", bmonth="January", bday="1", ayear="2015", amonth="February", aday="1",
                      secondary_address="secondary address", secondary_phone="secondary home", notes="hello"
                      ))
    app.choose_group()
    app.submit()
    app.logout()
