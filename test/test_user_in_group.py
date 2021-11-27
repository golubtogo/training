from fixture.group import Group
from fixture.user import User
import random
import time


def test_add_user_in_group(app, db):
    group_name_input = "group1"
    lastname_input = "lastname1"
    firstname_input = "firstname1"
    users_from_db = db.get_user_list()
    groups_from_db = db.get_group_list()
    if len(groups_from_db) == 0:
        app.group.create_group(Group(group_name=group_name_input))
    if len(users_from_db) == 0:
        app.user.create_user_in_group(User(lastname=lastname_input, firstname=firstname_input, new_group=group_name_input))
    users_from_db = db.get_user_list()
    groups_from_db = db.get_group_list()
    old_address_in_groups = db.get_address_in_groups_list()
    user = random.choice(users_from_db)
    app.user.add_user_to_group_by_id(user.id)
    app.user.open_link_selected_group()
    group_id = app.user.get_group_id(id)
    new_address = f"{group_id}:{user.id}"
    if len(old_address_in_groups) == 0:
        old_address_in_groups.append(new_address)
    for new_address in old_address_in_groups:
        if new_address not in old_address_in_groups:
            old_address_in_groups.append(new_address)
    time.sleep(1)
    new_address_in_groups = db.get_address_in_groups_list()
    assert sorted(old_address_in_groups) == sorted(new_address_in_groups)


def test_delete_user_in_group(app, db):
    group_name_input = "group1"
    lastname_input = "lastname1"
    firstname_input = "firstname1"
    users_from_db = db.get_user_list()
    groups_from_db = db.get_group_list()
    if len(groups_from_db) == 0:
        app.group.create_group(Group(group_name=group_name_input))
    if len(users_from_db) == 0:
        app.user.create_user_in_group(User(lastname=lastname_input, firstname=firstname_input, new_group=group_name_input))
    app.user.select_group()
    old_users_in_groups = app.user.get_user_list()
    if len(old_users_in_groups) == 0:
        users_from_db = db.get_user_list()
        user = random.choice(users_from_db)
        app.user.add_user_to_group_by_id(user.id)
        app.user.open_link_selected_group()
    old_address_in_groups = db.get_address_in_groups_list()
    time.sleep(1)
    new_users_in_groups = app.user.get_user_list()
    user = random.choice(new_users_in_groups)
    group_id = app.user.get_group_id(id)
    app.user.delete_user_from_group_by_id(user.id)
    new_address = f"{group_id}:{user.id}"
    if len(old_address_in_groups) > 0:
        for el in old_address_in_groups:
            if el == new_address:
                old_address_in_groups.remove(el)
    new_address_in_groups = db.get_address_in_groups_list()
    assert sorted(old_address_in_groups) == sorted(new_address_in_groups)


