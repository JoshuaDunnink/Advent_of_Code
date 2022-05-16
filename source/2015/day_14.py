"""
takeaways itertools cycle and accumulate
When dealing with a stepwise approach where steps are dependand on
the state per step, create a 'cycle' trough which you can iterate
per step.
When dealing with a list (or cycle) that you would like to
'accumulate' and keep track of, use accumulate
"""


from itertools import cycle, accumulate


def get_data() -> dict:
    with open("input/2015/day_14", "r") as file:
        data = file.readlines()
        return_values = {}
        for line in data:
            splitted_line = line.split(" ")
            name = splitted_line[0]
            speed = int(splitted_line[3])
            duration = int(splitted_line[6])
            rest = int(splitted_line[-2])
            return_values.update({name: [speed, duration, rest]})
        return return_values


def determine_distance_after(seconds: int, specifications: list):
    """returns a full list of distances in range of duration(seconds)
    - creates a list of steps in the cycle
    - for every second append and add the distance to the total distance


    Args:
        seconds (int): duration in seconds
        specifications (list): [speed, stamina, rest]

    Returns:
        list: distance per second
    """
    step = cycle(
        [specifications[0]] * specifications[1] + [0] * specifications[2]
    )
    distances = list(accumulate(next(step) for _ in range(seconds)))
    return distances


def main():
    duration = 2503
    ranking = {}
    for key, value in get_data().items():
        distances = determine_distance_after(duration, value)
        ranking.update({key: distances})
    print(
        f"max distance= {max([distance[-1] for distance in ranking.values()])}"
    )

    point_ranking = {key: 0 for key in ranking.keys()}
    compare = point_ranking.copy()
    for i in range(duration):
        for key, value in ranking.items():
            compare[key] = value[i]

        current_max_distance = max(compare.values())
        if list(compare.values()).count(current_max_distance) > 1:
            for key, value in compare.items():
                if value == current_max_distance:
                    point_ranking[key] += 1
        else:
            point_ranking[max(compare, key=compare.get)] += 1

    print(point_ranking)


main()
