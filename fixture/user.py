from selenium.webdriver.support.ui import Select
from model.user import User


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
        self.user_cache = None

    def change_field_value(self, user):
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
            if value is not None and not any(ext in label for ext in ["month", "day", "photo", "new_group", "id"]):
                wd.find_element_by_name(label).click()
                wd.find_element_by_name(label).clear()
                wd.find_element_by_name(label).send_keys(value)

    def fill_user_form(self, user):
        self.change_field_value(user)

    def modify_first_user(self, user):
        self.open_home_page()
        self.init_user_modification()
        self.fill_user_form(user)
        self.update()
        self.user_cache = None

    def init_user_modification(self):
        wd = self.app.wd
        # select first user
        wd.find_element_by_name("selected[]").click()
        # click edit selected user
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def delete_first_user(self):
        wd = self.app.wd
        self.open_home_page()
        # select first user
        wd.find_element_by_name("selected[]").click()
        # delete selected user
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.user_cache = None

    def submit(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[21]").click()

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
                id = element.find_element_by_css_selector("td.center input").get_attribute("value")
                lastname = element.find_elements_by_tag_name("td")[1].text
                firstname = element.find_elements_by_tag_name("td")[2].text
                self.user_cache.append(User(firstname=firstname, lastname=lastname, id=id))
        return list(self.user_cache)

