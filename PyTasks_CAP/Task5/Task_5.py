# Вариант 18

def main(y, x):
    ans = 0
    for i in range(len(x)):
        ans += 2 * (80 * x[i // 4] + 67 * x[len(x) - 1 - i] ** 3 + y[i // 4] ** 2) ** 5
    ans *= 55
    return ans


main([-0.98, -0.05, -0.03, 0.23, 0.34, 0.0],
     [0.03, -0.36, -0.0, -0.89, 0.52, 0.55])

# For CAP, you only need what is above, having checked in advance for PEP8

if __name__ == "__main__":
    print("Results:")
    res_1 = main([-0.98, -0.05, -0.03, 0.23, 0.34, 0.0],
                 [0.03, -0.36, -0.0, -0.89, 0.52, 0.55])
    res_2 = main([0.09, -0.8, -0.37, -0.66, -0.24, -1.0],
                 [0.62, 0.89, -0.05, 0.24, -0.59, -0.55])
    res_1 = "{:.2e}".format(res_1)
    res_2 = "{:.2e}".format(res_2)
    print('Res 1:', res_1)
    print('Res 2:', res_2)
    print("\n", "-" * 20, "Done!", "-" * 20)
