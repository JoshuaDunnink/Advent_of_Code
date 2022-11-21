from itertools import permutations
from math import prod


def data():
    with open("input/2020/day_1", "r") as file:
        return[int(line) for line in file.readlines()]


def calculate(combinations):
    for item in permutations(data(), combinations):
        if sum(item) == 2020:
            print(prod(item))
            break


calculate(2)
calculate(3)