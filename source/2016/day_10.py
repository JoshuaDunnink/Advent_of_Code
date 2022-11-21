def read_data():
    with open("input/2016/day_10", "r") as file:
        return file.readlines()


class Output:
    def __init__(self, number):
        self.id = number
        self.bin = []

    def set(self, chip):
        self.bin.append(chip)


class Bot:
    def __init__(self, number, instructions=None, chip=None):
        self.id = number

        self.inventory = []
        if chip:
            self.inventory.append(chip)

        self.instructions = {}
        if instructions:
            self.generate_instructions(instructions)

    def generate_instructions(self, instructions: str):
        """low to bot 203 and high to bot 32"""
        for instruction in instructions.split("and"):
            if "low" in instruction:
                self.instructions.update(
                    {"low": int(instruction.strip(" ").split(" ")[-1])}
                )
            elif "high" in instruction:
                self.instructions.update(
                    {"high": int(instruction.strip(" ").split(" ")[-1])}
                )

    def set(self, number):
        self.inventory.append(number)

    def get(self):
        return self.inventory

    def execute(self):
        if len(self.inventory) == 2:
            return {
                self.instructions.get("high"): self._pop("max"),
                self.instructions.get("low"): self._pop("min"),
            }

    def _pop(self, indicator):
        if indicator == "max":
            high = max(self.inventory)
            self.inventory.remove(high)
            return high
        if indicator == "min":
            low = min(self.inventory)
            self.inventory.remove(low)
            return low


def identify_outputs(instructions):
    outputs = []
    for instruction in instructions.strip("\n").split(" and"):
        outputs.append(int(instruction[-1]))
    return outputs


def generate_bots(lines):
    bots = {}
    outputs = []
    for line in lines:
        number = int()
        split_line = line.strip("\n").split(" ")

        if split_line[0] == "bot":
            number = int(split_line[1])
            bot = bots.get(number)
            if not bot:
                instructions = line.split("gives")[1]
                if "output" in instructions:
                    outputs.extend(identify_outputs(instructions))
                bots.update({number: Bot(number, instructions)})
            elif not bot.instructions:
                instructions = line.split("gives")[1]
                bot.generate_instructions(instructions)

        elif split_line[0] == "value":
            number = int(split_line[-1])
            chip = int(split_line[1])
            bot = bots.get(number)
            if bot:
                bots[number].set(chip)
            elif not bot:
                bots.update({number: Bot(number, chip=chip)})

    return bots, outputs


bots, outputs = generate_bots(read_data())

found = False
while not found:
    for bot in bots.values():
        # if 61 in bot.get() and 17 in bot.get():
        #     print(bot.id)
        #     found = True
        actions = bot.execute()
        if actions:
            for number, chip in actions.items():
                bots[number].set(chip)
            print([bot.get() for bot in bots.values() if bot.inventory])
