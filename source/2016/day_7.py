import re


def read_data():
    with open("input/2016/day_7", "r") as file:
        return file.readlines()


def find_abba(string: str):
    if "[" in string or "]" in string:
        string = string.strip("[").strip("]")

    for i, char in enumerate(string):
        if (
            i <= len(string) - 4
            and string[i : i + 2] == string[i + 2 : i + 4][::-1]
            and char != string[i + 1]
        ):
            return True
    return False


def part_1():
    count = 0
    for line in read_data():
        clean_line = line.strip("\n")
        results = re.finditer("\[[a-z]*\]", clean_line)
        split_line = re.split("\[|\]", clean_line)

        abba_inside_bracket = False
        for match in results:
            abba_inside_bracket = find_abba(match[0])
            split_line.remove(match[0].strip("[").strip("]"))

        if not abba_inside_bracket and any(
            [find_abba(item) for item in split_line]
        ):
            count += 1
    print(count)


part_1()


def cheat():
    def abba(x):
        return any(
            a == d and b == c and a != b
            for a, b, c, d in zip(x, x[1:], x[2:], x[3:])
        )

    lines = [
        re.split(r"\[([^\]]+)\]", line) for line in open("input/2016/day_7")
    ]
    parts = [(" ".join(p[::2]), " ".join(p[1::2])) for p in lines]
    print("Answer #1:", sum(abba(sn) and not (abba(hn)) for sn, hn in parts))
    print(
        "Answer #2:",
        sum(
            any(
                a == c and a != b and b + a + b in hn
                for a, b, c in zip(sn, sn[1:], sn[2:])
            )
            for sn, hn in parts
        ),
    )


cheat()
