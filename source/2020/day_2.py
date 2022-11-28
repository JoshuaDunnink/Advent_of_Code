def data():
    with open("input/2020/day_1", "r") as file:
        return [int(line) for line in file.readlines()]
