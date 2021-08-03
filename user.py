class UserName:
    def __init__(self, firstname, middlename, lastname, nickname):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname

class UserContacts:
    def __init__(self, company, address, home, mobile, work, fax, email, email_2, email_3, homepage):
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email_2 = email_2
        self.email_3 = email_3
        self.homepage = homepage

class UserDates:
    def __init__(self, byear, bmonth, bday, ayear, amonth, aday):
        self.byear = byear
        self.bmonth = bmonth
        self.bday = bday
        self.ayear = ayear
        self.amonth = amonth
        self.aday = aday


class SecondaryContacts:
    def __init__(self, secondary_address, secondary_phone, notes):
        self.secondary_address = secondary_address
        self.secondary_phone = secondary_phone
        self.notes = notes

