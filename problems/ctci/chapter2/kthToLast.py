# 2.2
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
    def kthToLast(self, linkedList, k):
        if not linkedList or k < 0:
            return

        linkedListLength = self.findLinkedListLength(linkedList)

        if linkedListLength < k:
            print("Error! K is greater than the length of the linked list:", k)
            return

        pointer = linkedList
        target = linkedListLength - k
        counter = 0

        while pointer:
            if counter == target:
                return pointer.val
            counter += 1
            if not pointer.next and counter == target:
                return pointer.val
            pointer = pointer.next
        return

    def findLinkedListLength(self, linkedList):
        pointer = linkedList
        counter = 0
        while pointer:
            counter += 1
            pointer = pointer.next
        return counter

    # O(N) runtime
    # O(1) space
    def kthToLastAuthor(self, linkedList, k):
        if not linkedList or k < 0:
            return None

        pointer1 = pointer2 = linkedList

        for i in range(k):
            if not pointer1:
                return None
            pointer1 = pointer1.next

        while pointer1:
            if k == 0 and not pointer2.next:
                return pointer2
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        return pointer2


linkedList = Node.linkedListFromValues([1, -2, 3, 1, -2, 1, 26, 13])

assert Solution().kthToLast(linkedList, 2) == 26
assert Solution().kthToLast(linkedList, 8) == 1
assert Solution().kthToLast(linkedList, 0) == 13
assert Solution().kthToLast(linkedList, 9) is None

assert Solution().kthToLastAuthor(linkedList, 2).val == 26
assert Solution().kthToLastAuthor(linkedList, 8).val == 1
assert Solution().kthToLastAuthor(linkedList, 0).val == 13
assert Solution().kthToLastAuthor(linkedList, 9) is None
