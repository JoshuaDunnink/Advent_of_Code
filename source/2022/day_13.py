"""
try to implement cmp_to_key?
from functools import cmp_to_key

why not work with booleans?

"""


def get_pairs():
    with open("input/2022/day_13", "r") as file:
        pairs = []
        for group in file.read().strip().split("\n\n"):
            pair = []
            for line in group.split("\n"):
                pair.append(eval(line))
            pairs.append(pair)
    return pairs


def lists_in_order(item_a, item_b):
    value_checks = []

    match item_a, item_b:
        case int(), int():
            return item_a - item_b
        case list(), int():
            value_checks.append(lists_in_order(item_a, [item_b]))
        case int(), list():
            value_checks.append(lists_in_order([item_a], item_b))
        case list(), list():
            for zip_a, zip_b in zip(item_a, item_b):
                value_checks.append(lists_in_order(zip_a, zip_b))
        
        # control??? for empty list and length of it????

    return all(value_checks)


sum_of_index_correct_pairs = []
list_of_pairs = get_pairs()
for index, (item_a, item_b) in enumerate(list_of_pairs):
    if lists_in_order(item_a, item_b):
        sum_of_index_correct_pairs.append(1 + index)

print(sum(sum_of_index_correct_pairs))

