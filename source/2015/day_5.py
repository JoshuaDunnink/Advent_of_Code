"""takeaway - string searches --> use regex"""

import re


def read_input():
    with open("input/2015/day_5") as f:
        data = [line.strip("\n") for line in f.readlines()]
    return data


def has_three_check_vowels(line=str):
    vowels = list("aeiou")
    count = 0
    for char in vowels:
        count += line.count(char)

    if count >= 3:
        return True
    else:
        return False


def does_not_contain_illegal_characters(line):
    illegal_characters = ["ab", "cd", "pq", "xy"]
    if not any(
        [
            True if illegal_character in line else False
            for illegal_character in illegal_characters
        ]
    ):
        return True
    else:
        return False


def has_letter_twice_in_a_row(line):
    for index, character in enumerate(line):
        if (
            index < len(list(line)) - 1
            and line.count(character) >= 2
            and line[index + 1] == character
        ):
            return True

    return False


def pat1(data=list):
    iterable_lines = data.copy()
    for line in iterable_lines:
        if not all(
            [
                does_not_contain_illegal_characters(line),
                has_three_check_vowels(line),
                has_letter_twice_in_a_row(line),
            ]
        ):
            data.remove(line)
    return data


def has_pair_twice(line):
    if len(re.findall(r"([a-z]{2}).*\1", line)):
        return True
    return False


def has_letter_in_repeated(line):
    if re.findall(r"([a-z]).\1", line):
        return True
    return False


def part2(data):
    iterable_lines = data.copy()
    for line in iterable_lines:
        if not all(
            [
                has_pair_twice(line),
                has_letter_in_repeated(line),
            ]
        ):
            data.remove(line)
    return data


data = read_input()
data = part2(data)
print(len(data))
