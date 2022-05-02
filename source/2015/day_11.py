import re

input = "vzbxkghb"


class PasswordGenerator:
    def __init__(self, input: str):
        self.password = input
        self.generating_password = ["" for _ in range(8)]
        self.lowerlimit = ord("a")
        self.upperlimit = ord("z")
        self.max_length = 8
        self.matcher = re.compile(r"(.)\1*")

    def increment_password(self):
        self.password = self.next_password()
        while not self.password_is_valid() and len(self.password) <= 8:
            self.password = self.next_password()
        return self.password

    def next_password(self):
        listed_password = list(self.password)
        ordinal_password = [ord(char) for char in listed_password]
        ordinal_password.reverse()
        increment_next = False
        for index, character in enumerate(ordinal_password):
            if index == 0 or increment_next:
                (
                    self.generating_password[index],
                    increment_next,
                ) = self.add_number(character)
            else:
                self.generating_password[index] = character
        reversed_generated_password = [
            chr(ords) for ords in self.generating_password
        ]
        reversed_generated_password.reverse()
        generated_password = ""
        return generated_password.join(reversed_generated_password)

    def add_number(self, ordinal_number):
        if ordinal_number == self.upperlimit:
            return self.lowerlimit, True
        elif (
            ordinal_number == ord("i") - 1
            or ordinal_number == ord("o") - 1
            or ordinal_number == ord("l") - 1
        ):
            return ordinal_number + 2, False
        else:
            return ordinal_number + 1, False

    def password_is_valid(self):
        if self.has_two_repeats() and self.has_3_increases():
            print(self.password)
            return True

    def has_two_repeats(self):
        matches = [
            match.group() for match in self.matcher.finditer(self.password)
        ]
        matches = [match for match in matches if len(match) == 2]
        if len(matches) == 2 and (matches[0] != matches[1]):
            return True

    def has_3_increases(self):
        for index, char in enumerate(list(self.password)):
            if (index != 0 and index != 7) and (
                ord(self.password[index - 1]) == ord(char) - 1
                and ord(self.password[index + 1]) == ord(char) + 1
            ):
                return True


new_pass = PasswordGenerator(input).increment_password()
next_pass = PasswordGenerator(new_pass).increment_password()
