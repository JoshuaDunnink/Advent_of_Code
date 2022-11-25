def data():
    with open("input/2020/day_5", "r") as file:
        return file.readlines()


def determine_row(instructions):
    rows = [num for num in range(0, 128)]
    selection = []
    for instruction in instructions:
        if instruction == "F":
            selection = rows[: int(len(rows) / 2)]
        elif instruction == "B":
            selection = rows[int(len(rows) / 2) :]
        rows = selection
    return rows


def determine_column(instructions):
    columns = [num for num in range(0, 8)]
    selection = []
    for instruction in instructions:
        if instruction == "L":
            selection = columns[: int(len(columns) / 2)]
        elif instruction == "R":
            selection = columns[int(len(columns) / 2) :]
        columns = selection
    return columns


def part_1():
    seat_ids = []
    for seat in data():
        row = determine_row(seat[:7])
        column = determine_column(seat[7:])
        seat_ids.append((int(row[0]) * 8) + int(column[0]))

    print("highest seat ID: " + str(max(seat_ids)))
    return seat_ids


def part_2(seat_ids):
    unused_seats = []
    for id in range(0, 884):
        if id not in seat_ids:
            unused_seats.append(id)
    print("Seat ID " + str(max(unused_seats)) + " is empty")


part_2(part_1())
