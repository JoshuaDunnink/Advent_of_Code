import numpy as np


def read_input():
    with open("input/2015/day_6") as f:
        data = [line.strip("\n") for line in f.readlines()]
    return data


def get_array(height, width):
    return np.zeros((height, width), dtype=int)


def switch(multiplyer, array, x_range, Y_range):
    for x in range(x_range[0], x_range[1]):
        for y in range(Y_range[0], Y_range[1]):
            match multiplyer:
                case "toggle":
                    array[x][y] += 2
                case "on":
                    array[x][y] += 1
                case "off":
                    if not array[x][y] == 0:
                        array[x][y] += -1
    return array


def get_x_y_range(point1, point2):
    points1 = [int(char) for char in point1.split(",")]
    points2 = [int(char) for char in point2.split(",")]

    x_range = (points1[0], points2[0] + 1)
    y_range = (points1[1], points2[1] + 1)

    return x_range, y_range


def translate_and_act(line, lamp_array):
    decomposed_line = line.split(" ")
    if decomposed_line[0] == "toggle":
        x_range, y_range = get_x_y_range(
            decomposed_line[1],
            decomposed_line[3],
        )
        lamp_array = switch("toggle", lamp_array, x_range, y_range)
    else:
        x_range, y_range = get_x_y_range(
            decomposed_line[2],
            decomposed_line[4],
        )
        match decomposed_line[1]:
            case "on":
                lamp_array = switch("on", lamp_array, x_range, y_range)
            case "off":
                lamp_array = switch("off", lamp_array, x_range, y_range)
    return lamp_array


def count_lamps(array):
    return array.sum()


def main():
    file_input = read_input()
    lamp_array = get_array(1000, 1000)
    for line in file_input:
        lamp_array = translate_and_act(line, lamp_array)

    print(count_lamps(lamp_array))


def test1():
    lamps_original = get_array(1000, 1000)
    lamps = translate_and_act("turn on 0,0 through 999,999", lamps_original)
    print(count_lamps(lamps) == (1000 * 1000))


main()
