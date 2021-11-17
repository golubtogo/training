from model.user import User
import random


def test_modify_some_user(app, db, check_ui):
    if app.user.count() == 0:
        app.user.create_user(User(lastname="test lastname mod", firstname="test firstname mod"))
    old_users = db.get_user_list()
    user = random.choice(old_users)
    user = User(lastname="MODIFIED lastname", firstname="MODIFIED firstname")
    app.user.modify_user_by_id(user.id, user)
    new_users = db.get_user_list()
    assert len(old_users) == app.user.count()
    # if check_ui:
    #     # old_users[id] = user
    #     assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)


# def test_modify_first_user_mobile(app):
#     if app.user.count() == 0:
#         app.user.create_user(User())
#         user = User(mobile="mobile modified")
#         app.user.modify_first_user(user)
