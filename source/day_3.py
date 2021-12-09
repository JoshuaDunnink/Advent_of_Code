def read_input():
    with open("input/day_3") as movement:
        results = movement.readlines()
    return results


def determine_gamma_epsilon(list):
    one = list.count(1)
    zero = list.count(0)

    if one > zero:
        return '1', '0'
    else:
        return '0', '1'


def get_power_consumption():
    lines = read_input()
    column_length = len(lines[0].strip('\n'))
    bin_gamma = ''
    bin_epsilon = ''

    for column in range(column_length):
        temp_container = []
        for line in lines:
            temp_container.append(int(line[column]))
        gamma, epsilon = determine_gamma_epsilon(temp_container)
        bin_gamma = bin_gamma+gamma
        bin_epsilon = bin_epsilon+epsilon

    gamma_rate = int(bin_gamma, 2)
    epsilon_rate = int(bin_epsilon, 2)
    power_consumption = gamma_rate * epsilon_rate

    return power_consumption


print(get_power_consumption())
