import re

WORD_NUMBERS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def data():
    with open("input/2023/day_1", "r") as file:
        return file.readlines()


def main():
    words = [num for num in WORD_NUMBERS.keys()]
    words = "|".join(words)

    input = data()
    numbers = []
    for line in input:
        for num in WORD_NUMBERS.keys():
            line = line.replace(num, num + str(WORD_NUMBERS.get(num)) + num)
        matches = re.findall(("\d"), line)
        numbers.append(int(str(matches[0]) + str(matches[-1])))
    print(sum(numbers))


main()
