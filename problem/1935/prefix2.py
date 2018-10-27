import sys


class MStack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if self.stack:
            return False
        return True

    def pop(self):
        if self.is_empty():
            raise RuntimeError("Stack is empty!!")
        return self.stack.pop()

    def push(self, op):
        self.stack.append(op)


def calc_function(op1, op2, operator):
    if operator == "+":
        return op1 + op2
    elif operator == "-":
        return op1 - op2
    elif operator == "*":
        return op1 * op2
    elif operator == "/":
        return op1 / op2
    else:
        raise RuntimeError("Unknown type operator is called")



if __name__ == "__main__":

    # input data
    num_of_variable = int(sys.stdin.readline())
    expression = sys.stdin.readline().strip()

    variable_dict = {}
    for i in range(num_of_variable):
        variable = int(sys.stdin.readline())
        variable_dict[i] = variable

    # calc expression
    m_stack = MStack()
    operators = "+-*/"
    res = 0
    for char in expression:
        if char in operators:
            op2 = m_stack.pop()
            op1 = m_stack.pop()
            res = calc_function(op1, op2, char)
            m_stack.push(res)
        else:
            m_stack.push(variable_dict[ord(char)-ord("A")])

    print("{:.2f}".format(round(m_stack.pop(), 2)))
