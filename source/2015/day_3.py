def read_input():
    with open("input/2015/day_3") as f:
        data = f.read()
        data.strip("\n")
    return data


class Sled():
    def __init__(self, directions) -> None:
        self.directions = list(directions)
        self.dropoff_locations = {"00":1}
        self.coordinates = [0, 0]
        self.x = 0
        self.y = 0

    def visit_houses(self):
        for direction in self.directions:
            match direction:
                case "^":
                    self.y += 1
                case "v":
                    self.y -= 1.
                case ">":
                    self.x += 1
                case "<":
                    self.x -= 1
            self.drop_present((self.x, self.y))

    def drop_present(self, location):
        coordinate = str(int(location[0]))+str(int(location[1]))
        if self.dropoff_locations.get(coordinate):
            self.dropoff_locations[coordinate] += 1
        else:
            self.dropoff_locations[coordinate] = 1

    def report_number_delivered_houses(self):
        print(len(self.dropoff_locations))


def main():
    directions = (read_input())
    santa = Sled(directions)
    santa.visit_houses()
    santa.report_number_delivered_houses()

main()
