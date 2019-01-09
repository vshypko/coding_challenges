# 4.4
class Tree(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


# O(N) runtime
# O(height(tree)) space
def isBalanced(tree):
    return checkHeight(tree) != float('-inf')


def checkHeight(tree):
    if not tree:
        return -1

    leftHeight = checkHeight(tree.left)
    rightHeight = checkHeight(tree.right)

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
print(isBalanced(tree))
