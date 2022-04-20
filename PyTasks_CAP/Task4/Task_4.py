# Вариант 18

import math


def main(n):
    if n == 0:
        return -0.51
    elif n == 1:
        return 0.10
    elif n >= 2:
        return main(n - 2) ** 2 + math.cos(main(n - 1)) / 52 + main(n - 2) ** 3


main(3)

# For CAP, you only need what is above, having checked in advance for PEP8

if __name__ == "__main__":
    print("Results:")
    res_1 = main(2)
    res_2 = main(3)
    res_3 = main(-1)
    res_1 = "{:.2e}".format(res_1)
    res_2 = "{:.2e}".format(res_2)
    try:
        res_3 = "{:.2e}".format(res_3)
    except TypeError:
        pass
    print('Res 1:', res_1)
    print('Res 2:', res_2)
    print('Res 3:', res_3)
