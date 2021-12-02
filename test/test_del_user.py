import time
import allure
import random
from model.user import User


def test_delete_some_user(app, db, check_ui):
    with allure.step('Given a user list'):
        if len(db.get_user_list()) == 0:
            app.user.create_user(User(firstname="firstname test delete", lastname="lastname test delete"))
    with allure.step('Given a non-empty group list'):
        old_users = db.get_user_list()
        user = random.choice(old_users)
    with allure.step('When I delete the user %s from the list' % user):
        app.user.delete_user_by_id(user.id)
        time.sleep(1)
    with allure.step('Then the new user list is equal to the old list without the deleted user'):
        new_users = db.get_user_list()
        assert len(old_users) - 1 == len(new_users)
        old_users.remove(user)
        assert old_users == new_users
    if check_ui:
        with allure.step('If I check UI'):
            assert sorted(new_users) == sorted(app.user.get_user_list(), key=User.id_or_max)
