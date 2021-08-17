from selenium.webdriver.support.ui import Select
import time


class UserHelper:

    def __init__(self, app):
        self.app = app

    def open_add_new_user(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.open_add_new_user()

    def update_user(self, user):
        wd = self.app.wd

        if user.photo:
            wd.find_element_by_name("photo").send_keys(user.photo)

        if user.bmonth:
            wd.find_element_by_name("bmonth").click()
            Select(wd.find_element_by_name("bmonth")).select_by_visible_text(user.bmonth)
            wd.find_element_by_xpath("//select[2]/option[2]").click()

        if user.bday:
            wd.find_element_by_name("bday").click()
            Select(wd.find_element_by_name("bday")).select_by_visible_text(user.bday)
            wd.find_element_by_xpath("//option[3]").click()

        if user.amonth:
            wd.find_element_by_name("amonth").click()
            Select(wd.find_element_by_name("amonth")).select_by_visible_text(user.amonth)
            wd.find_element_by_xpath("//select[4]/option[3]").click()

        if user.aday:
            wd.find_element_by_name("aday").click()
            Select(wd.find_element_by_name("aday")).select_by_visible_text(user.aday)
            wd.find_element_by_xpath("//select[3]/option[3]").click()

        if user.new_group:
            wd.find_element_by_name("new_group").click()
            wd.find_element_by_xpath("//option[@value='[none]']").click()

        user_data = user.__dict__

        for label in user_data:
            value = user_data[label]
            if value and not any(ext in label for ext in ["month", "day", "photo"]):
                wd.find_element_by_name(label).click()
                wd.find_element_by_name(label).clear()
                wd.find_element_by_name(label).send_keys(value)

        wd.find_element_by_name("submit").click()

    def delete_first_user(self):
        wd = self.app.wd
        self.open_home_page()
        # select first user
        wd.find_element_by_name("selected[]").click()
        # delete selected user
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def open_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def submit(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[21]").click()

