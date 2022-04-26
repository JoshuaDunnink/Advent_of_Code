from copy import deepcopy


def read_input():
    with open("input/2015/day_7") as f:
        data = f.readlines()
    return data


class Assembler:
    def __init__(self, data) -> None:
        self.data = data
        self.inventory = {}
        self.operators = [
            "NOT",
            "OR",
            "AND",
            "RSHIFT",
            "LSHIFT",
        ]
        self.process_data()

    def return_value(self, char):
        return self.inventory.get(char)

    def overwrite_and_reset_inventory(self, value):
        self.inventory = {"b": value}
        self.data = self.iterable_data
        self.data.remove("44430 -> b\n")
        self.process_data()

    def process_data(self):
        self.iterable_data = deepcopy(self.data)
        while len(self.data) > 0:
            for index, line in enumerate(self.iterable_data):
                listed_line = line.strip("\n").split(" ")
                if (
                    index := self.determine_operator_index(listed_line)
                ) is not None:
                    operator = listed_line.pop(index)
                else:
                    operator = None

                assignment = listed_line.index("->")

                if (
                    self.is_int(listed_line[0])
                    and not operator
                    and self.inventory.get(listed_line[-1]) is None
                ):
                    self.inventory.update(
                        {listed_line[-1]: int(listed_line[0])}
                    )
                    self.data.remove(line)
                    break
                elif (
                    operator == None
                    and len(listed_line) == 3
                    and (number := self.inventory.get(listed_line[0]))
                    is not None
                ):
                    self.inventory.update({listed_line[-1]: int(number)})
                    self.data.remove(line)
                elif self.all_variables_known_in_inventory(
                    listed_line[:assignment]
                ):
                    self.calculate_new_value(operator, listed_line)
                    try:
                        self.data.remove(line)
                    except ValueError:
                        pass

    @staticmethod
    def is_int(char):
        try:
            int(char)
            return True
        except ValueError:
            return False

    def determine_operator_index(self, listed_line):
        for operator in self.operators:
            if operator in listed_line:
                return listed_line.index(operator)

    def all_variables_known_in_inventory(self, input):
        check_input = [x for x in input if not self.is_int(x)]
        for character in check_input:
            if self.inventory.get(character) is None:
                return False
        return True

    def calculate_new_value(self, operator, input):
        if len(input) == 3 and operator == "NOT":
            value = self.inventory.get(input[0])
            self.inventory.update({input[-1]: ~int(value)})
        elif len(input) == 4:
            input1 = (
                int(input[0])
                if self.is_int(input[0])
                else self.inventory.get(input[0])
            )
            input2 = (
                int(input[1])
                if self.is_int(input[1])
                else self.inventory.get(input[1])
            )
            match operator:
                case "OR":
                    self.inventory.update({input[-1]: input1 | input2})
                case "AND":
                    self.inventory.update({input[-1]: input1 & input2})
                case "RSHIFT":
                    self.inventory.update({input[-1]: input1 >> input2})
                case "LSHIFT":
                    self.inventory.update({input[-1]: input1 << input2})


ass = Assembler(read_input())
print(ass.return_value("a"))
ass.overwrite_and_reset_inventory(ass.return_value("a"))
print(ass.return_value("a"))
