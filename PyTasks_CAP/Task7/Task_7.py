'''
Вариант 40
'''
'''
def main(x):
    a = x & 0b1111_1111_1111_11 #binary
    b = (x >> 15) & 0b1111_1111_1
    c = (x >> 24) & 0b1111_111
    d = (x >> 31) & 0b1
    result = c | (a << 7) | (b << 22) | (d << 31)
    return result

print(hex(main(0xe6e16978)))

Вариант 15
def main(x):
    a = x & 0b1111_1111_1111_111
    b = (x >> 15) & 0b1111_1111_1111_1
    c = (x >> 28) & 0b1
    d = (x >> 29) & 0b1
    e = (x >> 30) & 0b1
    f = (x >> 31) & 0b1
    result = c | (a << 1) | (b << 17) | (d << 30) | (e << 16) | (f << 31)
    return result


hex(main(0x8c14d656))
'''


def main(x):
    a = x & 0b1111_1111_1111_1  # binary
    b = (x >> 13) & 0b1111_1111_1111_111
    c = (x >> 28) & 0b1
    d = (x >> 29) & 0b111
    result = c | (a << 16) | (b << 1) | (d << 29)
    return result


hex(main(0x988dba6a))
