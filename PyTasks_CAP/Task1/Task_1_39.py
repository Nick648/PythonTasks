# Вариант 39

from math import sqrt, asin


def main(y):
    result = sqrt(59 * (99 * y ** 2 - y - y ** 3) + 87 * y ** 4)
    result -= sqrt(asin(62 * y ** 3 - y - y ** 2) ** 4)
    return result


main(0.16)

# For CAP, you only need what is above, having checked in advance for PEP8


if __name__ == '__main__':
    print("Results:")
    res = [main(0.16),
           main(0.25),
           main(-0.04),
           main(-0.19),
           main(0.09),
           ]
    for i in range(len(res)):
        print(f"Res {i + 1}:", "{:.2e}".format(res[i]))
    print("\n", "-" * 20, "Done!", "-" * 20)
