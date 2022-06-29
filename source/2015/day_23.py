def read():
    with open("input/2015/day_23", "r") as file:
        return [line.strip("\n") for line in file]


def match(action, register, a):
    index = 1
    match action:
        case "hlf":
            a = a / 2
        case "tpl":
            a *= 3
        case "inc":
            a += 1
        case "jmp":
            index = register
        case "jie":
            if a % 2 == 0:
                index = register
        case "jio":
            if a == 1:
                index = register
    return int(index), a, 0


def perform_next_action(instruction: str, a):
    action, register = instruction.split(" ")
    if register != "b":
        return match(action, register, a)
    else:
        return 1, a, 1


def main():
    instructions = read()
    a = 1
    b = 0
    index = 0
    while index < len(instructions):
        plus_i, a, plus_b = perform_next_action(instructions[index], a)
        index += plus_i
        b += plus_b
    print(b)


main()
