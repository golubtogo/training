from model.group import Group
from model.user import User


def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    db_list = db.get_group_list()

    # def clean(group):
    #     return Group(id=group.id, group_name=group.group_name.strip())
    # db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def test_user_list(app, db):
    ui_list = app.user.get_user_list()

    def clean(user):
        return User(id=user.id, lastname=user.lastname.strip(), firstname=user.firstname.strip())
    db_list = map(clean, db.get_user_list())
    assert sorted(ui_list, key=User.id_or_max) == sorted(db_list, key=User.id_or_max)


