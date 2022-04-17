import sys

def my_print(*args, sep = ' ', end = '\n'):
    sys.stdout.write(sep.join(map(str, args)) + end)
    #sys.stdout.write(sep.join([str(x) for x in args]) + end)

my_print(1, 2, 3, '456', 0.0, sep='\n', end=' %%%')