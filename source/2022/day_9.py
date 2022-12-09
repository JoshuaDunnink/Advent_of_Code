def get_moves():
    with open("input/2022/day_9", "r") as file:
        return [line.strip("\n").split(" ") for line in file]


class Rope_Section:
    def __init__(self, position: tuple, leader: "Rope_Section" = None) -> None:
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
                self.position = (x, y + steps)
            case "D":
                self.position = (x, y - steps)
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
        H=2,3    H=2,2    H=2,2
        T=2,2    T=2,4    T=2,3
        D=0,1    D=0,2    D=0,1
        """
        delta_x = self.leader.position[self.x] - self.position[self.x]
        delta_y = self.leader.position[self.y] - self.position[self.y]

        # diagonal delta
        if abs(delta_x) + abs(delta_y) > 2:
            if abs(delta_x) == 2:
                return [delta_x / 2, delta_y]
            elif abs(delta_y) == 2:
                return [delta_x, delta_y / 2]

        # horizontal delta
        elif delta_x == 0 and abs(delta_y) > 1:
            return [0, int(delta_y / 2)]

        # vertical delta
        elif abs(delta_x) > 1 and delta_y == 0:
            return [int(delta_x) / 2, 0]

        # leader still close
        else:
            return [0, 0]

    def follow(self):
        delta = self.get_delta()
        x = self.position[self.x] + delta[self.x]
        y = self.position[self.y] + delta[self.y]
        self.position = (int(x), int(y))
        self.has_been.add(self.position)


def part_1():
    head = Rope_Section(position=(0, 0))
    tail = Rope_Section(position=head.position, leader=head)
    for move in get_moves():
        for _ in range(0, int(move[1])):
            head.move(direction=move[0])
            tail.follow()
    print(tail.get_count_unique_locations())


def part_2():
    head = Rope_Section(position=(0, 0))
    tails = []
    for num in range(0, 9):
        if num == 0:
            tails.append(Rope_Section(position=head.position, leader=head))
        else:
            tails.append(
                Rope_Section(position=head.position, leader=tails[num - 1])
            )

    for move in get_moves():
        for _ in range(0, int(move[1])):
            head.move(direction=move[0])
            [tail.follow() for tail in tails]

    print(tails[0].get_count_unique_locations())


part_1()
part_2()
