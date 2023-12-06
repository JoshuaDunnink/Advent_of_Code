import re


def get_data():
    with open("input/2023/day_3", "r") as file:
        return file.readlines()


def find_symbol(line):
    sym_matches = []
    for index, char in enumerate(line.strip()):
        if not char == "." and not char.isdigit():
            if char == "*":
                sym_matches.append([index, True])
            else:
                sym_matches.append([index, False])
    return sym_matches


def get_dicts(grid):
    number_dict = {}
    symbol_dict = {}
    for index, line in enumerate(grid):
        re_num_matches = re.finditer("\\d+", line)
        num_matches = []
        for num_match in re_num_matches:
            span = num_match.span()
            number = num_match[0]
            num_matches.append((number, span))
        number_dict.update({index: num_matches})

        sym_matches = find_symbol(line)
        symbol_dict.update({index: sym_matches})

    return number_dict, symbol_dict


def part_1():
    def add_to_gear(gears: dict, row: int, match_index: int, number: str):
        if existing_row := gears.get(row, {}):
            if existing_row.get(match_index, {}):
                gears[row][match_index] += [number]
            else:
                gears[row].update({match_index: [number]})
        else:
            gears.update({row: {match_index: [number]}})
        return gears

    grid = get_data()
    valid_parts = []
    number_dict, symbol_dict = get_dicts(grid)
    line_lengt = len(grid[0].strip())
    column_length = len(grid)
    gears = {}
    for row, symbol in symbol_dict.items():
        for match_index, is_gear in symbol:
            for number in number_dict.get(row):
                start, end = number[1]
                if match_index != 0 and match_index - 1 in range(start, end):
                    valid_parts.append(int(number[0]))
                    if is_gear:
                        gears = add_to_gear(gears, row, match_index, number[0])
                elif match_index < line_lengt and match_index + 1 in range(
                    start, end
                ):
                    valid_parts.append(int(number[0]))
                    if is_gear:
                        gears = add_to_gear(gears, row, match_index, number[0])
            if row > 0 and row <= column_length:
                for number in number_dict.get(row - 1):
                    start, end = number[1]
                    if match_index != 0 and (
                        match_index - 1 in range(start, end)
                        or match_index in range(start, end)
                    ):
                        valid_parts.append(int(number[0]))
                        if is_gear:
                            gears = add_to_gear(
                                gears, row, match_index, number[0]
                            )
                    elif match_index < line_lengt and match_index + 1 in range(
                        start, end
                    ):
                        valid_parts.append(int(number[0]))
                        if is_gear:
                            gears = add_to_gear(
                                gears, row, match_index, number[0]
                            )
            if row < column_length:
                for number in number_dict.get(row + 1):
                    start, end = number[1]
                    if match_index != 0 and (
                        match_index - 1 in range(start, end)
                        or match_index in range(start, end)
                    ):
                        valid_parts.append(int(number[0]))
                        if is_gear:
                            gears = add_to_gear(
                                gears, row, match_index, number[0]
                            )
                    elif match_index < line_lengt and match_index + 1 in range(
                        start, end
                    ):
                        valid_parts.append(int(number[0]))
                        if is_gear:
                            gears = add_to_gear(
                                gears, row, match_index, number[0]
                            )
    gear_power = 0
    for gear in gears.values():
        for numbers in gear.values():
            if len(numbers) == 2:
                gear_power += int(numbers[0]) * int(numbers[1])

    print("SELF part 1: " + str(sum(valid_parts)))
    print("SELF part 2: " + str(gear_power))


part_1()
