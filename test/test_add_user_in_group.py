from fixture.group import Group
from fixture.user import User
import random


def test_add_user_in_group(app, orm):
    if len(orm.get_user_list()) == 0:
        app.user.create_user(User(lastname="lastname1", firstname="firstname1"))
    users_list = orm.get_user_list()
    user = random.choice(users_list)
    if len(orm.get_groups_without_user(User(id=user.id))) == 0:
        app.group.create_group(Group(group_name="group1"))
    groups = orm.get_groups_without_user(User(id=user.id))
    group = random.choice(groups)
    app.user.add_user_to_group_by_id(user.id, group.group_name)
    user_in_group = orm.get_users_in_group(sorted(orm.get_group_list_by_name(
        Group(group_name=group.group_name)), key=Group.id_or_max)[0])
    assert user in user_in_group
