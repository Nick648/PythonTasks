# Вариант 39

from math import atan


def main(x):
    if x < 31:
        return 71 * (x ** 2 / 9) ** 6 + \
               35 * (1 + x ** 2) ** 2 + atan(x) ** 4 / 57
    elif 31 <= x < 74:
        return (58 - x ** 2 / 32) ** 3 - 84 * (x / 10) ** 4
    elif 74 <= x < 163:
        return 26 * x ** 5 + 1 + (15 * x ** 2 - 58 - x) ** 2 / 55
    elif x >= 163:
        return (3 * x + 83 * x ** 2 + 20 * x ** 3) ** 4


main(104)

# For CAP, you only need what is above, having checked in advance for PEP8


if __name__ == '__main__':
    print("\nResults:")
    res = [main(104),
           main(221),
           main(15),
           main(213),
           main(105),
           ]
    for i in range(len(res)):
        print(f"Res {i + 1}:", "{:.2e}".format(res[i]))
    print("\n", "-" * 20, "Done!", "-" * 20)
