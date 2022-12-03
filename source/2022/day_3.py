import string


def data():
    with open("input/2022/day_3", "r") as file:
        return [line.strip("\n") for line in file.readlines()]


def get_score(character):
    if character.islower():
        return int(string.ascii_lowercase.index(character)) + 1
    else:
        return int(string.ascii_uppercase.index(character)) + 27


def get_score_three(packs):
    sets = [set(items) for items in packs]
    common = (sets[0] & sets[1]) & sets[2]
    return get_score(list(common)[0])


def get_score_split(pack):
    length = len(pack)
    first_compartement = set(pack[: int(length / 2)])
    second_compartement = set(pack[int(-length / 2) :])
    shared_item = list(first_compartement & second_compartement)[0]
    return get_score(shared_item)


def part_1():
    backpacks = data()
    score = 0
    for pack in backpacks:
        score += get_score_split(pack)
    print(score)


def part_2():
    score_common = 0
    set_of_packs = []
    counter = 0
    for pack in data():
        if counter == 2:
            set_of_packs.append(pack)
            score_common += get_score_three(set_of_packs)
            set_of_packs = []
            counter = 0
        else:
            set_of_packs.append(pack)
            counter += 1
    print(score_common)


part_1()
part_2()
