from model.user import User
import random
import time
import allure


def test_modify_some_user(app, db, check_ui):
    lastname_input = "zz22"
    firstname_input = "zz22"
    with allure.step('Given a user list'):
        if app.user.count() == 0:
            app.user.create_user(User(lastname=lastname_input, firstname=firstname_input))
        new_user_data = User(lastname=lastname_input, firstname=firstname_input)
    with allure.step('Given a non-empty user list'):
        old_users = db.get_user_list()
        user = random.choice(old_users)
    with allure.step('When I modify the user with id=%s in the list' % user.id):
        app.user.modify_user_by_id(user.id, new_user_data)
        time.sleep(1)
    with allure.step('Then the new user list is equal to the old list with the modified user'):
        new_users = db.get_user_list()
        assert len(old_users) == len(new_users)
        app.user.compare_users(old_users, user, firstname_input, lastname_input)
        assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)

        def clean(user):
            return User(id=user.id, lastname=user.lastname.strip(), firstname=user.firstname.strip())
        new_users_list = map(clean, db.get_user_list())
        if check_ui:
            with allure.step('Also check UI'):
                assert sorted(new_users_list, key=User.id_or_max) == sorted(app.user.get_user_list(), key=User.id_or_max)

