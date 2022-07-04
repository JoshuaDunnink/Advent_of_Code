"""
takeaway
always look for the smallest combination to match instead of brute force
"""

from itertools import combinations
from functools import reduce
from operator import mul


def get_data() -> dict:
    with open("input/2015/day_24", "r") as file:
        return [int(num.strip("\n")) for num in file]


def knapsacks(num_groups, weights):
    group_size = sum(weights) // num_groups
    for i in range(len(weights)):
        qes = [
                reduce(mul, c) for c in combinations(weights, i)
                if sum(c) == group_size
            ]
        if qes:
            return min(qes)


data = get_data()
print(knapsacks(4, data))
