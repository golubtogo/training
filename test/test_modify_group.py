import time
from model.group import Group
import random


def test_modify_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create_group(Group(group_name="test modify"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_group_data = Group(group_name="modify GROUP 1")
    app.group.modify_group_by_id(group.id, new_group_data)
    time.sleep(2)
    new_groups = db.get_group_list()
    group.group_header = None
    group.group_footer = None
    assert len(old_groups) == len(new_groups)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

