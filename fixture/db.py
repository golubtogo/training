import pymysql

from model.addressingroup import AddressInGroup
from model.group import Group
from model.user import User

from fixture.orm import ORMFixture
from model.group import Group


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name from group_list where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, name) = row
                list.append(Group(id=str(id), group_name=name))
        finally:
            cursor.close()
        return list

    def get_user_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(User(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def get_all_user_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3 "
                           "from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3) = row
                list.append(User(id=str(id), firstname=firstname, lastname=lastname,
                                 address=address, home=home, mobile=mobile, work=work, phone2=phone2, email=email,
                                 email2=email2, email3=email3))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

    def get_address_in_groups_list(self):

        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, id from address_in_groups where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (group_id, id) = row
                list.append(f"{group_id}:{id}")
        finally:
            cursor.close()
        return list

    def get_address_in_groups_list_id(self, group_id):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id from address_in_groups where group_id = group_id ")
            for row in cursor:
                id = row
                list.append(f"{id}")
        finally:
            cursor.close()
        return list

    def get_address_in_groups(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, id from address_in_groups where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (group_id, id) = row
                list.append(AddressInGroup(group_id, id))
        finally:
            cursor.close()
        return list


