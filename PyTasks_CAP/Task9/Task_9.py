class Mili:
    def __init__(self):
        self._state = 'A'
        self._graph = {
            ('A', 'slur'): ('B', 0),
            ('A', 'hop'): ('F', 1),
            ('B', 'hop'): ('C', 2),
            ('B', 'slur'): ('F', 3),
            ('C', 'hop'): ('D', 4),
            ('C', 'slur'): ('G', 5),
            ('D', 'slur'): ('E', 6),
            ('E', 'slur'): ('F', 7),
            ('F', 'slur'): ('G', 8),
            ('G', 'slur'): ('G', 9),
        }

    def slur(self):
        self._state, ret_value = self._graph[(self._state, 'slur')]
        return ret_value

    def hop(self):
        self._state, ret_value = self._graph[(self._state, 'hop')]
        return ret_value


def main():
    return Mili()


o = main()

'''
o = main()
o.slur()
o.hop()
o.hop()
# o.hop()
o.slur()
# o.hop()
o.slur()
o.slur()
o.slur()
o.slur()
o.slur()
o.slur()
o.slur()
o.slur()

o1 = main()


def str_raz(s_input):
    list_s = s_input.split(',')  # s_input.split(' ')
    for item in list_s:
        item.strip()
        if item == '.slur()' or item == '.slur' or item == 'slur()' or item == 'slur':
            o1.slur()
        elif item == '.hop()' or item == '.hop' or item == 'hop()' or item == 'hop':
            o1.hop()


s_input = 'slur(), \
hop(),\
hop(),\
*hop(),\
slur(),\
*hop(),\
slur(),\
slur(),\
slur(),\
slur(),\
slur(),\
slur(),\
slur(),\
slur()'

str_raz(s_input)


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
