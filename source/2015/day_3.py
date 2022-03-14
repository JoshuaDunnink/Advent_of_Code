def read_input():
    with open("input/2015/day_3") as f:
        data = f.read()
        data.strip("\n")
    return data


class Sled():
    def __init__(self, directions) -> None:
        self.directions = list(directions)
        self.x = 0
        self.y = 0
        self.santa = [0, 0]
        self.robot = [0, 0]
        self.santa_drop_list = {"00": 1}
        self.robot_drop_list = {"00": 1}
        self.dropoff_locations = {"0,0"}
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
        coordinate = str(int(location[0]))+","+str(int(location[1]))
        self.dropoff_locations.add(coordinate)
        if self.dropoff_locations_dict.get(coordinate):
            self.dropoff_locations_dict[coordinate] += 1
        else:
            self.dropoff_locations_dict[coordinate] = 1

    def report_number_delivered_houses(self):
        print(len(self.dropoff_locations))
        print(len(self.dropoff_locations_dict))


def main():
    directions = (read_input())
    santa = Sled(directions)
    santa.visit_houses()
    santa.report_number_delivered_houses()


main()
