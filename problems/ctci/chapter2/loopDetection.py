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

    # O(N) runtime
    # O(1) space
    def loopBeginningNode(self, linkedList):
        if not linkedList or not linkedList.next:
            return None

        pointer1 = linkedList
        pointer2 = linkedList.next

        while pointer1 and pointer2:
            pointer1 = pointer1.next
            if pointer2.next and pointer2.next.next:
                pointer2 = pointer2.next.next
            else:
                return None
            if pointer1 == pointer2:
                break

        if pointer1 is None or pointer2 is None:
            return None

        pointer1 = linkedList
        pointer2 = pointer2.next

        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        return pointer1


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
linkedList1.next.next.next.next.next = linkedList1.next.next

assert Solution().loopBeginningNode(linkedList1).val == 'C'

linkedList2 = NodeF
linkedList2.next = NodeF

assert Solution().loopBeginningNode(linkedList2).val == 'F'

linkedList3 = Node('A')
linkedList3.next = Node('A')

assert Solution().loopBeginningNode(linkedList3) is None
