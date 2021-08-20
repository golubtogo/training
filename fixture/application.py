from selenium import webdriver
from selenium.common.exceptions import InvalidSelectorException, NoSuchElementException

from fixture.session import SessionHelper
from fixture.user import UserHelper
from fixture.group import GroupHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()

        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.user = UserHelper(self)
        self.group = GroupHelper(self)

    def is_valid(self):
        try:
            if self.wd.find_element_by_xpath("//a[contains(text(),'Logout')]"):
                return True
        except NoSuchElementException:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost:80/addressbook/edit.php")

    def destroy(self):
        self.wd.quit()



