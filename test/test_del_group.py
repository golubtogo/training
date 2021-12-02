# -*- coding: utf-8 -*-
import random
import allure
from model.group import Group


def test_delete_some_group(app, db, check_ui):
    with allure.step('Given a group list'):
        if len(db.get_group_list()) == 0:
            app.group.create_group(Group(group_name="test delete"))
    with allure.step('Given a non-empty group list'):
        old_groups = db.get_group_list()
        group = random.choice(old_groups)
    with allure.step('When I delete the group %s from the list' % group):
        app.group.delete_group_by_id(group.id)
    with allure.step('Then the new group list is equal to the old list without the deleted group'):
        new_groups = db.get_group_list()
        assert len(old_groups) - 1 == len(new_groups)
        old_groups.remove(group)
        assert old_groups == new_groups
        if check_ui:
            with allure.step('Also check UI'):
                assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
