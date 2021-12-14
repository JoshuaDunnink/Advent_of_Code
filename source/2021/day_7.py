def get_input():
    with open("input/2021/day_7", "r") as file:
        data = [int(num) for num in file.read().strip("\n").split(",")]
    return data


def get_fuel_cost(position, crabs):
    cost = [
        (crab - position) if crab > position else (position - crab)
        for crab in crabs
    ]
    cost = [(item * (1+item)/2) for item in cost]
    return sum(cost)


def get_min_max_position(crabs):
    minimum = min(crabs)
    maximum = max(crabs)
    return minimum, maximum


def determine_minimum_cost(minimum_position, maximum_position, crabs):
    cost = {}
    for i in range(minimum_position, maximum_position):
        position_cost = get_fuel_cost(i, crabs)
        if not cost.get(position_cost):
            cost.update({position_cost: [i]})
        else:
            cost[position_cost].append(i)
    return [int(key) for key in cost.keys()]


def main():
    crabs = get_input()
    minimum, maximum = get_min_max_position(crabs)
    minimum_cost = determine_minimum_cost(minimum, maximum, crabs)
    print(min(minimum_cost))


main()
