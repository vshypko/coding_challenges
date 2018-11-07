# 3.3
class SetOfStacks:
    def __init__(self):
        self.stacks = list(Stack())
        self.capacity = 5
        self.numElements = 0
        self.numStacks = 1

    def addNewStack(self):
        self.stacks.append(Stack())
        self.numStacks += 1

    def push(self, item):
        if self.numElements % self.capacity == 0:
            self.addNewStack()
        self.stacks[self.numStacks - 1].push(item)
        self.numElements += 1

    def pop(self):
        if self.stacks[self.numStacks - 1].peek() is not None:
            self.stacks[self.numStacks - 1].pop()
        if self.stacks[self.numStacks - 1].peek() is None:
            del self.stacks[self.numStacks - 1]
            self.numStacks -= 1

    def popAt(self, index):
        self.stacks[index].pop()


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1] if not self.is_empty() else None

    def is_empty(self):
        return self.items == []


class Solution:
    def __init__(self):
        # for testing purposes
        pass

    # O() runtime
    # O() space
    def stackOfPlates(self):
        stack = Stack()
        stack.push(5)


Solution().stackOfPlates()
