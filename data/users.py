from model.user import User
import os.path

testdata = [
    User(firstname="firstname", middlename="middlename", lastname="lastname", nickname="nickname",
         photo=os.path.abspath("C:\\Users\\Nata\\PycharmProjects\\training\\images\\test_image.png"),
         title="title", company="company", address="address",
         home="home", mobile="mobile", work="work", fax="fax",
         email="email", email2="email2", email3="email3", homepage="homepage",
         byear="", bmonth="", bday="", ayear="", amonth="", aday="",
         address2="address2", phone2="phone2", notes="notes", new_group="")
]
