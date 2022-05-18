
class Contact:
    def __init__(self, first_name=None, middle_name=None, last_name=None, company=None, mobile_phone=None, email=None, home_page=None, address2=None, work_phone=None, id=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.company = company
        self.mobile_phone = mobile_phone
        self.email = email
        self.home_page = home_page
        self.address2 = address2
        self.work_phone = work_phone
        self.id = id

    def __repr__(self):
        return "%s:%s %s" % (self.id, self.first_name, self.last_name)

    def __eq__(self, other):
        return self.id == other.id and self.first_name == other.first_name and self.last_name == other.last_name