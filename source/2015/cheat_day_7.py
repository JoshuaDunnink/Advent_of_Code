import functools

data = {}


def read_input():
    with open("input/2015/day_7") as f:
        data = f.readlines()
    return data


for line in read_input():
    cmd, key = line.split(" -> ")
    data[key.strip()] = cmd


@functools.lru_cache()
def get_value(key):
    try:
        return int(key)
    except ValueError:
        pass

    cmd = data[key].split(" ")

    if "NOT" in cmd:
        return ~get_value(cmd[1])
    if "AND" in cmd:
        return get_value(cmd[0]) & get_value(cmd[2])
    elif "OR" in cmd:
        return get_value(cmd[0]) | get_value(cmd[2])
    elif "LSHIFT" in cmd:
        return get_value(cmd[0]) << get_value(cmd[2])
    elif "RSHIFT" in cmd:
        return get_value(cmd[0]) >> get_value(cmd[2])
    else:
        return get_value(cmd[0])


data["b"] = str(get_value("a"))
get_value.cache_clear()
print(get_value("b"))
