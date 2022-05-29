# package DevProgLang/Main.py
from DevProgLang import *

if __name__ == '__main__':
    # SyntaxError: invalid syntax
    # print(eval("12 + (6+2*4) / 7 -2")) !
    # filename = (input("Filename: ")).strip()
    filename = "code"  # DELETE
    filename = openfile(filename)
    file = open(filename)
    characters = file.read()  # str
    file.close()
    tokens = lexer(characters)  # list
    print('Tokens:')  # , tokens Tokens: [('5', 'INT'), ('+', 'PLUS_OP'),...
    # for token in tokens:
    #     print(">>>", token)
    print('\nLexer Done!\n')

    parser = parser(tokens)
    # tree = parser.parse()
