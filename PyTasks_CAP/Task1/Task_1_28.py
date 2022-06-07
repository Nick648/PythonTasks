# Вариант 28

def main(x, y):
    ans = ((70 * x) ** 3 - (y - y ** 2 - 35)) / \
          (23 * ((x ** 3 - y ** 2 - 8 * y) ** 4))
    ans += (abs(y / 85 - (x ** 2) / 22 - y ** 3) ** 5) ** 0.5
    return ans


main(0.17, -0.6)

# For CAP, you only need what is above, having checked in advance for PEP8

if __name__ == "__main__":
    print("Results:")
    res_1 = main(0.17, -0.6)
    res_2 = main(-0.08, -0.31)
    res_3 = main(0.36, -0.81)
    res_4 = main(-0.54, -0.6)
    res_5 = main(-0.42, -0.37)
    print('Res 1:', "{:.2e}".format(res_1))
    print('Res 2:', "{:.2e}".format(res_2))
    print('Res 3:', "{:.2e}".format(res_3))
    print('Res 4:', "{:.2e}".format(res_4))
    print('Res 5:', "{:.2e}".format(res_5))

    print("\n", "-" * 20, "Done!", "-" * 20)
