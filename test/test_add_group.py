# -*- coding: utf-8 -*-

import pytest
from fixture.application import ApplicationGroup
from model.group import Group


@pytest.fixture
def app(request):
    fixture = ApplicationGroup()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    app.group.create(Group(name="group name", header="1", footer="2"))
    app.group.return_to_groups_page()
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    app.group.create(Group(name="", header="", footer=""))
    app.group.return_to_groups_page()
    app.session.logout()



