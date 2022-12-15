def get_instructions():
    with open("input/2022/day_10", "r") as file:
        return [line.strip("\n").split(" ") for line in file.readlines()]


def sprite_is_in_range(cycle, list_of_values):
    x = sum(list_of_values)
    location = cycle % 40
    return location in range(x - 1, x + 2)


list_of_values = [1]
list_of_strength = []
cycle = 1
instructions = get_instructions()
image = [["." for _ in range(0, 40)] for _ in range(0, 6)]

for instruction in instructions:
    if instruction[0] == "noop":
        list_of_values.append(0)
        if sprite_is_in_range(cycle, list_of_values):
            row_n = cycle // 40
            columns = cycle % 40
            image[row_n][columns] = "#"
        cycle += 1
        if cycle == 20 or (cycle - 20) % 40 == 0:
            list_of_strength.append(cycle * sum(list_of_values))
    else:
        for index in range(0, 2):
            if index == 0:
                if sprite_is_in_range(cycle, list_of_values):
                    row_n = cycle // 40
                    columns = cycle % 40
                    image[row_n][columns] = "#"
                cycle += 1
                if cycle == 20 or (cycle - 20) % 40 == 0:
                    list_of_strength.append(cycle * sum(list_of_values))
            else:
                list_of_values.append(int(instruction[1]))
                if sprite_is_in_range(cycle, list_of_values):
                    row_n = cycle // 40
                    columns = cycle % 40
                    image[row_n][columns] = "#"
                cycle += 1
                if cycle == 20 or (cycle - 20) % 40 == 0:
                    list_of_strength.append(cycle * sum(list_of_values))

[print("".join(line)) for line in image]
print(sum(list_of_strength))
