def read_input():
    with open("input/day_1") as sonar:
        results = sonar.readlines()
        result = [int(line) for line in results]
    return result


def number_of_increases():
    count = -1
    previous = 0
    for number in read_input():
        current = number
        if current > previous:
            count += 1
        previous = current
    return count


def sliding_window_increases():
    data = read_input()
    interval = 3
    window = 0
    count = -1
    previous = 0

    for _ in data:
        slide = data[window : (window + interval)]
        if len(slide) == interval:
            current = sum(slide)
            if current > previous:
                count += 1

        window += 1
        previous = current
    return count


if __name__ == "__main__":
    print(sliding_window_increases())
