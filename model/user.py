from sys import maxsize


class User:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None,
                 photo=None, title=None,
                 company=None, address=None, home=None, mobile=None, work=None, fax=None, email=None,
                 email2=None, email3=None, homepage=None,
                 byear=None, bmonth=None, bday=None, ayear=None, amonth=None, aday=None,
                 address2=None, phone2=None, notes=None, new_group=None, id=None):

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

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
