# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.session.login("admin", "secret")
    app.contact.add_new(Contact("first_name", "middle_name", "last_name", "roga_and_kopyta", "89111234567",
                             "something@mail.ru", "www.wwwww.com", "SPb", "work_place"))
    app.session.logout()

