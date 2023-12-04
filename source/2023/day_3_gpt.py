import re


def get_data():
    with open("input/2023/day_3", "r") as file:
        return file.readlines()


def find_symbol(line):
    return [
        index
        for index, char in enumerate(line.strip())
        if char != "." and not char.isdigit()
    ]


def extract_numbers(line):
    return [
        (match.group(), match.span()) for match in re.finditer(r"\d+", line)
    ]


def get_dicts(grid):
    number_dict = {}
    symbol_dict = {}
    for index, line in enumerate(grid):
        number_matches = extract_numbers(line)
        number_dict[index] = number_matches

        sym_matches = find_symbol(line)
        symbol_dict[index] = sym_matches

    return number_dict, symbol_dict


def check_adjacent_numbers(match_index, numbers):
    adjacent_numbers = []
    for number in numbers:
        start, end = number[1]
        if match_index != 0 and match_index - 1 in range(start, end):
            adjacent_numbers.append(int(number[0]))
        elif match_index < line_length and match_index + 1 in range(
            start, end
        ):
            adjacent_numbers.append(int(number[0]))
    return adjacent_numbers


def check_adjacent_numbers_in_row(row, match_index, number_dict):
    return check_adjacent_numbers(match_index, number_dict.get(row, []))


def check_adjacent_numbers_in_previous_row(row, match_index, number_dict):
    adjacent_numbers = []
    if 0 < row < column_length:
        numbers = number_dict.get(row - 1, [])
        adjacent_numbers.extend(check_adjacent_numbers(match_index, numbers))
    return adjacent_numbers


def check_adjacent_numbers_in_next_row(row, match_index, number_dict):
    adjacent_numbers = []
    if 0 <= row < column_length - 1:
        numbers = number_dict.get(row + 1, [])
        adjacent_numbers.extend(check_adjacent_numbers(match_index, numbers))
    return adjacent_numbers


def part_1():
    grid = get_data()
    valid_parts = []
    number_dict, symbol_dict = get_dicts(grid)
    global column_length
    column_length = len(grid)
    global line_length
    line_length = len(grid[0].strip())

    for row, matches in symbol_dict.items():
        for match_index in matches:
            valid_parts.extend(
                check_adjacent_numbers_in_row(row, match_index, number_dict)
            )
            valid_parts.extend(
                check_adjacent_numbers_in_previous_row(
                    row, match_index, number_dict
                )
            )
            valid_parts.extend(
                check_adjacent_numbers_in_next_row(
                    row, match_index, number_dict
                )
            )

    print("GPT refactored, but incorrect: " + str(sum(valid_parts)))


part_1()
