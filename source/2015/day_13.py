from itertools import permutations


def get_data() -> dict:
    with open("input/2015/day_13", "r") as file:
        return file.readlines()


class SeatAranger:
    def __init__(self, data):
        self.participants = set()
        self.distribution = {}
        self.raw_data = data
        self.combined_happines = []

        self.load_participants_and_distribution()

    def load_participants_and_distribution(self):
        for line in self.raw_data:
            split_line = line.strip("\n").strip(".").split(" ")

            subject = split_line[0]
            effect = split_line[2]
            points = int(split_line[3])
            neighbor = split_line[-1]

            if effect == "gain":
                multiplier = 1
            else:
                multiplier = -1

            if subject not in self.participants:
                self.participants.add(subject)
                self.distribution.update(
                    {subject: {neighbor: multiplier * points}}
                )
            else:
                self.distribution[subject].update(
                    {neighbor: (multiplier * points)}
                )
        self.add_satan()

    def add_satan(self):
        self.distribution.update({"satan": {}})
        for participant in self.participants:
            self.distribution[participant].update({"satan": 0})
            self.distribution["satan"].update({participant: 0})

        self.participants.add("satan")

    def determine_options(self):
        options = permutations(self.participants)
        for option_list in options:
            happines = 0
            for index, participant in enumerate(option_list):
                if index == 0:
                    neighbor_1 = option_list[-1]
                    neighbor_2 = option_list[1]
                elif index == len(option_list) - 1:
                    neighbor_1 = option_list[index - 1]
                    neighbor_2 = option_list[0]
                else:
                    neighbor_1 = option_list[index - 1]
                    neighbor_2 = option_list[index + 1]

                happines += self.distribution[participant].get(neighbor_1)
                happines += self.distribution[participant].get(neighbor_2)

            self.combined_happines.append(happines)
        print(max(self.combined_happines))


SeatAranger(get_data()).determine_options()
