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


def get_zero_six_and_nine(known_segments, unknown_sets):
    for id, unknown in enumerate(unknown_sets):
        six_zero_nine = [item for item in unknown if len(item) == 6]
        known_segments[id].update(
            breakdown_zero_six_and_nine(six_zero_nine, known_segments[id])
        )
    return known_segments


def get_five(six, unknown_set):
    for id, number in enumerate(unknown_set):
        if len(six.difference(number)) == 1:
            unknown_set.pop(id)
            return unknown_set, {5: number}


def get_two_and_three(five, unknown_set):
    knowns = {}
    for number in unknown_set:
        if len(five.difference(number)) == 1:
            knowns.update({3: number})
        elif len(five.difference(number)) == 2:
            knowns.update({2: number})
    return knowns


def get_two_three_five_from(knowns_segments, unknown_sets):
    for id, unknown in enumerate(unknown_sets):
        six = knowns_segments[id].get(6)
        unknown_set, five = get_five(six, unknown)
        knowns_segments[id].update(five)
        knowns_segments[id].update(get_two_and_three(five.get(5), unknown_set))
    return knowns_segments


def identify_numbers(data):
    known_segments1478 = get_known_segments(data)
    unknown_set023569 = get_unknown_segments(data, known_segments1478)
    known_segments0146789 = get_zero_six_and_nine(
        known_segments1478, unknown_set023569
    )
    unknown_set235 = get_unknown_segments(data, known_segments0146789)
    known_segments0123456789 = get_two_three_five_from(
        known_segments0146789, unknown_set235
    )
    return known_segments0123456789


def get_number_from_line(line, identified_numbers):
    _, numbers_part = line.split("|")
    numbers = [set(number) for number in numbers_part.split(" ")]

    number = "0"
    for segments in numbers:
        for key, value in identified_numbers.items():
            if segments == value:
                number += str(key)
    return int(number)


def part2():
    data = get_input2()
    identified_numbers = identify_numbers(data)

    count = 0
    for id, line in enumerate(data):
        count += get_number_from_line(line, identified_numbers[id])
    print(count)


def part1():
    data = get_input1()
    count = 0
    for line in data:
        for set in line[1].split(" "):
            if len(set) in number_segments.values():
                count += 1
    print(count)


part2()
