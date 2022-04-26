# -*- coding: utf-8 -*-
import pytest
from fixrure.application import Application
from model.contact import Contact

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_add_contact(app):
    app.session.login("admin", "secret")
    app.contact.add_new(Contact("first_name", "middle_name", "last_name", "roga_and_kopyta", "89111234567",
                             "something@mail.ru", "www.wwwww.com", "SPb", "work_place"))
    app.session.logout()

