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

    # O() runtime
    # O() space
    def partition(self, linkedList, x):
        if not linkedList:
            return


linkedList = Node.linkedListFromValues([3, 5, 8, 5, 10, 2, 1])
Solution().partition(linkedList, 5)
# assert linkedList.printValues() == "1 -> 5 -> 26 -> 2 -> 13 -> null"
