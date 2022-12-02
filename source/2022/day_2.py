def data():
    with open("input/2022/day_2", "r") as file:
        return [line.strip("\n").split(" ") for line in file.readlines()]


def return_score_part1(A, B):
    """
        Rock A , X
        Paper B , Y
        Scissors C , Z

        Win 0
        Lose 6

        Rock 1
        Paper 2
        Scissors 3
    """
    rock = ["A", "X"]
    paper = ["B", "Y"]
    scissors = ["C", "Z"]

    rock_score = 1
    paper_score = 2
    scissors_score = 3

    win = 6
    draw = 3
    lose = 0

    if A in rock:
        if B in rock:
            return rock_score + draw
        elif B in paper:
            return paper_score + win
        elif B in scissors:
            return scissors_score + lose

    elif A in paper:
        if B in rock:
            return rock_score + lose
        elif B in paper:
            return paper_score + draw
        elif B in scissors:
            return scissors_score + win

    elif A in scissors:
        if B in rock:
            return rock_score + win
        elif B in paper:
            return paper_score + lose
        elif B in scissors:
            return scissors_score + draw


def determine_set_part_2(A, B):
    """
        X = lose
        Y = draw
        Z = win

        rock = ["A", "X"]
        paper = ["B", "Y"]
        scissors = ["C", "Z"]
    """
    # Loose
    if B == "X":
        if A == "A":
            return return_score_part1(A, "Z")
        elif A == "B":
            return return_score_part1(A, "X")
        elif A == "C":
            return return_score_part1(A, "Y")
    # draw
    if B == "Y":
        if A == "A":
            return return_score_part1(A, "X")
        elif A == "B":
            return return_score_part1(A, "Y")
        elif A == "C":
            return return_score_part1(A, "Z")
    # win
    if B == "Z":
        if A == "A":
            return return_score_part1(A, "Y")
        elif A == "B":
            return return_score_part1(A, "Z")
        elif A == "C":
            return return_score_part1(A, "X")


def part_1_and_2():
    total_score_pt1 = 0
    total_score_pt2 = 0
    for match in data():
        A, B = match
        total_score_pt1 += return_score_part1(A, B)
        total_score_pt2 += determine_set_part_2(A, B)
    print(total_score_pt1)
    print(total_score_pt2)


part_1_and_2()
