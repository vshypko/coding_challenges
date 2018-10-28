# 2.8
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
    def loopDetection(self, linkedList):
        if not linkedList or not linkedList.next:
            return None

        pointer1 = linkedList
        pointer2 = linkedList.next

        while pointer1 and pointer2:
            if pointer1 is pointer2:
                return pointer1
            if pointer2 is None or pointer2.next is None or pointer2.next.next is None:
                return None
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next
        return None


NodeA = Node('A')
NodeB = Node('B')
NodeC = Node('C')
NodeD = Node('D')
NodeE = Node('E')
NodeF = Node('F')

linkedList1 = NodeA
linkedList1.next = NodeB
linkedList1.next.next = NodeC
linkedList1.next.next.next = NodeD
linkedList1.next.next.next.next = NodeE
linkedList1.next.next.next.next.next = NodeC

assert Solution().loopDetection(linkedList1).val == 'C'

linkedList2 = NodeF
linkedList2.next = NodeF

assert Solution().loopDetection(linkedList2).val == 'F'

linkedList3 = Node('A')
linkedList3.next = Node('A')

assert Solution().loopDetection(linkedList3) is None
