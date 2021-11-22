from model.user import User
import random
import time


def test_modify_some_user(app, db, check_ui):
    lastname_input = "zz22"
    firstname_input = "zz22"
    if app.user.count() == 0:
        app.user.create_user(User(lastname=lastname_input, firstname=firstname_input))
    new_user_data = User(lastname=lastname_input, firstname=firstname_input)
    old_users = db.get_user_list()
    user = random.choice(old_users)
    app.user.modify_user_by_id(user.id, new_user_data)
    time.sleep(1)
    new_users = db.get_user_list()
    assert len(old_users) == len(new_users)
    for new_user in old_users:
        if new_user.id == user.id:
            new_user.firstname = firstname_input
            new_user.lastname = lastname_input
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)

    def clean(user):
        return User(id=user.id, lastname=user.lastname.strip(), firstname=user.firstname.strip())
    new_users_list = map(clean, db.get_user_list())
    if check_ui:
        assert sorted(new_users_list, key=User.id_or_max) == sorted(app.user.get_user_list(), key=User.id_or_max)

