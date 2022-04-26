# -*- coding: utf-8 -*-
import pytest
from application import Application
from contact import Contact

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_add_contact(self):
    self.login("admin", "secret")
    self.add_new_contact(Contact("first_name", "middle_name", "last_name", "roga_and_kopyta", "89111234567",
                             "something@mail.ru", "www.wwwww.com", "SPb", "work_place"))
    self.logout()

