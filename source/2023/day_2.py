def get_data():
    with open("input/2023/day_2", "r") as file:
        return file.readlines()


BAG_CONTENT = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def is_hand_possible(cubes_in_hand):
    possible = []
    for cubes in cubes_in_hand:
        number, color = cubes.strip().split(" ")
        possible.append(BAG_CONTENT.get(color) >= int(number))
    return all(possible)


def is_game_possible(hands):
    possible_game = []
    cubes_in_hand = []
    for hand in hands:
        cubes_in_hand = hand.split(",")
        possible_game.append(is_hand_possible(cubes_in_hand))
    return all(possible_game)


def get_fewest_cubes_required(hands_of_cubes):
    min_cubes = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    hands = hands_of_cubes.split(";")
    for hand in hands:
        cubes_in_hand = hand.split(",")
        for cubes in cubes_in_hand:
            number, color = cubes.strip().split(" ")
            if int(number) > min_cubes.get(color):
                min_cubes.update({color: int(number)})
    return min_cubes.values()


def part_1():
    data = get_data()
    possible_games = []
    for line in data:
        hands = []
        game, hands_of_cubes = line.split(":")
        hands = hands_of_cubes.split(";")
        if is_game_possible(hands):
            possible_games.append(int(game.split(" ")[1]))

    print("part one: " + str(sum(possible_games)))


def part_2():
    data = get_data()
    powers = []
    for line in data:
        _, hands_of_cubes = line.split(":")
        r, g, b = get_fewest_cubes_required(hands_of_cubes)
        powers.append(r * g * b)

    print("part two: " + str(sum(powers)))


part_2()
