# 2.6
import copy


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
    # O(N) space
    def isPalindrome(self, linkedList):
        if not linkedList or not linkedList.next:
            return True

        reversedList = self.reverseLinkedList(copy.deepcopy(linkedList))  # to not lose original LL
        pointerForward = linkedList
        pointerBackward = reversedList

        while pointerForward and pointerBackward:
            if not pointerForward.val == pointerBackward.val:
                return False
            pointerForward = pointerForward.next
            pointerBackward = pointerBackward.next
        return True

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


linkedList = Node.linkedListFromValues([6, 1, 6])
assert Solution().isPalindrome(linkedList) is True

linkedList = Node.linkedListFromValues([])
assert Solution().isPalindrome(linkedList) is True

linkedList = Node.linkedListFromValues([1])
assert Solution().isPalindrome(linkedList) is True

linkedList = Node.linkedListFromValues([1, 2])
assert Solution().isPalindrome(linkedList) is False

linkedList = Node.linkedListFromValues([6, 1, 1, 6])
assert Solution().isPalindrome(linkedList) is True

linkedList = Node.linkedListFromValues([1, 2, 3, 4, 5])
assert Solution().isPalindrome(linkedList) is False

linkedList = Node.linkedListFromValues(['a', 'b', 'c', 'b', 'a'])
assert Solution().isPalindrome(linkedList) is True

linkedList = Node.linkedListFromValues(['a', 'b', 'c', 'd', 'a'])
assert Solution().isPalindrome(linkedList) is False
