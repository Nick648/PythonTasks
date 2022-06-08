# Вариант 9

def main(x):
    if x[3] == 2004:
        return x0_1_1(x)
    elif x[3] == 2009:
        return x0_1_2(x)
    elif x[3] == 2001:
        return 12


def x0_1_1(x):
    if x[0] == 'OX':
        return x1_2(x)
    elif x[0] == 'SCALA':
        return x2_2_1(x)
    elif x[0] == 'SHELL':
        return 6


def x0_1_2(x):
    if x[0] == 'OX':
        return x2_2_2(x)
    elif x[0] == 'SCALA':
        return 10
    elif x[0] == 'SHELL':
        return 11


def x1_2(x):
    if x[1] == 1988:
        return 0
    elif x[1] == 1994:
        return 1
    elif x[1] == 1962:
        return 2


def x2_2_1(x):
    if x[2] == 'SQL':
        return 3
    elif x[2] == 'AGDA':
        return 4
    elif x[2] == 'HAML':
        return 5


def x2_2_2(x):
    if x[2] == 'SQL':
        return 7
    elif x[2] == 'AGDA':
        return 8
    elif x[2] == 'HAML':
        return 9


main(['OX', 1994, 'SQL', 2009])

# For CAP, you only need what is above, having checked in advance for PEP8

if __name__ == "__main__":
    print('Res 1:', main(['OX', 1994, 'SQL', 2009]))
    print('Res 2:', main(['SCALA', 1962, 'HAML', 2001]))
    print("\n", "-" * 20, "Done!", "-" * 20)
