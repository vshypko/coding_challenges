# 876
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result = list()
        currentNode = head

        while currentNode:
            result.append(currentNode.val)
            currentNode = currentNode.next

        return result[int(len(result) / 2):]
