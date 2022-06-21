cost, damage, armor, health = (0, 1, 2, 3)
weapons = {
    "Dagger": [8, 4, 0],
    "Shortsword": [10, 5, 0],
    "Warhammer": [25, 6, 0],
    "Longsword": [40, 7, 0],
    "Greataxe": [74, 8, 0],
}
armors = {
    "Nothing": [0, 0, 0],
    "Leather": [13, 0, 1],
    "Chainmail": [31, 0, 2],
    "Splintmail": [53, 0, 3],
    "Bandedmail": [75, 0, 4],
    "Platemail": [102, 0, 5],
}
rings = {
    "R": [0, 0, 0],
    "L": [0, 0, 0],
    "R1": [25, 1, 0],
    "R2": [50, 2, 0],
    "R3": [100, 3, 0],
    "R4": [20, 0, 1],
    "R5": [40, 0, 2],
    "R6": [80, 0, 3],
}


def get(item, value):
    if item in weapons.keys():
        return weapons.get(item)[value]
    elif item in armors.keys():
        return armors.get(item)[value]
    elif item in rings.keys():
        return rings.get(item)[value]


def create_options():
    options = []
    for weapon in weapons.keys():
        for thing in armors.keys():
            for ring_1 in rings.keys():
                for ring_2 in rings.keys():
                    if ring_2 != ring_1:
                        options.append([weapon, thing, ring_1, ring_2])
    return options


def get_player_options(options):
    player_equipment = {"default": [0, 1, 0, 100]}
    for index, option in enumerate(options):
        combined_cost = 0
        combined_damage = 0
        combined_armor = 0
        for equipment in option:
            combined_cost += get(equipment, cost)
            combined_damage += get(equipment, damage)
            combined_armor += get(equipment, armor)
        player_equipment.update(
            {index: [combined_cost, combined_damage, combined_armor, 100]}
        )
    return player_equipment


def play_game_min(player):
    boss = [0, 8, 2, 100]
    while boss[health] > 0 and player[health] > 0:
        player_damage = player[damage] - boss[armor]
        if player_damage - boss[armor] <= 0:
            player_damage = 1
        boss[health] -= player_damage
        player[health] -= boss[damage] - player[armor]
        if boss[health] <= 0 and player[health] >= 0:
            return player[cost]
        elif boss[health] >= 0 and player[health] <= 0:
            return None


def play_game_max(player):
    boss = [0, 8, 2, 100]
    while boss[health] > 0 and player[health] > 0:
        player_damage = player[damage] - boss[armor]
        if player_damage - boss[armor] <= 0:
            player_damage = 1
        boss[health] -= player_damage
        player[health] -= boss[damage] - player[armor]
        if boss[health] <= 0 and player[health] >= 0:
            return None
        elif boss[health] >= 0 and player[health] <= 0:
            return player[cost]


def main_1():
    cost_to_win = []
    player_tries = get_player_options(create_options())

    for attempt in player_tries.values():
        cost_to_win.append(play_game_min(attempt))
    cost_to_win = [value for value in cost_to_win if value]
    print(min(cost_to_win))


def main_2():
    cost_to_win = []
    player_tries = get_player_options(create_options())

    for attempt in player_tries.values():
        cost_to_win.append(play_game_max(attempt))
    cost_to_win = [value for value in cost_to_win if value]
    print(max(cost_to_win))


main_1()
main_2()
