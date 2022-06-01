# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import pytest

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(name=name, header=header, footer=footer)
    for name in ["", random_string("name", 10)]
    for header in ["", random_string("header", 10)]
    for footer in ["", random_string("footer", 10)]
]

testdata0 = [Group(name="", header="", footer="")]+[
    Group(name=random_string("name", 10), header=random_string("header", 15), footer=random_string("footer", 10))
    for i in range(5)
]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="12", middlename="22", lastname="32", company="42", homephone="52", mobilephone="62", workphone="72", email="82", email2="sss", email3="555", homepage="92", address="adddr11111", address2="102" )
    app.contact.add_new(contact)
    assert len(old_contacts)+1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
