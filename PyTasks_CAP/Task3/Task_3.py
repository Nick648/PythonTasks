# Вариант 18

def main(m, a, x):
    ans = 0
    for i in range(1, a + 1):
        for c in range(1, m + 1):
            ans += 63 * x ** 2 + c + 73 * (i / 39 + 85 + 93 * i ** 2) ** 7
    return ans


main(4, 8, -0.95)

# For CAP, you only need what is above, having checked in advance for PEP8

if __name__ == "__main__":
    print("Results:")
    res_1 = main(7, 5, 0.04)
    res_2 = main(4, 8, -0.95)
    res_1 = "{:.2e}".format(res_1)
    res_2 = "{:.2e}".format(res_2)
    print('Res 1:', res_1)
    print('Res 2:', res_2)
