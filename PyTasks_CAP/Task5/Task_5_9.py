# Вариант 9

def main(x, z):
    ans = 0
    for i in range(len(x)):
        a = x[len(x) - (i // 4) - 1]
        b = z[len(z) - i - 1]  # a,b - just for PEP8
        ans += (66 + a ** 3 + b / 87) ** 4 / 45
    ans *= 85
    return ans


main([0.45, 0.12, 0.75, -0.64, 0.86, 0.43, 0.7],
     [-0.57, -0.3, 0.98, 0.23, -0.27, 0.87, -0.98])

# For CAP, you only need what is above, having checked in advance for PEP8

if __name__ == "__main__":
    print("Results:")
    res_1 = main([0.45, 0.12, 0.75, -0.64, 0.86, 0.43, 0.7],
                 [-0.57, -0.3, 0.98, 0.23, -0.27, 0.87, -0.98])
    res_2 = main([-0.78, 0.5, 0.65, -0.38, -0.93, 0.3, -0.42],
                 [-0.8, -0.46, 0.41, 0.91, 0.39, 0.38, 0.34])
    res_1 = "{:.2e}".format(res_1)
    res_2 = "{:.2e}".format(res_2)
    print('Res 1:', res_1)
    print('Res 2:', res_2)
    print("\n", "-" * 20, "Done!", "-" * 20)
