from sys import maxsize


class User:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, id=None,
                 photo=None, title=None,
                 company=None, address=None, home=None, mobile=None, work=None, fax=None, email=None,
                 email2=None, email3=None, homepage=None,
                 byear=None, bmonth=None, bday=None, ayear=None, amonth=None, aday=None,
                 address2=None, phone2=None, notes=None, new_group=None, all_phones_from_home_page=None,
                 all_emails_from_home_page=None):

        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.photo = photo
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.byear = byear
        self.bmonth = bmonth
        self.bday = bday
        self.ayear = ayear
        self.amonth = amonth
        self.aday = aday
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.new_group = new_group
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s" % \
               (self.id, self.lastname, self.middlename, self.firstname, self.nickname,  self.photo,
                self.title, self.company, self.address, self.home, self.mobile, self.work, self.fax,
                self.email, self.email2, self.email3, self.homepage,
                self.byear, self.bmonth, self.bday, self.ayear, self.amonth, self.aday,
                self.address2, self.phone2, self.notes, self.new_group)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and self.firstname == other.firstname

    def __gt__(self, other):
        return self.id > other.id

    def __lt__(self, other):
        return self.id < other.id

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

