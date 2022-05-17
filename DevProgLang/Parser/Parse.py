from DevProgLang import lex, openfile


def par(line):
    print("Line:")
    print(line)

def par_line(tokens):
    pos = 0
    for i in range(len(tokens)):
        if tokens[i][1] == 'NEWLINE':
            par(tokens[pos:i])
            pos = i + 1
    print('\nDone!')

if __name__ == '__main__':
    filename = (input("Filename: ")).strip()
    filename = 'code'
    filename = openfile(filename)
    # filename = sys.argv[1]
    file = open(filename)
    characters = file.read()  # str
    file.close()
    tokens = lex(characters)  # list
    par_line(tokens)
    print('Tokens:')  # Tokens: [('5', 'INT'), ('+', 'PLUS_OP'),...
    for token in tokens:
        print(">>>", token)
    print('\nDone!')
