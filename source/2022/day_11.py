"""
lessons learned:
    use splitlines for multiline line
    use list(map(int, input)) or [int(x) for x in y]
"""


class Monkey:
    def __init__(
        self, name, items, operation, test, pass_true, pass_false
    ) -> None:
        self.name = name
        self.items = items
        self.operation = operation
        self.test = test
        self.pass_true = pass_true
        self.pass_false = pass_false
        self.inspections = 0

    def inspect_items(self):
        return_items = {self.pass_true: [], self.pass_false: []}
        for item in self.items:
            self.inspections += 1
            old = item
            value = int(eval(str(item) + self.operation)/3)
            if value % self.test == 0:
                return_items[self.pass_true].append(value)
            else:
                return_items[self.pass_false].append(value)
        self.items = []
        return return_items


def get_monkeys():
    monkeys = []
    with open("input/2022/day_11", "r") as file:
        for group in file.read().strip().split("\n\n"):
            lines = group.splitlines()
            monkey = Monkey(
                name=int(lines[0].strip(":")[-1]),
                items=[
                    int(num) for num in lines[1].split(": ")[1].split(", ")
                ],
                operation=" ".join(lines[2].split("=")[1].split(" ")[-2:]),
                test=int(lines[3].split()[-1]),
                pass_true=int(lines[4].split()[-1]),
                pass_false=int(lines[5].split()[-1]),
            )
            monkeys.append(monkey)
    return monkeys


pass_items = {}
monkeys = get_monkeys()
for round in range(0, 20):
    print(round)
    for monkey in monkeys:
        for monkey, items in monkey.inspect_items().items():
            monkeys[monkey].items.extend(items)

monkey_business = [monkey.inspections for monkey in monkeys]
monkey_business.sort()
print(monkey_business[-2] * monkey_business[-1])
