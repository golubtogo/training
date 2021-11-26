from sys import maxsize


class AddressInGroup:
    def __init__(self, group_id=None, id=None):
        self.group_id = group_id
        self.id = id

    def __repr__(self):
        return "%s:%s;" % (self.id, self.group_id)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.group_id == other.group_id

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
