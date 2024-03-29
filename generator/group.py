#import json
import jsonpickle
import os.path
import random
import string
from model.group import Group
import sys
import getopt

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file="])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")]+[
    Group(name=random_string("name", 10), header=random_string("header", 15), footer=random_string("footer", 10))
    for i in range(n)
]
# join ".." and f: /data/groups.json
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

# generation with package json - json.dumps
#with open(file, "w") as out:
#    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))


