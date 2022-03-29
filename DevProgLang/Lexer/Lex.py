import sys
import re
from Tokens import *


def lex(characters, token_exprs):
    pos = 0
    tokens = []
    while pos < len(characters):
        # print(">" * 10, pos)
        match = None
        for token_exp in token_exprs:
            pattern, tag = token_exp
            regex = re.compile(pattern)  # use reg
            match = regex.match(characters, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = (text, tag)
                    tokens.append(token)
                break
        if not match:
            sys.stderr.write('Illegal character: %s\n' % characters[pos])
            sys.exit(1)
        else:
            pos = match.end(0)  # new pos
    return tokens


# Is the file open?
def openfile(filename):
    if ".txt" not in filename:
        filename += ".txt"
    filename = 'data/' + filename
    try:
        with open(file=filename, mode='r', encoding='utf-8') as f:
            print('\nEverything is OK! The file is open!\n')
            return filename

    except:  # Error
        print("\nYou DON'T have a file with that name!\n")
        exit(1)


def imp_lex(characters):
    return lex(characters, token_exprs)  # lexer
