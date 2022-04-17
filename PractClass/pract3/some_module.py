global GLOBAL_VAR
GLOBAL_VAR = 1

def func_1():
    print('Its func_1')

if __name__ == "__main__":
    def func_2():
        print('Its func_2')

    print(GLOBAL_VAR)