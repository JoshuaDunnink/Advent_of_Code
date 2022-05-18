"""takeaway
https://adventofcode.com/2015/day/16

question was not concrete
What did they expect?
"""

characteristics = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def get_input() -> dict:
    with open("input/2015/day_16", "r") as file:
        data = {}
        for line in file.readlines():
            line = line.strip("\n").replace(":", "").replace(",", "").split()
            data[(line[1])] = {
                line[2]: int(line[3]),
                line[4]: int(line[5]),
                line[6]: int(line[7]),
            }
    return data


def could_match_1(data: dict) -> bool:
    return all(characteristics[k] == v for k, v in data.items())


def could_match_2(data: dict) -> bool:
    matches = []
    for k, v in data.items():
        if k == "cats" or k == "trees":
            matches.append(v > characteristics[k])
        if k == "pomeranians" or k == "goldfish":
            matches.append(v < characteristics[k])
        else:
            matches.append(v == characteristics[k])
    return all(matches)


data = get_input()
for aunt, line in data.items():
    if could_match_1(line):
        print(aunt)
    if could_match_2(line):
        print(aunt)
