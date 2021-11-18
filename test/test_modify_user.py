from model.user import User
import random
import time


def test_modify_some_user(app, db, check_ui):
    if app.user.count() == 0:
        app.user.create_user(User(lastname="test lastname mod", firstname="test firstname mod"))
    new_user_data = User(lastname="MODIFIED 2", firstname="MODIFIED 2")
    old_users = db.get_user_list()
    user = random.choice(old_users)
    app.user.modify_user_by_id(user.id, new_user_data)
    time.sleep(5)
    new_users = db.get_user_list()
    assert len(old_users) == len(new_users)

    def clean(user):
        return User(id=user.id, lastname=user.lastname.strip(), firstname=user.firstname.strip())
    new_users_list = map(clean, db.get_user_list())
    assert len(old_users) == len(new_users)
    if check_ui:
        assert sorted(new_users_list, key=User.id_or_max) == sorted(app.user.get_user_list(), key=User.id_or_max)

