from fixture.group import Group
from fixture.user import User
import random


def test_delete_user_from_group(app, orm):
    group_name = "group1"
    if len(orm.get_group_list()) == 0:
        app.group.create_group(Group(group_name=group_name))
    group_list = orm.get_group_list()
    group = random.choice(group_list)
    group_name = group.group_name
    gr = len(orm.get_users_in_group(group))
    if len(orm.get_users_in_group(group)) == 0:
        if len(orm.get_user_list()) == 0:
            app.user.create_user(User(lastname="lastname1", firstname="firstname1"))
        users_list = orm.get_user_list()
        user = random.choice(users_list)
        app.user.add_user_to_group_by_id(user.id, group.group_name)
    users_list = orm.get_users_in_group(group)
    user = random.choice(users_list)
    app.user.delete_user_from_group_by_id(user.id, group.group_name)
    user_in_group = orm.get_users_in_group(sorted(orm.get_group_list_by_name(
        Group(group_name=group_name)), key=Group.id_or_max)[0])
    assert user not in user_in_group





