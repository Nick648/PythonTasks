'''
Задача 1

Приведите примеры кода, которые соответствуют следующим нарушениям PEP 8:

1. whitespace before '('.
2. missing whitespace around operator.
3. missing whitespace after ','.
4. unexpected spaces around keyword / parameter equals.
5. expected 2 blank lines, found 1.
6. multiple statements on one line (colon).
7. multiple statements on one line (semicolon).
8. comparison to None should be 'if cond is None:'.
9. comparison to True should be 'if cond is True:' or 'if cond:'.

Для быстрой проверки используйте сайт pep8online.com.
'''
############ №1
def main (x):
    print(x)

main(1)

############ №2
def main(x):
    y=2*x
    print(y)

main(1)

############ №3
def main(x,y):
    print(x + y)

main(1, 2)

############ №4
print(4, end = ' ')

############ №5
import math

def main(num):
    print(num)

main(5)

############ №6
style: str = "6"

############ №7
x = 6; str = "7"

############ №8
def main(x):
    if x == None:
        print("x is equal to None")

main(8)

############ №9
def main(x):
    if x == True:
        print("x is equal to None")

main(9)