import numpy as np


def read_input():
    with open("input/day_4") as movement:
        nums, *cards = movement.read().split("\n\n")
    return nums, cards


class Cards:
    def __init__(self, cards) -> None:
        self.input = read_input()[2:]
        self.list_of_cards = []
        self.cards = cards
        self.winning_board_count = 0
        self.create_cards()
        print(len(self.list_of_cards))

    def create_cards(self):
        for board in self.cards:
            rows = [[int(i) for i in row.split()] for row in board.split('\n')]
            card = ([set(row) for row in rows])
            card_transposed = ([set(col) for col in zip(*rows)])
            self.list_of_cards.append(Card(card))
            self.list_of_cards.append(Card(card_transposed))

    def draw_number(self, number):
        for id, card in enumerate(self.list_of_cards):
            if card.cross_number(number):
                self.winning_board_count += 1
                if self.winning_board_count == 200:
                    return card


class Card:
    def __init__(self, array) -> None:
        self.array: list = array

    def cross_number(self, number):
        if {number} in self.array:
            self.array = [row.difference({number}) for row in self.array]
            return True
        else:
            self.array = [row.difference({number}) for row in self.array]


def determine_sum(winning_card):
    numbers = []
    for row in winning_card.array:
        numbers.append(
            sum([number for number in row])
        )
    return sum(numbers)


numbers, cards = read_input()
play_bingo_with = Cards(cards)
i = 0
for number in [int(number) for number in numbers.split(',')]:
    winning_card = play_bingo_with.draw_number(int(number))
    final_number = number
    i += 1
    print(str(i))
    if winning_card:
        break


sum_of_nums = determine_sum(winning_card)
print(sum_of_nums * int(final_number))
