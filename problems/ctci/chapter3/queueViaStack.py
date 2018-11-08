# 3.4
class MyQueue():
    def __init__(self):
        pass


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
    def stackMin(self):
        stack = Stack()


Solution().stackMin()
