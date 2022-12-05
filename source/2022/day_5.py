"""
starting positions

            [L] [M]         [M]    
        [D] [R] [Z]         [C] [L]
        [C] [S] [T] [G]     [V] [M]
[R]     [L] [Q] [B] [B]     [D] [F]
[H] [B] [G] [D] [Q] [Z]     [T] [J]
[M] [J] [H] [M] [P] [S] [V] [L] [N]
[P] [C] [N] [T] [S] [F] [R] [G] [Q]
[Z] [P] [S] [F] [F] [T] [N] [P] [W]
 1   2   3   4   5   6   7   8   9 


instructions:
move 7 from 3 to 9
"""

test_layout = {
    1: "NZ",
    2: "DCM",
    3: "P",
}

container_layout = {
    1: "RHMPZ",
    2: "BJCP",
    3: "DCLGHNS",
    4: "LRSQDMTF",
    5: "MZTBQPSF",
    6: "GBZSFT",
    7: "VRN",
    8: "MCVDTLGP",
    9: "LMFJNQW",
}


def instructions():
    with open("input/2022/day_5", "r") as file:
        raw_lines = [line.strip("\n") for line in file.readlines()]
        lines = []
        for line in raw_lines:
            lines.append(
                [
                    int(char)
                    for index, char in enumerate(line.split(" "))
                    if index in range(1, 6, 2)
                ]
            )
        return lines


# container_layout = test_layout


def move(containers, crane):
    for instruction in instructions():
        pick_order = instruction[0]
        source = instruction[1]
        target = instruction[2]

        pick_up = containers[source][:pick_order]

        if len(containers[source]) - pick_order == 0:
            containers[source] = ""
        else:
            containers[source] = containers[source][
                -(len(containers[source]) - pick_order) :
            ]

        if crane == 9000:
            put_down_order = pick_up[::-1]
        else:
            put_down_order = pick_up

        containers[target] = put_down_order + containers[target]

    upper_row = []
    for items in containers.values():
        upper_row.append(items[0])

    print("".join(upper_row))


move(container_layout, 9000)
move(container_layout, 9001)
