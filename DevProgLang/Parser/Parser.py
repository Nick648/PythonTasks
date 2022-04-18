import sys

# sys.path.insert(1, '../Lexer')
# from Lex import *
from functools import reduce
from typing import List

from DevProgLang.Lexer import lex, openfile, RESERVED, INT, ID, token_exprs


class Equality:
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)


class Result:
    def __init__(self, value, pos):
        self.value = value
        self.pos = pos

    def __repr__(self):
        return 'Result(%s, %d)' % (self.value, self.pos)


class Parser:
    def __add__(self, other):  # +
        return Concat(self, other)

    def __mul__(self, other):  # *
        return Exp(self, other)

    def __or__(self, other):  # |
        return Alternate(self, other)

    def __xor__(self, function):  # ^
        return Process(self, function)


class Tag(Parser):
    def __init__(self, tag):
        self.tag = tag

    def __call__(self, tokens, pos):
        if pos < len(tokens) and tokens[pos][1] is self.tag:
            return Result(tokens[pos][0], pos + 1)
        else:
            return None


class Reserved(Parser):
    def __init__(self, value, tag):
        self.value = value
        self.tag = tag

    def __call__(self, tokens, pos):
        if pos < len(tokens) and tokens[pos][0] == self.value and tokens[pos][1] is self.tag:
            return Result(tokens[pos][0], pos + 1)
        else:
            return None


class Concat(Parser):
    def __init__(self, left, right):
        # print("Concat left right:", left, right)
        self.left = left
        self.right = right
        self.__call__(token_exprs, 0)

    def __call__(self, tokens, pos):
        left_result = self.left(tokens, pos)
        if left_result:
            right_result = self.right(tokens, left_result.pos)
            if right_result:
                combined_value = (left_result.value, right_result.value)
                return Result(combined_value, right_result.pos)
        return None


class Exp(Parser):
    def __init__(self, parser, separator):
        self.parser = parser
        self.separator = separator

    def __call__(self, tokens, pos):
        result = self.parser(tokens, pos)

        def process_next(parsed):
            (sepfunc, right) = parsed
            return sepfunc(result.value, right)

        next_parser = self.separator + self.parser ^ process_next

        next_result = result
        while next_result:
            next_result = next_parser(tokens, result.pos)
            if next_result:
                result = next_result
        return result


class Alternate(Parser):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __call__(self, tokens, pos):
        left_result = self.left(tokens, pos)
        if left_result:
            return left_result
        else:
            right_result = self.right(tokens, pos)
            return right_result


class Opt(Parser):
    def __init__(self, parser):
        self.parser = parser

    def __call__(self, tokens, pos):
        result = self.parser(tokens, pos)
        if result:
            return result
        else:
            return Result(None, pos)


class Rep(Parser):
    def __init__(self, parser):
        self.parser = parser

    def __call__(self, tokens, pos):
        results = []
        result = self.parser(tokens, pos)
        while result:
            results.append(result.value)
            pos = result.pos
            result = self.parser(tokens, pos)
        return Result(results, pos)


class Process(Parser):
    def __init__(self, parser, function):
        self.parser = parser
        self.function = function

    def __call__(self, tokens, pos):
        result = self.parser(tokens, pos)
        if result:
            result.value = self.function(result.value)
            return result


class Lazy(Parser):
    def __init__(self, parser_func):
        self.parser = None
        self.parser_func = parser_func

    def __call__(self, tokens, pos):
        if not self.parser:
            self.parser = self.parser_func()
        return self.parser(tokens, pos)


class Phrase(Parser):
    def __init__(self, parser):
        self.parser = parser

    def __call__(self, tokens, pos):
        result = self.parser(tokens, pos)
        if result and result.pos == len(tokens):
            return result
        else:
            return None



parser = Concat(Concat(Tag(INT), Reserved('+', RESERVED)), Tag(INT))
print('1', parser)
parser = Tag(INT) + Reserved('+', RESERVED) + Tag(INT)
print('2', parser)
parser = Reserved('+', RESERVED) | Reserved('-', RESERVED) | Reserved('*', RESERVED) | Reserved('/', RESERVED)
print('3', parser)

# Top level parser
def imp_parse(tokens):
    ast = parser()(tokens, 0)
    return ast


if __name__ == '__main__':
    # filename = (input("Filename: ")).strip()
    filename = 'code'
    filename = openfile(filename)
    file = open(filename)
    characters = file.read()
    file.close()
    tokens = lex(characters)
    # parser = Parser()
    parser = globals()
    #aexp()  # [sys.argv[2]]
    result = parser
    print(result)
