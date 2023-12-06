from helpers import timing


def get_data():
    with open("input/2023/day_5", "r") as file:
        return file.read()


(
    seeds_str,
    seed_to_soil_str,
    soil_to_fertilizer_str,
    fertilizer_to_water_str,
    water_to_light_str,
    light_to_temp_str,
    temp_to_humid_str,
    humid_to_loc_str,
) = get_data().split("\n\n")


class Gardener:
    def __init__(self):
        self.maps = {}
        self.expanded_maps = {}
        self.seeds = []
        self.locations = []
        self.setup()

    @timing
    def part_1(self):
        self.perform_mappings(self.seeds)
        print(min(self.locations))

    @timing
    def part_2(self):
        seeds = set()
        seeds_len = len(self.seeds)
        for i in range(seeds_len):
            if i % 2 == 0:
                seeds.update(
                    set(
                        [
                            num
                            for num in range(
                                self.seeds[i],
                                self.seeds[i + 1] + self.seeds[i],
                            )
                        ]
                    )
                )

        self.perform_mappings(seeds)
        print(min(self.locations))

    @staticmethod
    def number_in_source(number, mappings):
        for mapping in mappings:
            if number > mapping[1] and number <= (mapping[1] + mapping[2]):
                distance = number - mapping[1]
                return mapping[0] + distance
        return number

    def perform_mappings(self, seeds):
        for number in seeds:
            for key, mappings in self.maps.items():
                number = self.number_in_source(number, mappings)
            self.locations.append(number)

    def setup(self):
        (
            seeds_str,
            seed_to_soil_str,
            soil_to_fertilizer_str,
            fertilizer_to_water_str,
            water_to_light_str,
            light_to_temp_str,
            temp_to_humid_str,
            humid_to_loc_str,
        ) = get_data().split("\n\n")

        self.seeds = [
            int(num) for num in seeds_str.split(":")[1].strip().split(" ")
        ]
        self.maps.update(
            {"seed_to_soil": self.unpack_numbers(seed_to_soil_str)}
        )
        self.maps.update(
            {"soil_to_fertilizer": self.unpack_numbers(soil_to_fertilizer_str)}
        )
        self.maps.update(
            {
                "fertilizer_to_water": self.unpack_numbers(
                    fertilizer_to_water_str
                )
            }
        )
        self.maps.update(
            {"water_to_light": self.unpack_numbers(water_to_light_str)}
        )
        self.maps.update(
            {"light_to_temp": self.unpack_numbers(light_to_temp_str)}
        )
        self.maps.update(
            {"temp_to_humid": self.unpack_numbers(temp_to_humid_str)}
        )
        self.maps.update(
            {"humid_to_loc": self.unpack_numbers(humid_to_loc_str)}
        )
        # self.generate_mappings()

    @staticmethod
    def unpack_numbers(data: str):
        split_data = data.split(":")[1].strip().split("\n")
        return_values = []
        for line in split_data:
            return_values.append([int(num) for num in line.strip().split(" ")])
        return return_values


Gardener().part_2()
