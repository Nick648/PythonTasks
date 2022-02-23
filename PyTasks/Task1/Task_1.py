import math


def main(z):
    ans = (z ** 3 / (74 * z ** 12 - 77 * z ** 2)) - \
          (math.log2(1 - 79 * z - z ** 2)) ** 6
    return ans


main(-0.96)
