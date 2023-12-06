tst_input = {"Time": [7, 15, 30], "Distance": [9, 40, 200]}
input = {"Time": [34, 90, 89, 86], "Distance": [204, 1713, 1210, 1780]}

times = [34908986]
distance = [204171312101780]


def power(list):
    result = 1
    for x in list:
        result = result * x
    return result


total_wins = []
for index, time in enumerate(times):
    winning = 0
    for action in range(time):
        travelled = action * (time - action)
        if travelled > distance[index]:
            winning += 1
    total_wins.append(winning)

print("part_1: " + str(power(total_wins)))
print("part_2: " + str(total_wins))
