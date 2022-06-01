import Errors
from Nodes import *


def check_brackets(line):  # Static check brackets
    if len(line) < 3 and line[-1].getTypeToken() != "COMMENT":
        k_line = line[-1].getNumberLine()
        Errors.FalseKod(k_line)
    if line[-1].getTypeToken() != "SEMICOLON" and line[-1].getTypeToken() != "COMMENT":  # ;
        k_line = line[-1].getNumberLine()
        Errors.NotSymbol(';', k_line)
    flag_1, flag_2, flag_3 = 0, 0, 0
    for elem in line:
        if elem.getTypeToken() == "L_BRACKET" and flag_1 > -1:
            flag_1 += 1
        if elem.getTypeToken() == "R_BRACKET":
            flag_1 -= 1
        if elem.getTypeToken() == "L_BRACE" and flag_2 > -1:
            flag_2 += 1
        if elem.getTypeToken() == "R_BRACE":
            flag_2 -= 1
        if elem.getTypeToken() == "L_SQUARE_BRACKET" and flag_3 > -1:
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

            if line[0].getTypeToken() == "VAR" and line[1].getTypeToken() == "ASSIGN":
                self.node_list.append(self.setAssign(line))
            elif line[0].getTypeToken() == "COMMENT":
                continue
            elif line[0].getTypeToken() == "KW_PRINT":
                self.node_list.append(self.setPrint(line))
            elif line[0].getTypeToken() == "KW_IF":
                self.node_list.append(self.set_If_While(line, "KW_IF"))
            elif line[0].getTypeToken() == "KW_WHILE":
                self.node_list.append(self.set_If_While(line, "KW_WHILE"))
            # elif line[0].getTypeToken() == "KW_FOR":
            #     self.node_list.append(self.setFor(line))
            elif line[0].getTypeToken() == "KW_LIST":
                self.node_list.append(self.setLinkedList(line))
            elif line[1].getTypeToken()[:3] == "LL_":
                self.node_list.append(self.set_LL_operation(line, line[1].getTypeToken()))
            # elif line[1].getTypeToken() == "LL_INSERT_END":
            #     self.node_list.append(self.setLLInsertAtEnd(line))
            # elif line[1].getTypeToken() == "LL_INSERT_HEAD":
            #     self.node_list.append(self.setLLInsertAtHead(line))
            # elif line[1].getTypeToken() == "LL_DELETE":
            #     self.node_list.append(self.setLLDelete(line))
            # elif line[1].getTypeToken() == "LL_DELETE_HEAD":
            #     self.node_list.append(self.setLLDeleteAtHead(line))
            # elif line[1].getTypeToken() == "LL_SEARCH":
            #     self.node_list.append(self.setLLSearch(line))
            # elif line[1].getTypeToken() == "LL_IS_EMPTY":
            #     self.node_list.append(self.setLLIsEmpty(line))
            else:
                Errors.FalseKod(ii + 1)
        # self.show_nodes()
        return self.node_list

    def setAssign(self, line):
        name_variable = line[0].getValue()
        value = line[2:len(line) - 1]
        if len(value) == 1:
            type_token = value[0].getTypeToken()
            if type_token == "INT" or type_token == "VAR" or type_token == "FLOAT":
                return AssignNode(name_variable, value, type_token)
        else:
            if len(value) == 3:
                return AssignNode(name_variable, self.setOperation(value), "Operation")
            else:
                return AssignNode(name_variable, self.setOperation(value), "OperationHard")

    def setPrint(self, line):
        value = line[1:len(line) - 1]
        if len(value) == 1:
            type_value = value[0].getTypeToken()
            if type_value == "INT":
                return PrintNode(int(value), type_value)
            elif type_value == "FLOAT":
                return PrintNode(float(value), type_value)
            elif type_value == "VAR":
                return PrintNode(value, type_value)
            else:
                Errors.FalseKod(line[0].getNumberLine())
        else:
            Errors.FalseKod(line[0].getNumberLine())

    def set_If_While(self, line, key_word):
        num_line = line[0].getNumberLine()
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
        for line in loop:
            if line[0].getTypeToken() == "VAR" and line[1].getTypeToken() == "ASSIGN":
                ready_loop.append(self.setAssign(line))
            elif line[0].getTypeToken() == "KW_PRINT":
                ready_loop.append(self.setPrint(line))
            else:
                Errors.FalseKod(num_line)

        # print([elem.getValue() for elem in condition])
        # print([elem.getTypeNode() for elem in ready_loop])
        if key_word == "KW_IF":
            return IfNode(condition, ready_loop)
        elif key_word == "KW_WHILE":
            return WhileNode(condition, ready_loop)

    def setOperation(self, value):
        if len(value) == 3:
            left_operand = value[0]
            sign = value[1]
            right_operand = value[2]
            return OperationNode(left_operand, right_operand, sign, final=True)
        else:
            condition = [elem.getValue() for elem in value]
            return OperationNode(value, None, None, final=False)

    def setLinkedList(self, line):
        name_linked_list = line[1].getValue()
        values = line[4:len(line) - 2]
        new_values = list()
        for elem in values:
            if elem.getTypeToken() != "COMMA":
                new_values.append(elem)
        return LinkedListNode(name_linked_list, new_values)

    def set_LL_operation(self, line, token_type):
        name_variable = line[0].getValue()
        flag, value = 1, 0
        digits = list()
        for elem in line:
            if flag == 1 and elem.getValue() == "(":
                flag = 2
            elif flag == 2:
                if elem.getValue() == ")":
                    break
                digits.append(elem)
        if len(digits) == 1:
            if digits[0].getTypeToken() == 'INT':
                value = digits[0]

        if token_type == 'LL_INSERT_END' and value != 0:
            return LinkedListOperatioinNode("setLLInsertAtEnd", name_variable, value)
        elif token_type == 'LL_INSERT_HEAD' and value != 0:
            return LinkedListOperatioinNode("setLLInsertAtHead", name_variable, value)
        elif token_type == 'LL_DELETE' and value != 0:
            return LinkedListOperatioinNode("setLLDelete", name_variable, value)
        elif token_type == 'LL_DELETE_HEAD':
            return LinkedListOperatioinNode("setLLDeleteAtHead", name_variable, None)
        elif token_type == 'LL_SEARCH' and value != 0:
            return LinkedListOperatioinNode("setLLSearch", name_variable, value)
        elif token_type == 'LL_IS_EMPTY':
            return LinkedListOperatioinNode("setLLIsEmpty", name_variable, None)
        else:
            Errors.FalseKod(line[0].getNumberLine())

    # def setLLInsertAtEnd(self, line):
    #     name_variable = line[0].getValue()
    #     value = line[3]
    #     return LinkedListOperatioinNode("setLLInsertAtEnd", name_variable, value)
    #
    # def setLLInsertAtHead(self, line):
    #     name_variable = line[0].getValue()
    #     value = line[3]
    #     return LinkedListOperatioinNode("setLLInsertAtHead", name_variable, value)
    #
    # def setLLDelete(self, line):
    #     name_variable = line[0].getValue()
    #     value = line[3]
    #     return LinkedListOperatioinNode("setLLDelete", name_variable, value)
    #
    # def setLLDeleteAtHead(self, line):
    #     name_variable = line[0].getValue()
    #     return LinkedListOperatioinNode("setLLDeleteAtHead", name_variable, None)
    #
    # def setLLSearch(self, line):
    #     name_variable = line[0].getValue()
    #     value = line[3]
    #     return LinkedListOperatioinNode("setLLSearch", name_variable, value)
    #
    # def setLLIsEmpty(self, line):
    #     name_variable = line[0].getValue()
    #     return LinkedListOperatioinNode("setLLIsEmpty", name_variable, None)

    def getNodeList(self):
        return self.node_list

    def show_nodes(self):
        print("self.node_list:")
        for elem in self.node_list:
            print(elem.getTypeNode())
