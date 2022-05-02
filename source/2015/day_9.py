"""lessons learned use permutations for combination exploring"""


from itertools import permutations


def get_raw_data():
    with open("input/2015/day_9", "r") as file:
        return file.readlines()


class Traveler:
    def __init__(self):
        self.data = get_raw_data()
        self.cities = set()
        self.distance_from_to = []
        self.optional_distances = []
        self.process_raw_data()

    def process_raw_data(self):
        for line in self.data:
            listed_line = line.strip("\n").split(" ")
            self.cities.add(listed_line[0])
            self.cities.add(listed_line[2])
            self.options = permutations(self.cities)
            self.distance_from_to.append(
                [listed_line[0], listed_line[2], int(listed_line[4])]
            )
            self.distance_from_to.append(
                [listed_line[2], listed_line[0], int(listed_line[4])]
            )

    def begin_journey(self):
        for route in self.options:
            distance = 0
            self.traveled_cities = self.cities.copy()
            for index, city in enumerate(route):
                self.traveled_cities.remove(city)
                if not index == len(route) - 1:
                    distance += self.get_distance(city, route[index + 1])
            self.optional_distances.append(distance)
        print(max(self.optional_distances))

    def get_distance(self, start, destination):
        for path in self.distance_from_to:
            if path[0] == start and path[1] == destination:
                return path[2]


Traveler().begin_journey()
