import codecs


def get_data():
    with codecs.open("input/2015/day_8", "r", encoding="unicode_escape") as q:
        return q.readlines()


def get_raw_data():
    with open("input/2015/day_8", "r") as file:
        data = [rf"{element}" for element in file]
        return data


def main():
    line_characters = 0
    actual_characters = 0

    raw_data = get_raw_data()
    data = get_data()

    for line in data:
        line = line[:-2][1:]
        line_characters += len(line)

    for raw_line in raw_data:
        raw_line = raw_line.strip("\n")
        actual_characters += len(raw_line)
    actual_characters -= 13

    print(actual_characters - line_characters)


main()
