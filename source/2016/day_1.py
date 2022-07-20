def get_data():
    with open("input/2016/day_1", "r") as input:
        return [
            instruction.strip("\n").strip(" ")
            for instruction in input.read().split(",")
        ]


class GoTheDistance:
    def __init__(self, instructions: list) -> None:
        self.direction = 0
        self.position = [0, 0]
        self.visited = []
        self.instructions = instructions
        self.take_instructions()

    def take_instructions(self):
        for instruction in self.instructions:
            match instruction[0]:
                case "R":
                    if self.direction < 3:
                        self.direction += 1
                    else:
                        self.direction = 0
                case "L":
                    if self.direction > 0:
                        self.direction -= 1
                    else:
                        self.direction = 3
            self.make_steps(instruction)
            if self.check_locations():
                break

    def make_steps(self, instruction):
        steps = int(instruction[1:])
        match self.direction:
            case 0:
                for _ in range(steps):
                    self.position[0] += 1
                    self.visited.append(self.position[:])
            case 1:
                for _ in range(steps):
                    self.position[1] += 1
                    self.visited.append(self.position[:])
            case 2:
                for _ in range(steps):
                    self.position[0] -= 1
                    self.visited.append(self.position[:])
            case 3:
                for _ in range(steps):
                    self.position[1] -= 1
                    self.visited.append(self.position[:])

    def check_locations(self):
        for step in self.visited:
            if self.visited.count(step) == 2:
                print(abs(step[0]) + abs(step[1]))
                return True


data = get_data()
GoTheDistance(data)
