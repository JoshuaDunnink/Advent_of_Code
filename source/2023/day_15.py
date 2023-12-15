def data():
    with open("input/2023/day_15", "r") as file:
        return file.read().strip().split(",")


def hashing(string: str, number=0) -> int:
    """
    Determine the ASCII code for the current character of the string.
    Increase the current value by the ASCII code you just determined.
    Set the current value to itself multiplied by 17.
    Set the current value to the remainder of dividing itself by 256.
    """
    for char in string:
        number += ord(char)
        number *= 17
        number %= 256
    return number


def part_1():
    input_data = data()
    print("part_1: " + str(sum([hashing(string) for string in input_data])))


class LensArray:
    def __init__(self):
        self.array = {num: {} for num in range(0, 256)}

    def put_in_box(self, box_number, label, lens):
        if label in self.array[box_number].keys():
            slot = self.array[box_number].get(label)[1]
            self.array[box_number].update({label: [lens, slot]})
        else:
            slots = []
            if len(self.array[box_number]) >= 1:
                for items in self.array[box_number].values():
                    _, slot = items
                    slots.append(slot)
            else:
                slots.append(0)
            next_slot = max(slots) + 1
            self.array[box_number].update({label: [lens, next_slot]})

    def remove_from_box(self, box_number, label):
        if in_box := self.array[box_number].get(label, []):
            _, removed_slot = in_box
            self.array[box_number].pop(label)
            for label, (lens, slot) in self.array[box_number].items():
                if slot > removed_slot:
                    slot -= 1
                self.array[box_number].update({label: [lens, slot]})

    def calculate_focal_power(self):
        lens_powers = []
        for box_number, value in self.array.items():
            if value:
                for lens, slot in value.values():
                    lens_powers.append(
                        (int(box_number) + 1) * int(slot) * int(lens)
                    )
        return sum(lens_powers)


def part_2():
    input_data = data()
    lens_array = LensArray()

    for item in input_data:
        if "=" in item:
            box_label, lens = item.split("=")
            box_number = hashing(box_label)
            lens_array.put_in_box(box_number, box_label, lens)
        if "-" in item:
            box_label = item.split("-")[0]
            box_number = hashing(box_label)
            lens_array.remove_from_box(box_number, box_label)

    print("part_2: " + str(lens_array.calculate_focal_power()))


part_2()
