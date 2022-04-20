# Вариант 18

def main(x):  # x similar everywhere
    # print("x:", x, hex(x), bin(x), len(bin(x)) - 2)
    a = x & 0b1111_1111_1111_1  # binary
    # print("a:", a, hex(a), bin(a), len(bin(a)) - 2)
    b = (x >> 13) & 0b1111_1111_1111_111
    # print("b:", bin(x >> 13), b, hex(b), bin(b), len(bin(b)) - 2)
    c = (x >> 28) & 0b1
    # print("c:", bin(x >> 28), c, hex(c), bin(c), len(bin(c)) - 2)
    d = (x >> 29) & 0b111
    # print("d:", bin(x >> 29), d, hex(d), bin(d), len(bin(d)) - 2)
    # print('(a << 16):', (a << 16), hex(a << 16), bin(a << 16), len(bin(a << 16)) - 2)
    # print('(b << 1):', (b << 1), hex(b << 1), bin(b << 1), len(bin(b << 1)) - 2)
    # print('(d << 29)):', (d << 29), hex(d << 29), bin(d << 29), len(bin(d << 29)) - 2)
    result = c | (a << 16) | (b << 1) | (d << 29)
    # print('result:', result, hex(result), bin(result), len(bin(result)) - 2)
    return result


hex(main(0x988dba6a))

# For CAP, you only need what is above, having checked in advance for PEP8
if __name__ == "__main__":
    print(hex(main(0x988dba6a)))

"""
# Вариант 40
def main_40(x):
    a = x & 0b1111_1111_1111_11 #binary
    b = (x >> 15) & 0b1111_1111_1
    c = (x >> 24) & 0b1111_111
    d = (x >> 31) & 0b1
    result = c | (a << 7) | (b << 22) | (d << 31)
    return result

print(hex(main_40(0xe6e16978)))

# Вариант 15
def main_15(x):
    a = x & 0b1111_1111_1111_111
    b = (x >> 15) & 0b1111_1111_1111_1
    c = (x >> 28) & 0b1
    d = (x >> 29) & 0b1
    e = (x >> 30) & 0b1
    f = (x >> 31) & 0b1
    result = c | (a << 1) | (b << 17) | (d << 30) | (e << 16) | (f << 31)
    return result


hex(main_15(0x8c14d656))
"""
