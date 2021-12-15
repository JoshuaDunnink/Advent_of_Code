def get_input1():
    with open("input/2021/day_8") as file:
        data = [line.strip("\n").split("|") for line in file.readlines()]
    return data


def get_input2():
    with open("input/2021/day_8") as file:
        data = [line.strip("\n") for line in file.readlines()]
    return data


number_segments = {
    # 0: 6,
    1: 2,
    # 2: 5,
    # 3: 5,
    4: 4,
    # 5: 5,
    7: 3,
    8: 7,
    # 9: 6,
}


def get_known_segments(data) -> list:
    known_data = [item.strip("|").split(" ") for item in data]
    all_lines = []
    for line in known_data:
        known_segments = {}
        for number in line:
            for key, value in number_segments.items():
                if (
                    len(number) == value
                    and number not in known_segments.values()
                ):
                    known_segments.update(
                        {key: set([char for char in number])}
                    )
        all_lines.append(known_segments)
    return all_lines


def compare_line_sets(line1, line2) -> list:
    line_2 = [set([char for char in item]) for item in line2]
    diff = []
    for item in line_2:
        if item not in line1 and item not in diff:
            diff.append(item)
    return diff


def get_unknown_segments(data, known_segments) -> list:
    unknowns = []
    for id, line in enumerate(data):
        unknown_line_data = [
            char for char in line.replace(" | ", " ").split(" ")
        ]
        difference = compare_line_sets(
            known_segments[id].values(), unknown_line_data
        )
        unknowns.append(difference)
    return unknowns


def breakdown_zero_six_and_nine(unknown, known) -> dict:
    one = known.get(1)
    four = known.get(4)

    for id, segment in enumerate(unknown):
        if not all([True if char in segment else False for char in one]):
            known.update({6: segment})
            unknown.pop(id)
            break

    for id, segment in enumerate(unknown):
        if not all([True if char in segment else False for char in four]):
            known.update({0: segment})
            unknown.pop(id)
            break

    known.update({9: unknown[0]})

    return known


def get_zero_six_and_nine(known_segments, unknown_set):
    for id, unknown in enumerate(unknown_set):
        six_zero_nine = [item for item in unknown if len(item) == 6]
        known_segments[id].update(
            breakdown_zero_six_and_nine(six_zero_nine, known_segments[id])
        )
    return known_segments


def get_top_from_one_and_seven(knowns) -> set:
    one = set(char for char in knowns.get(1))
    seven = set(char for char in knowns.get(7))
    return seven.difference(one)


def part1():
    data = get_input1()
    count = 0
    for line in data:
        for set in line[1].split(" "):
            if len(set) in number_segments.values():
                count += 1
    print(count)


def part2():
    data = get_input2()
    known_segments1478 = get_known_segments(data)
    unknown_set023569 = get_unknown_segments(data, known_segments1478)
    # now known 1, 4, 7, 8
    # unknown 0, 2, 3, 5, 6, 9
    known_segments = get_zero_six_and_nine(
        known_segments1478, unknown_set023569
    )
    unknown_set235 = get_unknown_segments(data, known_segments)
    # now known 0, 1, 4, 6, 7, 8, 9
    # unknown 2, 3, 5
    print("till here")


part2()
