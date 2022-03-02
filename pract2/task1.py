def f1(s):
    return [int(x) for x in s]

def f2(s):
    return len(set(s))

def f3(s):
    return s[::-1]

def f4(s, x):
    return [index for index, el in enumerate(s) if el == x]

def f5(s):
    return sum(s[::2])

def f6(s):
    return max(s, key=len)


print("f1:", f1("03748211"))
print("f2:", f2("hello world"))
print("f3:", f3("reverse"))
print("f4:", f4("find something", 'i'))
print("f5:", f5([1,2,3,4,5,6,7,8,9,0]))
print("f6:", f6("Find max row, example this"))