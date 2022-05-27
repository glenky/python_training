from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, company=None, homephone=None, mobilephone=None, email=None, homepage=None, address2=None, workphone=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.company = company
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.email = email
        self.homepage = homepage
        self.address2 = address2
        self.workphone = workphone
        self.id = id

    def __repr__(self):
        return "%s:%s %s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.first_name and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize