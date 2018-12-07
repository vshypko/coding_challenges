# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        ptr1 = l1
        ptr2 = l2

        if ptr1.val <= ptr2.val:
            result = ListNode(ptr1.val)
            ptr1 = ptr1.next
        else:
            result = ListNode(ptr2.val)
            ptr2 = ptr2.next
        head = result

        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                result.next = ListNode(ptr1.val)
                ptr1 = ptr1.next
            else:
                result.next = ListNode(ptr2.val)
                ptr2 = ptr2.next
            result = result.next

        if not ptr1:
            result.next = ptr2
        elif not ptr2:
            result.next = ptr1

        return head
