def get_data():
    with open("input/2023/day_4", "r") as file:
        return file.readlines()


def determine_points(winning, have):
    hits = 0
    for num in have:
        if num in winning:
            if hits == 0:
                hits += 1
            else:
                hits *= 2
    return hits


def part_1():
    points = 0
    for line in get_data():
        card_winning, have = line.strip().split("|")
        have = have.replace("  ", " ").strip()
        have = [int(num) for num in have.split(" ")]

        card, winning = card_winning.strip().split(":")
        winning = winning.replace("  ", " ").strip()
        winning = [int(num) for num in winning.split(" ")]

        points += determine_points(winning, have)
    print(points)


class NumberOfCards:
    def __init__(self, data):
        self.data = data
        self.max_cards = len(data)
        self.cards = {}

        self.setup()
        self.add_up_winnings()
        print(self.sum_of_cards())

    def setup(self):
        for line in get_data():
            card_winning, have = line.strip().split("|")
            card, winning = card_winning.strip().split(":")
            _, card_number = card.split()
            winning = winning.replace("  ", " ").strip()
            winning = [int(num) for num in winning.split(" ")]

            have = have.replace("  ", " ").strip()
            have = [int(num) for num in have.split(" ")]

            hits = self.determine_hits(winning, have)
            self.cards.update({int(card_number): {"hits": hits, "count": 1}})

    def add_up_winnings(self):
        for card_id, details in self.cards.items():
            hits = details.get("hits")
            count = details.get("count")

            for _ in range(count):
                for hit in range(1, hits + 1):
                    if hit <= self.max_cards:
                        self.cards[int(card_id) + int(hit)]["count"] += 1

    @staticmethod
    def determine_hits(winning, have):
        hits = 0
        for num in have:
            if num in winning:
                hits += 1
        return hits

    def sum_of_cards(self):
        sum_of_cards = 0
        for value in self.cards.values():
            sum_of_cards += value["count"]
        return sum_of_cards


def part_2():
    NumberOfCards(get_data())


part_2()
