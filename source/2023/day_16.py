from helpers import timing


def data():
    with open("input/2023/day_16", "r") as file:
        return [
            [char for char in line.strip()] for line in file.read().split("\n")
        ]


class BeamTracer:
    def __init__(self):
        self.energised_cells = set()
        self.grid = data()

    @timing
    def part_1(self, start=[(0, 0, "R")]):
        self.start_location = start
        self.trace_beam(tuple(self.start_location))
        print(self.get_energized_count())

    @timing
    def part_2(self):
        numbers = []
        for start in self.edges():
            self.energised_cells = set()
            self.trace_beam(tuple(start))
            numbers.append(self.get_energized_count())
        print(max(numbers))

    def edges(self):
        edges = []
        max_y = len(self.grid)
        max_x = len(self.grid[0])
        for i in range(max_x):
            edges.append([(0, i, "D")])
            edges.append([(max_y, i, "U")])
        for i in range(len(self.grid)):
            edges.append([(i, 0, "R")])
            edges.append([(i, max_x, "L")])
        return edges

    def get_energized_count(self):
        real_energy = set()
        for y, x, _ in self.energised_cells:
            real_energy.add((y, x))
        return len(real_energy)

    def trace_beam(self, locations):
        new_locations = []
        for y, x, direction in locations:
            # self.trace_grid = data()
            # self.trace_grid[y][x] = "#"
            self.energised_cells.add((y, x, direction))
            match direction:
                case "R":
                    new_y, new_x = (y, x + 1)
                case "L":
                    new_y, new_x = (y, x - 1)
                case "U":
                    new_y, new_x = (y - 1, x)
                case "D":
                    new_y, new_x = (y + 1, x)
            if 0 <= new_y < len(self.grid) and 0 <= new_x < len(self.grid[0]):
                new_directions = self.get_next_instruction(
                    new_y, new_x, direction
                )
                for new_direction in new_directions:
                    if (
                        new_y,
                        new_x,
                        new_direction,
                    ) not in self.energised_cells:
                        new_locations.append((new_y, new_x, new_direction))
        if new_locations:
            self.trace_beam(tuple(new_locations))

    def get_next_instruction(self, y, x, direction):
        match self.grid[y][x]:
            case ".":
                return direction
            case "\\":
                return list(self.match_backslash(direction))
            case "/":
                return list(self.match_forwardslash(direction))
            case "-":
                return list(self.match_hyphen(direction))
            case "|":
                return list(self.match_pipe(direction))

    @staticmethod
    def match_backslash(direction):
        match direction:
            case "R":
                return "D"
            case "L":
                return "U"
            case "U":
                return "L"
            case "D":
                return "R"

    @staticmethod
    def match_forwardslash(direction):
        match direction:
            case "R":
                return "U"
            case "L":
                return "D"
            case "U":
                return "R"
            case "D":
                return "L"

    @staticmethod
    def match_hyphen(direction):
        match direction:
            case "R":
                return "R"
            case "L":
                return "L"
            case "U":
                return "R", "L"
            case "D":
                return "R", "L"

    @staticmethod
    def match_pipe(direction):
        match direction:
            case "R":
                return "U", "D"
            case "L":
                return "U", "D"
            case "U":
                return "U"
            case "D":
                return "D"


BeamTracer().part_2()
