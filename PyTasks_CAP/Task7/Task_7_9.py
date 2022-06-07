# Вариант 9

def main(x):  # x similar everywhere
    a = x & 0b1111_1111_1111_11  # binary
    b = (x >> 14) & 0b1111_1
    c = (x >> 19) & 0b1111_1
    d = (x >> 24) & 0b1111_1111
    result = d | (b << 8) | (c << 13) | (a << 18)
    return result


hex(main(0xdcf12f12))

# For CAP, you only need what is above, having checked in advance for PEP8

if __name__ == "__main__":
    print("Res 1:", hex(main(0xdcf12f12)))
    print("Res 1:", hex(main(0x94d66cd1)))
    print("\n", "-" * 20, "Done!", "-" * 20)
