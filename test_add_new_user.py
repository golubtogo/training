# -*- coding: utf-8 -*-
from selenium import webdriver

from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

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
        self.login(driver)
        self.add_new_user(driver)
        self.add_name(driver)
        self.add_photo(driver)
        self.add_title(driver)
        self.add_company(driver)
        self.add_address(driver)
        self.add_home(driver)
        self.add_mobile(driver)
        self.add_work(driver)
        self.add_fax(driver)
        self.add_email(driver)
        self.add_homepage(driver)
        self.add_bdate(driver)
        self.add_adate(driver)
        self.choose_group(driver)
        self.add_address2(driver)
        self.add_phone2(driver)
        self.add_notes(driver)
        self.submit(driver)

    def submit(self, driver):
        driver.find_element_by_xpath("//input[21]").click()

    def add_notes(self, driver):
        driver.find_element_by_name("notes").click()
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys("hello")

    def add_phone2(self, driver):
        driver.find_element_by_name("phone2").click()
        driver.find_element_by_name("phone2").clear()
        driver.find_element_by_name("phone2").send_keys("secondary home")

    def add_address2(self, driver):
        driver.find_element_by_name("address2").click()
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys("secondary address")

    def choose_group(self, driver):
        driver.find_element_by_name("new_group").click()
        driver.find_element_by_xpath("//option[@value='[none]']").click()

    def add_adate(self, driver):
        # add ayear
        driver.find_element_by_name("ayear").click()
        driver.find_element_by_name("ayear").clear()
        driver.find_element_by_name("ayear").send_keys("2015")
        # add amonth
        driver.find_element_by_name("amonth").click()
        Select(driver.find_element_by_name("amonth")).select_by_visible_text("February")
        driver.find_element_by_xpath("//select[4]/option[3]").click()
        # add aday
        driver.find_element_by_name("aday").click()
        Select(driver.find_element_by_name("aday")).select_by_visible_text("1")
        driver.find_element_by_xpath("//select[3]/option[3]").click()


    def add_bdate(self, driver):
        # add byear
        driver.find_element_by_name("byear").click()
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys("2000")
        # add bmonth
        driver.find_element_by_name("bmonth").click()
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text("January")
        driver.find_element_by_xpath("//select[2]/option[2]").click()
        # add dday
        driver.find_element_by_name("bday").click()
        Select(driver.find_element_by_name("bday")).select_by_visible_text("1")
        driver.find_element_by_xpath("//option[3]").click()

    def add_homepage(self, driver):
        driver.find_element_by_name("homepage").click()
        driver.find_element_by_name("homepage").clear()
        driver.find_element_by_name("homepage").send_keys("homepage")

    def add_email(self, driver):
        # add email
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("e-mail")
        # add email 2
        driver.find_element_by_name("email2").click()
        driver.find_element_by_name("email2").clear()
        driver.find_element_by_name("email2").send_keys("e-mail2")
        # add email 3
        driver.find_element_by_name("email3").click()
        driver.find_element_by_name("email3").clear()
        driver.find_element_by_name("email3").send_keys("e-mail3")

    def add_fax(self, driver):
        driver.find_element_by_name("fax").click()
        driver.find_element_by_name("fax").clear()
        driver.find_element_by_name("fax").send_keys("fax")

    def add_work(self, driver):
        driver.find_element_by_name("work").click()
        driver.find_element_by_name("work").clear()
        driver.find_element_by_name("work").send_keys("work")

    def add_mobile(self, driver):
        driver.find_element_by_name("mobile").click()
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys("mobile")

    def add_home(self, driver):
        driver.find_element_by_name("home").click()
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys("home")

    def add_address(self, driver):
        driver.find_element_by_name("address").click()
        driver.find_element_by_name("address").click()
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys("address\n+380111111111")

    def add_company(self, driver):
        driver.find_element_by_name("company").click()
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys("company")

    def add_title(self, driver):
        driver.find_element_by_name("title").click()
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys("title")

    def add_photo(self, driver):
        driver.find_element_by_name("photo").send_keys("C:\\Users\\Nata\\PycharmProjects\\test_image.png")

    def add_name(self, driver):
        # add firstname
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys("first name")
        # add middlename
        driver.find_element_by_name("middlename").click()
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys("middle name")
        # add lastname
        driver.find_element_by_name("lastname").click()
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys("last name")
        # add nickname
        driver.find_element_by_name("nickname").click()
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys("nickname")

    def add_new_user(self, driver):
        driver.find_element_by_link_text("add new").click()

    def login(self, driver):
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").send_keys("secret")
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
