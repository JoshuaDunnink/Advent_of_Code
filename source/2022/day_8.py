from math import prod


def grid():
    with open("input/2022/day_8", "r") as file:
        return [
            [int(tree) for tree in line.strip("\n")]
            for line in file.readlines()
        ]


def is_biggest(tree, tree_row, tree_column, x, y):
    return (
        1
        if any(
            [
                all(tree > other for other in tree_row[:x]),
                all(tree > other for other in tree_row[x + 1 :]),
                all(tree > other for other in tree_column[:y]),
                all(tree > other for other in tree_column[y + 1 :]),
            ]
        )
        else 0
    )


def determine_scenic_score(tree, tree_row, tree_column, x, y):
    left = tree_row[:x][::-1]
    right = tree_row[x + 1 :]
    up = tree_column[:y][::-1]
    down = tree_column[y + 1 :]
    directions = [left, right, up, down]

    score = []
    for direction in directions:
        for index, other_tree in enumerate(direction):
            if tree <= other_tree:
                score.append(index + 1)
                break
            elif index + 1 == len(direction):
                score.append(index + 1)

    return prod(score)


def forrest():
    tree_grid = grid()
    transposed_tree_grid = list(map(list, zip(*tree_grid)))

    visible_trees = 0
    edges = 2 * len(tree_grid) + 2 * (len(tree_grid[0]) - 2)
    visible_trees += edges

    scenic_scores = []

    for y, tree_row in enumerate(tree_grid):
        if y >= 1 and y <= len(tree_grid) - 2:
            for x, tree in enumerate(tree_row):
                if x >= 1 and x <= len(tree_row) - 2:
                    visible_trees += is_biggest(
                        tree, tree_row, transposed_tree_grid[x], x, y
                    )
                    scenic_scores.append(
                        determine_scenic_score(
                            tree, tree_row, transposed_tree_grid[x], x, y
                        )
                    )

    print("part 1: " + str(visible_trees))
    print("part 2: " + str(max(scenic_scores)))


forrest()
