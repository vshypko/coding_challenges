# 3.2
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        minItem = item if self.is_empty() else min(item, self.peekTuple()[1])
        self.items.append((item, minItem))

    def pop(self):
        return self.items.pop()[0]

    def peekTuple(self):
        return self.items[len(self.items) - 1]

    def peek(self):
        return self.peekTuple()[0]

    def is_empty(self):
        return self.items == []

    def stackMin(self):
        return self.peekTuple()[1] if not self.is_empty() else None


class Solution:
    def __init__(self):
        # for testing purposes
        pass

    # O(1) runtime
    # O(1) space
    def stackMin(self):
        stack = Stack()
        stack.push(5)
        print(stack.stackMin())
        print(stack.peek())
        stack.push(2)
        print(stack.stackMin())
        stack.push(3)
        print(stack.stackMin())
        stack.push(-1)
        print(stack.stackMin())
        stack.pop()
        print(stack.stackMin())
        stack.pop()
        print(stack.stackMin())
        stack.pop()
        print(stack.stackMin())
        stack.pop()
        print(stack.stackMin())


Solution().stackMin()
