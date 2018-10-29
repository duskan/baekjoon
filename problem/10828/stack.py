import sys


class mStack():
    def __init__(self):
        self.stack = []

    def top(self):
        if self.empty() == 1:
            return -1
        return self.stack[-1]

    def empty(self):
        if self.stack:
            return 0
        return 1

    def size(self):
        return len(self.stack)

    def push(self, op):
        self.stack.append(op)

    def pop(self):
        if self.empty() == 1:
            return -1
        return self.stack.pop()


if __name__ == "__main__":
    # input
    num_of_commands = int(sys.stdin.readline())
    stack = mStack()
    for i in range(num_of_commands):
        commands = sys.stdin.readline().strip().split()

        command = commands[0]

        if command == "push":
            stack.push(commands[1])
        elif command == "top":
            print(stack.top())
        elif command == "empty":
            print(stack.empty())
        elif command == "size":
            print(stack.size())
        elif command == "pop":
            print(stack.pop())

        # print(stack.stack)
