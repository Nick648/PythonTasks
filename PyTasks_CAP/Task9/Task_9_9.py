# Вариант 9

class Miles:
    def __init__(self):
        self._state = 'A'
        self._graph = {
            ('A', 'chalk'): ('B', 0),
            ('A', 'leer'): ('C', 1),
            ('B', 'chalk'): ('C', 2),
            ('B', 'leer'): ('G', 3),
            ('C', 'chalk'): ('D', 4),
            ('C', 'leer'): ('F', 5),
            ('D', 'leer'): ('E', 6),
            ('E', 'leer'): ('F', 7),
            ('F', 'chalk'): ('G', 8),
            ('G', 'chalk'): ('A', 9),
        }

    def chalk(self):
        self._state, ret_value = self._graph[(self._state, 'chalk')]
        return ret_value

    def leer(self):
        self._state, ret_value = self._graph[(self._state, 'leer')]
        return ret_value


def main():
    return Miles()


o = main()


# For CAP, you only need what is above, having checked in advance for PEP8

def str_raz(ob, s_input):
    list_s = s_input.split(' ')  # s_input.split(' ')
    for item in list_s:
        item.strip()
        if '.chalk()' in item or '.chalk' in item or 'chalk()' in item or 'chalk' in item:
            print(ob.chalk())
        elif '.leer()' in item or '.leer' in item or 'leer()' in item or 'leer' in item:
            print(ob.leer())


inp_1 = 'o.leer() # 1\
o.chalk() # 4\
o.leer() # 6\
o.leer() # 7\
o.chalk() # 8\
o.chalk() # 9\
o.chalk() # 0\
o.leer() # 3\
o.chalk() # 9\
o.chalk() # 0\
o.chalk() # 2\
o.leer() # 5\
o.chalk() # 8'

inp_2 = 'o.chalk() # 0\
o.leer() # 3\
o.chalk() # 9\
o.leer() # 1\
o.chalk() # 4\
o.leer() # 6\
o.leer() # 7\
o.leer() # KeyError\
o.chalk() # 8\
o.chalk() # 9\
o.chalk() # 0\
o.chalk() # 2\
o.leer() # 5\
o.chalk() # 8\
o.chalk() # 9'

if __name__ == "__main__":
    print("Results:\n")
    o1 = main()
    o2 = main()
    print("Res 1:")
    str_raz(o1, inp_1)
    print("\nRes 2:")
    str_raz(o2, inp_2)
