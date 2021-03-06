# 2.5
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

    # O(len(linkedList1) + len(linkedList2)) runtime
    # O(1) space
    def sumReverseListsIterative(self, linkedList1, linkedList2):
        if not linkedList1:
            return linkedList2
        if not linkedList2:
            return linkedList1

        lastNode1 = pointer1 = linkedList1
        pointer2 = linkedList2
        carry = 0
        firstShorter, secondShorter = False, False

        while pointer1 and pointer2:
            pointer1.val += pointer2.val
            if carry > 0:
                pointer1.val += carry
                carry = 0
            if pointer1.val >= 10:
                pointer1.val = pointer1.val % 10
                carry = 1
            lastNode1 = pointer1
            pointer1, pointer2 = pointer1.next, pointer2.next

            if not pointer1 and pointer2:
                firstShorter = True

            if pointer1 and not pointer2:
                secondShorter = True

        if firstShorter:
            while pointer2:
                lastNode1.next = Node(pointer2.val + carry)
                carry = 0
                lastNode1 = lastNode1.next
                pointer2 = pointer2.next
            lastNode1.next = None

        if secondShorter:
            while pointer1:
                pointer1.val += carry
                carry = 0
                pointer1 = pointer1.next

        if carry > 0:
            lastNode1.next = Node(carry)
        return linkedList1

    # O(A + B) runtime
    # O(A + B) space
    def sumForwardListsIterative(self, linkedList1, linkedList2):
        if not linkedList1:
            return linkedList2
        if not linkedList2:
            return linkedList1

        # length1 = length2 = 0
        # pointer1 = linkedList1
        # pointer2 = linkedList2
        #
        # while pointer1:
        #     pointer1 = pointer1.next
        #     length1 += 1
        #
        # while pointer2:
        #     pointer2 = pointer2.next
        #     length2 += 1
        #
        # i = 0
        # if length1 > length2:
        #     while i < length1 - length2:
        #         temp = Node(0)
        #         temp.next = linkedList2
        #         linkedList2 = temp
        #         i += 1
        # elif length2 > length1:
        #     while i < length2 - length1:
        #         temp = Node(0)
        #         temp.next = linkedList1
        #         linkedList1 = temp
        #         i += 1
        # linkedList1.printValues()
        # linkedList2.printValues()

        list1 = list()
        list2 = list()

        pointer1 = linkedList1
        pointer2 = linkedList2

        while pointer1:
            list1.append(pointer1.val)
            pointer1 = pointer1.next

        while pointer2:
            list2.append(pointer2.val)
            pointer2 = pointer2.next

        integer1 = int(''.join(str(x) for x in list1))
        integer2 = int(''.join(str(x) for x in list2))
        result = integer1 + integer2
        length = len(str(result))
        resultList = list(str(result))

        resultLL = Node(resultList[0])
        pointer = resultLL
        for i in range(length):
            pointer.next = Node(resultList[i])
            pointer = pointer.next

        resultLL = resultLL.next
        return resultLL


linkedList1 = Node.linkedListFromValues([7, 1, 6])
linkedList2 = Node.linkedListFromValues([5, 9, 2])
assert Solution().sumReverseListsIterative(linkedList1, linkedList2).printValues() == "2 -> 1 -> 9 -> null"

linkedList1 = Node.linkedListFromValues([9, 7, 8])
linkedList2 = Node.linkedListFromValues([6, 8, 5])
assert Solution().sumReverseListsIterative(linkedList1, linkedList2).printValues() == "5 -> 6 -> 4 -> 1 -> null"

linkedList1 = Node.linkedListFromValues([8])
linkedList2 = Node.linkedListFromValues([6, 8, 5])
assert Solution().sumReverseListsIterative(linkedList1, linkedList2).printValues() == "4 -> 9 -> 5 -> null"

linkedList1 = Node.linkedListFromValues([6, 8, 5])
linkedList2 = Node.linkedListFromValues([8])
assert Solution().sumReverseListsIterative(linkedList1, linkedList2).printValues() == "4 -> 9 -> 5 -> null"

linkedList1 = Node.linkedListFromValues([6, 1, 7])
linkedList2 = Node.linkedListFromValues([2, 9, 5])
assert Solution().sumReverseListsIterative(linkedList1, linkedList2).printValues() == "8 -> 0 -> 3 -> 1 -> null"
print()

linkedList1 = Node.linkedListFromValues([6, 1, 7])
linkedList2 = Node.linkedListFromValues([2, 9, 5])
assert Solution().sumForwardListsIterative(linkedList1, linkedList2).printValues() == "9 -> 1 -> 2 -> null"

linkedList1 = Node.linkedListFromValues([0])
linkedList2 = Node.linkedListFromValues([2, 9, 5])
assert Solution().sumForwardListsIterative(linkedList1, linkedList2).printValues() == "2 -> 9 -> 5 -> null"

linkedList1 = Node.linkedListFromValues([0])
linkedList2 = Node.linkedListFromValues([0])
assert Solution().sumForwardListsIterative(linkedList1, linkedList2).printValues() == "0 -> null"

linkedList1 = Node.linkedListFromValues([0])
linkedList2 = Node.linkedListFromValues([1, 4, 5])
assert Solution().sumForwardListsIterative(linkedList1, linkedList2).printValues() == "1 -> 4 -> 5 -> null"

linkedList1 = Node.linkedListFromValues([9, 9, 9])
linkedList2 = Node.linkedListFromValues([7, 7, 8])
assert Solution().sumForwardListsIterative(linkedList1, linkedList2).printValues() == "1 -> 7 -> 7 -> 7 -> null"


