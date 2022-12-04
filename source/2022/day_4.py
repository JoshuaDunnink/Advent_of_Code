def data():
    with open("input/2022/day_4", "r") as file:
        return [line.strip("\n").split(",") for line in file.readlines()]


def contains(section1, section2):
    # range_1 = range(section1[0], section1[1])
    # range_2 = range(section2[0], section2[1])
    # if range_1 in range_2 or range_2 in range_1:
    #     return True
    if (section1[0] <= section2[0] and section1[1] >= section2[1]) or (
        section1[0] >= section2[0] and section1[1] <= section2[1]
    ):
        return True
    return False


def overlaps(elf_1, elf_2):
    sections_1 = set(range(elf_1[0], elf_1[1]+1))
    sections_2 = set(range(elf_2[0], elf_2[1]+1))
    if (sections_1 & sections_2):
        return True
    return False


sections = data()
contains_count = 0
overlap_count = 0
for section in sections:
    elf_1 = [int(num) for num in section[0].split("-")]
    elf_2 = [int(num) for num in section[1].split("-")]

    if contains(elf_1, elf_2):
        contains_count += 1
    if overlaps(elf_1, elf_2):
        overlap_count += 1

print(contains_count)
print(overlap_count)
