from collections import deque

"""start list
    if present at day, number -1
    if 0 -> 6 and new 8

"""


def read_file():
    with open("input/day_6") as file:
        data = [int(num) for num in file.read().split(',')]
    return data


def next_day(init_fish):
    new_fish = 0
    for id, timer in enumerate(init_fish):
        if timer != 0:
            init_fish[id] -= 1
        if timer == 0:
            init_fish[id] = 6
            new_fish += 1

    for _ in range(new_fish):
        init_fish.append(8)

    return init_fish


# fish = read_file()
# for i in range(256):
#     next_fish = next_day(fish)
#     print(len(next_fish))


fish = read_file()

def AOC_day6_pt1_and_pt2(days):
    totals = deque(fish.count(i) for i in range(9))
    for _ in range(days):
        totals.rotate(-1)
        totals[6] += totals[8]
    return sum(totals)

print(AOC_day6_pt1_and_pt2(80))
print(AOC_day6_pt1_and_pt2(256))