import allure
from model.group import Group


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    with allure.step('Given a group list'):
        old_groups = db.get_group_list()
    with allure.step('When I add the %s group to the list' % group):
        group_id = app.group.create_group(group)
    with allure.step('Then the new group list is equal to the old list with the added group'):
        new_groups = db.get_group_list()
        group.id = group_id
        group.group_header = None
        group.group_footer = None
        old_groups.append(group)
        assert new_groups == old_groups
        ui_groups = app.group.get_group_list()
        if check_ui:
            def clean(group):
                return Group(id=group.id, group_name=group.group_name.strip())
            new_groups = map(clean, db.get_group_list())
            assert sorted(new_groups, key=Group.id_or_max) == sorted(ui_groups, key=Group.id_or_max)



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







