# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import pytest


def random_string(prefix, maxlen, type):
    if type == "phone":
        symbols = string.digits + " "*3 + "(" + ")"
        return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    elif type == "email":
        symbols = string.digits + string.ascii_letters
        return prefix + "@" + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    else:
        symbols = string.ascii_letters + string.digits + string.punctuation + " "*3
        return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="")]+[
    Contact(firstname=random_string("firstname", 10, "string"), middlename=random_string("middlename", 15, "string"), lastname=random_string("lastname", 11, "string"),
            company=random_string("company", 10, "string"), homephone=random_string("+", 10, "phone"), mobilephone=random_string("+", 10, "phone"),
            workphone=random_string("+", 10, "phone"), homephone2=random_string("+", 10, "phone"),
            email=random_string("email", 10, "email"), email2=random_string("email", 10, "email"), email3=random_string("email", 10, "email"),
            homepage=random_string("homepage", 10, "string"), address=random_string("address", 10, "string"), address2=random_string("address2", 10, "string"))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_new(contact)
    print()
    assert len(old_contacts)+1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
