class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def update_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        group_data = group.__dict__

        for label in group_data:
            value = group_data[label]
            if value:
                wd.find_element_by_name(label).click()
                wd.find_element_by_name(label).clear()
                wd.find_element_by_name(label).send_keys(value)

        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        # return to groups page
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()


