"""https://adventofcode.com/2015/day/17
takeaway, another repetition with itertools
explanations still quite cryptic
"""
from itertools import combinations

numbers = "33 14 18 20 45 35 16 35 1 13 18 13 50 44 48 6 24 41 30 42"
containers = [int(val) for val in numbers.split(" ")]

eggnog = 150
options_1 = 0
options_2 = 0

for i in range(len(containers)):
    volume = 0
    for combination in combinations(containers, i):
        if sum(combination) == 150:
            options_1 += 1
    if options_1:
        break


print(options_1)
