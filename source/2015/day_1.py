def read_input():
    with open("input/2015/day_1") as f:
        data = f.readlines()
    return data


data = read_input()
count = 0
for line in data:
    for id, character in enumerate(line):
        if character == "(":
            count += 1
        else:
            count -= 1
        if count == -1:
            print(id+1)

print(count)