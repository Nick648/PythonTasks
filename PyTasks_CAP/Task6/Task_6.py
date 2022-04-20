# Вариант 18

def main(x):
    if x[1] == 1970:
        return x2_2(x)
    elif x[1] == 2006:
        return x0_2(x)
    elif x[1] == 2008:
        return 10


def x2_2(x):
    if x[2] == 'GLYPH':
        return x3_3_1(x)
    elif x[2] == 'BLADE':
        return x0_3(x)


def x3_3_1(x):
    if x[3] == 'CLICK':
        return 0
    elif x[3] == 'CLEAN':
        return 1
    elif x[3] == 'DIFF':
        return 2


def x0_3(x):
    if x[0] == 'XSLT':
        return 3
    elif x[0] == 'STATA':
        return 4


def x0_2(x):
    if x[0] == 'XSLT':
        return x2_3(x)
    elif x[0] == 'STATA':
        return x3_3_2(x)


def x2_3(x):
    if x[2] == 'GLYPH':
        return 5
    elif x[2] == 'BLADE':
        return 6


def x3_3_2(x):
    if x[3] == 'CLICK':
        return 7
    elif x[3] == 'CLEAN':
        return 8
    elif x[3] == 'DIFF':
        return 9


main(['STATA', 1970, 'GLYPH', 'CLICK'])
