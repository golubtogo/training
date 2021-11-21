import time
from model.group import Group
import random


def test_modify_group_name(app, db, check_ui):
    group_name_input = "345"
    if app.group.count() == 0:
        app.group.create_group(Group(group_name=group_name_input))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_group_data = Group(group_name=group_name_input)
    app.group.modify_group_by_id(group.id, new_group_data)
    time.sleep(1)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    for new_group in new_groups:
        if new_group.id == group.id:
            assert new_group.group_name == group_name_input
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

