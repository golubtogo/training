# -*- coding: utf-8 -*-
from selenium import webdriver

from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from group import GroupName
from group import GroupEmail
from group import GroupBdate
from group import GroupAdate


class TestAddNewUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_new_user(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, username="admin", password="secret")
        self.add_new_user(driver)
        self.add_name(driver, GroupName(firstname="first name", middlename="middle name", lastname="last name", nickname="nickname"))
        self.add_photo(driver, photo="C:\\Users\\Nata\\PycharmProjects\\test_image.png")
        self.add_title(driver, title="title")
        self.add_company(driver, company="company")
        self.add_address(driver, address_phone="address\n+380111111111")
        self.add_home(driver, home="home")
        self.add_mobile(driver, mobile="mobile")
        self.add_work(driver, work="work")
        self.add_fax(driver, fax="fax")
        self.add_email(driver, GroupEmail(email="e-mail", email_2="e-mail2", email_3="e-mail3"))
        self.add_homepage(driver, homepage="homepage")
        self.add_bdate(driver, GroupBdate(b_year="2000", b_month="January", b_day="1"))
        self.add_adate(driver, GroupAdate(a_year="2015", a_month="February", a_day="1"))
        self.choose_group(driver)
        self.add_secondary_address(driver, secondary_address="secondary address")
        self.add_secondary_phone(driver, secondary_phone="secondary home")
        self.add_notes(driver, notes="hello")
        self.submit(driver)


    def submit(self, driver):
        driver.find_element_by_xpath("//input[21]").click()

    def add_notes(self, driver, notes):
        driver.find_element_by_name("notes").click()
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys(notes)

    def add_secondary_phone(self, driver, secondary_phone):
        driver.find_element_by_name("phone2").click()
        driver.find_element_by_name("phone2").clear()
        driver.find_element_by_name("phone2").send_keys(secondary_phone)

    def add_secondary_address(self, driver, secondary_address):
        driver.find_element_by_name("address2").click()
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys(secondary_address)

    def choose_group(self, driver):
        driver.find_element_by_name("new_group").click()
        driver.find_element_by_xpath("//option[@value='[none]']").click()

    def add_adate(self, driver, GroupAdate):
        # add anniversary year
        driver.find_element_by_name("ayear").click()
        driver.find_element_by_name("ayear").clear()
        driver.find_element_by_name("ayear").send_keys(GroupAdate.a_year)
        # add anniversary month
        driver.find_element_by_name("amonth").click()
        Select(driver.find_element_by_name("amonth")).select_by_visible_text(GroupAdate.a_month)
        driver.find_element_by_xpath("//select[4]/option[3]").click()
        # add anniversary day
        driver.find_element_by_name("aday").click()
        Select(driver.find_element_by_name("aday")).select_by_visible_text(GroupAdate.a_day)
        driver.find_element_by_xpath("//select[3]/option[3]").click()


    def add_bdate(self, driver, GroupBdate):
        # add Birthday year
        driver.find_element_by_name("byear").click()
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys(GroupBdate.b_year)
        # add Birthday month
        driver.find_element_by_name("bmonth").click()
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text(GroupBdate.b_month)
        driver.find_element_by_xpath("//select[2]/option[2]").click()
        # add birthday day
        driver.find_element_by_name("bday").click()
        Select(driver.find_element_by_name("bday")).select_by_visible_text(GroupBdate.b_day)
        driver.find_element_by_xpath("//option[3]").click()

    def add_homepage(self, driver, homepage):
        driver.find_element_by_name("homepage").click()
        driver.find_element_by_name("homepage").clear()
        driver.find_element_by_name("homepage").send_keys(homepage)

    def add_email(self, driver, GroupEmail):
        # add email
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(GroupEmail.email)
        # add email 2
        driver.find_element_by_name("email2").click()
        driver.find_element_by_name("email2").clear()
        driver.find_element_by_name("email2").send_keys(GroupEmail.email_2)
        # add email 3
        driver.find_element_by_name("email3").click()
        driver.find_element_by_name("email3").clear()
        driver.find_element_by_name("email3").send_keys(GroupEmail.email_3)

    def add_fax(self, driver, fax):
        driver.find_element_by_name("fax").click()
        driver.find_element_by_name("fax").clear()
        driver.find_element_by_name("fax").send_keys(fax)

    def add_work(self, driver, work):
        driver.find_element_by_name("work").click()
        driver.find_element_by_name("work").clear()
        driver.find_element_by_name("work").send_keys(work)

    def add_mobile(self, driver, mobile):
        driver.find_element_by_name("mobile").click()
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys(mobile)

    def add_home(self, driver, home):
        driver.find_element_by_name("home").click()
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys(home)

    def add_address(self, driver, address_phone):
        driver.find_element_by_name("address").click()
        driver.find_element_by_name("address").click()
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys(address_phone)

    def add_company(self, driver, company):
        driver.find_element_by_name("company").click()
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys(company)

    def add_title(self, driver, title):
        driver.find_element_by_name("title").click()
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys(title)

    def add_photo(self, driver, photo):
        driver.find_element_by_name("photo").send_keys(photo)

    def add_name(self, driver, GroupName):
        # add firstname
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(GroupName.firstname)
        # add middlename
        driver.find_element_by_name("middlename").click()
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys(GroupName.middlename)
        # add lastname
        driver.find_element_by_name("lastname").click()
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(GroupName.lastname)
        # add nickname
        driver.find_element_by_name("nickname").click()
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys(GroupName.nickname)

    def add_new_user(self, driver):
        driver.find_element_by_link_text("add new").click()

    def login(self, driver, username, password):
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()

    def open_home_page(self, driver):
        driver.get("http://localhost/addressbook/edit.php")

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
