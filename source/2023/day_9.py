lists = [
    [0, 3, 6, 9, 12, 15],
    [1, 3, 6, 10, 15, 21],
    [10, 13, 16, 21, 30, 45],
]


def data():
    with open("input/2023/day_9", "r") as file:
        file_data = file.readlines()
        lines = []
        for line in file_data:
            lines.append([int(num) for num in line.split(" ")])
        return lines


class FunctionGenerator:
    def __init__(self, sequence):
        self.layers = {0: sequence}

    def is_constant(self, sequence: list):
        checks = []
        list_len = len(sequence)
        for index, number in enumerate(sequence):
            if index + 1 < list_len:
                checks.append(number == sequence[index + 1])
        return all(checks)

    def get_sequence(self, depth, sequence):
        diff = []
        depth += 1
        len_sequence = len(sequence)
        for index, num in enumerate(sequence):
            if index + 1 < len_sequence:
                diff.append((sequence[index + 1] - num))

        self.layers.update({depth: diff})
        if not self.is_constant(diff):
            self.get_sequence(depth + 1, diff)

    def generate_next_val(self):
        next_val = 0
        for key in self.layers.keys():
            next_val += self.layers.get(key)[-1]
        return next_val


def part_1():
    numbers = []
    for sequence in data():
        func = FunctionGenerator(sequence)
        func.get_sequence(0, sequence)
        numbers.append(func.generate_next_val())
    print(sum(numbers))


def part_2():
    numbers = []
    for sequence in data():
        reversed_sequence = [num for num in reversed(sequence)]
        func = FunctionGenerator(reversed_sequence)
        func.get_sequence(0, reversed_sequence)
        numbers.append(func.generate_next_val())
    print(sum(numbers))


# part_1()
part_2()
