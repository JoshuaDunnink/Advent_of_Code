def data():
    with open("input/2022/day_1", "r") as file:
        data = file.readlines()
        normalized_lines = []
        appendable_line = []
        for line in data:
            if line != "\n":
                appendable_line.append(int(line.strip("\n")))
            elif line == "\n":
                normalized_lines.append(appendable_line)
                appendable_line = []
    return normalized_lines


def part_1():
    total_cals = []
    calories = data()
    for line in calories:
        total_cals.append(sum(line))
    print("Elf carrying most calories: " + str(max(total_cals)))
    return total_cals


def part_2(total_cals: list):
    total_cals.sort()
    print(
        "Three elf total carrying most calories: " + str(sum(total_cals[-3:]))
    )


part_2(part_1())
