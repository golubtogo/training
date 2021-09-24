import os
import pytest
import random
import string
from model.user import User


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5  # some tests doesn't passes with string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_year(maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return [random.choice(symbols) for i in range(random.randrange(maxlen))]


def random_day():
    day = random.choice(range(1, 31))
    return str(day)


def random_month():
    months_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                   "November", "December"]
    month = random.choice(months_list)
    return month


def remove_whitespaces(user):
    user.lastname = user.lastname.strip()
    user.firstname = user.firstname.strip()
    user.home = user.home.strip()
    user.mobile = user.mobile.strip()
    user.work = user.work.strip()
    user.phone2 = user.phone2.strip()
    user.email = user.email.strip()
    user.email2 = user.email2.strip()
    user.email3 = user.email3.strip()
    user.address = user.address.strip()

    # for name in user.attributes:
    #     setattr(user, name,  getattr(user, name).strip())
    # return user


test_user_data = [User(firstname="", middlename="", lastname="", nickname="",
                       photo="", title="",
                       company="", address="",
                       home="", mobile="", work="", fax="",
                       email="", email2="", email3="", homepage="",
                       byear="", bmonth="", bday="", ayear="", amonth="", aday="",
                       address2="", phone2="", notes="", new_group="")] + [
                     User(firstname=random_string(" firstname", 5), middlename=random_string("middlename", 5),
                          lastname=random_string("lastname", 5), nickname=random_string("nickname", 5),
                          photo=os.getcwd() + "\\images\\test_image.png", title=random_string("title", 10),
                          company=random_string("company", 5), address=random_string("address\n+380111111111", 10),
                          home=random_string("+123456", 5), mobile=random_string("+1234567", 5),
                          work=random_string("+12345678", 5),
                          fax=random_string("fax", 5), email=random_string("email-1+@gmail.com", 10),
                          email2=random_string("email-2+@gmail.com", 10),
                          email3=random_string("email-3+@gmail.com", 10),
                          homepage=random_string("homepage", 5),
                          byear=random_year(4), bmonth=random_month(), bday=random_day(),
                          ayear=random_year(4), amonth=random_month(), aday=random_day(),
                          address2=random_string("secondary address", 10), phone2=random_string("+123456789", 5),
                          notes=random_string("hello", 10), new_group="")
                     for i in range(1)
                 ]


@pytest.mark.parametrize("user", test_user_data, ids=[repr(x) for x in test_user_data])
def test_add_new_user(app, user):
    old_users = app.user.get_user_list()
    user_id = app.user.create_user(user)
    assert len(old_users) + 1 == app.user.count()
    user.id = user_id
    remove_whitespaces(user)
    new_users = app.user.get_user_list()
    old_users.append(user)
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)
