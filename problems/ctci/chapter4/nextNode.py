# 4.6
class Tree(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.parent = None


# O() runtime
# O() space
def nextNode(root):
    if root.right:
        root = root.right
        while root.left:
            root = root.left
        return root
    if root.parent.left == root:
        return root.parent
    if root.parent.right == root:
        while root.parent:
            if root.parent.data > root.data:
                return root.parent
            root = root.parent
        return root.parent


tree1 = Tree(7)

tree1.left = Tree(5)
tree1.left.parent = tree1

tree1.right = Tree(9)
tree1.right.parent = tree1

tree1.left.left = Tree(4)
tree1.left.left.parent = tree1.left
tree1.left.right = Tree(6)
tree1.left.right.parent = tree1.left

tree1.right.left = Tree(8)
tree1.right.left.parent = tree1.right
tree1.right.right = Tree(10)
tree1.right.right.parent = tree1.right

assert nextNode(tree1.left.right) == tree1


tree2 = Tree(7)

tree2.left = Tree(5)
tree2.left.parent = tree2

tree2.right = Tree(9)
tree2.right.parent = tree2

tree2.left.left = Tree(4)
tree2.left.left.parent = tree2.left
tree2.left.right = Tree(6)
tree2.left.right.parent = tree2.left

tree2.right.left = Tree(8)
tree2.right.left.parent = tree2.right
tree2.right.right = Tree(10)
tree2.right.right.parent = tree2.right

assert nextNode(tree2.right) == tree2.right.right


tree3 = Tree(7)

tree3.left = Tree(5)
tree3.left.parent = tree3

tree3.right = Tree(9)
tree3.right.parent = tree3

tree3.left.left = Tree(4)
tree3.left.left.parent = tree3.left
tree3.left.right = Tree(6)
tree3.left.right.parent = tree3.left

tree3.right.left = Tree(8)
tree3.right.left.parent = tree3.right
tree3.right.right = Tree(10)
tree3.right.right.parent = tree3.right
assert nextNode(tree3) == tree3.right.left
