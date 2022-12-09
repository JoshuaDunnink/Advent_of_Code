def get_moves():
    with open("input/2022/day_9", "r") as file:
        return [line.strip("\n").split(" ") for line in file]


class Rope_Section:
    def __init__(
        self, name, position: tuple, leader: "Rope_Section" = None
    ) -> None:
        self.name = name
        self.position = position
        self.has_been = {position}
        self.leader = leader
        self.x = 0
        self.y = 1

    def move(self, direction, steps=1):
        x = self.position[self.x]
        y = self.position[self.y]
        match direction:
            case "R":
                self.position = (x + steps, y)
            case "L":
                self.position = (x - steps, y)
            case "U":
                self.position = (x, y - steps)
            case "D":
                self.position = (x, y + steps)
        self.has_been.add(self.position)

    def get_position(self):
        return self.position

    def get_count_unique_locations(self):
        return len(self.has_been)

    def get_delta(self):
        """
        .....    .....    .....
        .....    ..H..    ..H..
        ..H.. -> ..... -> ..T..
        .T...    .T...    .....
        .....    .....    .....
        H=3,3    H=3,2    H=3,2
        T=2,4    T=2,4    T=3,3
        D=1,1    D=1,2    D=0,1

        .....    .....    .....
        .T...    .T...    .....
        .H... -> ..... -> .T...
        .....    .H...    .H...
        .....    .....    .....
        H=2,3    H=2,4    H=2,4
        T=2,2    T=2,2    T=2,3
        D=0,1    D=0,2    D=0,1
        """
        delta_x = self.leader.position[self.x] - self.position[self.x]
        delta_y = self.leader.position[self.y] - self.position[self.y]

        abs_x = abs(delta_x)
        abs_y = abs(delta_y)
        if abs_x > 1 or abs_y > 1:
            return (
                (0 if delta_x == 0 else delta_x // abs_x),
                (0 if delta_y == 0 else delta_y // abs_y),
            )
        else:
            return 0, 0

    def follow(self):
        delta = self.get_delta()
        x = self.position[self.x] + delta[self.x]
        y = self.position[self.y] + delta[self.y]
        self.position = (int(x), int(y))
        self.has_been.add(self.position)


def print_matrix(head, tails):
    x = []
    y = []
    x_max = 0
    y_max = 0

    for move in get_moves():
        match move[0]:
            case "U":
                y_max += int(move[1])
                y.append(y_max)
            case "D":
                y_max -= int(move[1])
                y.append(y_max)
            case "R":
                x_max += int(move[1])
                x.append(x_max)
            case "L":
                x_max -= int(move[1])
                x.append(x_max)

    biggest_x = max([abs(x) for x in x])
    biggest_y = max([abs(y) for y in y])
    min_x = min(x)
    min_y = min(y)

    row = ["." for _ in range(0, biggest_x * 2 + 1)]
    matrix = [row.copy() for _ in range(0, biggest_y * 2 + 1)]

    for tail in tails:
        matrix[tail.position[1] + min_x][tail.position[0] - min_y] = tail.name
    matrix[head.position[1] + min_x][head.position[0] - min_y] = head.name

    joined_matrix = []
    for line in matrix:
        joined_matrix.append("".join(line))

    for line in joined_matrix:
        print(line)


def part_1():
    head = Rope_Section(name="H", position=(0, 0))
    tail = Rope_Section(name="T", position=head.position, leader=head)
    for move in get_moves():
        for _ in range(0, int(move[1])):
            head.move(direction=move[0])
            tail.follow()
    print(tail.get_count_unique_locations())


def part_2():
    head = Rope_Section(name="H", position=(0, 0))
    tails = []
    for num in range(0, 9):
        if num == 0:
            tails.append(
                Rope_Section(name="1", position=head.position, leader=head)
            )
        else:
            tails.append(
                Rope_Section(
                    name=str(num + 1),
                    position=head.position,
                    leader=tails[num - 1],
                )
            )

    for move in get_moves():
        for _ in range(0, int(move[1])):
            head.move(direction=move[0])
            for tail in tails:
                tail.follow()

    print(tails[8].get_count_unique_locations())


part_1()
part_2()
