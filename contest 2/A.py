class MyStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        if len(self.items) > 0:
            self.items.append((item, min(item, self.items[-1][1])))
        else:
            self.items.append((item, item))

    def pop(self):
        return self.items.pop()[0]

    def peek(self):
        return self.items[-1][0]

    def min(self):
        return self.items[-1][1]


n = int(input())
stack = MyStack()

for _ in range(n):
    operation = input().split()
    if operation[0] == '1':
        item = int(operation[1])
        stack.push(item)
    elif operation[0] == '2':
        stack.pop()
    else:
        print(stack.min())