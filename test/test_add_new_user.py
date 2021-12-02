import time
import allure
from model.user import User


def test_add_new_user(app, db, json_users, check_ui):
    user = json_users
    with allure.step('Given a user list'):
        old_users = db.get_user_list()
    with allure.step('When I add the user %s to the list' % user):
        user_id = app.user.create_user(user)
        user.id = user_id
        time.sleep(1)
    with allure.step('Then the new user list is equal to the old list with the added user'):
        new_users = db.get_user_list()
        old_users.append(user)
        assert old_users == new_users
    if check_ui:
        with allure.step('If I check UI'):
            assert sorted(new_users, key=User.id_or_max) == sorted(app.user.get_user_list(), key=User.id_or_max)


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
