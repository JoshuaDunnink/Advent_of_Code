import re


def read_data():
    with open("input/2016/day_9", "r") as file:
        return file.readlines()


source = read_data()[0].strip("\n")
# source = "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"


def decompress(source):
    search_results = re.finditer("\([0-9]*x[0-9]*\)", source)
    cursor = 0
    result = ""

    for match in search_results:
        if cursor < match.start():
            result += source[cursor : match.start()]
            cursor = match.start()
        if cursor == match.start():
            cleaned = match[0].strip("(").strip(")").split("x")
            result += source[
                match.end() : match.end() + int(cleaned[0])
            ] * int(cleaned[1])
            cursor = match.end() + int(cleaned[0])

    if cursor < len(source):
        result += source[cursor:]
    return result


def day_1():
    print(len(decompress(source)))


def part_2():
    while bool(re.search("\([0-9]*x[0-9]*\)", source)):
        source = decompress(source)
        print(len(source))
