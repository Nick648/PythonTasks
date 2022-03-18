import math


def main(x):
    if x < 121:
        ans = 1 + 47 * (math.cos(1 + x / 12 + 37 * x ** 3) ** 4) + 93 * x ** 5
    elif x >= 200:
        ans = ((math.cos(96 * x ** 3)) ** 5) / 89
    else:
        ans = 92 * (x / 25 - x ** 2 - 93) ** 2 + 88 * math.tan(x) ** 5 + \
              68 * (6 * x ** 3 + 19 + x) ** 4
    return ans


main(179)
