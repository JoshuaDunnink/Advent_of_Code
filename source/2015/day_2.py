def read_input():
    with open("input/2015/day_2") as f:
        data = [line.strip("\n").split("x") for line in f.readlines()]
    return data


def determine_surface(line):
    h, w, l = line
    return (2*l*w + 2*w*h + 2*h*l)


def determine_smallest_surface(line=list):
    h, w, l = line
    return min([h*w, w*l, l*h])


def determine_wrapping_paper(data=list):
    wrapping_paper = 0
    for line in data:
        line_int = [int(num) for num in line]
        wrapping_paper += determine_surface(line_int)
        wrapping_paper += determine_smallest_surface(line_int)
    return wrapping_paper


def determine_volume(line=list):
    h, w, l = line
    return (h * w * l)


def determine_min_circumference(line=list):
    line.remove(max(line))
    h, w = line
    return (2 * h + 2 * w)


def determine_bow_length(data=list):
    bow_length = 0
    for line in data:
        line_int = [int(num) for num in line]
        bow_length += determine_volume(line_int)
        bow_length += determine_min_circumference(line_int)
    return bow_length


def main():
    data = read_input()
    print(f"square feet of paper: {determine_wrapping_paper(data)}")
    print(f"feet of ribbon: {determine_bow_length(data)}")


main()
