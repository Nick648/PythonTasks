# Вариант 28

import math


def main(n):
    if n == 0:
        return -0.67
    elif n == 1:
        return 0.17
    elif n >= 2:
        return main(n - 2) - main(n - 2) ** 3 / 72 - \
               (math.log10(main(n - 1) ** 3 + 35 + 43 * main(n - 1) ** 2)) ** 2


main(8)

# For CAP, you only need what is above, having checked in advance for PEP8

if __name__ == "__main__":
    print("Results:")
    res = [main(8),
           main(4),
           main(6),
           main(3),
           main(5)]
    for i in range(len(res)):
        print(f"Res {i + 1}", "{:.2e}".format(res[i]))

    print("\n", "-" * 20, "Done!", "-" * 20)
