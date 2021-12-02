import time
from model.group import Group
import random
import allure


def test_modify_group_name(app, db, check_ui):
    group_name_input = "2233"
    with allure.step('Given a group list'):
        if app.group.count() == 0:
            app.group.create_group(Group(group_name=group_name_input))
    with allure.step('Given a non-empty group list'):
        old_groups = db.get_group_list()
    with allure.step('Given a random group from the list'):
        group = random.choice(old_groups)
    with allure.step('When I modify the group name with id=%s in the list' % group.id):
        new_group_data = Group(group_name=group_name_input)
        app.group.modify_group_by_id(group.id, new_group_data)
        time.sleep(1)
    with allure.step('Then the new groups list is equal to the old list with the modified group'):
        new_groups = db.get_group_list()
        assert len(old_groups) == len(new_groups)
        app.group.compare_groups(old_groups, group, group_name_input)
        assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)
        if check_ui:
            with allure.step('Also check UI'):
                assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
