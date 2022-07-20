"""_summary_
takeaway
list(zip(*input)) wil transpose a table
"""


def get_data():
    with open("input/2016/day_3", "r") as file:
        return [
            [int(num) for num in line.strip("\n").split()] for line in file
        ]


def can_be_triangle(sides: list):
    sides.sort()
    return sides[0] + sides[1] > sides[2]


def pt_1(input):
    counter = 0
    for sides in input:
        if can_be_triangle(sides):
            counter += 1
    print(counter)


def pt_2(transposed):
    counter = 0
    for line in transposed:
        index = 0
        while index + 3 <= len(line):
            counter += can_be_triangle(list(line[index : index + 3]))
            index += 3
    print(counter)


input = get_data()
transposed = list(zip(*input))

pt_1(input)
pt_2(transposed)
