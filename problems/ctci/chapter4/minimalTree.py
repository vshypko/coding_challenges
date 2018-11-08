# 4.2
class Tree(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class Solution:
    def __init__(self):
        # for testing purposes
        pass

    # O(N) runtime
    # O(1) space
    def minimalTree(self, array):
        if not array:
            return
        if len(array) == 1:
            return array[0]
        mid = len(array) // 2 if len(array) % 2 == 0 else len(array) // 2 + 1
        root = Tree(array[mid])
        root.left = self.minimalTree(array[:mid])
        root.right = self.minimalTree(array[mid + 1:])
        return root


temp = Solution().minimalTree([1, 5, 6, 7, 12, 43, 66, 70, 73])
