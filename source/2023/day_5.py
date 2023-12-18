from helpers import timing


def get_data():
    with open("input/2023/day_5_tst", "r") as file:
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
        location = []
        seed_ranges = [
            [start, range] for start, range in zip(self.seeds[0::2], self.seeds[1::2])
        ]
        for seed_range in seed_ranges:
            location.extend(self.perform_mappings([seed_range]))
        location

    def perform_mappings(self, seed_range: list):
        for mappings in self.maps.values():
            seed_range = self.perform_mapping(seed_range, mappings)
        return seed_range

    def perform_mapping(self, seed_range, mappings):
        for seeds in seed_range:
            for mapping in mappings:
                new = self.get_intervals(seeds, tuple(mapping))
                if new != seed_range:
                    print(seeds, new)
                    return new
            print(seed_range, seed_range)
            return seed_range

    @staticmethod
    def get_intervals(seed_range: tuple, mapping: tuple):
        shift = mapping[0] - mapping[1]
        seed_start = seed_range[0]
        seed_end = seed_range[0] + seed_range[1] - 1
        source_start = mapping[1]
        source_end = mapping[1] + mapping[2] - 1

        # seed   [---]
        # source    [-]
        if seed_start <= source_start and seed_end >= source_start:
            print(2)
            return [
                [seed_start, source_start - seed_start],
                [seed_start + shift, seed_end - source_start],
            ]
        # seed    [-]
        # source [---]
        elif seed_start >= source_start and source_end >= seed_end:
            print(3)
            return [[seed_start + shift, seed_range[1]]]
        # seed      [-]
        # source [----]
        elif seed_start >= source_start and seed_end <= source_end:
            print(4)
            return [[seed_start + shift, source_end - seed_start]]
        # seed       [-]
        # source [----]
        elif seed_start >= source_start and seed_end > source_end:
            print(5)
            return [
                [seed_start + shift, seed_end - source_end],
                [source_start, seed_end - source_end],
            ]
        # seed [---]       OR  seed      [---]
        # source    [-]        source [-]
        elif seed_end <= source_start or seed_start >= source_end:
            print(1)
            return [seed_range]

    @staticmethod
    def number_in_source(number, mappings):
        for mapping in mappings:
            if number > mapping[1] and number <= (mapping[1] + mapping[2]):
                distance = number - mapping[1]
                return mapping[0] + distance
        return number

    # def perform_mappings(self, seeds):
    #     for number in seeds:
    #         for key, mappings in self.maps.items():
    #             number = self.number_in_source(number, mappings)
    #         self.locations.append(number)

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

        self.seeds = [int(num) for num in seeds_str.split(":")[1].strip().split(" ")]
        self.maps.update({"seed_to_soil": self.unpack_numbers(seed_to_soil_str)})
        self.maps.update(
            {"soil_to_fertilizer": self.unpack_numbers(soil_to_fertilizer_str)}
        )
        self.maps.update(
            {"fertilizer_to_water": self.unpack_numbers(fertilizer_to_water_str)}
        )
        self.maps.update({"water_to_light": self.unpack_numbers(water_to_light_str)})
        self.maps.update({"light_to_temp": self.unpack_numbers(light_to_temp_str)})
        self.maps.update({"temp_to_humid": self.unpack_numbers(temp_to_humid_str)})
        self.maps.update({"humid_to_loc": self.unpack_numbers(humid_to_loc_str)})
        # self.generate_mappings()

    @staticmethod
    def unpack_numbers(data: str):
        split_data = data.split(":")[1].strip().split("\n")
        return_values = []
        for line in split_data:
            return_values.append([int(num) for num in line.strip().split(" ")])
        return return_values


Gardener().part_2()


# seeds, *maps = open("input/2023/day_5_tst").read().split("\n\n")
# seeds = [int(seed) for seed in seeds.split()[1:]]
# maps = [[list(map(int, line.split())) for line in m.splitlines()[1:]] for m in maps]

# locations = []
# for i in range(0, len(seeds), 2):
#     ranges = [[seeds[i], seeds[i + 1] + seeds[i]]]
#     results = []
#     for _map in maps:
#         while ranges:
#             start_range, end_range = ranges.pop()
#             for target, start_map, r in _map:
#                 end_map = start_map + r
#                 offset = target - start_map
#                 if end_map <= start_range or end_range <= start_map:  # no overlap
#                     continue
#                 if start_range < start_map:
#                     ranges.append([start_range, start_map])
#                     start_range = start_map
#                 if end_map < end_range:
#                     ranges.append([end_map, end_range])
#                     end_range = end_map
#                 results.append([start_range + offset, end_range + offset])
#                 break
#             else:
#                 results.append([start_range, end_range])
#         ranges = results
#         results = []
#     locations += ranges
# print(min(loc[0] for loc in locations))
