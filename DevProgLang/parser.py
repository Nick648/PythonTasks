from nodes import *


class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.advance()

    def raise_error(self):
        raise Exception("Invalid syntax")

    def advance(self):
        try:
            self.current_token = next(self.tokens)
            print("current_token:", self.current_token)
        except StopIteration:
            self.current_token = None

    def parse(self):
        if self.current_token == None:
            return None

        result = self.expr()  # поместим метод expr в собственный метод

        if self.current_token != None:
            self.raise_error()

        return result

    def expr(self):
        result = self.term()

        while self.current_token[1] != None and self.current_token[1] in ["PLUS_OP", "MINUS_OP"]:
            if self.current_token[1] == "PLUS_OP":
                self.advance()
                result = AddNode(result, self.term())
            elif self.current_token[1] == "MINUS_OP":
                self.advance()
                result = SubtractNode(result, self.term())

        return result

    def term(self):
        result = self.factor()

        while self.current_token[1] != None and self.current_token[1] in ["MULTIPLICATION_OP", "SLASH"]:
            if self.current_token[1] == "MULTIPLICATION_OP":
                self.advance()
                result = MultiplyNode(result, self.factor())
            elif self.current_token[1] == "SLASH":
                self.advance()
                result = DivideNode(result, self.factor())

        return result

    def factor(self):
        token = self.current_token
        print(token)

        if token[1] == "L_BRACKET":
            self.advance()
            result = self.expr()

            if self.current_token[1] != "R_BRACKET":
                self.raise_error()

            self.advance()
            return result

        elif token[1] == "INT":
            self.advance()
            return NumberNode(int(token[0]))

        elif token[1] == "PLUS_OP":
            self.advance()
            return PlusNode(self.factor())

        elif token[1] == "MINUS_OP":
            self.advance()
            return MinusNode(self.factor())
        else:
            return None
        self.raise_error()
