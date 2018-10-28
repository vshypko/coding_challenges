# 2.7
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

    # O() runtime
    # O() space
    def intersection(self, linkedList1, linkedList2):
        if not linkedList1 or not linkedList2:
            return False



linkedList1 = Node.linkedListFromValues([1, 2, 3])
linkedList2 = Node.linkedListFromValues([3, 4])
Solution().intersection(linkedList1, linkedList2)
