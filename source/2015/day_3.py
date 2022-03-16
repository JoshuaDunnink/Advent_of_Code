"""Importance of better writing down orderable items"""


def read_input():
    with open("input/2015/day_3") as f:
        data = f.read()
        data.strip("\n")
    return data


class Sled:
    def __init__(self, directions) -> None:
        self.directions = list(directions)
        self.x = 0
        self.y = 0
        self.santa = [0, 0]
        self.robot = [0, 0]
        self.santa_drop_list = {"00": 1}
        self.robot_drop_list = {"00": 1}
        self.dropoff_locations = {"0,0"}
        self.dropoff_locations_incorrect = {"00"}
        self.dropoff_locations_dict = {"0,0": 2}

    @staticmethod
    def update_coordinates(direction, mover):
        match direction:
            case "^":
                mover[1] += 1
            case "v":
                mover[1] -= 1
            case ">":
                mover[0] += 1
            case "<":
                mover[0] -= 1

    def visit_houses(self):
        for index, direction in enumerate(self.directions):
            if index % 2:
                mover = self.robot
            else:
                mover = self.santa

            self.update_coordinates(direction, mover)
            self.drop_present(mover)

    def drop_present(self, location):
        coordinate_correct = (
            str(int(location[0])) + "," + str(int(location[1]))
        )
        # coordinate_incorrect = str(int(location[0])) + str(int(location[1]))

        self.dropoff_locations.add(coordinate_correct)
        # self.dropoff_locations_incorrect.add(coordinate_incorrect)

        # if len(self.dropoff_locations) != len(
        #     self.dropoff_locations_incorrect
        # ):
        #     raise ValueError(f"{coordinate_correct=} {coordinate_incorrect=}")

        if self.dropoff_locations_dict.get(coordinate_correct):
            self.dropoff_locations_dict[coordinate_correct] += 1
        else:
            self.dropoff_locations_dict[coordinate_correct] = 1

    def report_number_delivered_houses(self):
        print(f"{len(self.dropoff_locations)=}")
        print(f"{len(self.dropoff_locations_dict)=}")


def main():
    directions = read_input()
    santa = Sled(directions)
    santa.visit_houses()
    santa.report_number_delivered_houses()


main()
