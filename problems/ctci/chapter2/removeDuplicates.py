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
        print(hashmap)

        prev = pointer = linkedList
        startDone = False
        while pointer and pointer.next:
            if hashmap[pointer.val] > 1:
                if not startDone:
                    linkedList = linkedList.next
                    prev = linkedList
                    pointer = linkedList
                else:
                    prev.next = pointer.next
            else:
                startDone = True
            prev = pointer
            pointer = pointer.next

        return linkedList



linkedList = Node.linkedListFromValues([1, -2, 3, 1, -2, 1, 26, 1])
print("Before:")
linkedList.printValues()
print("After:")
Solution().removeDuplicates(linkedList).printValues()

# assert (Solution().removeDuplicates([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# assert (Solution().removeDuplicates([]) == [])
