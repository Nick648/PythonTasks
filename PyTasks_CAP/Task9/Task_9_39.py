# Вариант 39
class Miles:
    def __init__(self):
        self.state = 'A'
        self.graph = {
            ('A', 'mix'): ('A', 1),
            ('A', 'jog'): ('B', 0),
            ('A', 'smash'): ('C', 2),
            ('B', 'jog'): ('B', 4),
            ('B', 'smash'): ('C', 3),
            ('C', 'mix'): ('D', 5),
            ('D', 'jog'): ('E', 6),
            ('E', 'smash'): ('F', 7),
            ('F', 'jog'): ('D', 8)
        }

    def mix(self):
        self.state, res = self.graph[(self.state, 'mix')]
        return res

    def jog(self):
        self.state, res = self.graph[(self.state, 'jog')]
        return res

    def smash(self):
        self.state, res = self.graph[(self.state, 'smash')]
        return res


def main():
    return Miles()


o = main()


# For CAP, you only need what is above, having checked in advance for PEP8

def str_raz(ob, s_input):
    list_s = s_input.split(' ')
    for item in list_s:
        item.strip()
        if '.mix()' in item or '.mix' in item or 'mix()' in item or 'mix' in item:
            print(ob.mix())
        elif '.jog()' in item or '.jog' in item or 'jog()' in item or 'jog' in item:
            print(ob.jog())
        elif '.smash()' in item or '.smash' in item or 'smash()' in item or 'smash' in item:
            print(ob.smash())


inp_1 = 'o = main() \
o.mix() # 1 \
o.mix() # 1 \
o.jog() # 0 \
o.jog() # 4 \
o.jog() # 4 \
o.smash() # 3 \
o.mix() # 5 \
o.jog() # 6 \
o.mix() # KeyError \
o.smash() # 7 \
o.jog() # 8 \
o.mix() # KeyError \
o.jog() # 6'

inp_2 = 'o = main() \
o.mix() # 1 \
o.mix() # 1 \
o.jog() # 0 \
o.jog() # 4 \
o.smash() # 3 \
o.jog() # KeyError \
o.mix() # 5 \
o.jog() # 6 \
o.mix() # KeyError \
o.smash() # 7 \
o.jog() # 8 \
o.jog() # 6 \
o.smash() # 7'

if __name__ == "__main__":
    print("Results:\n")
    o1 = main()
    o2 = main()
    print("Res 1:")
    str_raz(o1, inp_1)
    print("\nRes 2:")
    str_raz(o2, inp_2)
