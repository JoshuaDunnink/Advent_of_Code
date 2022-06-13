import numpy as np


def read_input() -> list:
    with open("input/2015/day_18") as f:
        data = [list(line.strip("\n")) for line in f.readlines()]
    return data


class LightShow:
    def __init__(
        self,
        input=read_input(),
        iterations: int = 100,
        show=False,
    ) -> None:
        self.input = input
        self.iterations = iterations
        self.grid = self.get_starting_grid()
        for _ in range(iterations + 2):
            if show:
                print(self.grid)
            print(f"{(self.grid == 1).sum()}")
            self.next_state()

    def get_starting_grid(
        self,
    ) -> np.array:
        dimensions = (
            len(self.input),
            len(self.input[0]),
        )
        grid = np.zeros(
            dimensions,
            dtype=int,
        )
        for (
            line_number,
            line,
        ) in enumerate(self.input):
            for (
                light_number,
                state,
            ) in enumerate(line):
                if state == "#":
                    grid[line_number][light_number] = 1
        return grid

    def next_state(
        self,
    ):
        previous_line = []
        next_line = []
        new_grid = self.grid.copy()
        self.line_length = len(self.grid[0]) - 1

        for (
            line_number,
            current_line,
        ) in enumerate(self.grid):
            if line_number < len(self.grid) - 1:
                next_line = list(self.grid[line_number + 1])
            else:
                next_line = []

            for (
                light_number,
                light_state,
            ) in enumerate(current_line):
                surrounding_state = []
                if line_number == 0:
                    match light_number:
                        case 0:
                            surrounding_state.append(
                                current_line[light_number + 1]
                            )
                            surrounding_state.extend(
                                next_line[: light_number + 2]
                            )
                        case self.line_length:
                            surrounding_state.append(
                                current_line[light_number - 1]
                            )
                            surrounding_state.extend(
                                next_line[len(current_line) - 2 :]
                            )
                        case _:
                            surrounding_state.append(
                                current_line[light_number - 1]
                            )
                            surrounding_state.append(
                                current_line[light_number + 1]
                            )
                            surrounding_state.extend(
                                next_line[light_number - 1 : light_number + 2]
                            )

                elif line_number == len(self.grid) - 1:
                    match light_number:
                        case 0:
                            surrounding_state.extend(
                                previous_line[: light_number + 2]
                            )
                            surrounding_state.extend(
                                [int(current_line[light_number + 1])]
                            )
                        case self.line_length:
                            surrounding_state.append(
                                list(previous_line[len(current_line) - 2 :])
                            )
                            surrounding_state.extend(
                                [int(current_line[light_number - 2])]
                            )
                        case _:
                            surrounding_state.extend(
                                list(
                                    previous_line[
                                        light_number - 1 : light_number + 2
                                    ]
                                )
                            )
                            surrounding_state.extend(
                                [current_line[light_number + 1]]
                            )
                            surrounding_state.extend(
                                [current_line[light_number - 1]]
                            )

                else:
                    match light_number:
                        case 0:
                            surrounding_state.extend(
                                list(previous_line[: light_number + 2])
                            )
                            surrounding_state.extend(
                                [current_line[light_number + 1]]
                            )
                            surrounding_state.extend(
                                next_line[: light_number + 2]
                            )
                        case self.line_length:
                            surrounding_state.extend(
                                list(previous_line[len(current_line) - 2 :])
                            )
                            surrounding_state.extend(
                                [current_line[light_number - 1]]
                            )
                            surrounding_state.extend(
                                next_line[len(current_line) - 2 :]
                            )
                        case _:
                            surrounding_state.extend(
                                list(
                                    previous_line[
                                        light_number - 1 : light_number + 2
                                    ]
                                )
                            )
                            surrounding_state.extend(
                                [current_line[light_number + 1]]
                            )
                            surrounding_state.extend(
                                [current_line[light_number - 1]]
                            )
                            surrounding_state.extend(
                                next_line[light_number - 1 : light_number + 2]
                            )

                if light_state == 1:
                    if not (
                        surrounding_state.count(1) == 2
                        or surrounding_state.count(1) == 3
                    ):
                        new_grid[line_number][light_number] = 0
                elif int(light_state) == 0 and surrounding_state.count(1) == 3:
                    new_grid[line_number][light_number] = 1

            previous_line = current_line

        self.grid = new_grid


LightShow()
