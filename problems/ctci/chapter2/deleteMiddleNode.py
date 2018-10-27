# 2.3
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

    # O(N) runtime
    # O(1) space
    def deleteMiddleNode(self, middleNode):
        if not middleNode or not middleNode.next:
            return

        pointer = middleNode
        while pointer:
            if pointer.next:
                pointer.val = pointer.next.val
            if not pointer.next.next:
                pointer.next = None
            pointer = pointer.next


linkedList = Node(1)
linkedList.next = Node(5)
linkedList.next.next = Node(26)
linkedList.next.next.next = Node(2)
linkedList.next.next.next.next = Node(13)

Solution().deleteMiddleNode(linkedList.next)
assert linkedList.printValues() == "1 -> 26 -> 2 -> 13 -> null"

linkedList = Node(1)
linkedList.next = Node(5)
linkedList.next.next = Node(26)
linkedList.next.next.next = Node(2)
linkedList.next.next.next.next = Node(13)

Solution().deleteMiddleNode(linkedList.next.next.next.next)
assert linkedList.printValues() == "1 -> 5 -> 26 -> 2 -> 13 -> null"
