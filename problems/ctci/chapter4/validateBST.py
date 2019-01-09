# 4.5
class Tree(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


# O(N) runtime
# O(log(N)) space
def validateBST(root, minValue=float('-inf'), maxValue=float('inf')):
    if not root:
        return True
    if root.data < minValue or root.data > maxValue:
        return False
    return validateBST(root.left, float('-inf'), root.data) \
           and validateBST(root.right, root.data, float('inf'))


tree1 = Tree(7)
tree1.left = Tree(5)
tree1.right = Tree(9)
tree1.left.left = Tree(4)
tree1.left.right = Tree(6)
tree1.right.left = Tree(8)
tree1.right.right = Tree(10)
assert validateBST(tree1) is True

tree2 = Tree(7)
tree2.left = Tree(5)
tree2.right = Tree(9)
tree2.left.left = Tree(4)
tree2.left.right = Tree(6)
tree2.right.left = Tree(13)
tree2.right.right = Tree(10)
assert validateBST(tree2) is False
