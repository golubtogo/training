
from model.user import User


def test_add_new_user(app, json_users):
    user = json_users
    old_users = app.user.get_user_list()
    user_id = app.user.create_user(user)
    assert len(old_users) + 1 == app.user.count()
    user.id = user_id
    new_users = app.user.get_user_list()
    old_users.append(user)
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)


# @pytest.mark.parametrize("user", test_user_data, ids=[repr(x) for x in test_user_data])
# def test_add_new_user(app, user):
#     old_users = app.user.get_user_list()
#     user_id = app.user.create_user(user)
#     assert len(old_users) + 1 == app.user.count()
#     user.id = user_id
#     remove_whitespaces(user)
#     new_users = app.user.get_user_list()
#     old_users.append(user)
#     assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)
