def get_instructions():
    with open("input/2022/day_10", "r") as file:
        return [line.strip("\n").split(" ") for line in file.readlines()]


list_of_values = [1]
list_of_strength = []
cycle_count = 1
instructions = get_instructions()

for instruction in instructions:
    if instruction[0] == 'noop':
        list_of_values.append(0)
        cycle_count += 1
        if cycle_count == 20 or (cycle_count - 20) % 40 == 0:
            list_of_strength.append(cycle_count * sum(list_of_values))
    else:
        for cycle in range(0, 2):
            if cycle == 0:
                cycle_count += 1
                if cycle_count == 20 or (cycle_count - 20) % 40 == 0:
                    list_of_strength.append(cycle_count * sum(list_of_values))
            else:
                list_of_values.append(int(instruction[1]))
                cycle_count += 1
                if cycle_count == 20 or (cycle_count - 20) % 40 == 0:
                    list_of_strength.append(cycle_count * sum(list_of_values))
print(sum(list_of_strength))