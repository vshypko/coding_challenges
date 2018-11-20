# 559
"""
# Definition for a Node.
    class Node(object):
        def __init__(self, val, children):
            self.val = val
            self.children = children
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0

        elif len(root.children) == 0:
            return 1

        heights = list()
        for child in root.children:
            heights.append(self.maxDepth(child))
        return 1 + max(heights)
