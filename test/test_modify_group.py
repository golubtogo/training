import time
from model.group import Group
import random


def test_modify_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create_group(Group(group_name="test modify"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    # group = Group(group_name="modify GROUP")
    app.group.modify_group_by_id(group.id, Group(group_name="modify GROUP"))
    new_groups = db.get_group_list()
    assert len(old_groups) == app.group.count()
    # if check_ui:
    #     assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


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
