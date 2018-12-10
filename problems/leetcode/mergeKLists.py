# 23
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return

        listOfNums = list()

        for li in lists:
            if li:
                ptr = li
                while ptr:
                    listOfNums.append(ptr.val)
                    ptr = ptr.next

        if not listOfNums:
            return

        listOfNums.sort()

        head = ptr = ListNode(listOfNums[0])
        for elem in listOfNums[1:]:
            ptr.next = ListNode(elem)
            ptr = ptr.next

        return head
