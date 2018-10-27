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
    def removeDuplicates(self, linkedList):
        if not linkedList:
            return

        hashmap = {}
        pointer = linkedList

        while pointer:
            if pointer.val not in hashmap.keys():
                hashmap[pointer.val] = 1
            else:
                hashmap[pointer.val] += 1
            pointer = pointer.next

        pointer = linkedList
        foundHead = False

        while pointer:
            if not foundHead:
                if hashmap[pointer.val] == 1:
                    foundHead = True
                    continue
                pointer = pointer.next
                linkedList = pointer
            else:
                if pointer.next and hashmap[pointer.next.val] > 1:
                    pointer.next = pointer.next.next
                else:
                    pointer = pointer.next
        return linkedList


linkedList = Node.linkedListFromValues([1, -2, 3, 1, -2, 1, 26, 1])
assert Solution().removeDuplicates(linkedList).printValues() == "3 -> 26 -> null"

linkedList = Node.linkedListFromValues([4, -2, 3, 1, -2, 1, 26, 2])
assert Solution().removeDuplicates(linkedList).printValues() == "4 -> 3 -> 26 -> 2 -> null"

linkedList = Node.linkedListFromValues([1, 1, 1])
assert Solution().removeDuplicates(linkedList) is None

linkedList = Node.linkedListFromValues([1])
assert Solution().removeDuplicates(linkedList).printValues() == "1 -> null"

linkedList = Node.linkedListFromValues([])
assert Solution().removeDuplicates(linkedList) is None
