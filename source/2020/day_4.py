import re


def data():
    with open("input/2020/day_4", "r") as file:
        normalized_lines = []
        data = file.readlines()
        appendable_line = ""
        for line in data:
            if line != "\n":
                appendable_line += line.replace("\n", " ")
            elif line == "\n":
                normalized_lines.append(appendable_line)
                appendable_line = ""

        return normalized_lines


def get_dict_data():
    actual_data = []
    for line in data():
        actual_data.append(
            {k.split(":")[0]: k.split(":")[1] for k in line.split()}
        )
    return actual_data


def required_fields(actual_data):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid = []

    for line in actual_data:
        keys = line.keys()
        if all([field in keys for field in required_fields]):
            valid.append(line)
    return valid


def validate_fields(line):
    validation = []
    for key in line.keys():
        match key:
            case "byr":
                if (
                    len(line[key]) == 4
                    and int(line[key]) >= 1920
                    and int(line[key]) <= 2002
                ):
                    validation.append(True)
                else:
                    validation.append(False)
            case "iyr":
                if (
                    len(line[key]) == 4
                    and int(line[key]) >= 2010
                    and int(line[key]) <= 2020
                ):
                    validation.append(True)
                else:
                    validation.append(False)
            case "eyr":
                if (
                    len(line[key]) == 4
                    and int(line[key]) >= 2020
                    and int(line[key]) <= 2030
                ):
                    validation.append(True)
                else:
                    validation.append(False)
            case "hgt":
                if "cm" in line[key]:
                    length = int(re.search(r"\d+", line[key]).group())
                    if length >= 150 and length <= 193:
                        validation.append(True)
                    else:
                        validation.append(False)
                elif "in" in line[key]:
                    length = int(re.search(r"\d+", line[key]).group())
                    if length >= 59 and length <= 76:
                        validation.append(True)
                    else:
                        validation.append(False)
                else:
                    validation.append(False)
            case "hcl":
                if len(line[key]) == 7:
                    validation.append(True)
                else:
                    validation.append(False)
            case "ecl":
                if line[key] in [
                    "amb",
                    "blu",
                    "brn",
                    "gry",
                    "grn",
                    "hzl",
                    "oth",
                ]:
                    validation.append(True)
                else:
                    validation.append(False)
            case "pid":
                try:
                    if len(line[key]) == 9 and int(line[key]):
                        validation.append(True)
                    else:
                        validation.append(False)
                except ValueError:
                    validation.append(False)
            case "cid":
                validation.append(True)
    return validation


def validate_content(valid):
    validated = 0

    for line in valid:
        validation = validate_fields(line)
        if all(validation):
            validated += 1

    return validated


actual_data = get_dict_data()
valid = required_fields(actual_data)
validated = validate_content(valid)

print(str(validated))
