# package DevProgLang/Lexer/Main.py
from DevProgLang import *
from DevProgLang.parser import Parser

if __name__ == '__main__':
    filename = (input("Filename: ")).strip()
    filename = openfile(filename)
    # filename = sys.argv[1]
    file = open(filename)
    characters = file.read()  # str
    file.close()
    tokens = lex(characters)  # list
    print('Tokens:', tokens)  # Tokens: [('5', 'INT'), ('+', 'PLUS_OP'),...
    # for token in tokens:
    #     print(">>>", token)
    print('\nLexer Done!')

    parser = Parser(tokens)
    tree = parser.parse()
