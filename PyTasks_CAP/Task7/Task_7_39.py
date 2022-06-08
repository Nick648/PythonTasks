# Вариант 39
def main(x):
    a = x & 0b1111_1
    b = (x >> 5) & 0b1111_1
    c = (x >> 10) & 0b1111_1
    d = (x >> 15) & 0b1111
    e = (x >> 19) & 0b1111_1111_111
    f = (x >> 30) & 0b11
    result = a | (c << 5) | (b << 10) | (e << 15) | (f << 26) | (d << 28)
    return result


main(0xdcf12f12)

# For CAP, you only need what is above, having checked in advance for PEP8

if __name__ == "__main__":
    res = [
        main(0xb90405a3),
        main(0x71087e81),
        main(0x87861a48),
        main(0xf303f36e),
        main(0x4f2aa168)
    ]
    for i in range(len(res)):
        print(f"Res {i + 1}:", hex(res[i]))
    print("\n", "-" * 20, "Done!", "-" * 20)

# main(0xb90405a3) = 0x8b903423
# main(0x71087e81) = 0x0710d3e1
# main(0x87861a48) = 0xc87848c8
# main(0xf303f36e) = 0x7f306f8e
# main(0x4f2aa168) = 0x54f2ad08
