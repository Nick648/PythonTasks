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
def main_1 (x):
    print(x)

main_1(1)

############ №2
def main_2(x):
    y=2*x
    print(y)

main_2(1)

############ №3
def main_3(x,y):
    print(x + y)

main_3(1, 2)

############ №4
print(4, end = ' ')

############ №5
import math

def main_5(num):
    print(num)

main_5(5)

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