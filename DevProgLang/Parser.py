import Errors
from Nodes import *


def check_brackets(line):  # Static check brackets
    flag_1, flag_2, flag_3 = 0, 0, 0
    for elem in line:
        if elem.getTypeToken() == "L_BRACKET":
            flag_1 += 1
        if elem.getTypeToken() == "R_BRACKET":
            flag_1 -= 1
        if elem.getTypeToken() == "L_BRACE":
            flag_2 += 1
        if elem.getTypeToken() == "R_BRACE":
            flag_2 -= 1
        if elem.getTypeToken() == "L_SQUARE_BRACKET":
            flag_3 += 1
        if elem.getTypeToken() == "R_SQUARE_BRACKET":
            flag_3 -= 1
    if flag_1 != 0:
        Errors.NotSymbol(")", line)
    if flag_2 != 0:
        Errors.NotSymbol("}", line)
    if flag_3 != 0:
        Errors.NotSymbol("]", line)


class Parser:

    def __init__(self, tokens):  # Constructor
        self.kod = list()
        self.tokens = tokens
        self.node_list = list()
        self.split_on_lines()

    def split_on_lines(self):  # Division into lines of code
        pos = 0
        for i in range(len(self.tokens)):
            if self.token_type(i, "NEWLINE") or self.token_type(i, "KW_EXIT"):
                if self.tokens[pos:i]:
                    self.kod.append(self.tokens[pos:i])
                pos = i + 1

    def token_type(self, pos, typ):  # Token comparison
        # print(self.tokens[pos].getTypeToken(), "?", typ)
        if self.tokens[pos].getTypeToken() == typ:
            return True
        return False

    def parse(self):
        for ii in range(len(self.kod)):  # Lines of code
            line = self.kod[ii]
            check_brackets(line)
            print("line:", line)
            if line[-1].getTypeToken() != "SEMICOLON":
                Errors.NotSymbol(';', ii + 1)

            if line[0].getTypeToken() == "VAR" and line[1].getTypeToken() == "ASSIGN":
                self.node_list.append(self.setAssign(line))
            elif line[0].getTypeToken() == "KW_PRINT":
                self.node_list.append(self.setPrint(line))
            elif line[0].getTypeToken() == "KW_IF":
                self.node_list.append(self.setIf(line))
            elif line[0].getTypeToken() == "KW_WHILE":
                self.node_list.append(self.setWhile(line))
            elif line[0].getTypeToken() == "KW_LIST":
                self.node_list.append(self.setLinkedList(line))
            elif line[1].getTypeToken() == "LL_INSERT_END":
                self.node_list.append(self.setLLInsertAtEnd(line))
            elif line[1].getTypeToken() == "LL_INSERT_HEAD":
                self.node_list.append(self.setLLInsertAtHead(line))
            elif line[1].getTypeToken() == "LL_DELETE":
                self.node_list.append(self.setLLDelete(line))
            elif line[1].getTypeToken() == "LL_DELETE_HEAD":
                self.node_list.append(self.setLLDeleteAtHead(line))
            elif line[1].getTypeToken() == "LL_SEARCH":
                self.node_list.append(self.setLLSearch(line))
            elif line[1].getTypeToken() == "LL_IS_EMPTY":
                self.node_list.append(self.setLLIsEmpty(line))
            else:
                Errors.FalseKod(ii + 1)
        return self.node_list

    def setAssign(self, line):
        print("setAssign:", line)
        name_variable = line[0].getValue()
        print("name_variable:", name_variable)
        value = line[2:len(line) - 1]
        print("value:", value)
        if len(value) == 1:
            type_token = value[0].getTypeToken()
            if type_token == "INT" or type_token == "VAR" or type_token == "FLOAT":
                return AssignNode("ASSIGN", name_variable, value, type_token)
        else:
            if len(value) == 3:
                return AssignNode("Assign", name_variable, self.setOperation(value), "Operation")
            else:
                return AssignNode("Assign", name_variable, self.setOperation(value), "OperationHard")

    def setPrint(self, line):
        value = line[2:len(line) - 2]
        if len(value) == 1:
            type_value = value[0].getTypeToken()
            if type_value == "INT":
                return PrintNode("Print", int(value), type_value)
                # self.node_list.append(PrintNode("Print", value, type_value))
            elif type_value == "VAR":
                return PrintNode("Print", value, type_value)
                # self.node_list.append(PrintNode("Print", value, type_value))
            else:
                pass
        else:
            pass

    def setIf(self, line):
        flag = 1
        condition = list()
        loop = list()
        line_kod = list()
        for elem in line:
            if flag == 1 and elem.getValue() == "(":
                flag = 2
            elif flag == 2:
                if elem.getValue() == ")":
                    flag = 3
                    continue
                condition.append(elem)
            elif flag == 3 and elem.getValue() == "{":
                flag = 4
            elif flag == 4:
                if elem.getValue() == "}":
                    flag = 5
                    continue
                    #############################################
                line_kod.append(elem)
                if elem.getValue() == ";":
                    loop.append(line_kod)
                    line_kod = list()
        ready_loop = list()
        for line in loop:
            if line[0].getTypeToken() == "VAR" and line[1].getTypeToken() == "ASSIGNMENT":
                ready_loop.append(self.setAssign(line))
            elif line[0].getTypeToken() == "PRINT_TRIGGER":
                ready_loop.append(self.setPrint(line))
            else:
                print("ERROR")

        # print([elem.getValue() for elem in condition])
        # print(ready_loop[0].getValue()[0].getValue())
        return IfNode("If", condition, ready_loop)

    def setWhile(self, line):
        flag = 1
        condition = list()
        loop = list()
        line_kod = list()
        for elem in line:
            if flag == 1 and elem.getValue() == "(":
                flag = 2
            elif flag == 2:
                if elem.getValue() == ")":
                    flag = 3
                    continue
                condition.append(elem)
            elif flag == 3 and elem.getValue() == "{":
                flag = 4
            elif flag == 4:
                if elem.getValue() == "}":
                    flag = 5
                    continue

                line_kod.append(elem)
                if elem.getValue() == ";":
                    loop.append(line_kod)
                    line_kod = list()
        ready_loop = list()
        # print([elem.getValue() for elem in loop[0]])
        for line in loop:
            if line[0].getTypeToken() == "VAR" and line[1].getTypeToken() == "ASSIGNMENT":
                ready_loop.append(self.setAssign(line))
            elif line[0].getTypeToken() == "PRINT_TRIGGER":
                ready_loop.append(self.setPrint(line))
            else:
                print("ERROR")

        # print([elem.getValue() for elem in condition])
        # print(ready_loop[1])
        return WhileNode("While", condition, ready_loop)

    def setOperation(self, value):
        if len(value) == 3:
            left_operand = value[0]
            sign = value[1]
            right_operand = value[2]
            return OperationNode("Operation", left_operand, right_operand, sign, final=True)
        else:
            condition = [elem.getValue() for elem in value]
            return OperationNode("Operation", value, None, None, final=False)

    def setLinkedList(self, line):
        name_linked_list = line[1].getValue()
        values = line[4:len(line) - 2]
        new_values = list()
        for elem in values:
            if elem.getTypeToken() != "VIRGULE":
                new_values.append(elem)
        return LinkedListNode("LinkedList", name_linked_list, new_values)

    def setLLInsertAtEnd(self, line):
        name_variable = line[0].getValue()
        value = line[3]
        return LinkedListOperatioinNode("LinkedListOperationNode", "setLLInsertAtEnd", name_variable, value)

    def setLLInsertAtHead(self, line):
        name_variable = line[0].getValue()
        value = line[3]
        return LinkedListOperatioinNode("LinkedListOperationNode", "setLLInsertAtHead", name_variable, value)

    def setLLDelete(self, line):
        name_variable = line[0].getValue()
        value = line[3]
        return LinkedListOperatioinNode("LinkedListOperationNode", "setLLDelete", name_variable, value)

    def setLLDeleteAtHead(self, line):
        name_variable = line[0].getValue()
        return LinkedListOperatioinNode("LinkedListOperationNode", "setLLDeleteAtHead", name_variable, None)

    def setLLSearch(self, line):
        name_variable = line[0].getValue()
        value = line[3]
        return LinkedListOperatioinNode("LinkedListOperationNode", "setLLSearch", name_variable, value)

    def setLLIsEmpty(self, line):
        name_variable = line[0].getValue()
        return LinkedListOperatioinNode("LinkedListOperationNode", "setLLIsEmpty", name_variable, None)

    def getNodeList(self):
        return self.node_list

    '''
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.line = 1
        self.vars_name = list()
        self.func_name = list()

    def error(self, s):
        print("SyntaxError: invalid syntax")
        print("In line", self.line, "expected:", s, "in pos", self.pos)
        exit(1)

    def token_type(self, pos, typ):
        print(self.tokens[pos][1], "?", typ)
        if self.tokens[pos][1] == typ:
            return True
        return False

    def parse(self):
        for i in range(len(self.tokens)):
            if self.token_type(i, "NEWLINE") or self.token_type(i, "KW_EXIT"):
                if self.tokens[self.pos:i]:
                    token_line = self.tokens[self.pos:i]
                    self.parse_line(token_line)
                self.pos = i + 1
                self.line += 1

    def parse_line(self, token_line):
        print(f"line = {self.line}; {token_line}")
        if self.token_type(0, "KW_IF"):
            self.parse_if(token_line)

    def parse_if(self, token_line):
        pass

    '''
