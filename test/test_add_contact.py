# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="12", middlename="22", lastname="32", company="42", homephone="52", mobilephone="62", workphone="72", email="82", email2="sss", email3="555", homepage="92", address="adddr11111", address2="102" )
    app.contact.add_new(contact)
    assert len(old_contacts)+1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
