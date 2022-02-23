import math


def main(n):
    if n == 0:
        return -0.51
    elif n == 1:
        return 0.10
    elif n >= 2:
        return main(n - 2) ** 2 + math.cos(main(n - 1)) / 52 + main(n - 2) ** 3


main(3)
