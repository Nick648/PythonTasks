# Вариант 18

import math


def main(z):
    ans = (z ** 3 / (74 * z ** 12 - 77 * z ** 2)) - \
          (math.log2(1 - 79 * z - z ** 2)) ** 6
    return ans


main(-0.96)

# For CAP, you only need what is above, having checked in advance for PEP8


if __name__ == "__main__":
    print("Results:")
    res_1 = main(-0.06)
    res_2 = main(-0.96)
    res_1 = "{:.2e}".format(res_1)
    res_2 = "{:.2e}".format(res_2)
    print('Res 1:', res_1)
    print('Res 2:', res_2)
    print("\n", "-" * 20, "Done!", "-" * 20)
