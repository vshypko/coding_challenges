# 4.4
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
    # O(height(tree)) space
    def isBalanced(self, tree):
        return self.checkHeight(tree) != float('-inf')

    def checkHeight(self, tree):
        if not tree:
            return -1

        leftHeight = self.checkHeight(tree.left)
        rightHeight = self.checkHeight(tree.right)

        if leftHeight == float('-inf'):
            return float('-inf')

        if rightHeight == float('-inf'):
            return float('-inf')

        heightDiff = abs(leftHeight - rightHeight)

        if heightDiff > 1:
            return float('-inf')
        else:
            return max(leftHeight, rightHeight) + 1

tree = Tree(5)
tree.left = Tree(3)
tree.right = Tree(7)
tree.right.right = Tree(7)
# tree.right.right.right = Tree(7)
print(Solution().isBalanced(tree))
