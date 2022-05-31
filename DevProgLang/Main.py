# package DevProgLang/Main.py
from DevProgLang import *


def work_lex_out(tokens):
    line = 1
    print('Tokens:\nLine = 1:')
    for token in tokens:
        if token.getNumberLine() != line:
            line = token.getNumberLine()
            print(f"Line = {line}:")
        # print(">>>", token)
        token.toString()


# print(eval("12 + (6+2*4) / 7 -2"))

if __name__ == '__main__':
    # filename = (input("Filename: ")).strip()
    filename = "code"  # DELETE !
    filename = openfile(filename)
    file = open(filename)
    code = file.read()  # str
    file.close()
    tokens = lexer(code)  # list of objects
    # work_lex_out(tokens)  # Out lexer

    print('\nLexer Done!\n')

    parser = Parser(tokens)  # Object for parsing
    parser.parse()  # Start parsing for search nodes
    # node_list = parser.getNodeList()  # Get list of nodes
