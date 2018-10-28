# 2.4
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def printValues(self):
        string = ""
        temp = self
        while temp:
            string += str(temp.val) + " -> "
            temp = temp.next
        print(string + "null")
        return string + "null"

    def linkedListFromValues(listOfValues):
        if not listOfValues:
            return
        linkedList = Node(listOfValues[0])
        temp = linkedList
        for value in listOfValues[1:]:
            temp.next = Node(value)
            temp = temp.next
        return linkedList


class Solution:
    def __init__(self):
        # for testing purposes
        pass

    # O(N^2) runtime
    # O(1) space
    def partition(self, linkedList, x):
        if not linkedList:
            return

        pointer1 = linkedList
        while pointer1:
            if pointer1.val >= x:
                pointer2 = pointer1.next
                swapped = False
                while pointer2 and not swapped:
                    if pointer2.val < x:
                        pointer1.val, pointer2.val = pointer2.val, pointer1.val
                        swapped = True
                    pointer2 = pointer2.next
            pointer1 = pointer1.next
        return linkedList


linkedList = Node.linkedListFromValues([3, 5, 8, 5, 10, 2, 1])
assert Solution().partition(linkedList, 5).printValues() == "3 -> 2 -> 1 -> 5 -> 10 -> 5 -> 8 -> null"

linkedList = Node.linkedListFromValues([3, 5, 8, 5, 10, 2, 1])
assert Solution().partition(linkedList, -10).printValues() == "3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 -> null"
