from Lex import *

if __name__ == '__main__':
    filename = (input("Filename: ")).strip()
    filename = openfile(filename)
    # filename = sys.argv[1]
    file = open(filename)
    characters = file.read()  # str
    file.close()
    tokens = imp_lex(characters)  # list
    print('Tokens:')
    for token in tokens:
        print(">>>", token)
    print('\nDone!')
