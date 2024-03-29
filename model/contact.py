from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, address=None,  company=None, homephone=None, mobilephone=None,
                 workphone=None, email=None, email2=None, email3=None, homepage=None, address2=None, homephone2=None,  id=None,
                 all_phones_from_home_page=None, all_emails_from_homepage=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.address = address
        self.company = company
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.address2 = address2
        self.homephone2 = homephone2
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_homepage = all_emails_from_homepage
        self.id = id

    def __repr__(self):
        return "%s:%s %s %s" % (self.id, self.firstname, self.lastname, self.address)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize