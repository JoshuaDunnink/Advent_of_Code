from cgi import test


test_input = ["ULL", "RRDDD", "LURDL", "UUUUD"]


def get_data():
    with open("input/2016/day_2", "r") as file:
        return [line.strip("\n") for line in file]


def part_1():
    code = []
    cursor_part_1 = [1, 1]
    part_1_pad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    data = get_data()
    for item in data:
        for char in item:
            if char == "U" and cursor_part_1[0] >= 1:
                cursor_part_1[0] -= 1
            if char == "D" and cursor_part_1[0] <= 1:
                cursor_part_1[0] += 1
            if char == "L" and cursor_part_1[1] >= 1:
                cursor_part_1[1] -= 1
            if char == "R" and cursor_part_1[1] <= 1:
                cursor_part_1[1] += 1
        code.append(part_1_pad[cursor_part_1[0]][cursor_part_1[1]])
    print(code)


def part_2():
    code = []
    part_2_pad = [
        [0, 0, 1, 0, 0],
        [0, 2, 3, 4, 0],
        [5, 6, 7, 8, 9],
        [0, "A", "B", "C", 0],
        [0, 0, "D", 0, 0],
    ]
    cursor_part_2 = [2, 0]
    data = get_data()
    for item in data:
        for char in item:
            if (
                char == "U"
                and cursor_part_2[0] >= 1
                and part_2_pad[cursor_part_2[0] - 1][cursor_part_2[1]] != 0
            ):
                cursor_part_2[0] -= 1
            if (
                char == "D"
                and cursor_part_2[0] <= 3
                and part_2_pad[cursor_part_2[0] + 1][cursor_part_2[1]] != 0
            ):
                cursor_part_2[0] += 1
            if (
                char == "L"
                and cursor_part_2[1] >= 1
                and part_2_pad[cursor_part_2[0]][cursor_part_2[1] - 1] != 0
            ):
                cursor_part_2[1] -= 1
            if (
                char == "R"
                and cursor_part_2[1] <= 3
                and part_2_pad[cursor_part_2[0]][cursor_part_2[1] + 1] != 0
            ):
                cursor_part_2[1] += 1
        code.append(part_2_pad[cursor_part_2[0]][cursor_part_2[1]])
    print(code)


part_1()
part_2()
