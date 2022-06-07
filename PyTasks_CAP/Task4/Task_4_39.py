# Вариант 39

def main(n):
    if n == 0:
        return -0.08
    elif n >= 1:
        return 83 * main(n - 1) ** 3 + main(n - 1) / 70


main(8)

# For CAP, you only need what is above, having checked in advance for PEP8


if __name__ == '__main__':
    print("\nResults:")
    res = [
        main(8),
        main(4),
        main(1),
        main(7),
        main(3),
    ]
    for i in range(len(res)):
        print(f"Res {i + 1}:", "{:.2e}".format(res[i]))
    print("\n", "-" * 20, "Done!", "-" * 20)
