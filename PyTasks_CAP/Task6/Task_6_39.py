# вариант 39

def x0_3(x):
    if x[0] == 'MQL5':
        return 8
    if x[0] == 'DM':
        return 9


def x1_3(x):
    if x[1] == 'VOLT':
        return 0
    if x[1] == 'LEX':
        return 1
    if x[1] == 'NGINX':
        return 2


def x1_3_2(x):
    if x[1] == 'VOLT':
        return 3
    if x[1] == 'LEX':
        return 4
    if x[1] == 'NGINX':
        return 5


def x1_2(x):
    if x[1] == 'VOLT':
        return 7
    if x[1] == 'LEX':
        return x0_3(x)
    if x[1] == 'NGINX':
        return 10


def x0_2(x):
    if x[0] == 'MQL5':
        return x1_3(x)
    if x[0] == 'DM':
        return x1_3_2(x)


def begin(x):
    if x[2] == 1978:
        return x0_2(x)
    if x[2] == 1962:
        return 6
    if x[2] == 1975:
        return x1_2(x)


def main(x):
    return begin(x)


main(['MQL5', 'VOLT', 1978, 1965])

# For CAP, you only need what is above, having checked in advance for PEP8

if __name__ == '__main__':
    print("\nResults:")
    res = [
        main(['MQL5', 'VOLT', 1978, 1965]),
        main(['DM', 'LEX', 1962, 1965]),
        main(['MQL5', 'LEX', 1975, 1965]),
        main(['DM', 'VOLT', 1978, 2004]),
        main(['MQL5', 'LEX', 1978, 2004])
    ]
    for i in range(len(res)):
        print(f"Res {i + 1}: {res[i]}", )
    print("\n", "-" * 20, "Done!", "-" * 20)
