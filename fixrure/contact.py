import re

from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_new(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit update
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.return_to_home_page()
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(new_contact_data)
        # submit update
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").text
        print("address = "+address)
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        homephone2 = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, homephone2=homephone2, address=address, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        homephone2 = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, homephone2=homephone2)


    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0, new_contact_data)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("company", contact.company)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.homephone2)
        self.change_field_value("address", contact.address)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("Send e-Mail")) > 0):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, all_phones_from_home_page=all_phones,
                                                  address=address, all_emails_from_homepage=all_emails))
        return list(self.contact_cache)

#    def contact_count(self):
#        wd = self.app.wd
#        self.return_to_home_page()
#        count = 0
#        for row in wd.find_elements_by_name("entry"):
#            count = count + 1
#        return count

    def contact_count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))
