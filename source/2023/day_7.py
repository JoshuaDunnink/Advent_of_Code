from collections import defaultdict
from functools import cmp_to_key


def data():
    with open("input/2023/day_7", "r") as file:
        return file.readlines()


POINTS = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
}

HAND_RANKS = {
    (5,): 7,
    (4, 1): 6,
    (3, 2): 5,
    (3, 1, 1): 4,
    (2, 2, 1): 3,
    (2, 1, 1, 1): 2,
    (1, 1, 1, 1, 1): 1,
}

test_input = [
    "32T3K 765",
    "T55J5 684",
    "KK677 28",
    "KTJJT 220",
    "QQQJA 483",
]


def reverse_hand_rank(cards) -> dict:
    reverse = {}
    for key, value in cards.items():
        if reverse.get(value, {}):
            reverse[value].append(key)
        else:
            reverse.update({value: [key]})
    return reverse


def replace_jokers(cards):
    jokers = cards["J"]
    cards["J"] -= jokers
    reversed_cards = reverse_hand_rank(cards)
    max_occurances = max(reversed_cards.keys())
    count_max = len(reversed_cards[max_occurances])
    if count_max == 1:
        card = reversed_cards.get(max_occurances)[0]
        cards[card] += jokers
    elif count_max > 1:
        multiple = {
            POINTS.get(item): item
            for item in reversed_cards.get(max_occurances)
        }
        cards[multiple[max(multiple.keys())]] += jokers
    return {key: val for key, val in cards.items() if val}


def determine_hand_rank(hand):
    cards = defaultdict(int)
    for card in hand:
        if cards.get(card, {}):
            cards[card] += 1
        else:
            cards.update({card: 1})

    if "J" in cards.keys():
        cards = replace_jokers(cards)

    return HAND_RANKS.get(tuple(sorted(cards.values(), reverse=True)))


def determine_game_hand_ranks(str_input):
    full_game = {}
    for line in str_input:
        hand, bid = line.strip("\n").split(" ")
        hand_rank = determine_hand_rank(hand)
        full_game.update({hand: (bid, hand_rank)})
    return full_game


def sorting_logic(a: str, b: str):
    POINTS = {
        "A": 13,
        "K": 12,
        "Q": 11,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2,
        "J": 1,
    }
    for index, _ in enumerate(a):
        if POINTS.get(a[index]) == POINTS.get(b[index]):
            continue
        elif POINTS.get(a[index]) > POINTS.get(b[index]):
            return 1
        elif POINTS.get(a[index]) < POINTS.get(b[index]):
            return -1


def determine_rank(input):
    hands = determine_game_hand_ranks(input)
    sorted_scores = []
    rank_list = {
        7: [],
        6: [],
        5: [],
        4: [],
        3: [],
        2: [],
        1: [],
    }
    for hand, (bid, rank) in hands.items():
        rank_list[rank].append(hand)
    # for rank in range(7,0, -1):
    for rank in range(1, 8, 1):
        sorted_scores += sorted(
            rank_list.get(rank), key=cmp_to_key(sorting_logic)
        )
    return sorted_scores, hands


def get_winning_totals():
    sorted_hands, hands = determine_rank(data())
    totals = 0
    for index, rank in enumerate(sorted_hands):
        totals += (index + 1) * (int(hands.get(rank)[0]))
    print(totals)


get_winning_totals()
