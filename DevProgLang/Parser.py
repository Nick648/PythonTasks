vars_value = dict()
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.line = 1
    def error(self, s):
        print("SyntaxError: invalid syntax")
        print("In line", self.line, "expected:", s, "in pos", self.pos)
        exit(1)
    def parse(self):
        pass

def parser(tokens):
    pos, line = 0, 1
    for i in range(len(tokens)):
        if tokens[i][1] == "NEWLINE" or tokens[i][0] == "exit":
            if tokens[pos:i]:
                token_line = tokens[pos:i]
                parse_line(token_line, line)
            pos = i + 1
            line += 1


def parse_line(token_line, line):
    print(f"line = {line}")
    print(token_line)
