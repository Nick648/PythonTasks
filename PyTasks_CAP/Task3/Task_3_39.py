# Вариант 39
from math import log2, floor


def main(n, a, y):
    res = 0
    for j in range(1, n + 1):
        res += log2(j) ** 4 / 4 - 1
    sec_sum = 0
    for i in range(1, a + 1):
        sec_mul = 1
        for j in range(1, n + 1):
            sec_mul *= 51 * (floor(75 * y ** 3)) ** 2 + \
                       24 * (0.02 - i / 82 - j ** 2) ** 3
        sec_sum += sec_mul
    res += sec_sum
    return res


main(4, 3, 0.98)

# For CAP, you only need what is above, having checked in advance for PEP8


if __name__ == '__main__':
    print("\nResults:")
    res = [
        main(4, 3, 0.98),
        main(8, 7, -0.34),
        main(3, 7, -0.12),
        main(4, 4, 0.89),
        main(6, 6, 0.42),
    ]
    for i in range(len(res)):
        print(f"Res {i + 1}:", "{:.2e}".format(res[i]))
    print("\n", "-" * 20, "Done!", "-" * 20)
