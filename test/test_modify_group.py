# -*- coding: utf-8 -*-

from model.group import Group
from random import randrange


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create_group(Group(group_name="test modify"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(group_name="modify name 5555")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == app.group.count()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_clean_group_name(app):
#     old_groups = app.group.get_group_list()
#     if app.group.count() == 0:
#         app.group.create_group(Group(group_name="test name"))
#     app.group.modify_first_group(Group(group_name=""))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#
#
# def test_modify_group_header(app):
#     old_groups = app.group.get_group_list()
#     if app.group.count() == 0:
#         app.group.create_group(Group(group_header=""))
#     app.group.modify_first_group(Group(group_header="modify header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#
#
# def test_clean_group_header(app):
#     old_groups = app.group.get_group_list()
#     if app.group.count() == 0:
#         app.group.create_group(Group(group_header="modify header"))
#     app.group.modify_first_group(Group(group_header=""))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
