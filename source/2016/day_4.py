def read_data():
    with open("input/2016/day_4", "r") as file:
        return [line.strip("\n") for line in file.readlines()]


class Checker:
    def __init__(self, line: str):
        self.counted = {}
        self.line = line
        self.checksum = line[-6:-1]
        self.new_line = self.line[0 : len(line) - 7]
        self.number_location = len(self.new_line.split("-")) - 1

    def validate(self):
        self.count_and_sort()
        self.create_check_sum()
        return self.validate_checksum()

    def count_and_sort(self):
        for char in self.new_line:
            if (
                char not in self.counted.keys()
                and char != "-"
                and not char.isdigit()
            ):
                self.counted.update({char: self.new_line.count(char)})

        self.sorted_counted = dict(
            sorted(
                self.counted.items(), key=lambda item: item[1], reverse=True
            )
        )

    def create_check_sum(self):
        self.determine_check_sum = {}
        for k, v in self.sorted_counted.items():
            if v in self.determine_check_sum.keys():
                self.determine_check_sum[v].append(k)
            else:
                self.determine_check_sum.update({v: [k]})

        self.check_sum = ""
        for k, v in self.determine_check_sum.items():
            v.sort()
            for char in v:
                if len(self.check_sum) < 5:
                    self.check_sum += char

    def validate_checksum(self):
        if self.checksum == self.check_sum:
            return int(self.new_line.split("-")[self.number_location])
        else:
            return 0


def part_1():
    sum_of_rooms = 0
    for line in read_data():
        number = Checker(line).validate()
        sum_of_rooms += number

    print(sum_of_rooms)


class Decryptor:
    def __init__(self, line):
        self.new_line = line.split("-")
        self.number = int(self.new_line[-1].split("[")[0])
        self.rotations = self.number % 26

    def rotate(self):
        decrypted = ""
        for section in self.new_line:
            for char in section:
                if char == "z":
                    char = "a"
                    decrypted += chr(ord(char) + self.rotations - 1)
                if ord(char) + self.rotations > ord("z"):
                    char = "a"
                    temp_rotations = self.rotations - (ord("z") - ord(char))
                    decrypted += chr(ord(char) + temp_rotations)
                else:
                    decrypted += chr(ord(char) + self.rotations)
        if "north" in decrypted:
            return decrypted


def part_2():
    for line in read_data():
        print(Decryptor(line).rotate())


part_1()
