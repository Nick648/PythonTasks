# Вариант 39
from math import log10


def main(x):
    result = 0
    for i in range(len(x)):
        result += log10(37 * x[i // 3] ** 2 + 82) ** 4
    result *= 54 * 68
    return result


main([-0.82, 0.59, 0.83, -0.39, 0.98, 0.48])

# For CAP, you only need what is above, having checked in advance for PEP8

if __name__ == '__main__':
    print("\nResults:")
    res = [
        main([-0.82, 0.59, 0.83, -0.39, 0.98, 0.48]),
        main([0.03, -0.19, -0.71, 0.28, 0.62, -0.45]),
        main([-0.93, 0.11, -0.15, -0.41, -0.99, -0.58]),
        main([0.32, -0.71, 0.97, -0.79, 0.82, 0.9]),
        main([-0.36, -0.17, 0.22, 0.13, 0.98, 0.45])
    ]
    for pos in range(len(res)):
        print(f"Res {pos + 1}:", "{:.2e}".format(res[pos]))
    print("\n", "-" * 20, "Done!", "-" * 20)
