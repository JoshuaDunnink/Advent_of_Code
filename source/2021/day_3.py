def read_input():
    with open("input/day_3") as movement:
        results = movement.readlines()
    return results


def determine_gamma_epsilon(list):
    one = list.count(1)
    zero = list.count(0)

    if one > zero:
        return "1", "0"
    else:
        return "0", "1"


def get_power_consumption():
    lines = read_input()
    column_length = len(lines[0].strip("\n"))
    bin_gamma = ""
    bin_epsilon = ""

    for column in range(column_length):
        temp_container = []
        for line in lines:
            temp_container.append(int(line[column]))
        gamma, epsilon = determine_gamma_epsilon(temp_container)
        bin_gamma = bin_gamma + gamma
        bin_epsilon = bin_epsilon + epsilon

    gamma_rate = int(bin_gamma, 2)
    epsilon_rate = int(bin_epsilon, 2)
    power_consumption = gamma_rate * epsilon_rate

    return power_consumption


def get_most_common(list):
    one = list.count(1)
    zero = list.count(0)

    if one > zero:
        return 1
    elif one == zero:
        return 1
    else:
        return 0


def get_least_common(list):
    one = list.count(1)
    zero = list.count(0)

    if one > zero:
        return 0
    elif one == zero:
        return 0
    else:
        return 1


def get_bit_from_columns(lines, column):
    temp_container = []
    for line in lines:
        temp_container.append(int(line[column]))
    return temp_container


def select_common_lines(lines, selector, column):
    common_lines = []
    for line in lines:
        if int(line[column]) == selector:
            common_lines.append(line)
    return common_lines


def get_oxygen_rating():
    lines = read_input()
    column_length = len(lines[0].strip("\n"))
    column = 0

    for column in range(column_length):
        temp_container = get_bit_from_columns(lines, column)
        common = get_most_common(temp_container)
        common_lines = select_common_lines(lines, common, column)
        lines = common_lines
        if len(lines) == 1:
            return int(lines[0].strip("\n"), 2)


def get_co2_rating():
    lines = read_input()
    column_length = len(lines[0].strip("\n"))
    column = 0

    for column in range(column_length):
        temp_container = get_bit_from_columns(lines, column)
        uncommon = get_least_common(temp_container)
        uncommon_lines = select_common_lines(lines, uncommon, column)
        lines = uncommon_lines
        if len(lines) == 1:
            return int(lines[0].strip("\n"), 2)


oxygen_rating = get_oxygen_rating()
co2_rating = get_co2_rating()
life_support = print(str(co2_rating * oxygen_rating))
