# -*- coding: utf-8 -*-
from selenium import webdriver

from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from user import UserName
from user import UserContacts
from user import UserDates
from user import UserSecondaryContacts




class TestAddNewUser(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_new_user(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.add_new_user(wd)
        self.add_name(wd, UserName(firstname="firstname", middlename="middlename", lastname="lastname", nickname="nickname"))
        self.add_photo(wd, photo="C:\\Users\\Nata\\PycharmProjects\\test_image.png", title="title")
        self.add_contacts(wd, UserContacts(company="company", address="address\n+380111111111", home="home", mobile="mobile", work="work", fax="fax", email="e-mail", email_2="e-mail2", email_3="e-mail3", homepage="homepage" ))
        self.add_dates(wd, UserDates(byear="2000", bmonth="January", bday="1", ayear="2015", amonth="February", aday="1"))
        self.choose_group(wd)
        self.add_secondary_contacts(wd, UserSecondaryContacts(secondary_address="secondary address", secondary_phone="secondary home", notes="hello"))
        self.submit(wd)




    def submit(self, wd):
        wd.find_element_by_xpath("//input[21]").click()

    def add_secondary_contacts(self, wd, user):
        # add secondary address
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(user.secondary_address)
        # add secondary phone
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(user.secondary_phone)
        # add notes
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(user.notes)


    def choose_group(self, wd):
        wd.find_element_by_name("new_group").click()
        wd.find_element_by_xpath("//option[@value='[none]']").click()

    def add_dates(self, wd, user):
        # add Birthday year
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(user.byear)
        # add Birthday month
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(user.bmonth)
        wd.find_element_by_xpath("//select[2]/option[2]").click()
        # add birthday day
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(user.bday)
        wd.find_element_by_xpath("//option[3]").click()
        # add anniversary year
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(user.ayear)
        # add anniversary month
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(user.amonth)
        wd.find_element_by_xpath("//select[4]/option[3]").click()
        # add anniversary day
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(user.aday)
        wd.find_element_by_xpath("//select[3]/option[3]").click()


    def add_contacts(self, wd, user):
        # add contacts
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(user.company)
        # add address
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(user.address)
        # add home number
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(user.home)
        # add mobile number
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(user.mobile)
        # add work number
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(user.work)
        # add fax number
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(user.fax)
        # add email
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(user.email)
        # add email 2
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(user.email_2)
        # add email 3
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(user.email_3)
        # add homepage
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(user.homepage)


    def add_photo(self, wd, photo, title):
        # add photo
        wd.find_element_by_name("photo").send_keys(photo)
        # add title
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(title)


    def add_name(self, wd, user):
        # add firstname
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(user.firstname)
        # add middlename
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(user.middlename)
        # add lastname
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(user.lastname)
        # add nickname
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(user.nickname)


    def add_new_user(self, wd):
        wd.find_element_by_link_text("add new").click()


    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/edit.php")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    

    def tearDown(self):
        self.wd.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
