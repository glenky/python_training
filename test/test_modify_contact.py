# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    app.contact.modify_first_contact(Contact("first_name1", "middle_name1", "last_name1", "roga_and_kopyta1", "891112345671",
                             "something1@mail.ru", "www.wwwww1.com", "SPb1", "work_place1"))


def test_modify_contact_firstname(app):
    app.contact.modify_first_contact(Contact(first_name="abrakadabra"))


