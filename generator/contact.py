import jsonpickle
import os.path
import random
import string
from model.contact import Contact
import sys
import getopt

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file="])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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


testdata = [Contact(firstname=random_string("firstname", 10, "string"), middlename=random_string("middlename", 15, "string"), lastname=random_string("lastname", 11, "string"),
            company=random_string("company", 10, "string"), homephone=random_string("+", 10, "phone"), mobilephone=random_string("+", 10, "phone"),
            workphone=random_string("+", 10, "phone"), homephone2=random_string("+", 10, "phone"),
            email=random_string("email", 10, "email"), email2=random_string("email", 10, "email"), email3=random_string("email", 10, "email"),
            homepage=random_string("homepage", 10, "string"), address=random_string("address", 10, "string"), address2=random_string("address2", 10, "string"))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))


