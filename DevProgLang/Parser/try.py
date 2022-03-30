import sys
import os

from DevProgLang.Lexer import openfile, lex, RESERVED

# sys.path.insert(1, '../Lexer')
# from Lex import *
'''
#Create new directory
if not os.path.exists('test_dir'):
    os.mkdir('test_dir')
#ls(Linux) directory
os.listdir(os.getcwd())
print(os.path.exists('../Lexer/Lex.py')))
filename = os.path.abspath('../Lexer/data/code.txt')
'''
# print(f'Current Working Directory is: {os.getcwd()}')

filename = 'code.txt'
print(RESERVED)
filename = openfile(filename)
file = open(filename)
characters = file.read()  # str
file.close()
tokens = lex(characters)  # list
for t in tokens:
    print(">" * 3, t, type(t))
    print(">" * 3, t[0], t[1], type(t[0]), type(t[1]))

print('\n')

import ast


class MyOptimizer(ast.NodeTransformer):

    def visit_Name(self, node: ast.Name):
        if node.id == 'pi':
            result = ast.Num(n=3.14159265)
            result.lineno = node.lineno
            result.col_offset = node.col_offset
            return result
        return node


tree = ast.parse("print(2 * pi)")
optimizer = MyOptimizer()
tree = optimizer.visit(tree)
code = compile(tree, "<string>", "exec")
exec(code)

class MyVisitor(ast.NodeTransformer):

    def visit_BinOp(self, node: ast.BinOp):
        node.left = self.visit(node.left)
        node.right = self.visit(node.right)
        if isinstance(node.left, ast.Num) and isinstance(node.right, ast.Num):
            if isinstance(node.op, ast.Add):
                result = ast.Num(n=node.left.n + node.right.n)
                return ast.copy_location(result, node)
            elif isinstance(node.op, ast.Mult):
                result = ast.Num(n=node.left.n * node.right.n)
                return ast.copy_location(result, node)
        return node

    def visit_Name(self, node: ast.Name):
        if node.id == 'pi':
            result = ast.Num(n=3.14159265)
            return ast.copy_location(result, node)
        return node


tree = ast.parse("y = 2 * pi + 1")
optimizer = MyOptimizer()
tree = optimizer.visit(tree)
print(ast.dump(tree))
