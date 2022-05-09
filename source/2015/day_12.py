import json


def get_data() -> dict:
    with open("input/2015/day_12.json", "r") as file:
        return json.load(file)


class Walker:
    def __init__(self, data: dict):
        self.data = data
        self.unpack_data()

    def unpack_data(self):
        self.unpacked_sum = 0
        self.unpacked_dicts = []
        self.unpacked_lists = []

        for value in self.data.values():
            self.unpack(value)

        while self.unpacked_dicts or self.unpacked_lists:
            self.unpack_dict()
            self.unpack_list()

    def unpack_dict(self):
        while self.unpacked_dicts:
            copy_unpacked_dicts = self.unpacked_dicts.copy()
            for item in copy_unpacked_dicts:
                for value in item.values():
                    if type(value) == dict and self.red_not_in_(value):
                        self.unpack(value)
                    else:
                        self.unpack(value)
                self.unpacked_dicts.remove(item)

    def unpack_list(self):
        while self.unpacked_lists:
            copy_unpacked_lists = self.unpacked_lists.copy()
            for item in copy_unpacked_lists:
                for value in item:
                    if type(value) == dict and self.red_not_in_(value):
                        self.unpack(value)
                    else:
                        self.unpack(value)
                self.unpacked_lists.remove(item)

    def unpack(self, value):
        value_type = type(value)
        if value_type == dict and self.red_not_in_(value):
            self.unpacked_dicts.append(value)
        elif value_type == list:
            self.unpacked_lists.append(value)
        elif value_type == int:
            self.unpacked_sum += value

    @staticmethod
    def red_not_in_(value: dict):
        return "red" not in value.values()


data = get_data()
print(Walker(data).unpacked_sum)
