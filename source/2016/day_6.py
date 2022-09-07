from collections import Counter


def read_data():
    with open("input/2016/day_6", "r") as file:
        return file.readlines()


data = read_data()
zipped_data = zip(*data)

word1 = ""
word2 = ""
for line in zipped_data:
    word1 += Counter(line).most_common()[0][0]
    word2 += Counter(line).most_common()[-1][0]

print(word1)
print(word2)
