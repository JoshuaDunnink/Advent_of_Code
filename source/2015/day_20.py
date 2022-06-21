from math import sqrt
from functools import wraps
from time import time


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print(
            "func:%r args:[%r, %r] took: %2.4f sec",
            (f.__name__, args, kw, te - ts),
        )
        return result

    return wrap


def deliver_presents():
    """Brute force approach

    Args:
        numbers (_type_): _description_
    """
    house = 1
    elfs = 1
    while True:
        gifts = int()
        for elf in range(1, elfs + 1):
            if house % elf == 0 and gifts != 36_000_000 and house >= elf:
                gifts += elf * 10
            elif gifts == 36_000_000:
                print(house - 1)
                return house
            elif house < elf:
                house += 1
        elfs += 1


def other_reverse():
    gifts = 3_600_000
    for gift in range(1, gifts + 1):
        amount = 0
        for elf in range(1, gift + 1):
            if gift % elf == 0:
                amount += elf
        if amount == gifts:
            print(gift)


def reverse_abc(target):
    """making use of the rule to quickly get to the sum of numbers
    0.5*i*(i+1)
    comes to
    0.5*i**2+0.5i
    in this case multiplied by 10
    5i**2+5*i = x

    to resolve the issue making use of the
    abc formula

    (-b+sqrt(b**2-4ac))/(2a)
    becomes

    when x = 1000

    (-5+sqrt(5**2-4*5*-1000))/(2*5)

    Args:
        target (_type_): _description_
    """
    solution_a = (-5 + sqrt(25 - 20 * -target)) / 20
    solution_b = (-5 - sqrt(25 - 20 * -target)) / 20
    print(f"{solution_a=} \n {solution_b=}")


def another_aliqout(n):
    divisors = {
        index + 1: i for index, i in enumerate(range(1, n + 1)) if n % i == 0
    }
    a = 0

    while a <= n:
        for index, i in divisors.items():
            a += i
        print(index)


# reverse_computation(550)
# aliquot_sum_solution(n)

# n = 360000
# i = 1
# gifts = 40000
# while n > gifts:
#     gifts = aliquot_sum_solution(i)
#     i += 1
# print(str(i))


def divSum(n, max_houses=None):
    if n == 1:
        return 1
    result = 0
    for i in range(2, (int)(sqrt(n)) + 1):
        if (
            n % i
            == 0
            # and (n / i <= max_houses)
        ):
            if i == (n / i):
                result = result + i
            else:
                result = result + (i + n // i)
    return result + n + 1


def aliquot_sum_solution(minimum):
    gifts = 0
    for i in range(1, minimum + 1):
        if minimum % i == 0:
            gifts += i
    return gifts


@timing
def main():
    n = int(36000000 / 10)
    i = 1
    gifts = 0
    while n > gifts:
        gifts = divSum(i)
        i += 1
    print(i - 1)


print(divSum(36))
print(aliquot_sum_solution(36))
