# -*- coding: utf-8 -*-
from random import randrange

from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact("first_name_first", "middle_name1_first", "last_name1_first", "roga_and_kopyta1_first", "891112345671_first",
                             "first_something1@mail.ru", "www.wwwww1.com_first", "SPb1_first", "work_place1_first"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    print(str(index)+"    index!!!!!!!!!!")
    contact = Contact("first_name0000000", "middle_name1", "last_name1", "roga_and_kopyta1", "891112345671",
                             "something1@mail.ru", "www.wwwww1.com", "SPb1", "work_place1")
    contact.id = old_contacts[index].id
    print(str(contact.id) + "    contact.id!!!!!!!!!!")
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_modify_contact_firstname(app):
#    if app.contact.count() == 0:
#        app.contact.add_new(Contact("first_name_first", "middle_name1_first", "last_name1_first", "roga_and_kopyta1_first", "891112345671_first",
#                             "first_something1@mail.ru", "www.wwwww1.com_first", "SPb1_first", "work_place1_first"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(first_name="abrakadabra"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)


