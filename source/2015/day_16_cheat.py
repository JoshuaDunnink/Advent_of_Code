def check(types, value):
    value = int(value)
    if types == "cats:" or types == "trees:":
        return props[types] < value
    elif types == "pomeranians:" or types == "goldfish:":
        return props[types] > value
    return props[types] == value

props = {}

g = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""

g = g.split("\n")
for line in g:
    line = line.strip("\n").split(" ")
    props[line[0]] = int(line[1])

with open("input/2015/day_16") as f:
    for line in f:
        line = line.strip("\n").split(" ")
        if (check(line[2], line[3].strip(",")) and check(line[4], line[5].strip(",")) and check(line[6], line[7])):
            print(line)
