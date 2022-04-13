def in2(a):
    n = ''
    k = ''
    while a > 0:
        n = n + str(a % 2)
        a = a // 2
    n =  list(reversed(n))
    for j in range(len(n)):
        k += n[j]
    return k


def in10(a, n):
    a = str(a)
    k = 0
    for i in range(len(a)):
        k += int(a[len(a) - i - 1]) * int(n ** i)
    return k

x = int(input())
y1 = in2(x)
z1 = in10(y1, 2)
y = bin(x)
z = hex(x)
print(x, y, z, y1, z1, sep='\n')
