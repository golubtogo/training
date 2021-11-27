from model.group import Group
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif a == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*2  # some tests don't pass with string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Group(group_name=random_string("group_name", 10),
          group_header=random_string("group_header", 20),
          group_footer=random_string("group_footer", 20)
          )
    for i in range(5)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
