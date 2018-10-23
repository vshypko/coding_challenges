# 2.1
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
    def removeDuplicates(self, m):
        return


# linkedList = Node(1)
# linkedList.next = Node(-2)
# linkedList.next.next = Node(1)
# linkedList.next.next.next = Node(1)
# linkedList.next.next.next.next = Node(26)
# linkedList.next.next.next.next.next = Node(1)
# linkedList.printValues()
linkedList = Node.linkedListFromValues([1, -2, 1, 1, 26, 1])
linkedList.printValues()

# assert (Solution().removeDuplicates([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# assert (Solution().removeDuplicates([]) == [])
