import re
import allure


def test_phones_on_home_page(app):
    with allure.step('Given a user info from home page'):
        user_from_home_page = app.user.get_user_list()[0]
    with allure.step('Given a user info from edit page'):
        user_from_edit_page = app.user.get_user_info_from_edit_page(0)
    with allure.step('Then the user phones from home page is equal to user phones from edit page'):
        assert user_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(user_from_edit_page)


def test_all_data_on_home_page(app):
    with allure.step('Given a user info from home page'):
        user_from_home_page = app.user.get_user_list()[0]
    with allure.step('Given a user info from edit page'):
        user_from_edit_page = app.user.get_user_info_from_edit_page(0)
    with allure.step('Then the user info from home page is equal to user info from edit page'):
        assert user_from_home_page.id == user_from_edit_page.id
        assert user_from_home_page.lastname == user_from_edit_page.lastname
        assert user_from_home_page.firstname == user_from_edit_page.firstname
        assert user_from_home_page.address == user_from_edit_page.address
        assert user_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(user_from_edit_page)
        assert user_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(user_from_edit_page)


def test_all_data_all_users_on_home_page(app, db):
    with allure.step('Given a user list from home page'):
        users_from_home_page = app.user.get_user_list()
    with allure.step('Given a user list from db'):
        users_from_db = db.get_all_user_list()
    with allure.step('Then for all users the user info from home page is equal to user info from edit page'):
        assert len(users_from_db) == len(users_from_home_page)
        list_id = {}
        for user in users_from_home_page:
            list_id.setdefault(user.id, user)
        for user_from_db in users_from_db:
            user_from_home_page = list_id[user_from_db.id]
            assert user_from_home_page.firstname == user_from_db.firstname
            assert user_from_home_page.lastname == user_from_db.lastname
            assert user_from_home_page.address == merge_address_like_on_home_page(user_from_db)
            assert user_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(user_from_db)
            assert user_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(user_from_db)


def merge_address_like_on_home_page(user):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_address(x),
                                filter(lambda x: x is not None,
                                [user.address]))))


def merge_emails_like_on_home_page(user):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_email(x),
                                filter(lambda x: x is not None,
                                [user.email, user.email2, user.email3]))))


def merge_phones_like_on_home_page(user):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                [user.home, user.mobile, user.work, user.phone2]))))


def clear(s):
    return re.sub("[() -]", "", s)


def clear_email(s):
    return re.sub("[ ]", "", s)


def clear_address(s):
    return re.sub("[\r]", "", s)



# def test_phones_on_user_view_page(app):
#     user_from_view_page = app.user.get_user_from_view_page(0)
#     user_from_edit_page = app.user.get_user_info_from_edit_page(0)
#     assert user_from_view_page.merge_phones_like_on_view_page == merge_phones_like_on_home_page(user_from_edit_page)


# def merge_phones_like_on_view_page(user):
#     return "\n".join(filter(lambda x: x != "",
#                             map(lambda x: clear(x),
#                                 filter(lambda x: x is not None,
#                                 [user.home, user.mobile, user.work, user.phone2]))))

