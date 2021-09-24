# -*- coding: utf-8 -*-

from model.group import Group
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10  # some tests don't pass with string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(group_name="", group_header="", group_footer="")] + [
    Group(group_name=random_string("group_name", 10),
          group_header=random_string("group_header", 20),
          group_footer=random_string("group_footer", 20)
          )
    for i in range(1)

]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    group_id = app.group.create_group(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    group.id = group_id
    group.group_name = group.group_name.strip()
    group.group_header = None
    group.group_footer = None
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)





