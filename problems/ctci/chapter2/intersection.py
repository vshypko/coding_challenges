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

    # O(A + b) runtime
    # O(1) space
    def intersection(self, linkedList1, linkedList2):
        if not linkedList1 or not linkedList2:
            return False

        isIntersection = self.isIntersection(linkedList1, linkedList2)
        if not isIntersection[0]:
            return None

        length1 = isIntersection[1]
        length2 = isIntersection[2]

        i = 0
        pointer1 = linkedList1
        pointer2 = linkedList2
        if length1 > length2:
            while (i < length1 - length2):
                pointer1 = pointer1.next
                i += 1
        else:
            while (i < length2 - length1):
                pointer2 = pointer2.next
                i += 1

        while pointer1 and pointer2:
            if pointer1 == pointer2:
                return pointer1
            else:
                pointer1 = pointer1.next
                pointer2 = pointer2.next

        return None


    def isIntersection(self, linkedList1, linkedList2):
        if not linkedList1 or not linkedList2:
            return False

        pointer1 = linkedList1
        length1 = 0
        pointer2 = linkedList2
        length2 = 0

        while pointer1 and pointer1.next:
            pointer1 = pointer1.next
            length1 += 1

        while pointer2 and pointer2.next:
            pointer2 = pointer2.next
            length2 += 1

        return (pointer1 == pointer2, length1 + 1, length2 + 1)

    def reverseLinkedList(self, linkedList):
        prev = pointer = linkedList

        if not pointer.next:
            return linkedList

        nxt = pointer.next
        prev.next = None

        while nxt and nxt.next:
            pointer = nxt
            nxt = nxt.next
            pointer.next = prev
            prev = pointer

        nxt.next = prev
        return nxt


Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node4 = Node(4)
Node5 = Node(5)
Node6 = Node(6)
Node7 = Node(7)

linkedList1 = Node1
linkedList1.next = Node2
linkedList1.next.next = Node3
linkedList1.next.next.next = Node4
linkedList1.next.next.next.next = Node6
linkedList1.next.next.next.next.next = Node7

linkedList2 = Node5
linkedList2.next = Node4

assert Solution().intersection(linkedList1, linkedList2).val == 4
