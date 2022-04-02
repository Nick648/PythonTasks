ast = Add(Num(7), Mul(Num(3), Num(2)))
pv = PrintVisitor()
cv = CalcVisitor()
sv = StackVisitor()
print(pv.visit(ast))
print(cv.visit(ast))
sv.visit(ast)
print(sv.get_code())

'''
Результат:

(7 + (3 * 2))
13
PUSH 7
PUSH 3
PUSH 2
MUL
ADD
'''
