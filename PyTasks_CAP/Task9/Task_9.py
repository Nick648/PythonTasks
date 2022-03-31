class Mili():
    def __init__(self):
        self.__pos = 'A'

    def getpos(self):
        return self.__pos

    def slur(self):
        if self.__pos == 'A':
            self.__pos = 'B'
            return 0  # '-> ' + str(0)
        elif self.__pos == 'C':
            self.__pos = 'G'
            return 5  # '-> ' + str(0)
        elif self.__pos == 'D':
            self.__pos = 'E'
            return 6  # '-> ' + str(0)
        elif self.__pos == 'E':
            self.__pos = 'F'
            return 7  # '-> ' + str(0)
        elif self.__pos == 'F':
            self.__pos = 'G'
            return 8  # '-> ' + str(0)
        elif self.__pos == 'G':
            self.__pos = 'G'
            return 9  # '-> ' + str(0)
        elif self.__pos == 'B':
            self.__pos = 'F'
            return 3  # '-> ' + str(0)
        else:
            return 'KeyError'

    def hop(self):
        if self.__pos == 'B':
            self.__pos = 'C'
            return 2  # '-> ' + str(0)
        elif self.__pos == 'C':
            self.__pos = 'D'
            return 4  # '-> ' + str(0)
        elif self.__pos == 'A':
            self.__pos = 'F'
            return 1  # '-> ' + str(0)
        else:
            return 'KeyError'


def main():
    return Mili()


o = main()
o.slur()
o.hop()
o.hop()
o.hop()
o.slur()
o.hop()
o.slur()
o.slur()
o.slur()
o.slur()
o.slur()
o.slur()
o.slur()
o.slur()

'''
def r_1():
    print('r_1')
    o = main()
    ap1 = [
        o.slur(),
        o.hop(),
        o.hop(),
        o.hop(),
        o.slur(),
        o.hop(),
        o.slur(),
        o.slur(),
        o.slur(),
        o.slur(),
        o.slur(),
        o.slur(),
        o.slur(),
        o.slur()
    ]
    for i1 in ap1:
        print(i1)
    for i1 in ap1:
        res1 = i1


def r_2():
    print('r_2')
    o = main()
    ap2 = [
        o.slur(),
        o.hop(),
        o.hop(),
        o.slur(),
        o.slur(),
        o.hop(),
        o.slur(),
        o.slur(),
        o.slur(),
        o.slur(),
        o.slur(),
        o.hop(),
        o.slur(),
        o.slur()
    ]
    for i2 in ap2:
        print(i2)
    for i2 in ap2:
        res2 = i2


r_1()
r_2()
'''
