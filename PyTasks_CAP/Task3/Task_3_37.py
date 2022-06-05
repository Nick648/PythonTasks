# Вариант 37
from math import atan


def main(a, m, p, b):
    # print("Values: ", a, m, p, b)
    first_sum = 0
    first_mul = 1
    second_sum = 0
    for i in range(1, m + 1):
        for c in range(1, a + 1):
            first_mul *= (29 * i - 2 * atan(31 * p ** 3 + 72 * c) ** 4)
        first_sum += first_mul
    for k in range(1, b + 1):
        for i in range(1, a + 1):
            second_sum += (17 * (i ** 2 + 10 + 83 * k) ** 2 - k ** 3)

    result = first_sum - second_sum
    return result


print(main(2, 4, -0.98, 4))

# For CAP, you only need what is above, having checked in advance for PEP8

if __name__ == "__main__":
    print("\nResults:")
    results = [main(2, 4, -0.98, 4),
               main(2, 6, -0.14, 5),
               main(5, 2, 0.02, 8),
               main(2, 7, -0.18, 3),
               main(3, 7, -0.76, 8)]
    for i in range(len(results)):
        results[i] = "{:.2e}".format(results[i])
        print(f"Res_{i + 1}: {results[i]}")
    print("\n", "-" * 20, "Done!", "-" * 20)
