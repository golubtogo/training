import re
import time

from selenium.webdriver.support.ui import Select
from model.user import User
import random


class UserHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("Send e-Mail")) > 0):
            wd.find_element_by_link_text("home").click()

    def init_user_creation(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create_user(self, user):
        self.open_home_page()
        self.init_user_creation()
        self.fill_user_form(user)
        self.submit()
        self.return_to_home_page()
        self.user_cache = None

    def change_field_value(self, user):
        wd = self.app.wd
        if user.photo:
            wd.find_element_by_name("photo").send_keys(user.photo)

        if user.bmonth:
            wd.find_element_by_name("bmonth").click()
            Select(wd.find_element_by_name("bmonth")).select_by_visible_text(user.bmonth)
#            wd.find_element_by_xpath("//select[2]/option[2]").click()

        if user.bday:
            wd.find_element_by_name("bday").click()
            Select(wd.find_element_by_name("bday")).select_by_visible_text(user.bday)
#            wd.find_element_by_xpath("//option[3]").click()

        if user.amonth:
            wd.find_element_by_name("amonth").click()
            Select(wd.find_element_by_name("amonth")).select_by_visible_text(user.amonth)
#            wd.find_element_by_xpath("//select[4]/option[3]").click()

        if user.aday:
            wd.find_element_by_name("aday").click()
            Select(wd.find_element_by_name("aday")).select_by_visible_text(user.aday)
#            wd.find_element_by_xpath("//select[3]/option[3]").click()

        if user.new_group:
            wd.find_element_by_name("new_group").click()
            wd.find_element_by_xpath("//option[@value='[none]']").click()

        user_data = user.__dict__

        for label in user_data:
            value = user_data[label]
            if value is not None and \
               not any(ext in label for ext in ["month", "day", "photo", "new_group"]) and \
               label != 'id':
                wd.find_element_by_name(label).click()
                wd.find_element_by_name(label).clear()
                wd.find_element_by_name(label).send_keys(value)

    def fill_user_form(self, user):
        self.change_field_value(user)

    def modify_first_user(self):
        self.modify_user_by_index(0)

    def modify_user_by_index(self, index, new_user_data):
        wd = self.app.wd
        self.open_home_page()
        self.select_user_by_index(index)
        # open modification form
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_user_form(new_user_data)
        self.update()
        self.return_to_home_page()
        self.user_cache = None

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def select_user_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_user(self):
        self.delete_user_by_index(0)

    def delete_user_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        # select first user
        wd.find_elements_by_name("selected[]")[index].click()
        # delete selected user
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.user_cache = None

    def submit(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Enter']").click()

    def update(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    user_cache = None

    def get_user_list(self):
        if self.user_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.user_cache = []
            for element in wd.find_elements_by_css_selector("tr[name=entry]"):
                cells = element.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                address =cells[3].text
                self.user_cache.append(User(lastname=lastname, firstname=firstname, id=id,
                                            all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails,
                                            address=address))
        return list(self.user_cache)

    def open_user_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        element = wd.find_elements_by_css_selector("tr[name=entry]")[index]
        cell = element.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_user_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        element = wd.find_elements_by_css_selector("tr[name=entry]")[index]
        cell = element.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_user_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_user_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")

        return User(firstname=firstname, lastname=lastname, id=id, address=address, home=home,
                    mobile=mobile, work=work, phone2=phone2, email=email, email2=email2, email3=email3)

    def get_user_from_view_page(self, index):
        wd = self.app.wd
        self.open_user_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return User(home=home, mobile=mobile, work=work, phone2=phone2)



