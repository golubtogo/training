
class Group:
    def __init__(self, name, header, footer):
        self.name = name
        self.header = header
        self.footer = footer


class GroupModify:
    def __init__(self, modified_name):
        self.modified_name = modified_name
