# Вариант 18

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

# For CAP, you only need what is above, having checked in advance for PEP8

if __name__ == "__main__":
    print("Results:")
    res_1 = main(193)
    res_2 = main(179)
    res_1 = "{:.2e}".format(res_1)
    res_2 = "{:.2e}".format(res_2)
    print('Res 1:', res_1)
    print('Res 2:', res_2)
