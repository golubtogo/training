
from model.group import Group


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = db.get_group_list()
    group_id = app.group.create_group(group)
    new_groups = db.get_group_list()
    group.id = group_id
    group.group_name = group.group_name.strip()
    group.group_header = None
    group.group_footer = None
    old_groups.append(group)
    assert new_groups == old_groups
    # if check_ui:
    #     assert sorted(old_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

# @pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
# def test_add_group(app, group):
#     old_groups = app.group.get_group_list()
#     group_id = app.group.create_group(group)
#     assert len(old_groups) + 1 == app.group.count()
#     new_groups = app.group.get_group_list()
#     group.id = group_id
#     group.group_name = group.group_name.strip()
#     group.group_header = None
#     group.group_footer = None
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)







